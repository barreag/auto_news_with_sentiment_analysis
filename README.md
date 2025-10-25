# Automotive News Sentiment Analysis System# 🚗 Automotive News Sentiment Analysis System# Automotive News Sentiment Analysis



[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)

[![LangChain](https://img.shields.io/badge/LangChain-Latest-green)](https://www.langchain.com/)

[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)](https://langchain-ai.github.io/langgraph/)[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)A multi-agent system that searches, summarizes, and analyzes sentiment for automotive news from GM, Ford, and Tesla in the US market. Built with LangGraph for agent orchestration, LangChain for agent tools, and Google Gemini API for LLM capabilities.

[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-red)](https://ai.google.dev/)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)[![LangChain](https://img.shields.io/badge/LangChain-Latest-green)](https://www.langchain.com/)



A sophisticated multi-agent system that automatically searches, summarizes, and analyzes sentiment in automotive industry news. Built with **LangGraph** for orchestration, **LangChain** for agent tools, and **Google Gemini 2.5** for AI-powered analysis.[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)](https://langchain-ai.github.io/langgraph/)## 🚀 Features



---[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-red)](https://ai.google.dev/)



## Features[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)- **Multi-Agent Architecture**: Three specialized agents working in orchestration



- **Intelligent News Search**: Automated DuckDuckGo searches with rate limiting protection  - **News Search Agent**: Searches DuckDuckGo for automotive news from the past 7 days

- **AI-Powered Summarization**: Concise 2-3 sentence summaries using Google Gemini 2.5

- **Advanced Sentiment Analysis**: Classification (positive/negative/neutral) with confidence scores (0.90-0.98)A sophisticated multi-agent system that automatically searches, summarizes, and analyzes sentiment in automotive industry news. Built with **LangGraph** for orchestration, **LangChain** for agent tools, and **Google Gemini 2.5** for AI-powered analysis.  - **Summarization Agent**: Creates concise summaries of news articles

- **Multi-Agent Architecture**: Three specialized agents orchestrated by LangGraph

- **Multiple Output Formats**: JSON and CSV export with timestamped files  - **Sentiment Analysis Agent**: Analyzes sentiment and enriches summaries

- **Highly Configurable**: Environment-based configuration via `.env` file

- **Production-Ready**: Built-in error handling, retry logic, and rate limiting---- **LangGraph Orchestration**: Efficient workflow management between agents



---- **Real-time News**: Focused on US market automotive news



## Architecture## 🌟 Features- **Automated Pipeline**: From search to sentiment analysis in one execution



```

┌─────────────────────────────────────────────────────────┐

│                  LangGraph Orchestrator                  │- **🔍 Intelligent News Search**: Automated DuckDuckGo searches with rate limiting protection## 📋 Requirements

│                    (Sequential Pipeline)                 │

└─────────────────────────────────────────────────────────┘- **📝 AI-Powered Summarization**: Concise 2-3 sentence summaries using Google Gemini 2.5

                            │

        ┌───────────────────┼───────────────────┐- **😊 Advanced Sentiment Analysis**: Classification (positive/negative/neutral) with confidence scores (0.90-0.98)- Python 3.9+

        ▼                   ▼                   ▼

┌──────────────┐   ┌─────────────────┐  ┌────────────────┐- **🤖 Multi-Agent Architecture**: Three specialized agents orchestrated by LangGraph- Google Gemini API key

│ Search Agent │ → │ Summarize Agent │→ │ Sentiment Agent│

│              │   │                 │  │                │- **💾 Multiple Output Formats**: JSON and CSV export with timestamped files- Internet connection for news search

│ DuckDuckGo   │   │   Gemini 2.5    │  │  Gemini 2.5    │

│   + Retry    │   │   (2-3 sent.)   │  │  (with conf.)  │- **⚙️ Highly Configurable**: Environment-based configuration via `.env` file

└──────────────┘   └─────────────────┘  └────────────────┘

        │                   │                   │- **🛡️ Production-Ready**: Built-in error handling, retry logic, and rate limiting## 🛠️ Installation

        ▼                   ▼                   ▼

   5 articles         Summaries            Sentiment

   per search        + context          + confidence

```---1. **Clone the repository**



### Agent Workflow   ```bash



1. **Search Agent**: Searches for automotive news using DuckDuckGo (3-second delays between requests)## 🏗️ Architecture   git clone https://github.com/yourusername/auto_news_sentiment_analysis.git

2. **Summarization Agent**: Creates business-focused summaries for each article

3. **Sentiment Agent**: Analyzes sentiment with confidence scores and reasoning   cd auto_news_sentiment_analysis



---```   ```



## Quick Start┌─────────────────────────────────────────────────────────┐



### Prerequisites│                  LangGraph Orchestrator                  │2. **Create a virtual environment**



- **Python 3.11+** (recommended: 3.11.6)│                    (Sequential Pipeline)                 │   ```bash

- **Google Gemini API key** → [Get one FREE here](https://makersuite.google.com/app/apikey)

- Internet connection└─────────────────────────────────────────────────────────┘   python -m venv venv



### Installation                            │   # On Windows



```bash        ┌───────────────────┼───────────────────┐   venv\Scripts\activate

# 1. Clone the repository

git clone https://github.com/barreag/auto_news_with_sentiment_analysis.git        ▼                   ▼                   ▼   # On macOS/Linux

cd auto_news_with_sentiment_analysis

┌──────────────┐   ┌─────────────────┐  ┌────────────────┐   source venv/bin/activate

# 2. Create and activate virtual environment

# Windows:│ Search Agent │ → │ Summarize Agent │→ │ Sentiment Agent│   ```

python -m venv agent_env

.\agent_env\Scripts\activate│              │   │                 │  │                │



# Linux/Mac:│ DuckDuckGo   │   │   Gemini 2.5    │  │  Gemini 2.5    │3. **Install dependencies**

python -m venv agent_env

source agent_env/bin/activate│   + Retry    │   │   (2-3 sent.)   │  │  (with conf.)  │   ```bash



# 3. Install dependencies└──────────────┘   └─────────────────┘  └────────────────┘   pip install -r requirements.txt

pip install -r requirements.txt

        │                   │                   │   ```

# 4. Configure environment variables

copy .env.example .env  # Windows        ▼                   ▼                   ▼

cp .env.example .env    # Linux/Mac

   5 articles         Summaries            Sentiment4. **Set up environment variables**

# 5. Edit .env and add your Google Gemini API key

# GOOGLE_API_KEY=your_actual_api_key_here   per search        + context          + confidence   ```bash

```

```   # Copy the example environment file

### Basic Usage

   copy .env.example .env  # Windows

```bash

# Run with default companies (GM, Ford, Tesla)### Agent Workflow   # cp .env.example .env  # macOS/Linux

python main.py

   ```

# Analyze specific companies

python main.py --companies GM Ford1. **Search Agent**: Searches for automotive news using DuckDuckGo (3-second delays between requests)   



# Output formats2. **Summarization Agent**: Creates business-focused summaries for each article   Edit `.env` and add your Google Gemini API key:

python main.py --output-format json   # JSON only

python main.py --output-format csv    # CSV only3. **Sentiment Agent**: Analyzes sentiment with confidence scores and reasoning   ```

python main.py --output-format both   # Both formats (default)

   GOOGLE_API_KEY=your_actual_api_key_here

# Suppress console output

python main.py --no-console---   ```

```



---

## 🚀 Quick Start## 🎯 Usage

## Configuration



Customize behavior by editing the `.env` file:

### Prerequisites### Basic Usage

```env

# ========== REQUIRED ==========

# Get your key at: https://makersuite.google.com/app/apikey

GOOGLE_API_KEY=your_api_key_here- **Python 3.11+** (recommended: 3.11.6)Run the main script to execute the multi-agent pipeline:



# ========== TARGET CONFIGURATION ==========- **Google Gemini API key** → [Get one FREE here](https://makersuite.google.com/app/apikey)

COMPANIES=GM,Ford,Tesla    # Comma-separated company names

MARKET=US                  # Market focus- Internet connection```bash



# ========== SEARCH SETTINGS ==========python main.py

NEWS_DAYS_BACK=7                # Days of historical news to search

MAX_RESULTS_PER_COMPANY=5       # Articles per company (lower = faster)### Installation```

SEARCH_DELAY_SECONDS=3.0        # Delay between searches (avoid rate limits)



# ========== LLM SETTINGS ==========

TEMPERATURE=0.5                 # Model creativity (0.0-1.0, 0.5 = balanced)```bashThis will:

MAX_TOKENS=2000                # Maximum response length

```# 1. Clone the repository1. Search for recent automotive news for GM, Ford, and Tesla



---git clone https://github.com/yourusername/auto_news_sentiment_analysis.git2. Summarize each article found



## Output Examplescd auto_news_sentiment_analysis3. Analyze sentiment for each article



### Console Output4. Save results to `outputs/` directory

```

================================================================================# 2. Create and activate virtual environment

AUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT

================================================================================# Windows:### Configuration



Generated: 2025-10-25 19:07:30python -m venv agent_env

Companies Analyzed: GM, Ford, Tesla

Total Articles: 5.\agent_env\Scripts\activateYou can customize the behavior by editing `.env`:



********************************************************************************

COMPANY: GM,Ford,Tesla

********************************************************************************# Linux/Mac:```env



[1] Auto Stocks Surge as Carmakers Navigate Policy Shiftspython -m venv agent_env# Companies to track (comma-separated)

    Sentiment: positive (Confidence: 0.98)

    Summary: Auto stocks, notably GM and Ford, are surging as investors source agent_env/bin/activateCOMPANIES=GM,Ford,Tesla

    react positively to strong sales performance. This market enthusiasm 

    is further bolstered by favorable shifts in federal policy...



[2] GM bets big on electric cars even as market slows# 3. Install dependencies# Market focus

    Sentiment: negative (Confidence: 0.90)

    Summary: General Motors continues its aggressive EV investment strategy pip install -r requirements.txtMARKET=US

    despite an anticipated industry-wide sales slowdown...



================================================================================

Sentiment Distribution:# 4. Configure environment variables# News search settings

  Positive: 3 (60%)

  Negative: 2 (40%)copy .env.example .env  # WindowsNEWS_DAYS_BACK=7

  Neutral: 0 (0%)

================================================================================cp .env.example .env    # Linux/MacMAX_RESULTS_PER_COMPANY=10

```



### JSON Output Structure

```json# 5. Edit .env and add your Google Gemini API key# Agent settings

{

  "metadata": {# GOOGLE_API_KEY=your_actual_api_key_hereTEMPERATURE=0.7

    "timestamp": "2025-10-25T19:07:30",

    "companies": ["GM", "Ford", "Tesla"],```MAX_TOKENS=2000

    "total_articles": 5,

    "sentiment_distribution": {```

      "positive": 3,

      "negative": 2,### Basic Usage

      "neutral": 0

    }## 📁 Project Structure

  },

  "all_articles": [```bash

    {

      "company": "GM,Ford,Tesla",# Run with default companies (GM, Ford, Tesla)```

      "title": "Article Title",

      "url": "https://...",python main.pyauto_news_sentiment_analysis/

      "snippet": "Original content...",

      "summary": "AI-generated summary...",├── .github/

      "sentiment": "positive",

      "confidence": 0.98,# Analyze specific companies│   └── workflows/

      "reasoning": "Explanation...",

      "date": "2025-10-25",python main.py --companies GM Ford│       └── main.yml              # CI/CD pipeline

      "source": "Source Name"

    }├── .gitignore                    # Git ignore rules

  ]

}# Output formats├── README.md                     # Project documentation

```

python main.py --output-format json   # JSON only├── requirements.txt              # Python dependencies

---

python main.py --output-format csv    # CSV only├── .env.example                  # Example environment variables

## Project Structure

python main.py --output-format both   # Both formats (default)├── main.py                       # Main application entry point

```

auto_news_sentiment_analysis/├── config/

├── .env.example              # Example environment configuration

├── .gitignore               # Git ignore rules# Suppress console output│   └── settings.py               # Configuration management

├── LICENSE                  # MIT License

├── README.md               # This filepython main.py --no-console├── src/

├── requirements.txt        # Python dependencies

├── main.py                # Application entry point```│   ├── __init__.py

├── list_models.py         # Utility to list available Gemini models

││   ├── agents/

├── config/

│   └── settings.py        # Centralized configuration management---│   │   ├── __init__.py

│

├── src/│   │   ├── search_agent.py       # News search agent

│   ├── agents/

│   │   ├── search_agent.py      # News search with DuckDuckGo## ⚙️ Configuration│   │   ├── summarize_agent.py    # Summarization agent

│   │   ├── summarize_agent.py   # Article summarization

│   │   └── sentiment_agent.py   # Sentiment analysis│   │   └── sentiment_agent.py    # Sentiment analysis agent

│   ├── workflows/

│   │   └── news_workflow.py     # LangGraph orchestrationCustomize behavior by editing the `.env` file:│   ├── workflows/

│   ├── tools/

│   │   └── search_tool.py       # DuckDuckGo search wrapper│   │   ├── __init__.py

│   └── utils/

│       ├── logger.py            # Logging utilities```env│   │   └── news_workflow.py      # LangGraph orchestration

│       └── output_handler.py    # Output formatting (JSON/CSV)

│# ========== REQUIRED ==========│   ├── tools/

├── outputs/                 # Generated results (timestamped)

├── tests/                  # Unit tests# Get your key at: https://makersuite.google.com/app/apikey│   │   ├── __init__.py

└── docs/                   # Additional documentation

```GOOGLE_API_KEY=your_api_key_here│   │   └── search_tool.py        # DuckDuckGo search tool



---│   └── utils/



## Troubleshooting# ========== TARGET CONFIGURATION ==========│       ├── __init__.py



### Rate Limiting IssuesCOMPANIES=GM,Ford,Tesla    # Comma-separated company names│       ├── logger.py             # Logging utilities

**Problem**: DuckDuckGo returns `202 Ratelimit` error

MARKET=US                  # Market focus│       └── output_handler.py     # Output formatting

**Solutions**:

1. Increase `SEARCH_DELAY_SECONDS` to `5.0` or higher in `.env`├── data/

2. Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower

3. Wait 5-10 minutes between runs# ========== SEARCH SETTINGS ==========│   ├── raw/                      # Raw news data



### Gemini API ErrorsNEWS_DAYS_BACK=7                # Days of historical news to search│   └── processed/                # Processed results

**Problem**: `404 models/gemini-1.5-flash is not found`

MAX_RESULTS_PER_COMPANY=5       # Articles per company (lower = faster)├── outputs/                      # Generated reports

**Solution**:

```bashSEARCH_DELAY_SECONDS=3.0        # Delay between searches (avoid rate limits)├── docs/

# Check available models

python list_models.py│   └── architecture.md           # System architecture docs



# Update MODEL_NAME in config/settings.py if needed# ========== LLM SETTINGS ==========└── tests/

```

TEMPERATURE=0.5                 # Model creativity (0.0-1.0, 0.5 = balanced)    ├── __init__.py

### Common Issues

MAX_TOKENS=2000                # Maximum response length    └── test_agents.py            # Unit tests

| Error | Solution |

|-------|----------|``````

| `GOOGLE_API_KEY is required` | Add your API key to `.env` file |

| Import errors | Ensure virtual environment is activated |

| No articles found | Try different companies or increase `NEWS_DAYS_BACK` |

| Slow performance | Reduce `MAX_RESULTS_PER_COMPANY` or `COMPANIES` list |---## 🏗️ Architecture



---



## Performance Metrics## 📊 Output ExamplesThe system uses a **multi-agent architecture** orchestrated by LangGraph:



- **Processing Time**: ~15-45 seconds for 3 companies (5 articles each)

- **API Calls**: ~16 calls total (1 search + 15 LLM calls)

- **Success Rate**: 100% with proper configuration### Console Output1. **Search Agent** → Queries DuckDuckGo for automotive news

- **Confidence Scores**: 0.90-0.98 (high accuracy)

```2. **Summarization Agent** → Processes and summarizes articles

---

================================================================================3. **Sentiment Agent** → Analyzes sentiment and enriches data

## Testing

AUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT

```bash

# Run all tests================================================================================Each agent is powered by Google Gemini API and uses LangChain tools for enhanced capabilities.

pytest tests/



# Run with coverage

pytest tests/ --cov=srcGenerated: 2025-10-25 19:07:30## 🧪 Testing



# Run specific test fileCompanies Analyzed: GM, Ford, Tesla

pytest tests/test_agents.py

```Total Articles: 5Run tests with pytest:



---



## Contributing********************************************************************************```bash



Contributions welcome! Please follow these steps:COMPANY: GM,Ford,Teslapytest tests/



1. Fork the repository********************************************************************************```

2. Create feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit changes (`git commit -m 'Add AmazingFeature'`)

4. Push to branch (`git push origin feature/AmazingFeature`)

5. Open Pull Request[1] Auto Stocks Surge as Carmakers Navigate Policy Shifts## 📊 Output



---    Sentiment: positive (Confidence: 0.98)



## License    Summary: Auto stocks, notably GM and Ford, are surging as investors Results are saved in JSON format in the `outputs/` directory with timestamps:



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.    react positively to strong sales performance. This market enthusiasm - News articles with titles, URLs, and snippets



---    is further bolstered by favorable shifts in federal policy...- Summaries for each article



## Acknowledgments- Sentiment scores (positive/negative/neutral) with confidence



- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework[2] GM bets big on electric cars even as market slows

- **[LangChain](https://www.langchain.com/)** - Agent tools and LLM integrations

- **[Google Gemini](https://ai.google.dev/)** - Advanced AI capabilities (Gemini 2.5 Flash)    Sentiment: negative (Confidence: 0.90)## 🤝 Contributing

- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine

    Summary: General Motors continues its aggressive EV investment strategy 

---

    despite an anticipated industry-wide sales slowdown...Contributions are welcome! Please feel free to submit a Pull Request.

## Support



- **Documentation**: Check the `/docs` folder

- **Issues**: [GitHub Issues](https://github.com/barreag/auto_news_with_sentiment_analysis/issues)================================================================================1. Fork the repository

- **Discussions**: [GitHub Discussions](https://github.com/barreag/auto_news_with_sentiment_analysis/discussions)

Sentiment Distribution:2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

---

  Positive: 3 (60%)3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

**Built with care for the automotive industry**

  Negative: 2 (40%)4. Push to the branch (`git push origin feature/AmazingFeature`)

*Powered by LangGraph + LangChain + Google Gemini 2.5*

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
