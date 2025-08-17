# Project Plan: Advanced Gamification System

This document outlines the plan to build an advanced, gamified learning environment for the 100 Days of Python challenge.

## Phase 1: Foundational Setup

1.  **Reset Repository:** All previous work will be discarded to ensure a clean slate for the new implementation.
2.  **Install Dependencies:** The `pygal` library will be installed to handle all chart generation.
3.  **Bootstrap Full Directory Structure:** The entire 100-day directory structure (`day-001` to `day-100`) will be created upfront. Each directory will contain:
    *   `README.md` (from a template)
    *   `practice.py` (empty file for daily code)

## Phase 2: Core Logic & Tracking

1.  **Implement Smart Date Tracking:**
    *   A `progress.json` file will be created to store all user data, including the start date of the challenge.
    *   The system will calculate progress based on calendar days from the start date.

2.  **Implement Time Tracking:**
    *   A `start_day.py` script will be created. The user will run this script to log the start time for a day's session.
    *   The `complete_day.py` script will calculate the duration between the start and end times and log it.

3.  **Implement Daily Logging:**
    *   A `run_practice.py` script will execute the user's daily code.
    *   It will automatically capture all terminal output and errors and save them to a `practice.log` file for that day.

## Phase 3: Advanced Visualization with `pygal`

1.  **Create Visualization Module (`scripts/visualize.py`):**
    *   This script will contain all the logic for generating `pygal` charts.
    *   It will read data from `progress.json` and the daily `practice.log` files.

2.  **Generate `pygal` Charts:** The script will generate the following SVG charts and save them in the `assets/` directory:
    *   An enhanced progress bar.
    *   A contribution heatmap for the entire challenge period.
    *   A line graph showing XP progression over time.
    *   A bar chart showing the number of errors per day.
    *   A graph visualizing the time spent per day.

## Phase 4: Finalization & Workflow Integration

1.  **Create Master `complete_day.py` Script:**
    *   This script will be the main user entry point to finalize a day's work.
    *   It will update `progress.json` with the day's data (completion, time spent, etc.).
    *   It will handle the "missed day" logic, appending a new day to the total if necessary.
    *   It will call the visualization script to regenerate all `pygal` charts.
    *   It will handle the `git add`, `commit`, and `push` automation.

2.  **Create Final `README.md`:**
    *   The main `README.md` will be overhauled to serve as a dashboard.
    *   It will embed all the newly generated `pygal` SVG charts.
    *   It will contain clear, step-by-step instructions for the new, advanced workflow (`start_day`, `run_practice`, `complete_day`).
