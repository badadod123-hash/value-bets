"""
Configuration settings for the value betting system
"""

# Discord Webhook URL - REPLACE WITH YOUR ACTUAL WEBHOOK URL
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"

# Edge threshold (percentage)
MIN_EDGE_PERCENTAGE = 2.0

# Time window (minutes)
TIME_WINDOW_MINUTES = 60

# Pinnacle URLs
PINNACLE_BASKETBALL_URL = "https://www.pinnacle.com/en/basketball/matchups/"
PINNACLE_HOCKEY_URL = "https://www.pinnacle.com/en/hockey/matchups/"

# Gamdom URLs
GAMDOM_BASKETBALL_URL = "https://gamdom.com/sports/sport/sport/20/8"
GAMDOM_ICE_HOCKEY_URL = "https://gamdom.com/sports/ice-hockey"

# Scraping settings
BROWSER_HEADLESS = True
PAGE_LOAD_TIMEOUT = 30
ELEMENT_WAIT_TIMEOUT = 10

# Logging
LOG_LEVEL = "INFO"
