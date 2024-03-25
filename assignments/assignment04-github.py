# Write a program in python that will read a file from a repository. 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

# Author: Francesco Troja

import requests
from github import Github
from config import api_keys as cfg
import re


# Retrieving the API key information
apikey = cfg['githubkey']
g = Github(apikey)

repo_name = "C-3sc0/aprivateone"
file_path = "test523.txt"
commit_mess = "Replace Andrew with Francesco"
add_text = "This text serves as example to replace the string andrew with a new one everytime it appears. Andrew is a masculine Greek name meaning “strong” Andrew also has biblical connections, andrew associated with Jesus’s first Apostle"
commit_new_file = 'Adding a new file in the repository'

# Get the repository
repo = g.get_repo(repo_name)

try:
    # Try to get the file from the repository
    file = repo.get_contents(file_path)
    data = file.decoded_content.decode("utf-8")
    print(f"Existing content in {file_path}:\n{data}")

    # Modify the content
    new_data = re.sub("Andrew", "Francesco", data, flags=re.IGNORECASE)
    print(f"The new content:\n{new_data}")

    # Update the file
    repo.update_file(file.path, commit_mess, new_data, file.sha)
    print(f"{file_path} updated successfully!")
except:
    # If the file doesn't exist in the repository, create it
    initial_content = add_text
    created_file = repo.create_file(file_path, commit_new_file, initial_content)
    print(f"The {file_path} has been created correctly.")
    file_content = created_file['content']
    dec_content = file_content.decoded_content.decode("utf-8")
    rep_data = re.sub("Andrew", "Francesco", dec_content, flags=re.IGNORECASE)
    repo.update_file(file_content.path, commit_mess, rep_data, file_content.sha)
    print(f"The new content that replace the strinng Adrew:\n{rep_data}")


