import os

repo_path = "D:/Google Disk/FRI (Google Drive)/FRI - PREDMETY/BC/PV, V predmety/PSA - Python v sieťových aplikáciach/Úlohy"
repo_name = "/Cvicenie 03"
repo_url = "https://github.com/JohnnyDT/psa-git.git"

def clone_repo(path, url):
    os.chdir(path)                    # os.* ---> volania operacneho systemu
    os.system("git clone " + url)

def add_file(path, rname, fname):
    os.chdir(path + rname)
    os.system("git add " + fname)

def commit_changes(path, rname, message):
    os.chdir(path)
    os.system("git commit -m \"" + message + "\"")

def push_git(path, rname):
    os.chdir(path)
    os.system("git push")

#clone_repo(repo_path, repo_url)

# file = open(repo_path + repo_path + "/pokus.txt", "w")
# file.write("Nahodny text v subore.")
# file.close()

#add_file(repo_path, repo_path, "pokus.txt")
#commit_changes(repo_path, repo_name, "Pridanie suboru.")
#push_git(repo_path, repo_name)