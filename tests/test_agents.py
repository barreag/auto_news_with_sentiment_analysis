"""
Unit tests for the agents.
"""
import pytest
from unittest.mock import Mock, patch
from src.agents.search_agent import NewsSearchAgent
from src.agents.summarize_agent import SummarizationAgent
from src.agents.sentiment_agent import SentimentAnalysisAgent


class TestNewsSearchAgent:
    """Tests for NewsSearchAgent."""
    
    def test_initialization(self):
        """Test agent initializes correctly."""
        agent = NewsSearchAgent()
        assert agent is not None
        assert agent.search_tool is not None
    
    @patch('src.agents.search_agent.NewsSearchTool')
    def test_search_news(self, mock_tool):
        """Test news search functionality."""
        # Mock the search tool
        mock_tool.return_value.search_multiple_companies.return_value = {
            "GM": [{"title": "Test", "url": "http://test.com"}]
        }
        
        agent = NewsSearchAgent()
        agent.search_tool = mock_tool.return_value
        
        results = agent.search_news(["GM"], "US")
        assert "GM" in results


class TestSummarizationAgent:
    """Tests for SummarizationAgent."""
    
    def test_initialization(self):
        """Test agent initializes correctly."""
        agent = SummarizationAgent()
        assert agent is not None
        assert agent.llm is not None


class TestSentimentAnalysisAgent:
    """Tests for SentimentAnalysisAgent."""
    
    def test_initialization(self):
        """Test agent initializes correctly."""
        agent = SentimentAnalysisAgent()
        assert agent is not None
        assert agent.llm is not None


if __name__ == "__main__":
    pytest.main([__file__])
