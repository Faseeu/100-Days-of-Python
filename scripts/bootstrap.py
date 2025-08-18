import os
import argparse
from datetime import datetime

# --- Constants ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATE_FILE = os.path.join(ROOT_DIR, 'scripts', 'day_template.md')

def create_day_structure(day_num, template_content):
    """Creates the directory and files for a single day."""
    day_str = f"{day_num:03d}"
    day_dir = os.path.join(ROOT_DIR, f'day-{day_str}')

    try:
        os.makedirs(day_dir, exist_ok=True)

        # Create README.md
        readme_path = os.path.join(day_dir, 'README.md')
        if not os.path.exists(readme_path):
            readme_content = template_content.replace('{day}', day_str)
            readme_content = readme_content.replace('{date}', datetime.now().strftime('%Y-%m-%d'))
            with open(readme_path, 'w') as f:
                f.write(readme_content)

        # Create practice.py
        practice_path = os.path.join(day_dir, 'practice.py')
        if not os.path.exists(practice_path):
            with open(practice_path, 'w') as f:
                f.write("# Your Python code for today goes here!\n")

        return True, f"✅ Created structure for day-{day_str}"

    except OSError as e:
        return False, f"❌ Error creating structure for day-{day_str}: {e}"

def main(start_day, end_day):
    """Generates a range of the 100-day directory structure."""
    print(f"🚀 Bootstrapping structure from day {start_day} to {end_day}...")

    try:
        with open(TEMPLATE_FILE, 'r') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Template file not found at {TEMPLATE_FILE}")
        return

    for i in range(start_day, end_day + 1):
        success, message = create_day_structure(i, template_content)
        print(message)
        if not success:
            break

    print(f"\n🎉 Bootstrap batch complete for days {start_day}-{end_day}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bootstrap day directories in batches.")
    parser.add_argument('--start', type=int, required=True, help='The starting day number.')
    parser.add_argument('--end', type=int, required=True, help='The ending day number.')
    args = parser.parse_args()

    main(args.start, args.end)
