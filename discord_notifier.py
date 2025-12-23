"""
Discord webhook notification system
"""

import requests
import json
from datetime import datetime


class DiscordNotifier:
    """Send notifications to Discord via webhook"""

    def __init__(self, webhook_url: str):
        """
        Initialize Discord notifier

        Args:
            webhook_url: Discord webhook URL
        """
        self.webhook_url = webhook_url

    def send_value_bet_alert(self, bet_info: dict):
        """
        Send a value bet alert to Discord

        Args:
            bet_info: Dictionary containing bet information
                - sport: Sport name (Basketball/Hockey)
                - game: Game matchup
                - bet_type: Type of bet (Moneyline, Spread, etc.)
                - selection: Team/outcome selected
                - pinnacle_odds: True odds from Pinnacle
                - gamdom_odds: Bookmaker odds from Gamdom
                - edge: Edge percentage
                - game_time: Game start time (datetime or string)
                - minutes_until: Minutes until game starts
        """

        embed = {
            "title": "📈 Value Bet Alert",
            "color": 0x00FF00,
            "timestamp": datetime.utcnow().isoformat(),
            "fields": [
                {
                    "name": "🏆 Sport",
                    "value": bet_info.get("sport", "N/A"),
                    "inline": True
                },
                {
                    "name": "🎮 Game",
                    "value": bet_info.get("game", "N/A"),
                    "inline": False
                },
                {
                    "name": "📊 Bet Type",
                    "value": bet_info.get("bet_type", "N/A"),
                    "inline": True
                },
                {
                    "name": "✅ Selection",
                    "value": bet_info.get("selection", "N/A"),
                    "inline": True
                },
                {
                    "name": "📉 Pinnacle Odds",
                    "value": str(bet_info.get("pinnacle_odds", "N/A")),
                    "inline": True
                },
                {
                    "name": "📈 Gamdom Odds",
                    "value": str(bet_info.get("gamdom_odds", "N/A")),
                    "inline": True
                },
                {
                    "name": "🔥 Edge",
                    "value": f"{bet_info.get('edge', 0):.2f}%",
                    "inline": True
                },
                {
                    "name": "⏰ Game Time",
                    "value": str(bet_info.get("game_time", "N/A")),
                    "inline": True
                },
                {
                    "name": "⌛ Starts In",
                    "value": f"{bet_info.get('minutes_until', 'N/A')} minutes",
                    "inline": True
                }
            ],
            "footer": {
                "text": "Value Betting System"
            }
        }

        payload = {
            "embeds": [embed]
        }

        response = requests.post(
            self.webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        response.raise_for_status()
