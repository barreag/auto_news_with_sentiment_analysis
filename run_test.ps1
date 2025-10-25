# Quick Start Script for Testing
# Run this script to test the automotive news sentiment analysis system

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Automotive News Sentiment Analysis" -ForegroundColor Cyan
Write-Host "Quick Start Test Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if .env file exists
if (-Not (Test-Path ".env")) {
    Write-Host "ERROR: .env file not found!" -ForegroundColor Red
    Write-Host "Please create .env file and add your GOOGLE_API_KEY" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Example .env content:" -ForegroundColor Yellow
    Write-Host "GOOGLE_API_KEY=your_actual_api_key_here" -ForegroundColor Gray
    exit 1
}

# Check if GOOGLE_API_KEY is set
$envContent = Get-Content ".env" -Raw
if ($envContent -match "GOOGLE_API_KEY=your_google_api_key_here" -or $envContent -match "GOOGLE_API_KEY=\s*$") {
    Write-Host "WARNING: Please update your GOOGLE_API_KEY in .env file" -ForegroundColor Yellow
    Write-Host "Get your key at: https://makersuite.google.com/app/apikey" -ForegroundColor Cyan
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        exit 1
    }
}

Write-Host "Starting analysis..." -ForegroundColor Green
Write-Host ""

# Run the main application
python main.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Test Complete!" -ForegroundColor Cyan
Write-Host "Check the 'outputs' folder for results" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
