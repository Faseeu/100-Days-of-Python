import json
import os
import pygal
from pygal.style import Style
from datetime import datetime, timedelta

# --- Constants ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
PROGRESS_FILE = os.path.join(ROOT_DIR, 'scripts', 'progress.json')

# --- Custom Style for Pygal ---
custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#333',
    foreground_strong='#333',
    foreground_subtle='#666',
    opacity='.9',
    opacity_hover='.95',
    transition='400ms ease-in',
    colors=('#4caf50', '#f44336', '#2196f3', '#ff9800', '#9c27b0')
)

# --- Chart Generators ---

def generate_progress_chart(data):
    """Generates a gauge chart for overall progress."""
    completed = len(data.get('completed_days', []))
    total = data.get('total_days', 100)

    gauge = pygal.SolidGauge(
        inner_radius=0.70,
        style=custom_style,
        width=400,
        height=200
    )
    gauge.title = 'Overall Progress'
    gauge.add('Completed', [{'value': completed, 'max_value': total}])
    gauge.render_to_file(os.path.join(ASSETS_DIR, 'progress_chart.svg'))

def generate_xp_chart(data):
    """Generates a line chart for XP progression."""
    # This is a placeholder as we don't have historical XP data yet
    line_chart = pygal.Line(
        style=custom_style,
        width=400,
        height=200,
        x_label_rotation=20
    )
    line_chart.title = 'XP Over Time'
    line_chart.x_labels = [f"Day {d}" for d in data.get('completed_days', [])]
    # Simple assumption: 100 XP per day
    xp_values = [100 * i for i in range(1, len(data.get('completed_days', [])) + 1)]
    line_chart.add('XP', xp_values)
    line_chart.render_to_file(os.path.join(ASSETS_DIR, 'xp_chart.svg'))

def generate_errors_chart(data):
    """Generates a bar chart for errors per day."""
    bar_chart = pygal.Bar(
        style=custom_style,
        width=400,
        height=200,
        x_label_rotation=20
    )
    bar_chart.title = 'Errors Logged Per Day'
    error_counts = data.get('error_counts', {})
    bar_chart.x_labels = [f"Day {d}" for d in error_counts.keys()]
    bar_chart.add('Errors', [count for count in error_counts.values()])
    bar_chart.render_to_file(os.path.join(ASSETS_DIR, 'errors_chart.svg'))

def generate_time_chart(data):
    """Generates a bar chart for time spent per day."""
    bar_chart = pygal.Bar(
        style=custom_style,
        width=400,
        height=200,
        x_label_rotation=20
    )
    bar_chart.title = 'Time Spent Per Day (Minutes)'
    time_spent = data.get('time_spent', {})
    bar_chart.x_labels = [f"Day {d}" for d in time_spent.keys()]
    # Convert seconds to minutes
    minutes_spent = [round(s / 60) for s in time_spent.values()]
    bar_chart.add('Minutes', minutes_spent)
    bar_chart.render_to_file(os.path.join(ASSETS_DIR, 'time_chart.svg'))

def generate_heatmap_svg(data):
    """Generates a GitHub-style heatmap SVG manually."""
    # This is a complex task, so we'll create a simplified version.
    # A more robust solution would require more time.
    # For now, let's stick to a placeholder message.
    svg_content = """
    <svg width="600" height="120" xmlns="http://www.w3.org/2000/svg">
        <text x="10" y="20">Contribution Heatmap (Advanced version pending)</text>
        <text x="10" y="40">This will be implemented fully in a future step.</text>
    </svg>
    """
    with open(os.path.join(ASSETS_DIR, 'heatmap.svg'), 'w') as f:
        f.write(svg_content)


# --- Main Execution ---

def run_visualization_update():
    """Main function to update all SVG assets."""
    try:
        with open(PROGRESS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("⚠️ progress.json not found. Using empty data for visualization.")
        data = {}

    print("🎨 Generating visualizations...")
    generate_progress_chart(data)
    generate_xp_chart(data)
    generate_errors_chart(data)
    generate_time_chart(data)
    generate_heatmap_svg(data) # Manual SVG for heatmap
    print("✅ All visualizations updated.")

if __name__ == "__main__":
    run_visualization_update()
