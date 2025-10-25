# Usage Guide

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/auto_news_sentiment_analysis.git
cd auto_news_sentiment_analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
copy .env.example .env  # Windows
# or
cp .env.example .env    # macOS/Linux

# Edit .env and add your Google API key
# GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Get Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your `.env` file

### 4. Run the Application

```bash
# Run with default settings (GM, Ford, Tesla in US market)
python main.py

# Run for specific companies
python main.py --companies GM Ford

# Run for different market
python main.py --market Europe

# Save only JSON output
python main.py --output-format json

# Save only CSV output
python main.py --output-format csv

# Suppress console output
python main.py --no-console
```

## Usage Examples

### Example 1: Basic Usage

```bash
python main.py
```

**Output:**
```
================================================================================
AUTOMOTIVE NEWS SENTIMENT ANALYSIS SYSTEM
================================================================================
Powered by LangGraph + LangChain + Google Gemini

Target companies: GM, Ford, Tesla
Market focus: US

Step 1: Searching for news articles...
GM: Found 10 articles
Ford: Found 10 articles
Tesla: Found 10 articles

Step 2: Summarizing articles...
Summarized 30/30 articles

Step 3: Analyzing sentiment...
Analyzed 30/30 articles

Results saved to: outputs/news_analysis_20250125_143022.json
Results saved to: outputs/news_analysis_20250125_143022.csv

================================================================================
ANALYSIS COMPLETE
================================================================================
Total articles analyzed: 30
Sentiment distribution:
  Positive: 12
  Negative: 8
  Neutral: 10
================================================================================
```

### Example 2: Analyzing Specific Companies

```bash
python main.py --companies GM Tesla
```

This will analyze only GM and Tesla news.

### Example 3: Custom Market Focus

```bash
python main.py --market Europe --companies BMW Mercedes Volkswagen
```

### Example 4: Programmatic Usage

You can also use the system programmatically in your Python code:

```python
from src.workflows.news_workflow import NewsAnalysisWorkflow
from src.utils.output_handler import OutputHandler

# Initialize workflow
workflow = NewsAnalysisWorkflow()

# Run analysis
results = workflow.run(
    companies=["GM", "Ford", "Tesla"],
    market="US"
)

# Process results
output_handler = OutputHandler()
output_handler.save_json(results)
output_handler.print_summary(results)
```

### Example 5: Accessing Individual Agents

```python
from src.agents.search_agent import NewsSearchAgent
from src.agents.summarize_agent import SummarizationAgent
from src.agents.sentiment_agent import SentimentAnalysisAgent

# Use individual agents
search_agent = NewsSearchAgent()
articles = search_agent.search_news(["GM"], "US")

summarize_agent = SummarizationAgent()
# Process articles...

sentiment_agent = SentimentAnalysisAgent()
# Analyze sentiment...
```

## Output Formats

### JSON Output Structure

```json
{
  "metadata": {
    "timestamp": "2025-01-25T14:30:22",
    "companies": ["GM", "Ford", "Tesla"],
    "market": "US",
    "status": "completed",
    "total_articles": 30,
    "sentiment_distribution": {
      "positive": 12,
      "negative": 8,
      "neutral": 10
    }
  },
  "results": [
    {
      "company": "GM",
      "articles": [
        {
          "title": "GM Announces Record EV Sales",
          "url": "https://example.com/article",
          "snippet": "General Motors reported...",
          "source": "AutoNews",
          "date": "2025-01-24",
          "summary": "GM reported record electric vehicle sales...",
          "sentiment": "positive",
          "confidence": 0.92,
          "reasoning": "Article discusses strong sales growth..."
        }
      ]
    }
  ]
}
```

### CSV Output Structure

| company | title | url | source | date | summary | sentiment | confidence | reasoning |
|---------|-------|-----|--------|------|---------|-----------|------------|-----------|
| GM | GM Announces... | https://... | AutoNews | 2025-01-24 | GM reported... | positive | 0.92 | Article discusses... |

## Advanced Configuration

### Environment Variables

Edit `.env` to customize behavior:

```env
# Required
GOOGLE_API_KEY=your_api_key_here

# Optional - Companies (comma-separated)
COMPANIES=GM,Ford,Tesla

# Optional - Market focus
MARKET=US

# Optional - Search settings
NEWS_DAYS_BACK=7
MAX_RESULTS_PER_COMPANY=10

# Optional - Model settings
TEMPERATURE=0.7
MAX_TOKENS=2000
```

### Custom Search Periods

To analyze news from a different time period, modify `.env`:

```env
# Last 3 days
NEWS_DAYS_BACK=3

# Last 30 days
NEWS_DAYS_BACK=30
```

### Adjusting Result Limits

To get more or fewer articles per company:

```env
# Get only 5 articles per company
MAX_RESULTS_PER_COMPANY=5

# Get 20 articles per company
MAX_RESULTS_PER_COMPANY=20
```

## Troubleshooting

### Issue: "GOOGLE_API_KEY is required"

**Solution:** Make sure you've created a `.env` file and added your API key:
```bash
GOOGLE_API_KEY=your_actual_key_here
```

### Issue: "Import errors" when running

**Solution:** Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: No articles found

**Possible causes:**
1. Network connectivity issues
2. DuckDuckGo rate limiting
3. No recent news for specified companies

**Solutions:**
- Check your internet connection
- Wait a few minutes and try again
- Try different companies or extend the search period

### Issue: API rate limiting from Google

**Solution:** 
- Reduce `MAX_RESULTS_PER_COMPANY` in `.env`
- Add delays between requests
- Check your API quota at [Google Cloud Console](https://console.cloud.google.com/)

## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_agents.py

# Run with coverage
pytest tests/ --cov=src
```

## Integration Examples

### Schedule Daily Analysis (Windows Task Scheduler)

Create a batch file `run_analysis.bat`:
```batch
@echo off
cd C:\path\to\auto_news_sentiment_analysis
call venv\Scripts\activate
python main.py
```

Schedule it in Task Scheduler to run daily at 8 AM.

### Schedule Daily Analysis (Linux Cron)

```bash
# Edit crontab
crontab -e

# Add this line (runs daily at 8 AM)
0 8 * * * cd /path/to/auto_news_sentiment_analysis && /path/to/venv/bin/python main.py
```

### Email Results

Add email functionality to `main.py`:

```python
import smtplib
from email.mime.text import MIMEText

def send_email_report(results, recipient):
    output_handler = OutputHandler()
    summary = output_handler.format_summary(results)
    
    msg = MIMEText(summary)
    msg['Subject'] = 'Daily Automotive News Sentiment Report'
    msg['From'] = 'your_email@example.com'
    msg['To'] = recipient
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)
```

## Performance Tips

1. **Parallel Processing**: For analyzing many companies, consider implementing parallel processing
2. **Caching**: Implement caching to avoid re-searching recent articles
3. **Batch Processing**: Process articles in batches to optimize API usage
4. **Rate Limiting**: Add rate limiting to respect API quotas

## Contributing

See the main README.md for contribution guidelines.

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review test files for examples
