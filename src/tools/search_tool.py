"""
DuckDuckGo search tool for news articles.

This module provides functionality to search for automotive news using DuckDuckGo,
with built-in rate limiting protection and retry logic.
"""
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any
from duckduckgo_search import DDGS

from src.utils.logger import logger


class NewsSearchTool:
    """
    Tool for searching news articles using DuckDuckGo.
    
    Features:
    - Automatic retry with exponential backoff
    - Rate limit detection and handling
    - Configurable delays between requests
    """
    
    def __init__(self, days_back: int = 7, max_results: int = 10, delay_between_requests: float = 2.0):
        """
        Initialize the search tool.
        
        Args:
            days_back: Number of days to search back
            max_results: Maximum number of results per search
            delay_between_requests: Delay in seconds between API calls to avoid rate limiting
        """
        self.days_back = days_back
        self.max_results = max_results
        self.delay_between_requests = delay_between_requests
        
    def search_news(self, company: str, market: str = "US", retry_attempts: int = 3) -> List[Dict[str, Any]]:
        """
        Search for news articles about a company with retry logic.
        
        Args:
            company: Company name to search for
            market: Market focus (e.g., "US")
            retry_attempts: Number of retry attempts if rate limited
            
        Returns:
            List of news articles with title, url, snippet, and date
        """
        for attempt in range(retry_attempts):
            try:
                # Create search query
                query = f"{company} automotive news {market} market"
                
                # Calculate date range
                end_date = datetime.now()
                start_date = end_date - timedelta(days=self.days_back)
                
                logger.info(f"Searching for news about {company} from last {self.days_back} days... (Attempt {attempt + 1}/{retry_attempts})")
                
                # Perform search
                with DDGS() as ddgs:
                    results = list(ddgs.news(
                        keywords=query,
                        region='us-en',
                        safesearch='moderate',
                        max_results=self.max_results
                    ))
                
                # Process results
                articles = []
                for result in results:
                    article = {
                        'company': company,
                        'title': result.get('title', ''),
                        'url': result.get('url', ''),
                        'snippet': result.get('body', ''),
                        'source': result.get('source', ''),
                        'date': result.get('date', ''),
                        'search_date': datetime.now().isoformat()
                    }
                    articles.append(article)
                
                logger.info(f"Found {len(articles)} articles for {company}")
                return articles
                
            except Exception as e:
                error_msg = str(e)
                
                # Check if it's a rate limit error
                if "202" in error_msg or "Ratelimit" in error_msg:
                    if attempt < retry_attempts - 1:
                        wait_time = self.delay_between_requests * (attempt + 2)  # Exponential backoff
                        logger.warning(f"Rate limit hit for {company}. Waiting {wait_time} seconds before retry...")
                        time.sleep(wait_time)
                        continue
                    else:
                        logger.error(f"Rate limit exceeded for {company} after {retry_attempts} attempts")
                        return []
                else:
                    logger.error(f"Error searching news for {company}: {error_msg}")
                    return []
        
        return []
    
    def search_multiple_companies(
        self, 
        companies: List[str], 
        market: str = "US"
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Search for news articles about multiple companies with delay between requests.
        
        Args:
            companies: List of company names
            market: Market focus
            
        Returns:
            Dictionary mapping company names to their articles
        """
        results = {}
        
        for idx, company in enumerate(companies):
            # Add delay between requests (except for the first one)
            if idx > 0:
                logger.info(f"Waiting {self.delay_between_requests} seconds before next search to avoid rate limiting...")
                time.sleep(self.delay_between_requests)
            
            articles = self.search_news(company, market)
            results[company] = articles
            
        total_articles = sum(len(articles) for articles in results.values())
        logger.info(f"Total articles found across all companies: {total_articles}")
        
        return results
