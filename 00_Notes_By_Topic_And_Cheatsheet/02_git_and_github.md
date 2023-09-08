# GIT:

## KEY CODE:

### LOCAL COMMIT:
```
; cd projectFolder
; echo "This is an intro to the project" > README
; git init
; git status
; git add README
; git commit -m "Initial commit"
; git status
; git log
```

`; cd projectFolder` make sure to be in project folder

`; echo "This is an intro to the project" > README` make change to project, can be external to terminal.

`; git init` initialise a .git folder locally

`; git status` check status of .git folder and changes yet to commit. This will show items to stage.

`; git add README` add files to stage

`; git commit -m "Initial commit"` commit files on stage to .git folder. Takes a snapshot of this version of each file in the repo.

`; git status`

`; git log` check log of changes



### LINK REMOTE WITH LOCAL & COMMIT TO REMOTE:
```
; cd projectFolder
; git remote add origin <YOUR REPOSITORY ADDRESS HERE>
; git remote -v
; git push -u origin main
```

`; cd projectFolder`

`; git remote add origin <YOUR REPOSITORY ADDRESS HERE>` remote repo's url + .git

`; git remote -v` lists remote repositories -- useful if there is more than one? Not sure about this one

`; git push -u origin main` or `; git push` push local folder to remote
    * Enter username and token here if prompted


### PULL FROM REMOTE:
```
; cd projectFolder
; git log
q
; git pull origin main
```

`; cd projectFolder`

`; git log` and `q` to check if there have been any changes to sync to the local

`; git pull origin main` or `; git pull` pull remote folder to local




### CLONE REMOTE REPO:
Make sure you are in the parent folder you want your repo to be in (ie MakersProjects/week00)

`; git clone <REPO LINK ENDING IN .GIT>` is equivalent to:

```
; mkdir ruby-kickstart
; cd ruby-kickstart
; git init
; git remote add origin <REPO LINK ENDING IN .GIT>
; git pull
; cd ..
```
Github `forking` is like cloning



## INTRODUCTION:

* Version control allows for multiple versions or 'branches' to be built simultaneously, then brought together.

* Travel back in time, parallel lives

* This is a similar workflow to when I copy over a project folder and rename to V2


## GIT SETUP:

This was done on my machine already but for future reference:
```
; brew upgrade git
; export PATH=/usr/local/bin:$PATH
; git --version
git version 2.32.0
; git config --global user.name "your name"
; git config --global user.email "your email"
; git config --global core.autocrlf input
; git config --global core.safecrlf true
; git config --global init.defaultBranch main
```
I also already added my authentication token, which is saved locally


## LOCAL GIT REPOSITORY: INITIALISE, ADD, COMMIT, STATUS, LOG:

CODE SEQUENCE:
```
; mkdir projectFolder
; cd projectFolder

; echo "This is the change to the project" > newText.txt

; git init
; git status

; git add newText.txt
; git commit -m "First commit"
; git status

; git log
```

* To start a new project, create a directory > `cd` into it > place under version control by running `git init`

  * Make sure you are inside the project repo when you `git init`. DO NOT INITIALISE YOUR DESKTOP.

  * REPOSITORY: a directory with files that are under "version control".


* `git init` git creates a hidden directory called `.git` that tracks all changes to the files in the directory.

  * Every project (homework, exercises, etc.) should have a separate directory.

* `; rm -rf .git` Delete .git if you accidentally initialise a folder


## REMOTE GITHUB REPOSITORY: PUSH AND PULL .GIT FOLDERS:
Make sure to make a remote repo on github first.

* Make sure you are the owner and that it is public.


LOGIN CREDENTIALS:
`Username for 'https://github.com':` clairepeng94
`Password for 'https://clairep94@github.com:` <my authorisation token> see local file called AuthorisationTokens


WHEN TO COMMIT:

* 'Commit early and commit often'
* You don't have to push to github right away, you can make several commits and pushes in one go
* Ideal commit log:
  * Initial commit
  * Add an empty webpage
  * Put a welcome message on the page
  * Add a header with a log
