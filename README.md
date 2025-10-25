# Automotive News Sentiment Analysis System

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2.0+-green.svg)](https://github.com/langchain-ai/langgraph)
[![Powered by Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-blue)](https://ai.google.dev/)

A multi-agent AI system that automatically searches, summarizes, and analyzes sentiment for automotive industry news. Built with **LangGraph**, **LangChain**, and **Google Gemini AI** to provide actionable insights on major automotive companies.

## Features

- **Intelligent News Search**: Automatically searches for recent automotive news using DuckDuckGo
- **AI-Powered Summaries**: Generates concise 2-3 sentence summaries using Google Gemini
- **Sentiment Analysis**: Classifies articles as positive, negative, or neutral with confidence scores
- **Multi-Company Support**: Analyzes news for multiple automotive companies simultaneously
- **Multiple Output Formats**: Exports results to JSON and CSV formats
- **LangGraph Orchestration**: Reliable multi-agent workflow with state management
- **Configurable & Extensible**: Easy to customize companies, markets, and parameters

## Architecture

The system uses a **multi-agent architecture** orchestrated by **LangGraph**:

```
┌─────────────────────────────────────────────────────────────┐
│                    Main Application                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           LangGraph Workflow Orchestration                   │
└────────────────────────┬────────────────────────────────────┘
                         │
            ┌────────────┼────────────┐
            │            │            │
            ▼            ▼            ▼
    ┌──────────┐  ┌──────────┐  ┌──────────┐
    │  Search  │  │Summarize │  │Sentiment │
    │  Agent   │  │  Agent   │  │  Agent   │
    └────┬─────┘  └────┬─────┘  └────┬─────┘
         │             │             │
    ┌────▼─────┐  ┌───▼──────┐  ┌───▼──────┐
    │DuckDuck  │  │  Gemini  │  │  Gemini  │
    │Go Search │  │   API    │  │   API    │
    └──────────┘  └──────────┘  └──────────┘
```

### Workflow Pipeline

1. **Search Agent** → Searches DuckDuckGo for automotive news articles
2. **Summarization Agent** → Generates concise summaries using Google Gemini
3. **Sentiment Analysis Agent** → Analyzes sentiment and provides confidence scores

All agents communicate through a shared state managed by **LangGraph**, ensuring reliable execution and error handling.

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/barreag/auto_news_with_sentiment_analysis.git
   cd auto_news_with_sentiment_analysis
   ```
2. **Create and activate virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   # Required
   GOOGLE_API_KEY=your_google_gemini_api_key_here

   # Optional - Companies to analyze (comma-separated)
   COMPANIES=GM,Ford,Tesla

   # Optional - Market focus
   MARKET=US

   # Optional - Search settings
   NEWS_DAYS_BACK=7
   MAX_RESULTS_PER_COMPANY=10
   SEARCH_DELAY_SECONDS=3.0

   # Optional - Model settings
   TEMPERATURE=0.5
   MAX_TOKENS=2000
   ```

### Usage

**Basic usage** (analyzes default companies: GM, Ford, Tesla):

```bash
python main.py
```

**Analyze specific companies**:

```bash
python main.py --companies GM Ford
```

**Custom market focus**:

```bash
python main.py --market Europe --companies BMW Mercedes Volkswagen
```

**Choose output format**:

```bash
# JSON only
python main.py --output-format json

# CSV only
python main.py --output-format csv

# Both formats (default)
python main.py --output-format both
```

**Suppress console output**:

```bash
python main.py --no-console
```

## Output Examples

### Console Output

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
          "title": "GM Announces Record EV Sales in Q4",
          "url": "https://example.com/article",
          "snippet": "General Motors reported...",
          "source": "AutoNews",
          "summary": "GM reported record EV sales with 50% year-over-year growth...",
          "sentiment": "positive",
          "confidence": 0.92,
          "reasoning": "Article discusses strong sales growth and positive market reception"
        }
      ]
    }
  ]
}
```

## Project Structure

```
auto_news_sentiment_analysis/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── .env                         # Environment configuration (create this)
├── LICENSE                      # MIT License
├── README.md                    # This file
│
├── config/                      # Configuration management
│   ├── __init__.py
│   └── settings.py              # Settings and environment variables
│
├── src/                         # Source code
│   ├── __init__.py
│   ├── agents/                  # Agent implementations
│   │   ├── __init__.py
│   │   ├── search_agent.py      # News search agent
│   │   ├── summarize_agent.py   # Summarization agent
│   │   └── sentiment_agent.py   # Sentiment analysis agent
│   │
│   ├── tools/                   # Custom tools
│   │   ├── __init__.py
│   │   └── search_tool.py       # DuckDuckGo search wrapper
│   │
│   ├── utils/                   # Utility functions
│   │   ├── __init__.py
│   │   ├── logger.py            # Logging utilities
│   │   └── output_handler.py    # Output formatting and saving
│   │
│   └── workflows/               # LangGraph workflows
│       ├── __init__.py
│       └── news_workflow.py     # Main workflow orchestration
│
├── tests/                       # Unit tests
│   ├── __init__.py
│   └── test_agents.py           # Agent tests
│
├── outputs/                     # Generated analysis results
│   └── *.json, *.csv
│
└── docs/                        # Documentation
    ├── architecture.md          # System architecture details
    ├── usage_guide.md           # Comprehensive usage guide
    └── PROJECT_SETUP_COMPLETE.md
```

## Technology Stack

- **Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph) - Multi-agent workflow management
- **Agent Framework**: [LangChain](https://github.com/langchain-ai/langchain) - Agent tools and LLM integrations
- **LLM**: [Google Gemini API](https://ai.google.dev/) - Summarization and sentiment analysis
- **Search**: [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search) - News article discovery
- **Data Processing**: Pandas, NumPy
- **Testing**: pytest

## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/test_agents.py
```

## Security & Best Practices

- API keys stored securely in environment variables
- No sensitive data in source control
- Input validation on all user inputs
- Secure HTTPS API communication
- Error handling and graceful degradation
- Rate limiting to respect API quotas

## Scalability & Extensibility

### Adding New Companies

Simply update the `COMPANIES` variable in `.env`:

```env
COMPANIES=GM,Ford,Tesla,BMW,Mercedes,Volkswagen
```

### Adding New Markets

Update the `MARKET` variable:

```env
MARKET=Europe
```

### Adding New Agents

1. Create a new agent in `src/agents/`
2. Add the agent to the workflow in `src/workflows/news_workflow.py`
3. Define edges in the LangGraph pipeline

### Parallel Processing

The architecture supports parallel processing for analyzing multiple companies simultaneously. Implement in the workflow if needed.

## Configuration Options

| Variable                    | Default           | Description                       |
| --------------------------- | ----------------- | --------------------------------- |
| `GOOGLE_API_KEY`          | *(required)*    | Google Gemini API key             |
| `COMPANIES`               | `GM,Ford,Tesla` | Comma-separated list of companies |
| `MARKET`                  | `US`            | Market focus for news search      |
| `NEWS_DAYS_BACK`          | `7`             | How many days back to search      |
| `MAX_RESULTS_PER_COMPANY` | `10`            | Maximum articles per company      |
| `SEARCH_DELAY_SECONDS`    | `3.0`           | Delay between search requests     |
| `TEMPERATURE`             | `0.5`           | LLM temperature (0-1)             |
| `MAX_TOKENS`              | `2000`          | Maximum tokens for LLM responses  |

## Troubleshooting

### "GOOGLE_API_KEY is required"

Make sure you've created a `.env` file with your API key:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### Import Errors

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### No Articles Found

- Check your internet connection
- Verify the company names are correct
- Try extending `NEWS_DAYS_BACK` in `.env`
- Wait a few minutes if rate-limited

### API Rate Limiting

- Reduce `MAX_RESULTS_PER_COMPANY` in `.env`
- Increase `SEARCH_DELAY_SECONDS`
- Check your API quota at [Google Cloud Console](https://console.cloud.google.com/)

## Roadmap

- [ ] **Database Integration**: Store historical results for trend analysis
- [ ] **Web Interface**: Flask/FastAPI frontend with interactive dashboards
- [ ] **Real-time Monitoring**: WebSocket updates for live news feeds
- [ ] **Advanced Analytics**: Time-series analysis and trend detection
- [ ] **Multi-language Support**: Analyze news in multiple languages
- [ ] **Email Reports**: Automated daily/weekly summary reports
- [ ] **Stock Correlation**: Link sentiment to stock price movements
- [ ] **Comparison Views**: Side-by-side company analysis

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact & Support

- **GitHub Issues**: [Create an issue](https://github.com/barreag/auto_news_with_sentiment_analysis/issues)
- **Documentation**: See the [docs](docs/) folder for detailed guides

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) & [LangGraph](https://github.com/langchain-ai/langgraph) for the agent framework
- [Google Gemini](https://ai.google.dev/) for powerful AI capabilities
- [DuckDuckGo](https://duckduckgo.com/) for search functionality

---

**Built with LangGraph, LangChain, and Google Gemini AI**
