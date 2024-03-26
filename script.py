import os
import random
from datetime import datetime, timedelta

# Configuration
total_days = 100  # Total number of days to make commits on over the past year
max_commits_per_day = 5  # Maximum number of commits to make on each day
author = "Your Name <your_email@example.com>"
start_date = datetime.now() - timedelta(days=365)  # Start from 365 days ago

# Generate a list of random unique days within the last year
unique_days = set()
while len(unique_days) < total_days:
    unique_days.add(random.randint(0, 365))
unique_days = list(unique_days)

# Navigate to your repository directory
os.chdir('/path/to/your/repository')

# Make a random number of commits on each selected day
for day in unique_days:
    # Calculate the date for commits
    commit_date = start_date + timedelta(days=day)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Determine the number of commits to make on this day
    num_commits_today = random.randint(1, max_commits_per_day)

    for _ in range(num_commits_today):
        # Create or update a file with a unique line
        with open('random_daily_update.txt', 'a') as file:
            file.write(f'Random update on {formatted_date}\n')
        # Stage the file, commit with the specific date, and push
        os.system('git add random_daily_update.txt')
        os.system(f'git commit --date="{formatted_date}" -m "Random update for {formatted_date}" --author="{author}"')

    # Push all commits for the day
    os.system('git push origin main')  # Ensure your branch name is 'main' or replace as necessary

print("Script completed. Check your GitHub repository.")
