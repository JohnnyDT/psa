import os

cwd = os.getcwd()                           # aktualny priecinok
print("\nAktualny priecinok: \n" + cwd) 

os.chdir("../")                             # zmena aktualneho priecinka

repo_path = "D:/Google Disk/FRI (Google Drive)/FRI - PREDMETY/BC/PV, V predmety/PSA - Python v sieťových aplikáciach/Git"
repo_name = "psa-git"
path = os.path.join(repo_path, repo_name)

#! os.mkdir("NEWWWW")
#! mode = 0o666
#! os.mkdir(path, mode)