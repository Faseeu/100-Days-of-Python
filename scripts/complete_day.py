import os
import sys
import json
import subprocess
from datetime import datetime, date

from visualize import run_visualization_update

# --- Constants ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROGRESS_FILE = os.path.join(ROOT_DIR, 'scripts', 'progress.json')

# --- Core Logic ---
def load_data():
    with open(PROGRESS_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def calculate_missed_days(start_date_str, completed_days, total_days):
    """Calculates if any days were missed."""
    start_date = date.fromisoformat(start_date_str)
    today = date.today()
    expected_days_completed = (today - start_date).days + 1

    # Simple check, can be made more robust
    if expected_days_completed > len(completed_days):
        missed_count = expected_days_completed - len(completed_days)
        print(f"⚠️ Detected {missed_count} missed day(s). Adding to total.")
        return total_days + missed_count
    return total_days

def update_progress(day_num, data):
    """Updates all progress metrics for a completed day."""
    day_num_str = str(day_num)
    today = date.today()

    # Set start date on first day completion
    if not data['challenge_start_date']:
        data['challenge_start_date'] = today.isoformat()

    # Add to completed list if not already there
    if day_num not in data['completed_days']:
        data['completed_days'].append(day_num)
        data['xp'] += 100

    # Calculate time spent
    session = data.get('session_tracking', {}).get(day_num_str)
    if session and 'start_time' in session:
        start_time = datetime.fromisoformat(session['start_time'])
        end_time = datetime.now()
        duration_seconds = (end_time - start_time).total_seconds()
        data['time_spent'][day_num_str] = data['time_spent'].get(day_num_str, 0) + duration_seconds
        # Clear the session
        del data['session_tracking'][day_num_str]

    # Handle missed days
    data['total_days'] = calculate_missed_days(
        data['challenge_start_date'],
        data['completed_days'],
        data['total_days']
    )

    # (Future logic for streaks, levels, achievements can go here)

    return data

def run_git_commands(commit_message):
    """Stages, commits, and pushes changes to GitHub."""
    try:
        print("\n--- Starting Git Automation ---")
        subprocess.run(["git", "add", "."], check=True, cwd=ROOT_DIR)
        subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=ROOT_DIR)
        subprocess.run(["git", "push"], check=True, cwd=ROOT_DIR)
        print("✅ Git operations complete.")
    except Exception as e:
        print(f"❌ Git automation failed: {e}")

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python3 scripts/complete_day.py <day_number> \"[commit message]\"")
        sys.exit(1)

    day_num = int(sys.argv[1])
    commit_message = sys.argv[2] if len(sys.argv) > 2 else f"feat: Complete Day {day_num}"

    print(f"🚀 Completing day {day_num}...")

    data = load_data()
    data = update_progress(day_num, data)
    save_data(data)
    print("✅ Progress data updated.")

    print("🎨 Regenerating visualizations...")
    run_visualization_update()

    run_git_commands(commit_message)

    print(f"\n🎉 Day {day_num} complete! Great work.")

if __name__ == "__main__":
    main()
