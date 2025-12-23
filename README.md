# value-bets
Project Summary
The Value Betting System is an automated tool tailored for sports betting enthusiasts. It analyzes odds from Pinnacle (true odds) and Gamdom (bookmaker odds) to uncover profitable betting opportunities with a minimum edge of 2%. The system enhances betting strategies by providing real-time alerts through Discord when qualifying bets are identified.

Project Module Description
The system consists of the following functional modules:

scraper.py: Scrapes live odds from Pinnacle and Gamdom.
odds_calculator.py: Utilities for odds conversion and edge calculation.
time_filter.py: Filters games based on their start times.
discord_notifier.py: Sends alerts to a Discord webhook.
main.py: Orchestrates the entire betting process.
scheduler.py: Automates the execution of the main script at regular intervals.
config.py: Holds configuration settings, including the Discord webhook URL and thresholds.
requirements.txt: Lists Python dependencies.
README.md: Provides documentation and usage instructions.
setup.sh: Script for setting up the project environment.
test_system.py: A comprehensive test script for validating system components without web scraping.
Directory Tree
.
├── README.md              # Comprehensive documentation
├── config.py              # Configuration settings
├── discord_notifier.py    # Sends alerts to Discord
├── main.py                # Main execution script
├── odds_calculator.py     # Odds conversion utilities
├── requirements.txt       # Python dependencies
├── scheduler.py           # Automated scheduler
├── scraper.py             # Web scraping modules
├── setup.sh               # Setup script for environment
├── test_system.py         # Test script for system components
├── time_filter.py         # Time filtering utilities
└── todo.md                # Development plan and tasks
File Description Inventory
README.md: Documentation on setup, usage, and features.
config.py: Contains configuration variables for the system.
discord_notifier.py: Manages sending notifications to Discord.
main.py: Executes the core functionality of the betting system.
odds_calculator.py: Provides methods for calculating odds and edge.
requirements.txt: Lists required Python packages for the project.
scheduler.py: Schedules the main script to run at defined intervals.
scraper.py: Implements web scraping logic for odds retrieval.
setup.sh: Automates the setup of the project environment.
test_system.py: Validates components of the system without web scraping.
time_filter.py: Filters events based on time constraints.
todo.md: Outlines the development plan and features to be implemented.
Technology Stack
Python 3.x: Programming language for system development.
Selenium/Playwright: For web scraping and dynamic content extraction.
Requests: For making HTTP requests.
Discord Webhooks: For sending notifications.
Schedule: For automating task scheduling.
Usage
Clone or download the repository.
Install Python dependencies:
pip install -r requirements.txt
Set up the environment using the setup.sh script:
bash setup.sh
Configure the Discord Webhook in config.py:
Replace YOUR_DISCORD_WEBHOOK_URL_HERE with your actual Discord webhook URL.
Run the main script to scan for value bets:
python main.py
For automated execution, use the scheduler.py:
python scheduler.py
To test the system, run:
python test_system.py
