"""
Time filtering utilities for game start times
"""

from datetime import datetime, timedelta
from dateutil import parser
import pytz


class TimeUtils:
    """Filter games by start time"""

    @staticmethod
    def is_within_time_window(game_time_str, window_minutes=60):
        """
        Check if game starts within the specified time window

        Args:
            game_time_str: String representation of game start time
            window_minutes: Time window in minutes (default 60)

        Returns:
            Boolean indicating if game is within time window
        """
        try:
            # Parse the game time string
            game_time = parser.parse(game_time_str)

            # Get current time
            current_time = datetime.now(pytz.UTC)

            # If game time is naive (no timezone), assume UTC
            if game_time.tzinfo is None:
                game_time = pytz.UTC.localize(game_time)
            else:
                game_time = game_time.astimezone(pytz.UTC)

            # Calculate time difference
            time_diff = game_time - current_time

            # Check if game is in the future and within window
            if timedelta(0) <= time_diff <= timedelta(minutes=window_minutes):
                return True

            return False

        except Exception as e:
            print(f"Error parsing time '{game_time_str}': {e}")
            return False

    @staticmethod
    def get_minutes_until_game(game_time_str):
        """
        Get minutes until game starts

        Args:
            game_time_str: String representation of game start time

        Returns:
            Minutes until game starts (negative if already started)
        """
        try:
            game_time = parser.parse(game_time_str)
            current_time = datetime.now(pytz.UTC)

            if game_time.tzinfo is None:
                game_time = pytz.UTC.localize(game_time)
            else:
                game_time = game_time.astimezone(pytz.UTC)

            time_diff = game_time - current_time
            return int(time_diff.total_seconds() / 60)

        except Exception as e:
            print(f"Error calculating time difference: {e}")
            return None

