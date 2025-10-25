"""
LangGraph workflow for orchestrating the multi-agent news analysis system.
"""
from typing import Dict, List, Any, TypedDict
from langgraph.graph import StateGraph, END

from config.settings import settings
from src.agents.search_agent import NewsSearchAgent
from src.agents.summarize_agent import SummarizationAgent
from src.agents.sentiment_agent import SentimentAnalysisAgent
from src.utils.logger import logger


class WorkflowState(TypedDict):
    """State shared across all agents in the workflow."""
    companies: List[str]
    market: str
    articles: Dict[str, List[Dict[str, Any]]]
    status: str
    error: str


class NewsAnalysisWorkflow:
    """
    LangGraph workflow that orchestrates the news analysis pipeline.
    
    Pipeline: Search -> Summarize -> Sentiment Analysis
    """
    
    def __init__(self):
        """Initialize the workflow with all agents."""
        logger.info("Initializing NewsAnalysisWorkflow")
        
        # Initialize agents
        self.search_agent = NewsSearchAgent()
        self.summarization_agent = SummarizationAgent()
        self.sentiment_agent = SentimentAnalysisAgent()
        
        # Build the workflow graph
        self.workflow = self._build_workflow()
        
        logger.info("NewsAnalysisWorkflow initialized successfully")
    
    def _build_workflow(self) -> StateGraph:
        """
        Build the LangGraph workflow.
        
        Returns:
            Compiled workflow graph
        """
        # Create the state graph
        workflow = StateGraph(WorkflowState)
        
        # Add nodes for each agent
        workflow.add_node("search", self._search_node)
        workflow.add_node("summarize", self._summarize_node)
        workflow.add_node("sentiment", self._sentiment_node)
        
        # Define the workflow edges (pipeline flow)
        workflow.set_entry_point("search")
        workflow.add_edge("search", "summarize")
        workflow.add_edge("summarize", "sentiment")
        workflow.add_edge("sentiment", END)
        
        # Compile the workflow
        return workflow.compile()
    
    def _search_node(self, state: WorkflowState) -> WorkflowState:
        """
        Execute the search agent node.
        
        Args:
            state: Current workflow state
            
        Returns:
            Updated state with search results
        """
        try:
            logger.info("Workflow node: search")
            state["status"] = "searching"
            
            # Execute search agent
            result = self.search_agent(state)
            
            # Check if we got any articles
            total_articles = sum(len(arts) for arts in result.get("articles", {}).values())
            if total_articles == 0:
                logger.warning("No articles found by search agent")
                state["status"] = "completed_with_no_results"
            else:
                state["status"] = "search_completed"
            
            return result
            
        except Exception as e:
            logger.error(f"Error in search node: {str(e)}")
            state["status"] = "error"
            state["error"] = str(e)
            return state
    
    def _summarize_node(self, state: WorkflowState) -> WorkflowState:
        """
        Execute the summarization agent node.
        
        Args:
            state: Current workflow state
            
        Returns:
            Updated state with summaries
        """
        try:
            logger.info("Workflow node: summarize")
            state["status"] = "summarizing"
            
            # Execute summarization agent
            result = self.summarization_agent(state)
            state["status"] = "summarization_completed"
            
            return result
            
        except Exception as e:
            logger.error(f"Error in summarization node: {str(e)}")
            state["status"] = "error"
            state["error"] = str(e)
            return state
    
    def _sentiment_node(self, state: WorkflowState) -> WorkflowState:
        """
        Execute the sentiment analysis agent node.
        
        Args:
            state: Current workflow state
            
        Returns:
            Updated state with sentiment analysis
        """
        try:
            logger.info("Workflow node: sentiment")
            state["status"] = "analyzing_sentiment"
            
            # Execute sentiment agent
            result = self.sentiment_agent(state)
            state["status"] = "completed"
            
            return result
            
        except Exception as e:
            logger.error(f"Error in sentiment node: {str(e)}")
            state["status"] = "error"
            state["error"] = str(e)
            return state
    
    def run(self, companies: List[str] = None, market: str = None) -> Dict[str, Any]:
        """
        Run the complete workflow.
        
        Args:
            companies: List of companies to analyze (defaults to config)
            market: Market focus (defaults to config)
            
        Returns:
            Final workflow state with all analysis results
        """
        # Set defaults
        if companies is None:
            companies = settings.COMPANIES
        if market is None:
            market = settings.MARKET
        
        logger.info(f"Starting workflow for companies: {', '.join(companies)}")
        
        # Initialize state
        initial_state: WorkflowState = {
            "companies": companies,
            "market": market,
            "articles": {},
            "status": "initialized",
            "error": ""
        }
        
        # Execute workflow
        try:
            final_state = self.workflow.invoke(initial_state)
            
            # Log completion
            total_articles = sum(len(arts) for arts in final_state.get("articles", {}).values())
            logger.info(f"Workflow completed. Status: {final_state.get('status')}")
            logger.info(f"Total articles processed: {total_articles}")
            
            return final_state
            
        except Exception as e:
            logger.error(f"Workflow execution failed: {str(e)}")
            return {
                **initial_state,
                "status": "error",
                "error": str(e)
            }
    
    def visualize(self, output_path: str = "workflow_graph.png"):
        """
        Visualize the workflow graph.
        
        Args:
            output_path: Path to save the visualization
        """
        try:
            # This requires additional dependencies (pygraphviz or graphviz)
            from IPython.display import Image, display
            display(Image(self.workflow.get_graph().draw_mermaid_png()))
            logger.info(f"Workflow graph saved to {output_path}")
        except ImportError:
            logger.warning("Visualization requires pygraphviz or graphviz to be installed")
        except Exception as e:
            logger.error(f"Error visualizing workflow: {str(e)}")
