import requests
import json

class GitHubAPI:
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = 'https://api.github.com'

    def get_user_info(self):
        url = f'{self.base_url}/users/{self.username}'
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_repos(self):
        url = f'{self.base_url}/users/{self.username}/repos'
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_commits(self, repo_name):
        url = f'{self.base_url}/repos/{self.username}/{repo_name}/commits'
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(url, headers=headers)
        return response.json()

def main():
    username = 'your_username'
    token = 'your_token'
    github = GitHubAPI(username, token)
    user_info = github.get_user_info()
    print(json.dumps(user_info, indent=4))
    repos = github.get_repos()
    print(json.dumps(repos, indent=4))
    for repo in repos:
        commits = github.get_commits(repo['name'])
        print(f'Commits for {repo["name"]}:')
        print(json.dumps(commits, indent=4))

if __name__ == '__main__':
    main()