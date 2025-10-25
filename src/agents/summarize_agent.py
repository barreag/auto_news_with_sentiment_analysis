"""
Summarization Agent - Summarizes news articles using Gemini API.
"""
from typing import List, Dict, Any, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config.settings import settings
from src.utils.logger import logger


class SummarizationAgentState(TypedDict):
    """State for the summarization agent."""
    articles: Dict[str, List[Dict[str, Any]]]


class SummarizationAgent:
    """Agent responsible for summarizing news articles."""
    
    def __init__(self):
        """Initialize the summarization agent."""
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_output_tokens=settings.MAX_TOKENS,
            google_api_key=settings.GOOGLE_API_KEY,
            convert_system_message_to_human=True  # For compatibility
        )
        
        # Create summarization prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert automotive industry analyst. 
            Your task is to create concise, informative summaries of automotive news articles.
            
            Guidelines:
            - Focus on key facts and developments
            - Highlight business impact and market implications
            - Keep summaries to 2-3 sentences
            - Maintain objectivity and accuracy
            - Include relevant financial or strategic information"""),
            ("user", """Please summarize the following automotive news article:
            
            Title: {title}
            Source: {source}
            Content: {content}
            
            Provide a concise 2-3 sentence summary.""")
        ])
        
        self.chain = self.prompt | self.llm | StrOutputParser()
        
        logger.info("SummarizationAgent initialized")
    
    def summarize_article(self, article: Dict[str, Any]) -> str:
        """
        Summarize a single news article.
        
        Args:
            article: Article dictionary with title, snippet, etc.
            
        Returns:
            Summarized text
        """
        try:
            summary = self.chain.invoke({
                "title": article.get('title', 'No title'),
                "source": article.get('source', 'Unknown source'),
                "content": article.get('snippet', 'No content available')
            })
            
            return summary.strip()
            
        except Exception as e:
            logger.error(f"Error summarizing article: {str(e)}")
            return "Summary unavailable due to processing error."
    
    def summarize_articles(self, articles: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Summarize all articles for all companies.
        
        Args:
            articles: Dictionary mapping company names to their articles
            
        Returns:
            Updated articles dictionary with summaries added
        """
        logger.info("Starting article summarization")
        
        total_articles = sum(len(arts) for arts in articles.values())
        processed = 0
        
        for company, company_articles in articles.items():
            logger.info(f"Summarizing {len(company_articles)} articles for {company}")
            
            for article in company_articles:
                summary = self.summarize_article(article)
                article['summary'] = summary
                processed += 1
                
                if processed % 5 == 0:
                    logger.info(f"Summarized {processed}/{total_articles} articles")
        
        logger.info(f"Completed summarization of {total_articles} articles")
        return articles
    
    def __call__(self, state: SummarizationAgentState) -> SummarizationAgentState:
        """
        Execute the summarization agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with summaries
        """
        logger.info("Executing SummarizationAgent")
        
        articles = state.get("articles", {})
        
        if not articles:
            logger.warning("No articles to summarize")
            return state
        
        summarized_articles = self.summarize_articles(articles)
        state["articles"] = summarized_articles
        
        return state
