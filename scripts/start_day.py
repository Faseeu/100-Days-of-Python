import json
import os
import sys
from datetime import datetime

# --- Constants ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROGRESS_FILE = os.path.join(ROOT_DIR, 'scripts', 'progress.json')

def main():
    """Records the start time for a day's session."""
    if len(sys.argv) < 2:
        print("❌ Usage: python3 scripts/start_day.py <day_number>")
        sys.exit(1)

    try:
        day_num_str = sys.argv[1]
        day_num = int(day_num_str)
        if not 1 <= day_num <= 200: # Allow for extended days
            raise ValueError("Day number is out of the expected range.")
    except ValueError as e:
        print(f"❌ Invalid day number provided. {e}")
        sys.exit(1)

    try:
        with open(PROGRESS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: progress.json not found. Please ensure it exists.")
        sys.exit(1)

    # Record the start time
    now_iso = datetime.now().isoformat()
    if 'session_tracking' not in data:
        data['session_tracking'] = {}

    data['session_tracking'][day_num_str] = {"start_time": now_iso}

    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Day {day_num_str} session started at {now_iso}. Happy coding!")
    except IOError as e:
        print(f"❌ Error writing to progress file: {e}")

if __name__ == "__main__":
    main()
