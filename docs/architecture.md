# System Architecture

## Overview

The Automotive News Sentiment Analysis System is a multi-agent application that automatically searches, summarizes, and analyzes sentiment for automotive news articles. It focuses on three major automotive companies (GM, Ford, and Tesla) in the US market.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Main Application (main.py)                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           LangGraph Workflow Orchestration                   │
│                (news_workflow.py)                            │
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
         │             │             │
    ┌────▼─────┐  ┌───▼──────┐  ┌───▼──────┐
    │DuckDuck  │  │  Gemini  │  │  Gemini  │
    │Go Search │  │   API    │  │   API    │
    └──────────┘  └──────────┘  └──────────┘
```

## Components

### 1. Main Application (`main.py`)
- Entry point for the system
- Handles command-line arguments
- Orchestrates workflow execution
- Manages output formatting and saving

### 2. LangGraph Workflow (`src/workflows/news_workflow.py`)
- Orchestrates the three agents in sequence
- Manages state between agents
- Handles error recovery
- Flow: Search → Summarize → Sentiment

### 3. News Search Agent (`src/agents/search_agent.py`)
- Searches DuckDuckGo for automotive news
- Filters by date range (last 7 days)
- Targets US market specifically
- Returns article metadata (title, URL, snippet, source)

### 4. Summarization Agent (`src/agents/summarize_agent.py`)
- Uses Google Gemini API to create summaries
- Generates 2-3 sentence summaries
- Focuses on business impact and key developments
- Maintains objectivity

### 5. Sentiment Analysis Agent (`src/agents/sentiment_agent.py`)
- Analyzes sentiment using Google Gemini API
- Classifies as positive, negative, or neutral
- Provides confidence scores
- Includes reasoning for classification

### 6. Supporting Components

#### Configuration (`config/settings.py`)
- Environment variable management
- Default settings
- Validation

#### Tools (`src/tools/`)
- `search_tool.py`: DuckDuckGo search wrapper

#### Utils (`src/utils/`)
- `logger.py`: Logging utilities
- `output_handler.py`: Output formatting and saving

## Data Flow

```
1. User Input (Companies, Market)
   ↓
2. Search Agent
   - Queries DuckDuckGo
   - Returns raw articles
   ↓
3. State Update (Articles in workflow state)
   ↓
4. Summarization Agent
   - Processes each article
   - Adds summary field
   ↓
5. State Update (Articles with summaries)
   ↓
6. Sentiment Analysis Agent
   - Analyzes each article
   - Adds sentiment, confidence, reasoning
   ↓
7. Final State (Complete analysis)
   ↓
8. Output Handler
   - Formats results
   - Saves to JSON/CSV
   - Displays summary
```

## State Management

The workflow uses a shared state dictionary that flows through all agents:

```python
{
    "companies": ["GM", "Ford", "Tesla"],
    "market": "US",
    "articles": {
        "GM": [
            {
                "title": "...",
                "url": "...",
                "snippet": "...",
                "summary": "...",
                "sentiment": "positive",
                "confidence": 0.85,
                "reasoning": "..."
            }
        ],
        "Ford": [...],
        "Tesla": [...]
    },
    "status": "completed",
    "error": ""
}
```

## Agent Communication

Agents communicate through the shared state managed by LangGraph:

1. Each agent receives the current state
2. Agent performs its task
3. Agent updates the state with new information
4. Updated state flows to next agent

## Error Handling

- Each agent has try-catch error handling
- Errors are logged and added to state
- Workflow continues with partial results when possible
- Final status indicates success or failure

## Scalability Considerations

- **Adding Companies**: Simply update the COMPANIES config
- **Adding Markets**: Update MARKET config and search queries
- **Adding Agents**: Add new node to LangGraph workflow
- **Parallel Processing**: Can be added for multiple companies
- **Rate Limiting**: Implemented in API calls
- **Caching**: Can be added to reduce duplicate searches

## Technology Stack

- **Orchestration**: LangGraph
- **Agent Framework**: LangChain
- **LLM**: Google Gemini API
- **Search**: DuckDuckGo (duckduckgo-search)
- **Language**: Python 3.9+
- **Data Processing**: Pandas, NumPy
- **Testing**: pytest

## Security Considerations

- API keys stored in environment variables
- No sensitive data in source control
- Input validation on all user inputs
- Secure API communication (HTTPS)

## Future Enhancements

1. **Database Integration**: Store historical results
2. **Web Interface**: Add Flask/FastAPI frontend
3. **Real-time Monitoring**: WebSocket updates
4. **Advanced Analytics**: Trend analysis over time
5. **Multi-language Support**: Analyze non-English news
6. **Email Reports**: Automated daily/weekly reports
7. **Comparison Views**: Side-by-side company analysis
8. **Stock Price Correlation**: Link sentiment to market data
