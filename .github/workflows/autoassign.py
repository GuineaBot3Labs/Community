import requests
import random
import os

def get_all_users():
    users = []
    with open("users.txt", "r") as file:
        for line in file:
            username = line.strip()  # Directly get the username from each line
            users.append(username)
    return users

def assign_issue(issue_number, assignee, repo_name, token):
    url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}/assignees"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {'assignees': [assignee]}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code not in [200, 201]:
        print(f"Failed to assign issue: {response.status_code}, {response.text}")

def main():
    token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('REPO_NAME')
    issue_number = os.getenv('ISSUE_NUMBER')

    all_users = get_all_users()

    if not all_users:
        print("No users found.")
        return

    assignee = random.choice(all_users)
    assign_issue(issue_number, assignee, repo_name, token)
    print(f"Issue {issue_number} has been assigned to {assignee}")

if __name__ == "__main__":
    main()
