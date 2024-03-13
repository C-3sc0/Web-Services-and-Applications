# Write a program in python that will read a file from a repository. 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

# Author: Francesco Troja

import requests
from github import Github
from config import api_keys as cfg

# retrieving the API key information
apikey = cfg['githubkey']
g = Github(apikey)

def get_repo(repo_name):
    repo = g.get_repo(repo_name)
    return repo_name, repo.clone_url

# add your repository path and name below:
repo_name = "C-3sc0/aprivateone"
name, url = get_repo(repo_name)
print (f'Link of my repository {name} is {url}')







