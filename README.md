# Almabase
PyGitHub is a Python (2 and 3) library to access the [GitHub API v3] and [Github Enterprise API v3].
This library enables you to manage [GitHub] resources such as repositories, user profiles, and organizations in your Python applications.

[GitHub API v3]: https://developer.github.com/v3
[Github Enterprise API v3]: https://developer.github.com/enterprise/2.13/v3/
[GitHub]: https://github.com

## Install

```bash
$ pip install PyGithub
```

## Simple Demo

```python
from github import Github

# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
```
## Working with the code
Input Variables:-
  1. Organisation Name
  2. Number of Top Repository
  3. Number of Top Committers
  4. Github Token Access

Output:-
  1. Array with top repositories of the given organisation with their fork's count.
  2. For given number of repository, array of top committers with their commit's count.
