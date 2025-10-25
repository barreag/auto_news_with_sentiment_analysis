# 🚗 Automotive News Sentiment Analysis System# Automotive News Sentiment Analysis



[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)A multi-agent system that searches, summarizes, and analyzes sentiment for automotive news from GM, Ford, and Tesla in the US market. Built with LangGraph for agent orchestration, LangChain for agent tools, and Google Gemini API for LLM capabilities.

[![LangChain](https://img.shields.io/badge/LangChain-Latest-green)](https://www.langchain.com/)

[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)](https://langchain-ai.github.io/langgraph/)## 🚀 Features

[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-red)](https://ai.google.dev/)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)- **Multi-Agent Architecture**: Three specialized agents working in orchestration

  - **News Search Agent**: Searches DuckDuckGo for automotive news from the past 7 days

A sophisticated multi-agent system that automatically searches, summarizes, and analyzes sentiment in automotive industry news. Built with **LangGraph** for orchestration, **LangChain** for agent tools, and **Google Gemini 2.5** for AI-powered analysis.  - **Summarization Agent**: Creates concise summaries of news articles

  - **Sentiment Analysis Agent**: Analyzes sentiment and enriches summaries

---- **LangGraph Orchestration**: Efficient workflow management between agents

- **Real-time News**: Focused on US market automotive news

## 🌟 Features- **Automated Pipeline**: From search to sentiment analysis in one execution



- **🔍 Intelligent News Search**: Automated DuckDuckGo searches with rate limiting protection## 📋 Requirements

- **📝 AI-Powered Summarization**: Concise 2-3 sentence summaries using Google Gemini 2.5

- **😊 Advanced Sentiment Analysis**: Classification (positive/negative/neutral) with confidence scores (0.90-0.98)- Python 3.9+

- **🤖 Multi-Agent Architecture**: Three specialized agents orchestrated by LangGraph- Google Gemini API key

- **💾 Multiple Output Formats**: JSON and CSV export with timestamped files- Internet connection for news search

- **⚙️ Highly Configurable**: Environment-based configuration via `.env` file

- **🛡️ Production-Ready**: Built-in error handling, retry logic, and rate limiting## 🛠️ Installation



---1. **Clone the repository**

   ```bash

## 🏗️ Architecture   git clone https://github.com/yourusername/auto_news_sentiment_analysis.git

   cd auto_news_sentiment_analysis

```   ```

┌─────────────────────────────────────────────────────────┐

│                  LangGraph Orchestrator                  │2. **Create a virtual environment**

│                    (Sequential Pipeline)                 │   ```bash

└─────────────────────────────────────────────────────────┘   python -m venv venv

                            │   # On Windows

        ┌───────────────────┼───────────────────┐   venv\Scripts\activate

        ▼                   ▼                   ▼   # On macOS/Linux

┌──────────────┐   ┌─────────────────┐  ┌────────────────┐   source venv/bin/activate

│ Search Agent │ → │ Summarize Agent │→ │ Sentiment Agent│   ```

│              │   │                 │  │                │

│ DuckDuckGo   │   │   Gemini 2.5    │  │  Gemini 2.5    │3. **Install dependencies**

│   + Retry    │   │   (2-3 sent.)   │  │  (with conf.)  │   ```bash

└──────────────┘   └─────────────────┘  └────────────────┘   pip install -r requirements.txt

        │                   │                   │   ```

        ▼                   ▼                   ▼

   5 articles         Summaries            Sentiment4. **Set up environment variables**

   per search        + context          + confidence   ```bash

```   # Copy the example environment file

   copy .env.example .env  # Windows

### Agent Workflow   # cp .env.example .env  # macOS/Linux

   ```

1. **Search Agent**: Searches for automotive news using DuckDuckGo (3-second delays between requests)   

2. **Summarization Agent**: Creates business-focused summaries for each article   Edit `.env` and add your Google Gemini API key:

3. **Sentiment Agent**: Analyzes sentiment with confidence scores and reasoning   ```

   GOOGLE_API_KEY=your_actual_api_key_here

---   ```



## 🚀 Quick Start## 🎯 Usage



### Prerequisites### Basic Usage



- **Python 3.11+** (recommended: 3.11.6)Run the main script to execute the multi-agent pipeline:

- **Google Gemini API key** → [Get one FREE here](https://makersuite.google.com/app/apikey)

- Internet connection```bash

python main.py

### Installation```



```bashThis will:

# 1. Clone the repository1. Search for recent automotive news for GM, Ford, and Tesla

git clone https://github.com/yourusername/auto_news_sentiment_analysis.git2. Summarize each article found

cd auto_news_sentiment_analysis3. Analyze sentiment for each article

4. Save results to `outputs/` directory

# 2. Create and activate virtual environment

# Windows:### Configuration

python -m venv agent_env

.\agent_env\Scripts\activateYou can customize the behavior by editing `.env`:



# Linux/Mac:```env

python -m venv agent_env# Companies to track (comma-separated)

source agent_env/bin/activateCOMPANIES=GM,Ford,Tesla



# 3. Install dependencies# Market focus

pip install -r requirements.txtMARKET=US



# 4. Configure environment variables# News search settings

copy .env.example .env  # WindowsNEWS_DAYS_BACK=7

cp .env.example .env    # Linux/MacMAX_RESULTS_PER_COMPANY=10



# 5. Edit .env and add your Google Gemini API key# Agent settings

# GOOGLE_API_KEY=your_actual_api_key_hereTEMPERATURE=0.7

```MAX_TOKENS=2000

```

### Basic Usage

## 📁 Project Structure

```bash

# Run with default companies (GM, Ford, Tesla)```

python main.pyauto_news_sentiment_analysis/

├── .github/

# Analyze specific companies│   └── workflows/

python main.py --companies GM Ford│       └── main.yml              # CI/CD pipeline

├── .gitignore                    # Git ignore rules

# Output formats├── README.md                     # Project documentation

python main.py --output-format json   # JSON only├── requirements.txt              # Python dependencies

python main.py --output-format csv    # CSV only├── .env.example                  # Example environment variables

python main.py --output-format both   # Both formats (default)├── main.py                       # Main application entry point

├── config/

# Suppress console output│   └── settings.py               # Configuration management

python main.py --no-console├── src/

```│   ├── __init__.py

│   ├── agents/

---│   │   ├── __init__.py

│   │   ├── search_agent.py       # News search agent

## ⚙️ Configuration│   │   ├── summarize_agent.py    # Summarization agent

│   │   └── sentiment_agent.py    # Sentiment analysis agent

Customize behavior by editing the `.env` file:│   ├── workflows/

│   │   ├── __init__.py

```env│   │   └── news_workflow.py      # LangGraph orchestration

# ========== REQUIRED ==========│   ├── tools/

# Get your key at: https://makersuite.google.com/app/apikey│   │   ├── __init__.py

GOOGLE_API_KEY=your_api_key_here│   │   └── search_tool.py        # DuckDuckGo search tool

│   └── utils/

# ========== TARGET CONFIGURATION ==========│       ├── __init__.py

COMPANIES=GM,Ford,Tesla    # Comma-separated company names│       ├── logger.py             # Logging utilities

MARKET=US                  # Market focus│       └── output_handler.py     # Output formatting

├── data/

# ========== SEARCH SETTINGS ==========│   ├── raw/                      # Raw news data

NEWS_DAYS_BACK=7                # Days of historical news to search│   └── processed/                # Processed results

MAX_RESULTS_PER_COMPANY=5       # Articles per company (lower = faster)├── outputs/                      # Generated reports

SEARCH_DELAY_SECONDS=3.0        # Delay between searches (avoid rate limits)├── docs/

│   └── architecture.md           # System architecture docs

# ========== LLM SETTINGS ==========└── tests/

TEMPERATURE=0.5                 # Model creativity (0.0-1.0, 0.5 = balanced)    ├── __init__.py

MAX_TOKENS=2000                # Maximum response length    └── test_agents.py            # Unit tests

``````



---## 🏗️ Architecture



## 📊 Output ExamplesThe system uses a **multi-agent architecture** orchestrated by LangGraph:



### Console Output1. **Search Agent** → Queries DuckDuckGo for automotive news

```2. **Summarization Agent** → Processes and summarizes articles

================================================================================3. **Sentiment Agent** → Analyzes sentiment and enriches data

AUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT

================================================================================Each agent is powered by Google Gemini API and uses LangChain tools for enhanced capabilities.



Generated: 2025-10-25 19:07:30## 🧪 Testing

Companies Analyzed: GM, Ford, Tesla

Total Articles: 5Run tests with pytest:



********************************************************************************```bash

COMPANY: GM,Ford,Teslapytest tests/

********************************************************************************```



[1] Auto Stocks Surge as Carmakers Navigate Policy Shifts## 📊 Output

    Sentiment: positive (Confidence: 0.98)

    Summary: Auto stocks, notably GM and Ford, are surging as investors Results are saved in JSON format in the `outputs/` directory with timestamps:

    react positively to strong sales performance. This market enthusiasm - News articles with titles, URLs, and snippets

    is further bolstered by favorable shifts in federal policy...- Summaries for each article

- Sentiment scores (positive/negative/neutral) with confidence

[2] GM bets big on electric cars even as market slows

    Sentiment: negative (Confidence: 0.90)## 🤝 Contributing

    Summary: General Motors continues its aggressive EV investment strategy 

    despite an anticipated industry-wide sales slowdown...Contributions are welcome! Please feel free to submit a Pull Request.



================================================================================1. Fork the repository

Sentiment Distribution:2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

  Positive: 3 (60%)3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

  Negative: 2 (40%)4. Push to the branch (`git push origin feature/AmazingFeature`)

  Neutral: 0 (0%)5. Open a Pull Request

================================================================================

```## 📝 License



### JSON Output StructureThis project is licensed under the MIT License - see the LICENSE file for details.

```json

{## 🙏 Acknowledgments

  "metadata": {

    "timestamp": "2025-10-25T19:07:30",- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration

    "companies": ["GM", "Ford", "Tesla"],- [LangChain](https://github.com/langchain-ai/langchain) for agent tools

    "total_articles": 5,- [Google Gemini](https://ai.google.dev/) for LLM capabilities

    "sentiment_distribution": {- [DuckDuckGo](https://duckduckgo.com/) for news search

      "positive": 3,

      "negative": 2,## 📧 Contact

      "neutral": 0

    }Your Name - [@yourhandle](https://twitter.com/yourhandle)

  },

  "all_articles": [Project Link: [https://github.com/yourusername/auto_news_sentiment_analysis](https://github.com/yourusername/auto_news_sentiment_analysis)

    {
      "company": "GM,Ford,Tesla",
      "title": "Article Title",
      "url": "https://...",
      "snippet": "Original content...",
      "summary": "AI-generated summary...",
      "sentiment": "positive",
      "confidence": 0.98,
      "reasoning": "Explanation...",
      "date": "2025-10-25",
      "source": "Source Name"
    }
  ]
}
```

---

## 📁 Project Structure

```
auto_news_sentiment_analysis/
├── .env.example              # Example environment configuration
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── main.py                # Application entry point
├── list_models.py         # Utility to list available Gemini models
│
├── config/
│   └── settings.py        # Centralized configuration management
│
├── src/
│   ├── agents/
│   │   ├── search_agent.py      # News search with DuckDuckGo
│   │   ├── summarize_agent.py   # Article summarization
│   │   └── sentiment_agent.py   # Sentiment analysis
│   ├── workflows/
│   │   └── news_workflow.py     # LangGraph orchestration
│   ├── tools/
│   │   └── search_tool.py       # DuckDuckGo search wrapper
│   └── utils/
│       ├── logger.py            # Logging utilities
│       └── output_handler.py    # Output formatting (JSON/CSV)
│
├── outputs/                 # Generated results (timestamped)
├── tests/                  # Unit tests
└── docs/                   # Additional documentation
```

---

## 🔧 Troubleshooting

### Rate Limiting Issues
**Problem**: DuckDuckGo returns `202 Ratelimit` error

**Solutions**:
1. Increase `SEARCH_DELAY_SECONDS` to `5.0` or higher in `.env`
2. Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower
3. Wait 5-10 minutes between runs

### Gemini API Errors
**Problem**: `404 models/gemini-1.5-flash is not found`

**Solution**:
```bash
# Check available models
python list_models.py

# Update MODEL_NAME in config/settings.py if needed
```

### Common Issues

| Error | Solution |
|-------|----------|
| `GOOGLE_API_KEY is required` | Add your API key to `.env` file |
| Import errors | Ensure virtual environment is activated |
| No articles found | Try different companies or increase `NEWS_DAYS_BACK` |
| Slow performance | Reduce `MAX_RESULTS_PER_COMPANY` or `COMPANIES` list |

---

## 📈 Performance Metrics

- **Processing Time**: ~15-45 seconds for 3 companies (5 articles each)
- **API Calls**: ~16 calls total (1 search + 15 LLM calls)
- **Success Rate**: 100% with proper configuration
- **Confidence Scores**: 0.90-0.98 (high accuracy)

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/test_agents.py
```

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework
- **[LangChain](https://www.langchain.com/)** - Agent tools and LLM integrations
- **[Google Gemini](https://ai.google.dev/)** - Advanced AI capabilities (Gemini 2.5 Flash)
- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine

---

## 📧 Support

- 📖 **Documentation**: Check the `/docs` folder
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/auto_news_sentiment_analysis/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/auto_news_sentiment_analysis/discussions)

---

**Built with ❤️ for the automotive industry**

*Powered by LangGraph + LangChain + Google Gemini 2.5*
