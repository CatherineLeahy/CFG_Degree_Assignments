# Assignment 1
## Introduction
Assignment 1 of the CFGDegree is centered around Git and GitHub operation. Git was installed and a GitHub account created before demonstrating various operations such as: 
- Creating and using repositories
- Navigating directories
- Creating and adding files to branches
- Opening pull requests


## About Me
I have been working in a Corrosion Laboratory in various roles for almost 7 years before joining the CFGDegree. My coding experience to date consists of some introductory matlab coding in my final year of university, and then a few MOOC Sprints through CFG. I'm super excited to be advancing my skills further on the CFGDegree.
### My Cats
![A picture of Sashimi and Maki](/images/IMG_2565.jpeg)
In my free time, I love spending time at home with my three cats. Above are my oldest two Sashimi and Maki.
## Useful Commands
Some commands I found useful during the assignment, particularly the directory navigation commands. 
- `git status` - shows status of current git branch
- `pwd` - shows current directory
- `cd` - change directory 
- `git add` - add new changes ready to be committed 
## Question 1 - Using Git and GitHub
- ***Checking the status***
  - Command - `git status`
  - ![Screenshot of checking the git status in terminal](/images/git-status.png)
  - Git status is checked to get information such as: 
    - which branch you're currently on
    - if the branch is up to date
    - any changes yet to be committed
    

- ***Creating a branch*** 
  - Command - `git branch <branch name>` or `git checkout -b <branch-name>`
  -  ![Screenshot of creating a branch](/images/creating-a-branch.png)
  - `git branch` is used to create a new branch, but does not automatically switch to the newly created branch
  - `git checkout -b` creates a new branch and then automatically switches to the newly created branch


- ***Adding files to a branch*** 
  - Command - `git add <file-name>` 
- ***Adding commits with meaningful messages*** 
  - Commands -`git commit -m <message>`
  - ![Screenshot of adding commits with meaningful messages](/images/git-commit.png)
- ***Opening a pull request***
  - Done on GitHub website
- ***Merging and deploying to main branch*** 
  - Command - `git checkout main` then, `git merge <branch-name>` 



