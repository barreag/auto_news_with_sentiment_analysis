"""
Main entry point for the Automotive News Sentiment Analysis System.

This system uses a multi-agent architecture powered by LangGraph to:
1. Search for automotive news using DuckDuckGo
2. Summarize articles using Google Gemini
3. Analyze sentiment of each article

Architecture:
- LangGraph: Orchestrates the multi-agent workflow
- LangChain: Provides agent tools and LLM integrations
- Google Gemini API: Powers summarization and sentiment analysis
"""
import argparse
from datetime import datetime
from typing import List, Optional

from config.settings import settings
from src.workflows.news_workflow import NewsAnalysisWorkflow
from src.utils.output_handler import OutputHandler
from src.utils.logger import logger


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Automotive News Sentiment Analysis System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze default companies (from .env)
  python main.py

  # Analyze specific companies
  python main.py --companies GM Ford Tesla

  # Output only JSON format
  python main.py --output-format json

  # Suppress console output
  python main.py --no-console
        """
    )
    
    parser.add_argument(
        "--companies",
        type=str,
        nargs="+",
        default=None,
        help="Companies to analyze (e.g., GM Ford Tesla)"
    )
    
    parser.add_argument(
        "--market",
        type=str,
        default=None,
        help="Market focus (default: US)"
    )
    
    parser.add_argument(
        "--output-format",
        type=str,
        choices=["json", "csv", "both"],
        default="both",
        help="Output format for results (default: both)"
    )
    
    parser.add_argument(
        "--no-console",
        action="store_true",
        help="Suppress console output"
    )
    
    return parser.parse_args()


def format_results(workflow_state: dict) -> dict:
    """
    Format workflow results for output.
    
    Args:
        workflow_state: Final state from workflow execution
        
    Returns:
        Formatted results dictionary
    """
    articles = workflow_state.get("articles", {})
    
    # Calculate statistics
    total_articles = sum(len(arts) for arts in articles.values())
    
    sentiment_counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }
    
    # Flatten articles for easier processing
    all_articles = []
    for company, company_articles in articles.items():
        for article in company_articles:
            sentiment = article.get("sentiment", "neutral")
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
            all_articles.append(article)
    
    # Create results structure
    results = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "companies": workflow_state.get("companies", []),
            "market": workflow_state.get("market", "US"),
            "status": workflow_state.get("status", "unknown"),
            "total_articles": total_articles,
            "sentiment_distribution": sentiment_counts
        },
        "companies": workflow_state.get("companies", []),
        "total_articles": total_articles,
        "results": [
            {
                "company": company,
                "articles": company_articles
            }
            for company, company_articles in articles.items()
        ],
        "all_articles": all_articles
    }
    
    return results


def main():
    """
    Main execution function.
    
    Workflow:
    1. Parse command line arguments
    2. Validate configuration
    3. Initialize multi-agent workflow
    4. Execute analysis pipeline
    5. Save and display results
    """
    # Parse arguments
    args = parse_arguments()
    
    # Display banner
    logger.info("=" * 80)
    logger.info("AUTOMOTIVE NEWS SENTIMENT ANALYSIS SYSTEM")
    logger.info("=" * 80)
    logger.info(f"Powered by LangGraph + LangChain + Google Gemini")
    logger.info("")
    
    try:
        # Validate settings
        settings.validate()
        logger.info("Configuration validated successfully")
        
        # Determine companies and market
        companies = args.companies if args.companies else settings.COMPANIES
        market = args.market if args.market else settings.MARKET
        
        logger.info(f"Target companies: {', '.join(companies)}")
        logger.info(f"Market focus: {market}")
        logger.info("")
        
        # Initialize workflow
        logger.info("Initializing multi-agent workflow...")
        workflow = NewsAnalysisWorkflow()
        
        # Run workflow
        logger.info("Starting analysis pipeline...")
        logger.info("Step 1: Searching for news articles...")
        workflow_state = workflow.run(companies=companies, market=market)
        
        # Check for errors
        if workflow_state.get("status") == "error":
            logger.error(f"Workflow failed: {workflow_state.get('error')}")
            return
        
        # Format results
        results = format_results(workflow_state)
        
        # Display summary if console output is enabled
        if not args.no_console:
            output_handler = OutputHandler()
            output_handler.print_summary(results)
        
        # Save results
        output_handler = OutputHandler()
        
        if args.output_format in ["json", "both"]:
            json_path = output_handler.save_json(results)
            logger.info(f"Results saved to: {json_path}")
        
        if args.output_format in ["csv", "both"]:
            csv_path = output_handler.save_csv(results["all_articles"])
            logger.info(f"Results saved to: {csv_path}")
        
        # Display final statistics
        logger.info("")
        logger.info("=" * 80)
        logger.info("ANALYSIS COMPLETE")
        logger.info("=" * 80)
        logger.info(f"Total articles analyzed: {results['total_articles']}")
        logger.info(f"Sentiment distribution:")
        for sentiment, count in results["metadata"]["sentiment_distribution"].items():
            logger.info(f"  {sentiment.capitalize()}: {count}")
        logger.info("=" * 80)
        
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        logger.error("Please check your .env file and ensure all required variables are set.")
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        logger.exception("Full traceback:")


if __name__ == "__main__":
    main()
