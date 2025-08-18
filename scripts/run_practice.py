import os
import sys
import json
import subprocess
from datetime import datetime

# --- Constants ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROGRESS_FILE = os.path.join(ROOT_DIR, 'scripts', 'progress.json')

def update_error_count(day_num_str, has_error):
    """Updates the error count for a given day in progress.json."""
    if not has_error:
        return

    try:
        with open(PROGRESS_FILE, 'r+') as f:
            data = json.load(f)

            if 'error_counts' not in data:
                data['error_counts'] = {}

            # Increment error count for the day
            data['error_counts'][day_num_str] = data['error_counts'].get(day_num_str, 0) + 1

            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except (FileNotFoundError, IOError) as e:
        print(f"⚠️ Warning: Could not update error count. {e}")


def main():
    """Executes a day's practice.py and logs its output."""
    if len(sys.argv) < 2:
        print("❌ Usage: python3 scripts/run_practice.py <day_number>")
        sys.exit(1)

    try:
        day_num_str = sys.argv[1]
        day_num = int(day_num_str)
        if not 1 <= day_num <= 200: # Allow for extended days
            raise ValueError("Day number is out of the expected range.")
    except ValueError as e:
        print(f"❌ Invalid day number provided. {e}")
        sys.exit(1)

    day_dir = os.path.join(ROOT_DIR, f'day-{day_num_str.zfill(3)}')
    practice_file = os.path.join(day_dir, 'practice.py')
    log_file = os.path.join(day_dir, 'practice.log')

    if not os.path.exists(practice_file):
        print(f"❌ Error: Practice file not found at {practice_file}")
        sys.exit(1)

    print(f"🚀 Executing practice script for day-{day_num_str}...")

    start_time = datetime.now()
    timestamp = start_time.strftime('%Y-%m-%d %H:%M:%S')

    result = subprocess.run(
        [sys.executable, practice_file],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )

    # If an error occurred, capture the code that caused it
    code_snapshot = ""
    if result.stderr:
        try:
            with open(practice_file, 'r', encoding='utf-8') as f:
                code_snapshot = f.read()
            code_snapshot = f"\n--- CODE AT TIME OF ERROR ---\n{code_snapshot}"
        except IOError:
            code_snapshot = "\n--- CODE AT TIME OF ERROR ---\n[Could not read practice file]"

    # Log results
    log_header = f"\n{'='*20} LOG ENTRY: {timestamp} {'='*20}"
    log_output = f"--- STDOUT ---\n{result.stdout or '[No output]'}"
    log_errors = f"--- STDERR ---\n{result.stderr or '[No errors]'}"
    full_log = f"{log_header}{code_snapshot}\n{log_output}\n{log_errors}\n"

    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(full_log)
        print(f"✅ Successfully executed. Log updated at: {log_file}")
    except IOError as e:
        print(f"❌ Error writing to log file: {e}")

    # Update error count if an error occurred
    if result.stderr:
        print("Stderr detected, updating error count...")
        update_error_count(day_num_str, True)

if __name__ == "__main__":
    main()
