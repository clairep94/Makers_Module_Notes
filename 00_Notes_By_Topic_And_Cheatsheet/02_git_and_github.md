# GIT: 

* .git is a hidden folder that keeps all the past versions ("commits" or snapshot) of a project folders. 

  * Similar workflow to when I copy over a "V2" folder or a "V2" file

* Repository is a directory with files that are under "version control"

* Version control allows for multiple versions or "branches" to be built simultaneously, then brought together

* These can be saved onto GitHub, which is a cloud service for git repos and version control.

#### REMEMBER FOR EACH CHANGE:

`; git status`
`; git add <file name>`
`; git commit -m "description of change"`
`; git push -u origin main`

=======================================================================================
## INITIALISING A LOCAL REPO & FIRST LOCAL COMMIT:

```
; mkdir projectFolder
; cd projectFolder 
; echo "This is an intro to the project" > README   #This is a change to the project, this can be external to the terminal   

; git init  
; git status  

; git echo .DS_Store >> .gitignore
; git add .gitignore


; git add README  
; git commit -m "Initial commit and ignoring .DS_Store files"
; git status

; git log
q
```

### EXPLANATION OF KEY CODE:

`; cd projectFolder` make sure to be INSIDE the master folder of the entire project.

`; git init` initialise a .git folder locally. Note that .git will ignore empty directories.

`: git echo .DS_Store >> .gitignore` makes it so that git ignores .DS_Store files

`; git status` check status of .git folder and changes yet to commit. This will show items to stage.

`; git add README` add files to stage. Use `; git add --all` to add all changes.

`; git commit -m "Initial commit"` commit files on stage to .git folder. Takes a snapshot of this version of each file in the staging area.

`; git status` check that there are no changes left to stage.

`; git log` check log of changes.

`q` to exit from log.


#### TO DELETE A .GIT FILE IF YOU ACCIDENTALLY INITIALISE A FOLDER:

```
; rm -rf .git
``` 

=======================================================================================
## LOCAL COMMIT:

```
; git status
; git add ChangedProject
; git commit -m "ChangedProject changed described"

; git status
```


=======================================================================================
## LINKING REMOTE WITH LOCAL & PUSHING TO REMOTE:

Make sure to make a remote repo on github first.

* Make sure you are the owner and that it is public.

```
; cd projectFolder
; git remote add origin <YOUR REPOSITORY ADDRESS HERE>
; git remote -v

; git push -u origin main

; git status
```

### EXPLANATION OF KEY CODE:

`; cd projectFolder`

`; git remote add origin <YOUR REPOSITORY ADDRESS HERE>` remote repo's url + .git

`; git remote -v` lists remote repositories -- useful if there is more than one? Not sure about this one

`; git push -u origin main` or `; git push` push local folder to remote
    * Enter username and token here if prompted, see below for initial set-up and authorisation instructions



=======================================================================================

## PULLING & RESETTING FROM REMOTE:

### PULL FROM REMOTE:

```
; cd projectFolder
; git log
q

; git pull origin main
; git status
```

For `pulling` changes by collaborators made after your last push to GitHub

`; cd projectFolder`

`; git log` and `q` to check if there have been any changes to sync to the local

`; git pull origin main` or `; git pull` pull remote folder to local


### RESET FROM REMOTE:

```
; git reset --hard
; git status
```

For `resetting` to the last pushed set up of files on GitHub. Resets ALL files in the repo.


=======================================================================================

## CLONING A REMOTE REPO TO LOCAL:

Make sure you are in the parent folder you want your repo to be in (ie MakersProjects/week00)

```
; git clone <REPO LINK ENDING IN .GIT>
``` 

is equivalent to:

```
; mkdir ruby-kickstart
; cd ruby-kickstart
; git init
; git remote add origin <REPO LINK ENDING IN .GIT>
; git pull
; cd ..
```
Github `forking` is like cloning


=======================================================================================

## GIT SETUP ON MACHINE & PERSONAL ACCESS TOKEN:

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

### PERSONAL ACCESS TOKEN:
[Here the Github documentation on creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)


#### LOGIN CREDENTIALS:
`Username for 'https://github.com':` <my username>
`Password for 'https://clairep94@github.com:` <my authorisation token> see local file called AuthorisationTokens


=======================================================================================

## WHEN TO COMMIT:

* 'Commit early and commit often'
* You don't have to push to github right away, you can make several commits and pushes in one go
* Ideal commit log:
  * Initial commit
  * Add an empty webpage
  * Put a welcome message on the page
  * Add a header with a log
