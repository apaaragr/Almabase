from github import Github
import sys
from collections import Counter

max_pages = 50000

class GitLookUp :
    def __init__(self,userToken=None) :
        if not userToken :
            print("User token not defined")
            sys.exit(0)

        try :
            self.g = Github(userToken)
        except Exception as e:
            print("Unable to connect to github",e)
            sys.exit(0)

    def query(self, orgname="google",repoCount=1,committiesCount=1) :
        try :
            org = self.g.get_organization(orgname)
        except Exception as e :
            print("Unable to fetch org data for the given")
            print("Exception : ",e)
            sys.exit(0)
        try :
            repo_arr = [(repo.forks_count,repo) for repo in org.get_repos()]
        except Exception as e :
            print("Failed ")
        
        repo_arr.sort(key=lambda x:x[0],reverse=True)
        repo_arr = repo_arr[:min(len(repo_arr),repoCount)]

        print("Top repositories are : ")
        print(repo_arr)

        for _,repo in repo_arr :
            count = Counter()
            commits = repo.get_commits()
            for page_number in range(max_pages) :
                
                gotit = False
                commits_on_page = []
                while not gotit :
                    try :
                        commits_on_page = commits.get_page(page_number)
                        gotit = True
                    except :
                        pass
                
                if len(commits_on_page) == 0 :
                    break
                for commit in commits_on_page :
                    name =  commit.commit.committer.name
                    count[name] += 1

            
            commit_counts = list(count.items())
            commit_counts.sort(key=lambda x:x[1], reverse=True)
            commit_counts = commit_counts[:min(len(commit_counts),committiesCount)]
            print("Top committies are :")
            print(commit_counts)
        return repo_arr, commit_counts



if __name__ == '__main__' :
	inputorg = input("Organization Name = ")
	inputrepo = int(input("Number of top repository = "))
	inputcommit = int(input("Number of top communities = "))
	userToken = input("User Token = ")

	lookup = GitLookUp(userToken.strip())
	lookup.query(orgname=inputorg,committiesCount=inputcommit,repoCount=inputrepo)
