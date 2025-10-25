"""
Configuration settings for the automotive news sentiment analysis system.

This module loads environment variables and provides centralized configuration
for all application components.
"""
import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """
    Application settings and configuration.
    
    All settings can be overridden via environment variables in the .env file.
    """
    
    # ========== API Configuration ==========
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    
    # ========== Target Configuration ==========
    COMPANIES: List[str] = os.getenv("COMPANIES", "GM,Ford,Tesla").split(",")
    MARKET: str = os.getenv("MARKET", "US")
    
    # ========== News Search Settings ==========
    NEWS_DAYS_BACK: int = int(os.getenv("NEWS_DAYS_BACK", "7"))
    MAX_RESULTS_PER_COMPANY: int = int(os.getenv("MAX_RESULTS_PER_COMPANY", "5"))
    SEARCH_DELAY_SECONDS: float = float(os.getenv("SEARCH_DELAY_SECONDS", "3.0"))
    
    # ========== LLM Settings ==========
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.5"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "2000"))
    
    # Model configuration (verified via list_models.py)
    # Available models: gemini-2.5-flash, gemini-2.0-flash, gemini-pro-latest
    MODEL_NAME: str = "gemini-2.5-flash"
    
    def validate(self) -> bool:
        """
        Validate that all required settings are present and valid.
        
        Returns:
            bool: True if validation passes
            
        Raises:
            ValueError: If any required settings are missing or invalid
        """
        if not self.GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY is required. "
                "Please set it in your .env file. "
                "Get your key at: https://makersuite.google.com/app/apikey"
            )
        
        if not self.COMPANIES:
            raise ValueError("At least one company must be specified in COMPANIES")
        
        if self.MAX_RESULTS_PER_COMPANY < 1:
            raise ValueError("MAX_RESULTS_PER_COMPANY must be at least 1")
        
        if self.SEARCH_DELAY_SECONDS < 0:
            raise ValueError("SEARCH_DELAY_SECONDS must be non-negative")
        
        return True


# Create a global settings instance
settings = Settings()
