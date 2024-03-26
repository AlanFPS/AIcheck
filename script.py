import os
import random
from datetime import datetime, timedelta

# Configuration
total_days = 730  # Total number of days to make commits on
max_commits_per_day = 5  # Maximum number of commits to make on each day
author = "Alan <alan_ps@hotmail.com>"
start_date = datetime(2023, 12, 1) - timedelta(days=730)  # Start from December 1, 2023, and go back 730 days

# List of file names and formats
file_names = ['algorithm', 'fix', 'update', 'feature', 'bugfix', 'layout', 'style', 'test']
file_formats = ['.py', '.js', '.jsx', '.css', '.dart', '.java', '.swift', '.json']

# List of commit messages
commit_messages = [
    'Add new feature',
    'Fix boundary issue',
    'Update documentation',
    'Refactor code structure',
    'Optimize performance',
    'Correct spelling mistake',
    'Improve UI layout',
    'Enhance user experience'
]

# Generate a list of random unique days within the specified period
unique_days = set()
while len(unique_days) < total_days:
    unique_days.add(random.randint(0, 730))
unique_days = list(unique_days)

# Navigate to your repository directory
os.chdir('C:/Users/alan_/Desktop/cdng/AIcheck')

# Make a random number of commits on each selected day
for day in unique_days:
    # Calculate the date for commits
    commit_date = start_date + timedelta(days=day)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Determine the number of commits to make on this day
    num_commits_today = random.randint(1, max_commits_per_day)

    for _ in range(num_commits_today):
        # Select a random file name and format
        file_name_base = random.choice(file_names)
        file_format = random.choice(file_formats)
        # Create a complete file name
        file_name = f'{file_name_base}_{random.randint(1, 100)}{file_format}'
        # Select a random commit message
        commit_message = random.choice(commit_messages)
        # Create or update a file with a unique line
        with open(file_name, 'a') as file:
            file.write(f'Random update on {formatted_date}\n')
        # Stage the file, commit with the specific date, and push
        os.system(f'git add {file_name}')
        os.system(f'git commit --date="{formatted_date}" -m "{commit_message} on {formatted_date}" --author="{author}"')

    # Push all commits for the day
    os.system('git push origin master')  # Ensure your branch name is correct

print("Script completed. Check your GitHub repository.")
