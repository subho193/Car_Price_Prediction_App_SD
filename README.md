# Car_Price_Prediction_App_SD
This app helps us to get an idea of the price of our old car if we want to sale it.

### Software and Tools Requirements
1. [GitHub Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Render Account](https://render.com/)
4. [GitCLI](https://git-scm.com/docs/gitcli)

### GitHub Part Understanding:
1. create new repository(add readme, gitignore:python, licence :apache)
2. we need to clone the repository so that we can commit our code in that repository 
#### a. click code
#### b. Local>HTTPS>Copy or Clone
#### c. open cmd-go to the folder path where we need to clone the repository(in cmd put: cd path)
#### d. git clone <enter the url copied from the GitHub(repository URL)>
#### e. open VS code inside that folder so that all the files that we are going to create will present over there.
#### f. create a virtual environment

## Step 1 : Create a new virtual environment for our project

#### command for creating virtual environment : python -m venv env
#### command for activating the virtual environment : env\scripts\activate

#### g. git config --global user.name (If the name is not set then :git config --global user.name "your name" )
#### h. git config --global user.email (If the email is not set then : git config --global user.email "your email address")
#### When we are going to commit our code into the GitHub Repository then it will ask for the credentials.

## Most Important : Adding files into repository
#### 1. Command for adding any file into the repository : git add file name with extention
#### 2. Command for adding all the files into the repository : git add .
#### 3. To check which files need to be added : git status
#### 4. To commit(pushes our code from our local to the github staging environment) our code into github : git commit -m "commit message"
#### 5. To push our commit into the github main branch from the stage environment : git push origin main
