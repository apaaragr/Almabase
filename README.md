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

# or using an access token
g = Github("access_token")
__main__
inputorg = input("Organization Name = ")
inputrepo = int(input("Number of top repository = "))
inputcommit = int(input("Number of top communities = "))
userToken = input("User Token = ")
lookup = GitLookUp(userToken.strip())
lookup.query(orgname=inputorg,committiesCount=inputcommit,repoCount=inputrepo)
```
<p align="center">
  <img alt="Git" src="https://cloud.githubusercontent.com/assets/11839736/16642200/6624dde0-43bd-11e6-8595-c81885ba0dc2.png">
</p>

## Working with the code
Input Variables:-
  1. Organisation Name
  2. Number of Top Repository
  3. Number of Top Committers
  4. Github Token Access

Output:-
  1. Array with top repositories of the given organisation with their fork's count.
  2. For given number of repository, array of top committers with their commit's count.
