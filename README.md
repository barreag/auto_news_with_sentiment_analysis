# Automotive News Sentiment Analysis System# Automotive News Sentiment Analysis System# Automotive News Sentiment Analysis System# 🚗 Automotive News Sentiment Analysis System# Automotive News Sentiment Analysis



A production-ready multi-agent system for automated sentiment analysis of automotive industry news. This system intelligently searches, summarizes, and analyzes sentiment for news articles about major automotive companies in the US market.



[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)A production-ready multi-agent system for automated sentiment analysis of automotive industry news. This system intelligently searches, summarizes, and analyzes sentiment for news articles about major automotive companies in the US market.

[![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)](https://langchain-ai.github.io/langgraph/)

[![LangChain](https://img.shields.io/badge/LangChain-latest-orange.svg)](https://www.langchain.com/)

[![Google Gemini](https://img.shields.io/badge/Gemini-2.5--flash-red.svg)](https://ai.google.dev/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)



---[![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)](https://langchain-ai.github.io/langgraph/)



## Table of Contents[![LangChain](https://img.shields.io/badge/LangChain-latest-orange.svg)](https://www.langchain.com/)[![LangChain](https://img.shields.io/badge/LangChain-Latest-green)](https://www.langchain.com/)



- [Overview](#overview)[![Google Gemini](https://img.shields.io/badge/Gemini-2.5--flash-red.svg)](https://ai.google.dev/)

- [Key Features](#key-features)

- [System Architecture](#system-architecture)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)](https://langchain-ai.github.io/langgraph/)[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)A multi-agent system that searches, summarizes, and analyzes sentiment for automotive news from GM, Ford, and Tesla in the US market. Built with LangGraph for agent orchestration, LangChain for agent tools, and Google Gemini API for LLM capabilities.

- [Prerequisites](#prerequisites)

- [Installation](#installation)

- [Configuration](#configuration)

- [Usage](#usage)---[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-red)](https://ai.google.dev/)

- [Output Format](#output-format)

- [Project Structure](#project-structure)

- [How It Works](#how-it-works)

- [Troubleshooting](#troubleshooting)## Table of Contents[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)[![LangChain](https://img.shields.io/badge/LangChain-Latest-green)](https://www.langchain.com/)

- [Performance Optimization](#performance-optimization)

- [Contributing](#contributing)

- [License](#license)

- [Acknowledgments](#acknowledgments)- [Overview](#overview)



---- [Key Features](#key-features)



## Overview- [System Architecture](#system-architecture)A sophisticated multi-agent system that automatically searches, summarizes, and analyzes sentiment in automotive industry news. Built with **LangGraph** for orchestration, **LangChain** for agent tools, and **Google Gemini 2.5** for AI-powered analysis.[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-purple)](https://langchain-ai.github.io/langgraph/)## 🚀 Features



This system addresses the need for automated, scalable sentiment analysis of automotive industry news. By leveraging cutting-edge AI technologies, it provides:- [Prerequisites](#prerequisites)



- **Real-time insights** into market sentiment for major automotive companies- [Installation](#installation)

- **Automated workflow** from news discovery to sentiment classification

- **High accuracy** sentiment analysis with confidence scores (typically 0.90-0.98)- [Configuration](#configuration)

- **Scalable architecture** that can be extended to additional companies and markets

- [Usage](#usage)---[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-red)](https://ai.google.dev/)

### Why This Project?

- [Output Format](#output-format)

In the fast-paced automotive industry, staying informed about market sentiment is crucial. This system automates the time-consuming process of:

- [Project Structure](#project-structure)

1. Finding relevant news articles across multiple sources

2. Reading and summarizing lengthy articles- [How It Works](#how-it-works)

3. Determining sentiment and market implications

4. Aggregating insights across multiple companies- [Troubleshooting](#troubleshooting)## Features[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)- **Multi-Agent Architecture**: Three specialized agents working in orchestration



---- [Performance Optimization](#performance-optimization)



## Key Features- [Contributing](#contributing)



### Multi-Agent Architecture- [License](#license)



- **Search Agent**: Queries DuckDuckGo for recent automotive news with intelligent rate limiting- [Acknowledgments](#acknowledgments)- **Intelligent News Search**: Automated DuckDuckGo searches with rate limiting protection  - **News Search Agent**: Searches DuckDuckGo for automotive news from the past 7 days

- **Summarization Agent**: Creates concise, business-focused summaries using Google Gemini 2.5

- **Sentiment Agent**: Performs advanced sentiment analysis with confidence scoring



### Intelligent Orchestration---- **AI-Powered Summarization**: Concise 2-3 sentence summaries using Google Gemini 2.5



- **LangGraph-powered workflow**: Sequential pipeline ensuring data flows correctly between agents

- **Error handling**: Robust retry logic with exponential backoff for API rate limits

- **State management**: Maintains context throughout the multi-step analysis process## Overview- **Advanced Sentiment Analysis**: Classification (positive/negative/neutral) with confidence scores (0.90-0.98)A sophisticated multi-agent system that automatically searches, summarizes, and analyzes sentiment in automotive industry news. Built with **LangGraph** for orchestration, **LangChain** for agent tools, and **Google Gemini 2.5** for AI-powered analysis.  - **Summarization Agent**: Creates concise summaries of news articles



### Production-Ready Design



- **Environment-based configuration**: Easy deployment across different environmentsThis system addresses the need for automated, scalable sentiment analysis of automotive industry news. By leveraging cutting-edge AI technologies, it provides:- **Multi-Agent Architecture**: Three specialized agents orchestrated by LangGraph

- **Multiple output formats**: JSON and CSV exports with timestamps

- **Comprehensive logging**: Detailed execution logs for debugging and monitoring

- **Rate limiting protection**: Built-in delays and retry mechanisms for external APIs

- **Real-time insights** into market sentiment for major automotive companies- **Multiple Output Formats**: JSON and CSV export with timestamped files  - **Sentiment Analysis Agent**: Analyzes sentiment and enriches summaries

### High Performance

- **Automated workflow** from news discovery to sentiment classification

- **Processing speed**: Analyzes 15 articles in approximately 38-46 seconds

- **High accuracy**: Sentiment confidence scores consistently above 90%- **High accuracy** sentiment analysis with confidence scores (typically 0.90-0.98)- **Highly Configurable**: Environment-based configuration via `.env` file

- **Scalable**: Easily extend to monitor additional companies or markets

- **Scalable architecture** that can be extended to additional companies and markets

---

- **Production-Ready**: Built-in error handling, retry logic, and rate limiting---- **LangGraph Orchestration**: Efficient workflow management between agents

## System Architecture

### Why This Project?

```

┌─────────────────────────────────────────────────────────────────┐

│                    LangGraph Orchestrator                        │

│              (Sequential State Machine Pipeline)                 │In the fast-paced automotive industry, staying informed about market sentiment is crucial. This system automates the time-consuming process of:

└─────────────────────────────────────────────────────────────────┘

                               │1. Finding relevant news articles across multiple sources---- **Real-time News**: Focused on US market automotive news

                               │ Initial State:

                               │ {companies, market}2. Reading and summarizing lengthy articles

                               │

                               ▼3. Determining sentiment and market implications

┌──────────────────────────────────────────────────────────────────┐

│                        SEARCH AGENT                               │4. Aggregating insights across multiple companies

│  ┌────────────────────────────────────────────────────────────┐  │

│  │ • DuckDuckGo Search Tool                                   │  │## Architecture## 🌟 Features- **Automated Pipeline**: From search to sentiment analysis in one execution

│  │ • Rate Limit Detection                                     │  │

│  │ • Exponential Backoff (3s base delay)                      │  │---

│  │ • Returns: Articles with title, URL, snippet, date        │  │

│  └────────────────────────────────────────────────────────────┘  │

└──────────────────────────────────────────────────────────────────┘

                               │## Key Features

                               │ State Update:

                               │ {articles: [{...}, {...}]}```

                               │

                               ▼### Multi-Agent Architecture

┌──────────────────────────────────────────────────────────────────┐

│                    SUMMARIZATION AGENT                            │- **Search Agent**: Queries DuckDuckGo for recent automotive news with intelligent rate limiting┌─────────────────────────────────────────────────────────┐

│  ┌────────────────────────────────────────────────────────────┐  │

│  │ • Powered by: Google Gemini 2.5 Flash                      │  │- **Summarization Agent**: Creates concise, business-focused summaries using Google Gemini 2.5

│  │ • Temperature: 0.5 (balanced)                              │  │

│  │ • Max Tokens: 2000                                         │  │- **Sentiment Agent**: Performs advanced sentiment analysis with confidence scoring│                  LangGraph Orchestrator                  │- **🔍 Intelligent News Search**: Automated DuckDuckGo searches with rate limiting protection## 📋 Requirements

│  │ • Output: 2-3 sentence professional summaries             │  │

│  └────────────────────────────────────────────────────────────┘  │

└──────────────────────────────────────────────────────────────────┘

                               │### Intelligent Orchestration│                    (Sequential Pipeline)                 │

                               │ State Update:

                               │ {articles: [{..., summary}]}- **LangGraph-powered workflow**: Sequential pipeline ensuring data flows correctly between agents

                               │

                               ▼- **Error handling**: Robust retry logic with exponential backoff for API rate limits└─────────────────────────────────────────────────────────┘- **📝 AI-Powered Summarization**: Concise 2-3 sentence summaries using Google Gemini 2.5

┌──────────────────────────────────────────────────────────────────┐

│                     SENTIMENT AGENT                               │- **State management**: Maintains context throughout the multi-step analysis process

│  ┌────────────────────────────────────────────────────────────┐  │

│  │ • Powered by: Google Gemini 2.5 Flash                      │  │                            │

│  │ • Pydantic Output Parser                                   │  │

│  │ • Returns: sentiment, confidence, reasoning                │  │### Production-Ready Design

│  │ • Classifications: positive / negative / neutral           │  │

│  └────────────────────────────────────────────────────────────┘  │- **Environment-based configuration**: Easy deployment across different environments        ┌───────────────────┼───────────────────┐- **😊 Advanced Sentiment Analysis**: Classification (positive/negative/neutral) with confidence scores (0.90-0.98)- Python 3.9+

└──────────────────────────────────────────────────────────────────┘

                               │- **Multiple output formats**: JSON and CSV exports with timestamps

                               │ Final State:

                               │ {articles: [{..., sentiment, confidence}]}- **Comprehensive logging**: Detailed execution logs for debugging and monitoring        ▼                   ▼                   ▼

                               │

                               ▼- **Rate limiting protection**: Built-in delays and retry mechanisms for external APIs

                        ┌──────────────┐

                        │ END NODE     │┌──────────────┐   ┌─────────────────┐  ┌────────────────┐- **🤖 Multi-Agent Architecture**: Three specialized agents orchestrated by LangGraph- Google Gemini API key

                        │ (Complete)   │

                        └──────────────┘### High Performance

```

- **Processing speed**: Analyzes 15 articles in approximately 38-46 seconds│ Search Agent │ → │ Summarize Agent │→ │ Sentiment Agent│

### Workflow Execution

- **High accuracy**: Sentiment confidence scores consistently above 90%

1. **Initialization**: LangGraph creates initial state with target companies and market

2. **Search Phase**: Search agent retrieves recent news articles (configurable time window)- **Scalable**: Easily extend to monitor additional companies or markets│              │   │                 │  │                │- **💾 Multiple Output Formats**: JSON and CSV export with timestamped files- Internet connection for news search

3. **Summarization Phase**: Each article is processed by the summarization agent

4. **Sentiment Phase**: Sentiment agent analyzes each summary and assigns classification

5. **Output Phase**: Results are formatted and saved to JSON/CSV files

---│ DuckDuckGo   │   │   Gemini 2.5    │  │  Gemini 2.5    │

---



## Prerequisites

## System Architecture│   + Retry    │   │   (2-3 sent.)   │  │  (with conf.)  │- **⚙️ Highly Configurable**: Environment-based configuration via `.env` file

Before installing, ensure you have:



- **Python 3.11 or higher** (tested on Python 3.11.6)

- **Google Gemini API Key** - Free tier available at [Google AI Studio](https://makersuite.google.com/app/apikey)```└──────────────┘   └─────────────────┘  └────────────────┘

- **Internet connection** for news search and API access

- **Git** (for cloning the repository)┌─────────────────────────────────────────────────────────────────┐



### System Requirements│                    LangGraph Orchestrator                        │        │                   │                   │- **🛡️ Production-Ready**: Built-in error handling, retry logic, and rate limiting## 🛠️ Installation



- **RAM**: Minimum 2GB available│              (Sequential State Machine Pipeline)                 │

- **Storage**: ~500MB for dependencies

- **OS**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)└─────────────────────────────────────────────────────────────────┘        ▼                   ▼                   ▼



---                               │



## Installation                               │ Initial State:   5 articles         Summaries            Sentiment



### Step 1: Clone the Repository                               │ {companies, market}



```bash                               │   per search        + context          + confidence

git clone https://github.com/barreag/auto_news_with_sentiment_analysis.git

cd auto_news_with_sentiment_analysis                               ▼

```

┌──────────────────────────────────────────────────────────────────┐```---1. **Clone the repository**

### Step 2: Create Virtual Environment

│                        SEARCH AGENT                               │

Using a virtual environment is strongly recommended to avoid dependency conflicts.

│  ┌────────────────────────────────────────────────────────────┐  │

**Windows:**

```powershell│  │ • DuckDuckGo Search Tool                                   │  │

python -m venv agent_env

.\agent_env\Scripts\activate│  │ • Rate Limit Detection                                     │  │### Agent Workflow   ```bash

```

│  │ • Exponential Backoff (3s base delay)                      │  │

**macOS/Linux:**

```bash│  │ • Returns: Articles with title, URL, snippet, date        │  │

python -m venv agent_env

source agent_env/bin/activate│  └────────────────────────────────────────────────────────────┘  │

```

└──────────────────────────────────────────────────────────────────┘1. **Search Agent**: Searches for automotive news using DuckDuckGo (3-second delays between requests)## 🏗️ Architecture   git clone https://github.com/yourusername/auto_news_sentiment_analysis.git

### Step 3: Install Dependencies

                               │

```bash

pip install -r requirements.txt                               │ State Update:2. **Summarization Agent**: Creates business-focused summaries for each article

```

                               │ {articles: [{...}, {...}]}

This will install:

- LangGraph (>=0.2.0) - Multi-agent orchestration                               │3. **Sentiment Agent**: Analyzes sentiment with confidence scores and reasoning   cd auto_news_sentiment_analysis

- LangChain (>=0.3.0) - Agent framework

- Google Generative AI (>=0.8.0) - Gemini API client                               ▼

- DuckDuckGo Search (>=6.0.0) - News search tool

- Additional utilities (pandas, pydantic, python-dotenv)┌──────────────────────────────────────────────────────────────────┐



### Step 4: Configure Environment│                    SUMMARIZATION AGENT                            │



```bash│  ┌────────────────────────────────────────────────────────────┐  │---```   ```

# Windows

copy .env.example .env│  │ • Powered by: Google Gemini 2.5 Flash                      │  │



# macOS/Linux│  │ • Temperature: 0.5 (balanced)                              │  │

cp .env.example .env

```│  │ • Max Tokens: 2000                                         │  │



Edit `.env` and add your Google Gemini API key:│  │ • Output: 2-3 sentence professional summaries             │  │## Quick Start┌─────────────────────────────────────────────────────────┐



```env│  └────────────────────────────────────────────────────────────┘  │

GOOGLE_API_KEY=your_actual_api_key_here

```└──────────────────────────────────────────────────────────────────┘



**How to get your API key:**                               │

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Sign in with your Google account                               │ State Update:### Prerequisites│                  LangGraph Orchestrator                  │2. **Create a virtual environment**

3. Click "Create API Key"

4. Copy and paste into your `.env` file                               │ {articles: [{..., summary}]}



---                               │



## Configuration                               ▼



The system is configured via the `.env` file. Below are all available settings:┌──────────────────────────────────────────────────────────────────┐- **Python 3.11+** (recommended: 3.11.6)│                    (Sequential Pipeline)                 │   ```bash



### API Configuration│                     SENTIMENT AGENT                               │



```env│  ┌────────────────────────────────────────────────────────────┐  │- **Google Gemini API key** → [Get one FREE here](https://makersuite.google.com/app/apikey)

# REQUIRED: Your Google Gemini API key

GOOGLE_API_KEY=your_api_key_here│  │ • Powered by: Google Gemini 2.5 Flash                      │  │

```

│  │ • Pydantic Output Parser                                   │  │- Internet connection└─────────────────────────────────────────────────────────┘   python -m venv venv

### Target Configuration

│  │ • Returns: sentiment, confidence, reasoning                │  │

```env

# Companies to analyze (comma-separated, no spaces)│  │ • Classifications: positive / negative / neutral           │  │

COMPANIES=GM,Ford,Tesla

│  └────────────────────────────────────────────────────────────┘  │

# Market focus (currently supports US)

MARKET=US└──────────────────────────────────────────────────────────────────┘### Installation                            │   # On Windows

```

                               │

### Search Settings

                               │ Final State:

```env

# How many days back to search for news                               │ {articles: [{..., sentiment, confidence}]}

NEWS_DAYS_BACK=7

                               │```bash        ┌───────────────────┼───────────────────┐   venv\Scripts\activate

# Maximum articles to retrieve per company

# Recommended: 5-10 for balance between speed and coverage                               ▼

MAX_RESULTS_PER_COMPANY=5

                        ┌──────────────┐# 1. Clone the repository

# Delay between search requests (seconds)

# Helps avoid DuckDuckGo rate limiting                        │ END NODE     │

# Recommended: 3.0 or higher

SEARCH_DELAY_SECONDS=3.0                        │ (Complete)   │git clone https://github.com/barreag/auto_news_with_sentiment_analysis.git        ▼                   ▼                   ▼   # On macOS/Linux

```

                        └──────────────┘

### LLM Settings

```cd auto_news_with_sentiment_analysis

```env

# Model creativity (0.0 = deterministic, 1.0 = creative)

# Recommended: 0.5 for balanced, professional outputs

TEMPERATURE=0.5### Workflow Execution┌──────────────┐   ┌─────────────────┐  ┌────────────────┐   source venv/bin/activate



# Maximum tokens in model response

# 2000 is sufficient for summaries and sentiment analysis

MAX_TOKENS=20001. **Initialization**: LangGraph creates initial state with target companies and market# 2. Create and activate virtual environment

```

2. **Search Phase**: Search agent retrieves recent news articles (configurable time window)

### Configuration Tips

3. **Summarization Phase**: Each article is processed by the summarization agent# Windows:│ Search Agent │ → │ Summarize Agent │→ │ Sentiment Agent│   ```

- **For faster execution**: Reduce `MAX_RESULTS_PER_COMPANY` to 3

- **For more coverage**: Increase `MAX_RESULTS_PER_COMPANY` to 10 (but slower)4. **Sentiment Phase**: Sentiment agent analyzes each summary and assigns classification

- **If rate limited**: Increase `SEARCH_DELAY_SECONDS` to 5.0 or higher

- **For more companies**: Add to `COMPANIES` (e.g., `COMPANIES=GM,Ford,Tesla,Rivian,Lucid`)5. **Output Phase**: Results are formatted and saved to JSON/CSV filespython -m venv agent_env



---



## Usage---.\agent_env\Scripts\activate│              │   │                 │  │                │



### Basic Execution



Run with default settings from `.env`:## Prerequisites



```bash

python main.py

```Before installing, ensure you have:# Linux/Mac:│ DuckDuckGo   │   │   Gemini 2.5    │  │  Gemini 2.5    │3. **Install dependencies**



### Command-Line Options



The system supports several command-line arguments for flexibility:- **Python 3.11 or higher** (tested on Python 3.11.6)python -m venv agent_env



#### Analyze Specific Companies- **Google Gemini API Key** - Free tier available at [Google AI Studio](https://makersuite.google.com/app/apikey)



```bash- **Internet connection** for news search and API accesssource agent_env/bin/activate│   + Retry    │   │   (2-3 sent.)   │  │  (with conf.)  │   ```bash

# Override companies from .env

python main.py --companies GM Ford- **Git** (for cloning the repository)



# Single company

python main.py --companies Tesla

```### System Requirements



#### Control Output Format# 3. Install dependencies└──────────────┘   └─────────────────┘  └────────────────┘   pip install -r requirements.txt



```bash- **RAM**: Minimum 2GB available

# JSON only

python main.py --output-format json- **Storage**: ~500MB for dependenciespip install -r requirements.txt



# CSV only- **OS**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)

python main.py --output-format csv

        │                   │                   │   ```

# Both formats (default)

python main.py --output-format both---

```

# 4. Configure environment variables

#### Suppress Console Output

## Installation

```bash

# Useful for scheduled runs or CI/CD pipelinescopy .env.example .env  # Windows        ▼                   ▼                   ▼

python main.py --no-console

```### Step 1: Clone the Repository



#### Combined Optionscp .env.example .env    # Linux/Mac



```bash```bash

# Analyze specific companies, JSON only, no console

python main.py --companies GM Ford --output-format json --no-consolegit clone https://github.com/barreag/auto_news_with_sentiment_analysis.git   5 articles         Summaries            Sentiment4. **Set up environment variables**

```

cd auto_news_with_sentiment_analysis

### Example Output

```# 5. Edit .env and add your Google Gemini API key

When running the system, you'll see:



```

================================================================================### Step 2: Create Virtual Environment# GOOGLE_API_KEY=your_actual_api_key_here   per search        + context          + confidence   ```bash

AUTOMOTIVE NEWS SENTIMENT ANALYSIS SYSTEM

================================================================================

Powered by LangGraph + LangChain + Google Gemini

Using a virtual environment is strongly recommended to avoid dependency conflicts.```

Configuration validated successfully

Target companies: GM, Ford, Tesla

Market focus: US

**Windows:**```   # Copy the example environment file

Initializing multi-agent workflow...

Starting analysis pipeline...```powershell

Step 1: Searching for news articles...

Step 2: Summarizing articles...python -m venv agent_env### Basic Usage

Step 3: Analyzing sentiment...

.\agent_env\Scripts\activate

================================================================================

AUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT```   copy .env.example .env  # Windows

================================================================================



Generated: 2025-10-25 19:07:30

Companies Analyzed: GM, Ford, Tesla**macOS/Linux:**```bash

Total Articles: 5

```bash

********************************************************************************

COMPANY: GM,Ford,Teslapython -m venv agent_env# Run with default companies (GM, Ford, Tesla)### Agent Workflow   # cp .env.example .env  # macOS/Linux

********************************************************************************

source agent_env/bin/activate

[1] Auto Stocks Surge as Carmakers Navigate Policy Shifts

    URL: https://example.com/article1```python main.py

    Published: 2025-10-24

    

    Summary: Auto stocks, notably GM and Ford, are surging as investors react 

    positively to strong sales performance. This market enthusiasm is further ### Step 3: Install Dependencies   ```

    bolstered by favorable shifts in federal policy.

    

    Sentiment: positive

    Confidence: 0.98```bash# Analyze specific companies

    Reasoning: The article discusses positive market reactions, strong sales, 

    and favorable policy changes, all indicating positive sentiment.pip install -r requirements.txt



[2] GM bets big on electric cars even as market slows```python main.py --companies GM Ford1. **Search Agent**: Searches for automotive news using DuckDuckGo (3-second delays between requests)   

    URL: https://example.com/article2

    Published: 2025-10-23

    

    Summary: General Motors continues its aggressive EV investment strategy This will install:

    despite an anticipated industry-wide sales slowdown, raising concerns 

    among investors about short-term profitability.- LangGraph (>=0.2.0) - Multi-agent orchestration

    

    Sentiment: negative- LangChain (>=0.3.0) - Agent framework# Output formats2. **Summarization Agent**: Creates business-focused summaries for each article   Edit `.env` and add your Google Gemini API key:

    Confidence: 0.90

    Reasoning: The article highlights concerns about investment during a sales - Google Generative AI (>=0.8.0) - Gemini API client

    slowdown and mentions investor worries about profitability.

- DuckDuckGo Search (>=6.0.0) - News search toolpython main.py --output-format json   # JSON only

================================================================================

Sentiment Distribution:- Additional utilities (pandas, pydantic, python-dotenv)

  Positive: 3 (60%)

  Negative: 2 (40%)python main.py --output-format csv    # CSV only3. **Sentiment Agent**: Analyzes sentiment with confidence scores and reasoning   ```

  Neutral: 0 (0%)

================================================================================### Step 4: Configure Environment



Results saved to: outputs/news_analysis_20251025_190730.jsonpython main.py --output-format both   # Both formats (default)

Results saved to: outputs/news_analysis_20251025_190730.csv

```bash

================================================================================

ANALYSIS COMPLETE# Windows   GOOGLE_API_KEY=your_actual_api_key_here

================================================================================

Total articles analyzed: 5copy .env.example .env

Sentiment distribution:

  Positive: 3# Suppress console output

  Negative: 2

  Neutral: 0# macOS/Linux

================================================================================

```cp .env.example .envpython main.py --no-console---   ```



---```



## Output Format```



Results are saved in the `outputs/` directory with timestamps for easy tracking.Edit `.env` and add your Google Gemini API key:



### JSON Output Structure



```json```env

{

  "metadata": {GOOGLE_API_KEY=your_actual_api_key_here---

    "timestamp": "2025-10-25T19:07:30",

    "companies": ["GM", "Ford", "Tesla"],```

    "market": "US",

    "status": "success",## 🚀 Quick Start## 🎯 Usage

    "total_articles": 5,

    "sentiment_distribution": {**How to get your API key:**

      "positive": 3,

      "negative": 2,1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)## Configuration

      "neutral": 0

    }2. Sign in with your Google account

  },

  "all_articles": [3. Click "Create API Key"

    {

      "company": "GM,Ford,Tesla",4. Copy and paste into your `.env` file

      "title": "Auto Stocks Surge as Carmakers Navigate Policy Shifts",

      "url": "https://example.com/article",Customize behavior by editing the `.env` file:

      "snippet": "Original article excerpt...",

      "summary": "Auto stocks, notably GM and Ford, are surging...",---

      "sentiment": "positive",

      "confidence": 0.98,### Prerequisites### Basic Usage

      "reasoning": "The article discusses positive market reactions...",

      "date": "2025-10-24",## Configuration

      "source": "Example News"

    }```env

  ]

}The system is configured via the `.env` file. Below are all available settings:

```

# ========== REQUIRED ==========

### CSV Output Structure

### API Configuration

| company | title | url | date | source | snippet | summary | sentiment | confidence | reasoning |

|---------|-------|-----|------|--------|---------|---------|-----------|------------|-----------|# Get your key at: https://makersuite.google.com/app/apikey

| GM,Ford,Tesla | Auto Stocks Surge... | https://... | 2025-10-24 | Example News | Original text... | Summary text... | positive | 0.98 | Reasoning... |

```env

### Field Descriptions

# REQUIRED: Your Google Gemini API keyGOOGLE_API_KEY=your_api_key_here- **Python 3.11+** (recommended: 3.11.6)Run the main script to execute the multi-agent pipeline:

- **company**: Target company or companies

- **title**: Original article headlineGOOGLE_API_KEY=your_api_key_here

- **url**: Direct link to source article

- **date**: Publication date```

- **source**: News source/publication

- **snippet**: Original article excerpt from search

- **summary**: AI-generated 2-3 sentence summary

- **sentiment**: Classification (positive/negative/neutral)### Target Configuration# ========== TARGET CONFIGURATION ==========- **Google Gemini API key** → [Get one FREE here](https://makersuite.google.com/app/apikey)

- **confidence**: Model confidence score (0.0-1.0)

- **reasoning**: Explanation for sentiment classification



---```envCOMPANIES=GM,Ford,Tesla    # Comma-separated company names



## Project Structure# Companies to analyze (comma-separated, no spaces)



```COMPANIES=GM,Ford,TeslaMARKET=US                  # Market focus- Internet connection```bash

auto_news_with_sentiment_analysis/

│

├── main.py                          # Application entry point

├── requirements.txt                 # Python dependencies# Market focus (currently supports US)

├── LICENSE                          # MIT License

├── README.md                        # This fileMARKET=US

│

├── .env.example                     # Environment template```# ========== SEARCH SETTINGS ==========python main.py

├── .env                            # Your configuration (not in git)

├── .gitignore                      # Git ignore rules

│

├── config/### Search SettingsNEWS_DAYS_BACK=7                # Days of historical news to search

│   ├── __init__.py

│   └── settings.py                 # Centralized configuration management

│

├── src/```envMAX_RESULTS_PER_COMPANY=5       # Articles per company (lower = faster)### Installation```

│   ├── __init__.py

│   │# How many days back to search for news

│   ├── agents/                     # Agent implementations

│   │   ├── __init__.pyNEWS_DAYS_BACK=7SEARCH_DELAY_SECONDS=3.0        # Delay between searches (avoid rate limits)

│   │   ├── search_agent.py         # News search agent

│   │   ├── summarize_agent.py      # Summarization agent

│   │   └── sentiment_agent.py      # Sentiment analysis agent

│   │# Maximum articles to retrieve per company

│   ├── workflows/                  # LangGraph orchestration

│   │   ├── __init__.py# Recommended: 5-10 for balance between speed and coverage

│   │   └── news_workflow.py        # Main workflow definition

│   │MAX_RESULTS_PER_COMPANY=5# ========== LLM SETTINGS ==========

│   ├── tools/                      # Agent tools

│   │   ├── __init__.py

│   │   └── search_tool.py          # DuckDuckGo search wrapper

│   │# Delay between search requests (seconds)TEMPERATURE=0.5                 # Model creativity (0.0-1.0, 0.5 = balanced)```bashThis will:

│   └── utils/                      # Utility functions

│       ├── __init__.py# Helps avoid DuckDuckGo rate limiting

│       ├── logger.py               # Logging configuration

│       └── output_handler.py       # Output formatting (JSON/CSV)# Recommended: 3.0 or higherMAX_TOKENS=2000                # Maximum response length

│

├── outputs/                        # Generated results (timestamped)SEARCH_DELAY_SECONDS=3.0

│   ├── .gitkeep                   # Preserve directory in git

│   ├── news_analysis_*.json       # JSON results (not in git)``````# 1. Clone the repository1. Search for recent automotive news for GM, Ford, and Tesla

│   └── news_analysis_*.csv        # CSV results (not in git)

│

├── tests/                          # Unit tests

│   ├── __init__.py### LLM Settings

│   └── test_agents.py             # Agent tests

│

├── docs/                           # Additional documentation

│   ├── architecture.md            # Detailed architecture docs```env---git clone https://github.com/yourusername/auto_news_sentiment_analysis.git2. Summarize each article found

│   └── usage_guide.md             # Extended usage examples

│# Model creativity (0.0 = deterministic, 1.0 = creative)

└── .github/

    └── workflows/# Recommended: 0.5 for balanced, professional outputs

        └── main.yml                # CI/CD pipeline (if applicable)

```TEMPERATURE=0.5



---## Output Examplescd auto_news_sentiment_analysis3. Analyze sentiment for each article



## How It Works# Maximum tokens in model response



### 1. Search Agent# 2000 is sufficient for summaries and sentiment analysis



**Purpose**: Find relevant automotive news articlesMAX_TOKENS=2000



**Process**:```### Console Output4. Save results to `outputs/` directory

- Constructs search queries combining company names and market focus

- Queries DuckDuckGo with date filters (past N days)

- Implements intelligent rate limiting (3-second delays between requests)

- Handles rate limit errors with exponential backoff retry logic### Configuration Tips```

- Extracts: title, URL, snippet, publication date, source



**Technologies**:

- `duckduckgo-search` library- **For faster execution**: Reduce `MAX_RESULTS_PER_COMPANY` to 3================================================================================# 2. Create and activate virtual environment

- Custom retry logic with exponential backoff

- Rate limit detection- **For more coverage**: Increase `MAX_RESULTS_PER_COMPANY` to 10 (but slower)



### 2. Summarization Agent- **If rate limited**: Increase `SEARCH_DELAY_SECONDS` to 5.0 or higherAUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT



**Purpose**: Create concise, business-focused summaries- **For more companies**: Add to `COMPANIES` (e.g., `COMPANIES=GM,Ford,Tesla,Rivian,Lucid`)



**Process**:================================================================================# Windows:### Configuration

- Receives article snippets from search agent

- Uses Google Gemini 2.5 Flash model for summarization---

- Configured for professional, objective tone

- Generates 2-3 sentence summaries

- Maintains key facts: companies mentioned, events, market implications

## Usage

**Technologies**:

- Google Gemini 2.5 Flash (via `langchain-google-genai`)Generated: 2025-10-25 19:07:30python -m venv agent_env

- LangChain agent framework

- Temperature: 0.5 (balanced creativity)### Basic Execution



### 3. Sentiment AgentCompanies Analyzed: GM, Ford, Tesla



**Purpose**: Classify sentiment with confidence scoringRun with default settings from `.env`:



**Process**:Total Articles: 5.\agent_env\Scripts\activateYou can customize the behavior by editing `.env`:

- Analyzes article summaries for sentiment

- Returns structured output: sentiment, confidence, reasoning```bash

- Uses Pydantic models for output validation

- Provides explainable AI with reasoning fieldpython main.py



**Output Classifications**:```

- **Positive**: Favorable news, growth, success, positive market reaction

- **Negative**: Challenges, declines, concerns, negative market reaction********************************************************************************

- **Neutral**: Factual reporting without clear positive/negative bias

### Command-Line Options

**Technologies**:

- Google Gemini 2.5 FlashCOMPANY: GM,Ford,Tesla

- LangChain output parsers

- Pydantic models for structured outputThe system supports several command-line arguments for flexibility:



### 4. LangGraph Orchestration********************************************************************************# Linux/Mac:```env



**Purpose**: Coordinate agent execution and state management#### Analyze Specific Companies



**Process**:

1. Creates initial state with companies and market

2. Executes search agent → updates state with articles```bash

3. Executes summarization agent → adds summaries to state

4. Executes sentiment agent → adds sentiment analysis to state# Override companies from .env[1] Auto Stocks Surge as Carmakers Navigate Policy Shiftspython -m venv agent_env# Companies to track (comma-separated)

5. Returns final state with complete analysis

python main.py --companies GM Ford

**Benefits**:

- **State management**: Maintains data consistency across agents    Sentiment: positive (Confidence: 0.98)

- **Error handling**: Isolates failures to specific agents

- **Extensibility**: Easy to add new agents or modify workflow# Single company

- **Debugging**: Clear state transitions for troubleshooting

python main.py --companies Tesla    Summary: Auto stocks, notably GM and Ford, are surging as investors source agent_env/bin/activateCOMPANIES=GM,Ford,Tesla

---

```

## Troubleshooting

    react positively to strong sales performance. This market enthusiasm 

### Common Issues and Solutions

#### Control Output Format

#### Issue: "GOOGLE_API_KEY is required"

    is further bolstered by favorable shifts in federal policy...

**Cause**: API key not set in `.env` file

```bash

**Solution**:

1. Ensure `.env` file exists in project root# JSON only

2. Add your API key: `GOOGLE_API_KEY=your_key_here`

3. No spaces around the `=` signpython main.py --output-format json

4. Key should start with `AIza...`

[2] GM bets big on electric cars even as market slows# 3. Install dependencies# Market focus

#### Issue: "202 Ratelimit" or Rate Limiting Errors

# CSV only

**Cause**: Too many requests to DuckDuckGo too quickly

python main.py --output-format csv    Sentiment: negative (Confidence: 0.90)

**Solutions**:

1. Increase `SEARCH_DELAY_SECONDS` to `5.0` in `.env`

2. Reduce `MAX_RESULTS_PER_COMPANY` to `3`

3. Wait 5-10 minutes before retrying# Both formats (default)    Summary: General Motors continues its aggressive EV investment strategy pip install -r requirements.txtMARKET=US

4. The system has built-in retry logic that will automatically handle this

python main.py --output-format both

#### Issue: "404 models/gemini-1.5-flash is not found"

```    despite an anticipated industry-wide sales slowdown...

**Cause**: Model name mismatch with API version



**Solution**:

The system is already configured to use `gemini-2.5-flash` which is the correct model. If you see this error, ensure you haven't manually changed the model name in `config/settings.py`.#### Suppress Console Output



#### Issue: No Articles Found



**Possible Causes & Solutions**:```bash================================================================================



1. **Too restrictive date range**# Useful for scheduled runs or CI/CD pipelines

   - Increase `NEWS_DAYS_BACK` in `.env` (e.g., `NEWS_DAYS_BACK=14`)

python main.py --no-consoleSentiment Distribution:# 4. Configure environment variables# News search settings

2. **Company names not in news**

   - Try different or more popular companies```

   - Verify spelling matches news articles

  Positive: 3 (60%)

3. **Network connectivity**

   - Check internet connection#### Combined Options

   - Verify DuckDuckGo is accessible

  Negative: 2 (40%)copy .env.example .env  # WindowsNEWS_DAYS_BACK=7

#### Issue: Import Errors

```bash

**Cause**: Virtual environment not activated or dependencies not installed

# Analyze specific companies, JSON only, no console  Neutral: 0 (0%)

**Solution**:

```bashpython main.py --companies GM Ford --output-format json --no-console

# Activate virtual environment

# Windows```================================================================================cp .env.example .env    # Linux/MacMAX_RESULTS_PER_COMPANY=10

.\agent_env\Scripts\activate



# macOS/Linux

source agent_env/bin/activate### Example Output```



# Reinstall dependencies

pip install -r requirements.txt

```When running the system, you'll see:



#### Issue: Slow Performance



**Causes & Solutions**:```### JSON Output Structure



1. **Too many articles**================================================================================

   - Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower

AUTOMOTIVE NEWS SENTIMENT ANALYSIS SYSTEM```json# 5. Edit .env and add your Google Gemini API key# Agent settings

2. **Too many companies**

   - Analyze fewer companies per run================================================================================



3. **Network latency**Powered by LangGraph + LangChain + Google Gemini{

   - Check internet connection speed

   - API calls require stable connection



**Expected performance**: 15 articles in approximately 38-46 secondsConfiguration validated successfully  "metadata": {# GOOGLE_API_KEY=your_actual_api_key_hereTEMPERATURE=0.7



---Target companies: GM, Ford, Tesla



## Performance OptimizationMarket focus: US    "timestamp": "2025-10-25T19:07:30",



### Speed vs. Coverage Tradeoffs



| Configuration | Articles | Execution Time | Use Case |Initializing multi-agent workflow...    "companies": ["GM", "Ford", "Tesla"],```MAX_TOKENS=2000

|--------------|----------|----------------|----------|

| Fast | 3 per company | ~20-25 seconds | Quick daily updates |Starting analysis pipeline...

| Balanced (default) | 5 per company | ~38-46 seconds | Regular monitoring |

| Comprehensive | 10 per company | ~70-90 seconds | Deep analysis |Step 1: Searching for news articles...    "total_articles": 5,



### Optimization TipsStep 2: Summarizing articles...



1. **Reduce API calls**:Step 3: Analyzing sentiment...    "sentiment_distribution": {```

   - Lower `MAX_RESULTS_PER_COMPANY`

   - Fewer companies per run



2. **Parallel processing** (future enhancement):================================================================================      "positive": 3,

   - Currently sequential for rate limit management

   - Could parallelize summarization and sentiment agentsAUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT



3. **Caching** (future enhancement):================================================================================      "negative": 2,### Basic Usage

   - Cache search results to avoid re-querying

   - Store processed articles to avoid reprocessing



4. **Rate limiting**:Generated: 2025-10-25 19:07:30      "neutral": 0

   - Current settings optimized for reliability

   - Can reduce `SEARCH_DELAY_SECONDS` if not hitting limitsCompanies Analyzed: GM, Ford, Tesla



---Total Articles: 5    }## 📁 Project Structure



## Contributing



Contributions are welcome! This project can be extended in many ways:********************************************************************************  },



### Areas for ContributionCOMPANY: GM,Ford,Tesla



- **Additional news sources**: Beyond DuckDuckGo********************************************************************************  "all_articles": [```bash

- **More AI models**: Support for Claude, GPT-4, etc.

- **Enhanced analytics**: Trend analysis over time

- **Visualization**: Charts and dashboards

- **API wrapper**: REST API for the system[1] Auto Stocks Surge as Carmakers Navigate Policy Shifts    {

- **Database integration**: Store results in PostgreSQL/MongoDB

- **Real-time monitoring**: Continuous news monitoring    URL: https://example.com/article1

- **Multi-language support**: Non-English news sources

- **Notification system**: Alerts for significant sentiment shifts    Published: 2025-10-24      "company": "GM,Ford,Tesla",# Run with default companies (GM, Ford, Tesla)```



### How to Contribute    



1. **Fork the repository**    Summary: Auto stocks, notably GM and Ford, are surging as investors react       "title": "Article Title",

   ```bash

   # Click "Fork" on GitHub    positively to strong sales performance. This market enthusiasm is further 

   git clone https://github.com/YOUR_USERNAME/auto_news_with_sentiment_analysis.git

   ```    bolstered by favorable shifts in federal policy.      "url": "https://...",python main.pyauto_news_sentiment_analysis/



2. **Create a feature branch**    

   ```bash

   git checkout -b feature/amazing-feature    Sentiment: positive      "snippet": "Original content...",

   ```

    Confidence: 0.98

3. **Make your changes**

   - Follow existing code style    Reasoning: The article discusses positive market reactions, strong sales,       "summary": "AI-generated summary...",├── .github/

   - Add tests for new features

   - Update documentation    and favorable policy changes, all indicating positive sentiment.



4. **Run tests**      "sentiment": "positive",

   ```bash

   pytest tests/[2] GM bets big on electric cars even as market slows

   ```

    URL: https://example.com/article2      "confidence": 0.98,# Analyze specific companies│   └── workflows/

5. **Commit with clear messages**

   ```bash    Published: 2025-10-23

   git commit -m "Add: Brief description of feature"

   ```          "reasoning": "Explanation...",



6. **Push and create Pull Request**    Summary: General Motors continues its aggressive EV investment strategy 

   ```bash

   git push origin feature/amazing-feature    despite an anticipated industry-wide sales slowdown, raising concerns       "date": "2025-10-25",python main.py --companies GM Ford│       └── main.yml              # CI/CD pipeline

   ```

    among investors about short-term profitability.

### Coding Standards

          "source": "Source Name"

- **Python style**: Follow PEP 8

- **Type hints**: Use type annotations    Sentiment: negative

- **Docstrings**: Google-style docstrings for functions/classes

- **Testing**: Write unit tests for new features    Confidence: 0.90    }├── .gitignore                    # Git ignore rules

- **Documentation**: Update README for significant changes

    Reasoning: The article highlights concerns about investment during a sales 

---

    slowdown and mentions investor worries about profitability.  ]

## License



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

================================================================================}# Output formats├── README.md                     # Project documentation

### MIT License Summary

Sentiment Distribution:

- Commercial use allowed

- Modification allowed  Positive: 3 (60%)```

- Distribution allowed

- Private use allowed  Negative: 2 (40%)

- Liability and warranty limitations apply

  Neutral: 0 (0%)python main.py --output-format json   # JSON only├── requirements.txt              # Python dependencies

---

================================================================================

## Acknowledgments

---

This project is built on the shoulders of giants:

Results saved to: outputs/news_analysis_20251025_190730.json

### Core Technologies

Results saved to: outputs/news_analysis_20251025_190730.csvpython main.py --output-format csv    # CSV only├── .env.example                  # Example environment variables

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework by LangChain

- **[LangChain](https://www.langchain.com/)** - Framework for developing applications with LLMs

- **[Google Gemini](https://ai.google.dev/)** - Advanced AI model for summarization and analysis

- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine================================================================================## Project Structure



### InspirationANALYSIS COMPLETE



- Automotive industry analysts who need efficient sentiment monitoring================================================================================python main.py --output-format both   # Both formats (default)├── main.py                       # Main application entry point

- Open-source AI community for democratizing access to advanced AI tools

- LangChain community for excellent documentation and examplesTotal articles analyzed: 5



### Special ThanksSentiment distribution:```



- Google for providing free-tier Gemini API access  Positive: 3

- DuckDuckGo for providing programmatic search access

- The open-source Python community  Negative: 2auto_news_sentiment_analysis/├── config/



---  Neutral: 0



## Support and Contact================================================================================├── .env.example              # Example environment configuration



### Getting Help```



- **Documentation**: Check the `/docs` folder for additional guides├── .gitignore               # Git ignore rules# Suppress console output│   └── settings.py               # Configuration management

- **Issues**: [GitHub Issues](https://github.com/barreag/auto_news_with_sentiment_analysis/issues)

- **Discussions**: [GitHub Discussions](https://github.com/barreag/auto_news_with_sentiment_analysis/discussions)---



### Reporting Bugs├── LICENSE                  # MIT License



When reporting bugs, please include:## Output Format

1. Python version (`python --version`)

2. Error messages and stack traces├── README.md               # This filepython main.py --no-console├── src/

3. Configuration (without API keys!)

4. Steps to reproduceResults are saved in the `outputs/` directory with timestamps for easy tracking.



### Feature Requests├── requirements.txt        # Python dependencies



Have an idea? Open an issue with the `enhancement` label and describe:### JSON Output Structure

1. Use case and motivation

2. Proposed solution├── main.py                # Application entry point```│   ├── __init__.py

3. Alternative approaches considered

```json

---

{├── list_models.py         # Utility to list available Gemini models

## Roadmap

  "metadata": {

### Version 1.0 (Current)

- Multi-agent architecture with LangGraph    "timestamp": "2025-10-25T19:07:30",││   ├── agents/

- Search, summarization, and sentiment analysis

- JSON and CSV output formats    "companies": ["GM", "Ford", "Tesla"],

- Rate limiting and error handling

- Comprehensive documentation    "market": "US",├── config/



### Future Enhancements    "status": "success",

- Web dashboard for visualization

- Historical trend analysis    "total_articles": 5,│   └── settings.py        # Centralized configuration management---│   │   ├── __init__.py

- Support for additional news sources (NewsAPI, Google News)

- Database persistence (PostgreSQL)    "sentiment_distribution": {

- REST API wrapper

- Docker containerization      "positive": 3,│

- Real-time monitoring with webhooks

- Multi-language support      "negative": 2,

- Advanced analytics (topic modeling, entity extraction)

- Automated scheduling and reporting      "neutral": 0├── src/│   │   ├── search_agent.py       # News search agent



---    }



**Built for the automotive industry | Powered by AI**  },│   ├── agents/



*Multi-agent sentiment analysis made simple*  "all_articles": [


    {│   │   ├── search_agent.py      # News search with DuckDuckGo## ⚙️ Configuration│   │   ├── summarize_agent.py    # Summarization agent

      "company": "GM,Ford,Tesla",

      "title": "Auto Stocks Surge as Carmakers Navigate Policy Shifts",│   │   ├── summarize_agent.py   # Article summarization

      "url": "https://example.com/article",

      "snippet": "Original article excerpt...",│   │   └── sentiment_agent.py   # Sentiment analysis│   │   └── sentiment_agent.py    # Sentiment analysis agent

      "summary": "Auto stocks, notably GM and Ford, are surging...",

      "sentiment": "positive",│   ├── workflows/

      "confidence": 0.98,

      "reasoning": "The article discusses positive market reactions...",│   │   └── news_workflow.py     # LangGraph orchestrationCustomize behavior by editing the `.env` file:│   ├── workflows/

      "date": "2025-10-24",

      "source": "Example News"│   ├── tools/

    }

  ]│   │   └── search_tool.py       # DuckDuckGo search wrapper│   │   ├── __init__.py

}

```│   └── utils/



### CSV Output Structure│       ├── logger.py            # Logging utilities```env│   │   └── news_workflow.py      # LangGraph orchestration



| company | title | url | date | source | snippet | summary | sentiment | confidence | reasoning |│       └── output_handler.py    # Output formatting (JSON/CSV)

|---------|-------|-----|------|--------|---------|---------|-----------|------------|-----------|

| GM,Ford,Tesla | Auto Stocks Surge... | https://... | 2025-10-24 | Example News | Original text... | Summary text... | positive | 0.98 | Reasoning... |│# ========== REQUIRED ==========│   ├── tools/



### Field Descriptions├── outputs/                 # Generated results (timestamped)



- **company**: Target company or companies├── tests/                  # Unit tests# Get your key at: https://makersuite.google.com/app/apikey│   │   ├── __init__.py

- **title**: Original article headline

- **url**: Direct link to source article└── docs/                   # Additional documentation

- **date**: Publication date

- **source**: News source/publication```GOOGLE_API_KEY=your_api_key_here│   │   └── search_tool.py        # DuckDuckGo search tool

- **snippet**: Original article excerpt from search

- **summary**: AI-generated 2-3 sentence summary

- **sentiment**: Classification (positive/negative/neutral)

- **confidence**: Model confidence score (0.0-1.0)---│   └── utils/

- **reasoning**: Explanation for sentiment classification



---

## Troubleshooting# ========== TARGET CONFIGURATION ==========│       ├── __init__.py

## Project Structure



```

auto_news_with_sentiment_analysis/### Rate Limiting IssuesCOMPANIES=GM,Ford,Tesla    # Comma-separated company names│       ├── logger.py             # Logging utilities

│

├── main.py                          # Application entry point**Problem**: DuckDuckGo returns `202 Ratelimit` error

├── requirements.txt                 # Python dependencies

├── LICENSE                          # MIT LicenseMARKET=US                  # Market focus│       └── output_handler.py     # Output formatting

├── README.md                        # This file

│**Solutions**:

├── .env.example                     # Environment template

├── .env                            # Your configuration (not in git)1. Increase `SEARCH_DELAY_SECONDS` to `5.0` or higher in `.env`├── data/

├── .gitignore                      # Git ignore rules

│2. Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower

├── config/

│   ├── __init__.py3. Wait 5-10 minutes between runs# ========== SEARCH SETTINGS ==========│   ├── raw/                      # Raw news data

│   └── settings.py                 # Centralized configuration management

│

├── src/

│   ├── __init__.py### Gemini API ErrorsNEWS_DAYS_BACK=7                # Days of historical news to search│   └── processed/                # Processed results

│   │

│   ├── agents/                     # Agent implementations**Problem**: `404 models/gemini-1.5-flash is not found`

│   │   ├── __init__.py

│   │   ├── search_agent.py         # News search agentMAX_RESULTS_PER_COMPANY=5       # Articles per company (lower = faster)├── outputs/                      # Generated reports

│   │   ├── summarize_agent.py      # Summarization agent

│   │   └── sentiment_agent.py      # Sentiment analysis agent**Solution**:

│   │

│   ├── workflows/                  # LangGraph orchestration```bashSEARCH_DELAY_SECONDS=3.0        # Delay between searches (avoid rate limits)├── docs/

│   │   ├── __init__.py

│   │   └── news_workflow.py        # Main workflow definition# Check available models

│   │

│   ├── tools/                      # Agent toolspython list_models.py│   └── architecture.md           # System architecture docs

│   │   ├── __init__.py

│   │   └── search_tool.py          # DuckDuckGo search wrapper

│   │

│   └── utils/                      # Utility functions# Update MODEL_NAME in config/settings.py if needed# ========== LLM SETTINGS ==========└── tests/

│       ├── __init__.py

│       ├── logger.py               # Logging configuration```

│       └── output_handler.py       # Output formatting (JSON/CSV)

│TEMPERATURE=0.5                 # Model creativity (0.0-1.0, 0.5 = balanced)    ├── __init__.py

├── outputs/                        # Generated results (timestamped)

│   ├── .gitkeep                   # Preserve directory in git### Common Issues

│   ├── news_analysis_*.json       # JSON results (not in git)

│   └── news_analysis_*.csv        # CSV results (not in git)MAX_TOKENS=2000                # Maximum response length    └── test_agents.py            # Unit tests

│

├── tests/                          # Unit tests| Error | Solution |

│   ├── __init__.py

│   └── test_agents.py             # Agent tests|-------|----------|``````

│

├── docs/                           # Additional documentation| `GOOGLE_API_KEY is required` | Add your API key to `.env` file |

│   ├── architecture.md            # Detailed architecture docs

│   └── usage_guide.md             # Extended usage examples| Import errors | Ensure virtual environment is activated |

│

└── .github/| No articles found | Try different companies or increase `NEWS_DAYS_BACK` |

    └── workflows/

        └── main.yml                # CI/CD pipeline (if applicable)| Slow performance | Reduce `MAX_RESULTS_PER_COMPANY` or `COMPANIES` list |---## 🏗️ Architecture

```



---

---

## How It Works



### 1. Search Agent

## Performance Metrics## 📊 Output ExamplesThe system uses a **multi-agent architecture** orchestrated by LangGraph:

**Purpose**: Find relevant automotive news articles



**Process**:

- Constructs search queries combining company names and market focus- **Processing Time**: ~15-45 seconds for 3 companies (5 articles each)

- Queries DuckDuckGo with date filters (past N days)

- Implements intelligent rate limiting (3-second delays between requests)- **API Calls**: ~16 calls total (1 search + 15 LLM calls)

- Handles rate limit errors with exponential backoff retry logic

- Extracts: title, URL, snippet, publication date, source- **Success Rate**: 100% with proper configuration### Console Output1. **Search Agent** → Queries DuckDuckGo for automotive news



**Technologies**:- **Confidence Scores**: 0.90-0.98 (high accuracy)

- `duckduckgo-search` library

- Custom retry logic with exponential backoff```2. **Summarization Agent** → Processes and summarizes articles

- Rate limit detection

---

### 2. Summarization Agent

================================================================================3. **Sentiment Agent** → Analyzes sentiment and enriches data

**Purpose**: Create concise, business-focused summaries

## Testing

**Process**:

- Receives article snippets from search agentAUTOMOTIVE NEWS SENTIMENT ANALYSIS REPORT

- Uses Google Gemini 2.5 Flash model for summarization

- Configured for professional, objective tone```bash

- Generates 2-3 sentence summaries

- Maintains key facts: companies mentioned, events, market implications# Run all tests================================================================================Each agent is powered by Google Gemini API and uses LangChain tools for enhanced capabilities.



**Technologies**:pytest tests/

- Google Gemini 2.5 Flash (via `langchain-google-genai`)

- LangChain agent framework

- Temperature: 0.5 (balanced creativity)

# Run with coverage

### 3. Sentiment Agent

pytest tests/ --cov=srcGenerated: 2025-10-25 19:07:30## 🧪 Testing

**Purpose**: Classify sentiment with confidence scoring



**Process**:

- Analyzes article summaries for sentiment# Run specific test fileCompanies Analyzed: GM, Ford, Tesla

- Returns structured output: sentiment, confidence, reasoning

- Uses Pydantic models for output validationpytest tests/test_agents.py

- Provides explainable AI with reasoning field

```Total Articles: 5Run tests with pytest:

**Output Classifications**:

- **Positive**: Favorable news, growth, success, positive market reaction

- **Negative**: Challenges, declines, concerns, negative market reaction

- **Neutral**: Factual reporting without clear positive/negative bias---



**Technologies**:

- Google Gemini 2.5 Flash

- LangChain output parsers## Contributing********************************************************************************```bash

- Pydantic models for structured output



### 4. LangGraph Orchestration

Contributions welcome! Please follow these steps:COMPANY: GM,Ford,Teslapytest tests/

**Purpose**: Coordinate agent execution and state management



**Process**:

1. Creates initial state with companies and market1. Fork the repository********************************************************************************```

2. Executes search agent → updates state with articles

3. Executes summarization agent → adds summaries to state2. Create feature branch (`git checkout -b feature/AmazingFeature`)

4. Executes sentiment agent → adds sentiment analysis to state

5. Returns final state with complete analysis3. Commit changes (`git commit -m 'Add AmazingFeature'`)



**Benefits**:4. Push to branch (`git push origin feature/AmazingFeature`)

- **State management**: Maintains data consistency across agents

- **Error handling**: Isolates failures to specific agents5. Open Pull Request[1] Auto Stocks Surge as Carmakers Navigate Policy Shifts## 📊 Output

- **Extensibility**: Easy to add new agents or modify workflow

- **Debugging**: Clear state transitions for troubleshooting



------    Sentiment: positive (Confidence: 0.98)



## Troubleshooting



### Common Issues and Solutions## License    Summary: Auto stocks, notably GM and Ford, are surging as investors Results are saved in JSON format in the `outputs/` directory with timestamps:



#### Issue: "GOOGLE_API_KEY is required"



**Cause**: API key not set in `.env` fileThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.    react positively to strong sales performance. This market enthusiasm - News articles with titles, URLs, and snippets



**Solution**:

1. Ensure `.env` file exists in project root

2. Add your API key: `GOOGLE_API_KEY=your_key_here`---    is further bolstered by favorable shifts in federal policy...- Summaries for each article

3. No spaces around the `=` sign

4. Key should start with `AIza...`



#### Issue: "202 Ratelimit" or Rate Limiting Errors## Acknowledgments- Sentiment scores (positive/negative/neutral) with confidence



**Cause**: Too many requests to DuckDuckGo too quickly



**Solutions**:- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework[2] GM bets big on electric cars even as market slows

1. Increase `SEARCH_DELAY_SECONDS` to `5.0` in `.env`

2. Reduce `MAX_RESULTS_PER_COMPANY` to `3`- **[LangChain](https://www.langchain.com/)** - Agent tools and LLM integrations

3. Wait 5-10 minutes before retrying

4. The system has built-in retry logic that will automatically handle this- **[Google Gemini](https://ai.google.dev/)** - Advanced AI capabilities (Gemini 2.5 Flash)    Sentiment: negative (Confidence: 0.90)## 🤝 Contributing



#### Issue: "404 models/gemini-1.5-flash is not found"- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine



**Cause**: Model name mismatch with API version    Summary: General Motors continues its aggressive EV investment strategy 



**Solution**:---

The system is already configured to use `gemini-2.5-flash` which is the correct model. If you see this error, ensure you haven't manually changed the model name in `config/settings.py`.

    despite an anticipated industry-wide sales slowdown...Contributions are welcome! Please feel free to submit a Pull Request.

#### Issue: No Articles Found

## Support

**Possible Causes & Solutions**:



1. **Too restrictive date range**

   - Increase `NEWS_DAYS_BACK` in `.env` (e.g., `NEWS_DAYS_BACK=14`)- **Documentation**: Check the `/docs` folder



2. **Company names not in news**- **Issues**: [GitHub Issues](https://github.com/barreag/auto_news_with_sentiment_analysis/issues)================================================================================1. Fork the repository

   - Try different or more popular companies

   - Verify spelling matches news articles- **Discussions**: [GitHub Discussions](https://github.com/barreag/auto_news_with_sentiment_analysis/discussions)



3. **Network connectivity**Sentiment Distribution:2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

   - Check internet connection

   - Verify DuckDuckGo is accessible---



#### Issue: Import Errors  Positive: 3 (60%)3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)



**Cause**: Virtual environment not activated or dependencies not installed**Built with care for the automotive industry**



**Solution**:  Negative: 2 (40%)4. Push to the branch (`git push origin feature/AmazingFeature`)

```bash

# Activate virtual environment*Powered by LangGraph + LangChain + Google Gemini 2.5*

# Windows

.\agent_env\Scripts\activate  Neutral: 0 (0%)5. Open a Pull Request



# macOS/Linux================================================================================

source agent_env/bin/activate

```## 📝 License

# Reinstall dependencies

pip install -r requirements.txt

```

### JSON Output StructureThis project is licensed under the MIT License - see the LICENSE file for details.

#### Issue: Slow Performance

```json

**Causes & Solutions**:

{## 🙏 Acknowledgments

1. **Too many articles**

   - Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower  "metadata": {



2. **Too many companies**    "timestamp": "2025-10-25T19:07:30",- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration

   - Analyze fewer companies per run

    "companies": ["GM", "Ford", "Tesla"],- [LangChain](https://github.com/langchain-ai/langchain) for agent tools

3. **Network latency**

   - Check internet connection speed    "total_articles": 5,- [Google Gemini](https://ai.google.dev/) for LLM capabilities

   - API calls require stable connection

    "sentiment_distribution": {- [DuckDuckGo](https://duckduckgo.com/) for news search

**Expected performance**: 15 articles in approximately 38-46 seconds

      "positive": 3,

---

      "negative": 2,## 📧 Contact

## Performance Optimization

      "neutral": 0

### Speed vs. Coverage Tradeoffs

    }Your Name - [@yourhandle](https://twitter.com/yourhandle)

| Configuration | Articles | Execution Time | Use Case |

|--------------|----------|----------------|----------|  },

| Fast | 3 per company | ~20-25 seconds | Quick daily updates |

| Balanced (default) | 5 per company | ~38-46 seconds | Regular monitoring |  "all_articles": [Project Link: [https://github.com/yourusername/auto_news_sentiment_analysis](https://github.com/yourusername/auto_news_sentiment_analysis)

| Comprehensive | 10 per company | ~70-90 seconds | Deep analysis |

    {

### Optimization Tips      "company": "GM,Ford,Tesla",

      "title": "Article Title",

1. **Reduce API calls**:      "url": "https://...",

   - Lower `MAX_RESULTS_PER_COMPANY`      "snippet": "Original content...",

   - Fewer companies per run      "summary": "AI-generated summary...",

      "sentiment": "positive",

2. **Parallel processing** (future enhancement):      "confidence": 0.98,

   - Currently sequential for rate limit management      "reasoning": "Explanation...",

   - Could parallelize summarization and sentiment agents      "date": "2025-10-25",

      "source": "Source Name"

3. **Caching** (future enhancement):    }

   - Cache search results to avoid re-querying  ]

   - Store processed articles to avoid reprocessing}

```

4. **Rate limiting**:

   - Current settings optimized for reliability---

   - Can reduce `SEARCH_DELAY_SECONDS` if not hitting limits

## 📁 Project Structure

---

```

## Contributingauto_news_sentiment_analysis/

├── .env.example              # Example environment configuration

Contributions are welcome! This project can be extended in many ways:├── .gitignore               # Git ignore rules

├── LICENSE                  # MIT License

### Areas for Contribution├── README.md               # This file

├── requirements.txt        # Python dependencies

- **Additional news sources**: Beyond DuckDuckGo├── main.py                # Application entry point

- **More AI models**: Support for Claude, GPT-4, etc.├── list_models.py         # Utility to list available Gemini models

- **Enhanced analytics**: Trend analysis over time│

- **Visualization**: Charts and dashboards├── config/

- **API wrapper**: REST API for the system│   └── settings.py        # Centralized configuration management

- **Database integration**: Store results in PostgreSQL/MongoDB│

- **Real-time monitoring**: Continuous news monitoring├── src/

- **Multi-language support**: Non-English news sources│   ├── agents/

- **Notification system**: Alerts for significant sentiment shifts│   │   ├── search_agent.py      # News search with DuckDuckGo

│   │   ├── summarize_agent.py   # Article summarization

### How to Contribute│   │   └── sentiment_agent.py   # Sentiment analysis

│   ├── workflows/

1. **Fork the repository**│   │   └── news_workflow.py     # LangGraph orchestration

   ```bash│   ├── tools/

   # Click "Fork" on GitHub│   │   └── search_tool.py       # DuckDuckGo search wrapper

   git clone https://github.com/YOUR_USERNAME/auto_news_with_sentiment_analysis.git│   └── utils/

   ```│       ├── logger.py            # Logging utilities

│       └── output_handler.py    # Output formatting (JSON/CSV)

2. **Create a feature branch**│

   ```bash├── outputs/                 # Generated results (timestamped)

   git checkout -b feature/amazing-feature├── tests/                  # Unit tests

   ```└── docs/                   # Additional documentation

```

3. **Make your changes**

   - Follow existing code style---

   - Add tests for new features

   - Update documentation## 🔧 Troubleshooting



4. **Run tests**### Rate Limiting Issues

   ```bash**Problem**: DuckDuckGo returns `202 Ratelimit` error

   pytest tests/

   ```**Solutions**:

1. Increase `SEARCH_DELAY_SECONDS` to `5.0` or higher in `.env`

5. **Commit with clear messages**2. Reduce `MAX_RESULTS_PER_COMPANY` to `3` or lower

   ```bash3. Wait 5-10 minutes between runs

   git commit -m "Add: Brief description of feature"

   ```### Gemini API Errors

**Problem**: `404 models/gemini-1.5-flash is not found`

6. **Push and create Pull Request**

   ```bash**Solution**:

   git push origin feature/amazing-feature```bash

   ```# Check available models

python list_models.py

### Coding Standards

# Update MODEL_NAME in config/settings.py if needed

- **Python style**: Follow PEP 8```

- **Type hints**: Use type annotations

- **Docstrings**: Google-style docstrings for functions/classes### Common Issues

- **Testing**: Write unit tests for new features

- **Documentation**: Update README for significant changes| Error | Solution |

|-------|----------|

---| `GOOGLE_API_KEY is required` | Add your API key to `.env` file |

| Import errors | Ensure virtual environment is activated |

## License| No articles found | Try different companies or increase `NEWS_DAYS_BACK` |

| Slow performance | Reduce `MAX_RESULTS_PER_COMPANY` or `COMPANIES` list |

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### MIT License Summary

## 📈 Performance Metrics

- ✅ Commercial use

- ✅ Modification- **Processing Time**: ~15-45 seconds for 3 companies (5 articles each)

- ✅ Distribution- **API Calls**: ~16 calls total (1 search + 15 LLM calls)

- ✅ Private use- **Success Rate**: 100% with proper configuration

- ⚠️ Liability and warranty limitations- **Confidence Scores**: 0.90-0.98 (high accuracy)



------



## Acknowledgments## 🧪 Testing



This project is built on the shoulders of giants:```bash

# Run all tests

### Core Technologiespytest tests/



- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework by LangChain# Run with coverage

- **[LangChain](https://www.langchain.com/)** - Framework for developing applications with LLMspytest tests/ --cov=src

- **[Google Gemini](https://ai.google.dev/)** - Advanced AI model for summarization and analysis

- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine# Run specific test file

pytest tests/test_agents.py

### Inspiration```



- Automotive industry analysts who need efficient sentiment monitoring---

- Open-source AI community for democratizing access to advanced AI tools

- LangChain community for excellent documentation and examples## 🤝 Contributing



### Special ThanksContributions welcome! Please follow these steps:



- Google for providing free-tier Gemini API access1. Fork the repository

- DuckDuckGo for providing programmatic search access2. Create feature branch (`git checkout -b feature/AmazingFeature`)

- The open-source Python community3. Commit changes (`git commit -m 'Add AmazingFeature'`)

4. Push to branch (`git push origin feature/AmazingFeature`)

---5. Open Pull Request



## Support and Contact---



### Getting Help## 📝 License



- **Documentation**: Check the `/docs` folder for additional guidesThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- **Issues**: [GitHub Issues](https://github.com/barreag/auto_news_with_sentiment_analysis/issues)

- **Discussions**: [GitHub Discussions](https://github.com/barreag/auto_news_with_sentiment_analysis/discussions)---



### Reporting Bugs## 🙏 Acknowledgments



When reporting bugs, please include:- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Multi-agent orchestration framework

1. Python version (`python --version`)- **[LangChain](https://www.langchain.com/)** - Agent tools and LLM integrations

2. Error messages and stack traces- **[Google Gemini](https://ai.google.dev/)** - Advanced AI capabilities (Gemini 2.5 Flash)

3. Configuration (without API keys!)- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-respecting search engine

4. Steps to reproduce

---

### Feature Requests

## 📧 Support

Have an idea? Open an issue with the `enhancement` label and describe:

1. Use case and motivation- 📖 **Documentation**: Check the `/docs` folder

2. Proposed solution- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/auto_news_sentiment_analysis/issues)

3. Alternative approaches considered- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/auto_news_sentiment_analysis/discussions)



------



## Roadmap**Built with ❤️ for the automotive industry**



### Version 1.0 (Current)*Powered by LangGraph + LangChain + Google Gemini 2.5*

- ✅ Multi-agent architecture with LangGraph
- ✅ Search, summarization, and sentiment analysis
- ✅ JSON and CSV output formats
- ✅ Rate limiting and error handling
- ✅ Comprehensive documentation

### Future Enhancements
- [ ] Web dashboard for visualization
- [ ] Historical trend analysis
- [ ] Support for additional news sources (NewsAPI, Google News)
- [ ] Database persistence (PostgreSQL)
- [ ] REST API wrapper
- [ ] Docker containerization
- [ ] Real-time monitoring with webhooks
- [ ] Multi-language support
- [ ] Advanced analytics (topic modeling, entity extraction)
- [ ] Automated scheduling and reporting

---

**Built for the automotive industry | Powered by AI**

*Multi-agent sentiment analysis made simple*

