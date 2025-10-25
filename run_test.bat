@echo off
REM Quick Start Batch Script for Testing
REM Activates the virtual environment and runs the application

echo ========================================
echo Automotive News Sentiment Analysis
echo Quick Start Test Script
echo ========================================
echo.

REM Check if .env file exists
if not exist .env (
    echo ERROR: .env file not found!
    echo Please create .env file and add your GOOGLE_API_KEY
    echo.
    echo Example .env content:
    echo GOOGLE_API_KEY=your_actual_api_key_here
    pause
    exit /b 1
)

echo Activating virtual environment...
cd C:\Users\TZCYT0
call .\agent_env\Scripts\activate

echo Navigating to project directory...
cd "OneDrive - General Motors\Personal_Development\Github\auto_news_sentiment_analysis"

echo.
echo Starting analysis...
echo.

REM Run the main application
python main.py

echo.
echo ========================================
echo Test Complete!
echo Check the 'outputs' folder for results
echo ========================================
pause
