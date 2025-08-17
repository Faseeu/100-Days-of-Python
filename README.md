# 100 Days of Python: Advanced Gamified Journey

Welcome to my 100-day Python learning challenge, powered by an advanced tracking and visualization system.

---

## My Dashboard

| Progress | XP Over Time |
| :---: | :---: |
| ![Progress Chart](./assets/progress_chart.svg) | ![XP Chart](./assets/xp_chart.svg) |

| Time Spent (Minutes) | Errors Logged |
| :---: | :---: |
| ![Time Chart](./assets/time_chart.svg) | ![Errors Chart](./assets/errors_chart.svg) |

### Contribution Heatmap
![Heatmap](./assets/heatmap.svg)

---

## Daily Workflow

This repository is highly automated. Follow this workflow carefully each day.

### 1. Start the Clock
When you are ready to begin working, run this command to log your start time:
```bash
python3 scripts/start_day.py <day_number>
# Example for day 1:
python3 scripts/start_day.py 1
```

### 2. Code & Log
Write your Python code in the `day-XXX/practice.py` file. To execute it and automatically log all output and errors, use this command. You can run this as many times as you need.
```bash
python3 scripts/run_practice.py <day_number>
# Example for day 1:
python3 scripts/run_practice.py 1
```

### 3. Document Your Learnings
Open the `README.md` file for the day and fill out the "Today's Goal" and "What I Learned" sections.

### 4. Complete the Day
When you have finished all work for the day, run this final command. It will log your end time, update all charts, and save everything to GitHub.
```bash
python3 scripts/complete_day.py <day_number> "[Your commit message]"
# Example for day 1:
python3 scripts/complete_day.py 1 "feat: Complete Day 1 with a new script"
```

---

## Getting Started: First-Time Setup

Before you begin, there are a few one-time steps to ensure the automation works smoothly.

### 1. Install Dependencies (if needed)
If you are running this on a new machine, you may need to install `pygal`.
```bash
pip install pygal
```

### 2. How Git Authentication Works
The scripts in this repository will automatically `commit` and `push` your work to GitHub. For this to work without asking for your password every time, Git uses a **Credential Manager**.

*   **What it is:** A secure, built-in tool that stores your GitHub login information after you use it once.
*   **How it works:** The very first time you run `scripts/complete_day.py`, your system's Git will prompt you to log in to GitHub. This usually opens a browser window for you to securely authenticate.
*   **After that:** The Credential Manager saves a token, and all future pushes from this repository will be automatic and secure. You will not be asked to log in again.

This process is handled entirely by Git itself, ensuring your credentials are safe.

### 3. Termux Users
If you are using Termux on Android, make sure you have installed Python and Git:
```bash
pkg install python
pkg install git
```

---

*This advanced gamified repository structure was built by Jules.*
