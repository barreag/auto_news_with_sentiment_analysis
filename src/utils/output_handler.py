"""
Output handler for saving and formatting results.
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd

from src.utils.logger import logger


class OutputHandler:
    """Handle saving and formatting of analysis results."""
    
    def __init__(self, output_dir: str = "outputs"):
        """
        Initialize the output handler.
        
        Args:
            output_dir: Directory to save output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def save_json(self, data: Dict[str, Any], filename: str = None) -> Path:
        """
        Save data as JSON file.
        
        Args:
            data: Data to save
            filename: Optional filename, otherwise timestamped
            
        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_analysis_{timestamp}.json"
            
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        logger.info(f"Results saved to {filepath}")
        return filepath
    
    def save_csv(self, data: List[Dict[str, Any]], filename: str = None) -> Path:
        """
        Save data as CSV file.
        
        Args:
            data: List of dictionaries to save
            filename: Optional filename, otherwise timestamped
            
        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_analysis_{timestamp}.csv"
            
        filepath = self.output_dir / filename
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        logger.info(f"Results saved to {filepath}")
        return filepath
    
    def format_summary(self, results: Dict[str, Any]) -> str:
        """
        Format results as a human-readable summary.
        
        Args:
            results: Analysis results
            
        Returns:
            Formatted summary string
        """
        summary_lines = [
            "=" * 80,
            "AUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT",
            "=" * 80,
            f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"\nCompanies Analyzed: {', '.join(results.get('companies', []))}",
            f"Total Articles: {results.get('total_articles', 0)}",
            "\n" + "=" * 80,
        ]
        
        for company_data in results.get('results', []):
            company = company_data.get('company', 'Unknown')
            articles = company_data.get('articles', [])
            
            summary_lines.append(f"\n\n{'*' * 80}")
            summary_lines.append(f"COMPANY: {company}")
            summary_lines.append(f"{'*' * 80}")
            summary_lines.append(f"Articles Found: {len(articles)}\n")
            
            for idx, article in enumerate(articles, 1):
                summary_lines.append(f"\n[{idx}] {article.get('title', 'No title')}")
                summary_lines.append(f"    URL: {article.get('url', 'N/A')}")
                summary_lines.append(f"    Sentiment: {article.get('sentiment', 'N/A')} "
                                   f"(Confidence: {article.get('confidence', 'N/A')})")
                summary_lines.append(f"    Summary: {article.get('summary', 'N/A')[:200]}...")
                
        summary_lines.append("\n" + "=" * 80)
        return "\n".join(summary_lines)
    
    def print_summary(self, results: Dict[str, Any]) -> None:
        """
        Print formatted summary to console.
        
        Args:
            results: Analysis results
        """
        summary = self.format_summary(results)
        print(summary)
