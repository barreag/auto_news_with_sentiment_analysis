"""
News Search Agent - Searches for automotive news using DuckDuckGo.
"""
from typing import List, Dict, Any, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import Tool
from langchain_core.prompts import ChatPromptTemplate

from config.settings import settings
from src.tools.search_tool import NewsSearchTool
from src.utils.logger import logger


class SearchAgentState(TypedDict):
    """State for the search agent."""
    companies: List[str]
    market: str
    articles: Dict[str, List[Dict[str, Any]]]


class NewsSearchAgent:
    """Agent responsible for searching automotive news."""
    
    def __init__(self):
        """Initialize the search agent."""
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_output_tokens=settings.MAX_TOKENS,
            google_api_key=settings.GOOGLE_API_KEY,
            convert_system_message_to_human=True  # For compatibility
        )
        
        self.search_tool = NewsSearchTool(
            days_back=settings.NEWS_DAYS_BACK,
            max_results=settings.MAX_RESULTS_PER_COMPANY,
            delay_between_requests=settings.SEARCH_DELAY_SECONDS
        )
        
        logger.info("NewsSearchAgent initialized")
    
    def search_news(self, companies: List[str], market: str = "US") -> Dict[str, List[Dict[str, Any]]]:
        """
        Search for news articles about specified companies.
        
        Args:
            companies: List of company names to search
            market: Market focus (default: US)
            
        Returns:
            Dictionary mapping company names to their articles
        """
        logger.info(f"Starting news search for companies: {', '.join(companies)}")
        
        try:
            # Use the search tool to find articles
            results = self.search_tool.search_multiple_companies(companies, market)
            
            # Log summary
            for company, articles in results.items():
                logger.info(f"{company}: Found {len(articles)} articles")
            
            return results
            
        except Exception as e:
            logger.error(f"Error in news search: {str(e)}")
            return {company: [] for company in companies}
    
    def __call__(self, state: SearchAgentState) -> SearchAgentState:
        """
        Execute the search agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with search results
        """
        companies = state.get("companies", settings.COMPANIES)
        market = state.get("market", settings.MARKET)
        
        logger.info("Executing NewsSearchAgent")
        
        articles = self.search_news(companies, market)
        
        state["articles"] = articles
        return state
