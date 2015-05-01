##############################################
# This script provides the github.com url    #
# for the git directory you're currently in. #
# Think of it as 'pwd', but for git - gwd    #
#                                            #
# To make this work, you'll need to add the  #
# following bash function to your rc/profile #
# file:                                      #
# gwdFunction() {                            #
#     python ~/bin/gwd.py                    #
# }                                          #
# alias gwd=gwdFunction                      #
#                                            #
# You'll also need to make sure that you     #
# place this script in your path. Mine is    #
# in my user's home directory / bin; which   #
# is in my PATH.                             #
##############################################
import subprocess

origin = subprocess.check_output("git config --get remote.origin.url | sed 's/:/\//' | awk -F@ '{print $2}' | cut -d. -f1,2", shell=True).rstrip('\n')
originSplit = origin.split("/")

directory = subprocess.check_output("pwd", shell=True).rstrip('\n')
directorySplit = directory.split("/")
branch = subprocess.check_output("git branch | grep '*' | awk '{print $2}'", shell=True).rstrip('\n')

output = str('https://') + origin + str('/tree/') + branch

testCase = False

for i in directorySplit:
        if testCase:
                output = output + "/" + i
        if i == originSplit[-1]:
                testCase = True

print output
