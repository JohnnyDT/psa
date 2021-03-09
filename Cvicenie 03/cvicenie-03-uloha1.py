# Napiste program, ktory podla vypisu "git status" 
# rozozna vsetky nove (untracked) subory,
# prida ich do repozitara,
# vykona commit a
# odosle zmeny na server

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import os
import sys

repo_path = "D:/Google Disk/FRI (Google Drive)/FRI - PREDMETY/BC/PV, V predmety/PSA - Python v sieťových aplikáciach/Git"
repo_name = "/psa-git"
repo_url = "https://github.com/JohnnyDT/psa-git.git"

def git_status(path, rname):
    os.chdir(path + rname)
    os.system("git status")

def git_status_add_commit_push(path, rname, message):
    os.chdir(path + rname)

    os.system("clear")

    output_file = "output.txt"                      # zadefinujem si nazov suboru

    if os.path.exists(output_file):                 # ak taky subor existuje - zmazem ho
        os.remove(output_file)

    os.system("git status -sb > " + output_file)    # git status -sb ---> skrateny vypis, ktory zobrazi pred untracked files znaky "??" ---> presmeruje do suboru

    untracked_files = []                            # list pre 'untracked files'
    git_status_data = []                            # list pre data zo suboru

    file = open(output_file, "r")                   # otvori subor na citanie "r"
    git_status_data = file.readlines()              # nacita data zo suboru po riadku

    for i in git_status_data:                       # odstranenie znakov "??" zo zaciatku, "\n" z konca
        if "??" in i:
            untracked_files.append(i[3:-1])         

    if untracked_files:
        print(f"{bcolors.HEADER}\nUNTRACKED FILES:{bcolors.ENDC}")                     # vypis untracked files

    for j in untracked_files:
        print(f"{bcolors.WARNING}FILE: " + j + f"{bcolors.ENDC}")

    for k in range(len(untracked_files)):           #
    #? GIT ADD file
        print(f"{bcolors.OKGREEN}\n---> git add " + untracked_files[k] + f"\n{bcolors.ENDC}")
        os.system("git add " + untracked_files[k])
        
    #? GIT COMMIT
        print(f"{bcolors.OKGREEN}\n---> git commit " + untracked_files[k] + " -m \"" + message + f"\" \n{bcolors.ENDC}")
        os.system("git commit " + untracked_files[k] + " -m \"" + message + "\"")

    if untracked_files:
        print(f"{bcolors.OKGREEN}\n---> git push\n{bcolors.ENDC}")

    os.system("git push")

git_status_add_commit_push(repo_path, repo_name, "Uprava suboru.")