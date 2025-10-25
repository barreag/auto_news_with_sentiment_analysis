"""
Sentiment Analysis Agent - Analyzes sentiment of news articles using Gemini API.
"""
from typing import List, Dict, Any, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

from config.settings import settings
from src.utils.logger import logger


class SentimentResult(BaseModel):
    """Sentiment analysis result structure."""
    sentiment: str = Field(description="Sentiment classification: positive, negative, or neutral")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reasoning: str = Field(description="Brief explanation of the sentiment classification")


class SentimentAgentState(TypedDict):
    """State for the sentiment agent."""
    articles: Dict[str, List[Dict[str, Any]]]


class SentimentAnalysisAgent:
    """Agent responsible for analyzing sentiment of news articles."""
    
    def __init__(self):
        """Initialize the sentiment analysis agent."""
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_output_tokens=settings.MAX_TOKENS,
            google_api_key=settings.GOOGLE_API_KEY,
            convert_system_message_to_human=True  # For compatibility
        )
        
        # Create sentiment analysis prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert sentiment analyst specializing in automotive industry news.
            
            Your task is to analyze the sentiment of news articles and their summaries.
            
            Classify sentiment as:
            - positive: Good news for the company (growth, innovation, success, positive market response)
            - negative: Bad news for the company (losses, recalls, scandals, market decline)
            - neutral: Factual reporting without clear positive or negative implications
            
            Provide:
            1. sentiment: One of "positive", "negative", or "neutral"
            2. confidence: A score between 0 and 1 indicating your confidence
            3. reasoning: A brief explanation (1-2 sentences) of why you classified it this way
            
            Return the result as a JSON object with these three fields."""),
            ("user", """Analyze the sentiment of this automotive news article:
            
            Company: {company}
            Title: {title}
            Summary: {summary}
            Original Content: {content}
            
            Provide sentiment analysis as JSON with sentiment, confidence, and reasoning.""")
        ])
        
        self.parser = JsonOutputParser(pydantic_object=SentimentResult)
        self.chain = self.prompt | self.llm | self.parser
        
        logger.info("SentimentAnalysisAgent initialized")
    
    def analyze_article(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze sentiment of a single article.
        
        Args:
            article: Article dictionary with title, summary, etc.
            
        Returns:
            Dictionary with sentiment, confidence, and reasoning
        """
        try:
            result = self.chain.invoke({
                "company": article.get('company', 'Unknown'),
                "title": article.get('title', 'No title'),
                "summary": article.get('summary', 'No summary'),
                "content": article.get('snippet', 'No content')
            })
            
            return {
                "sentiment": result.get("sentiment", "neutral"),
                "confidence": result.get("confidence", 0.5),
                "reasoning": result.get("reasoning", "Analysis unavailable")
            }
            
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {str(e)}")
            return {
                "sentiment": "neutral",
                "confidence": 0.0,
                "reasoning": "Sentiment analysis failed due to processing error."
            }
    
    def analyze_articles(self, articles: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Analyze sentiment for all articles.
        
        Args:
            articles: Dictionary mapping company names to their articles
            
        Returns:
            Updated articles dictionary with sentiment analysis
        """
        logger.info("Starting sentiment analysis")
        
        total_articles = sum(len(arts) for arts in articles.values())
        processed = 0
        
        for company, company_articles in articles.items():
            logger.info(f"Analyzing sentiment for {len(company_articles)} articles about {company}")
            
            for article in company_articles:
                sentiment_data = self.analyze_article(article)
                article.update(sentiment_data)
                processed += 1
                
                if processed % 5 == 0:
                    logger.info(f"Analyzed {processed}/{total_articles} articles")
        
        logger.info(f"Completed sentiment analysis of {total_articles} articles")
        return articles
    
    def __call__(self, state: SentimentAgentState) -> SentimentAgentState:
        """
        Execute the sentiment analysis agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with sentiment analysis
        """
        logger.info("Executing SentimentAnalysisAgent")
        
        articles = state.get("articles", {})
        
        if not articles:
            logger.warning("No articles to analyze")
            return state
        
        analyzed_articles = self.analyze_articles(articles)
        state["articles"] = analyzed_articles
        
        return state
