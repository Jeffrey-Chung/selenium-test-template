# Selenium-Test-Template

This is a template that can run your Selenium tests locally and on GitHub Actions.
* `test_firefox.py`: Runs your tests on Firefox Browser
* `test_chrome.py`: Runs your tests on Google Chrome Browser
* `test_edge.py`: Runs your tests on Microsoft Edge Browser

You can either Fork/Clone my repository. Instructions are down below

## Fork Repository

1. Simply click on the Fork button at the top right of my repo on Github
2. Make sure you keep the "Copy the master branch only" option ticked so that you can add your own branches later on
3. Copy the SSH URL of the repo (i.e.: `git@github.com:Jeffrey-Chung/<repo name>.git`)
4. Run the command `git clone <SSH URL>` on your terminal to clone the repo onto your local machine


## Clone Repository
Assuming that you have created a SSH key already 

1. Copy the SSH URL of the repo (i.e.: `git@github.com:Jeffrey-Chung/<repo name>.git`)
2. Run the command `git clone <SSH URL>` on your terminal to clone the repo onto your local machine
3. Move to the directory (Hint: use the `cd` command) and run `git remote rm origin` so that your progress doesn't affect my repo
4. Create a new repo on GitHub and add your origin to the directory


## Usage (GitHub Actions)
Follow this once you either fork/clone my repo

1. Add the link of your website to test on the `'''INSERT URL HERE'''` prompt(s) in `utilities.py`
2. Write all your tests in the try block on the `ui_test` function in `utilities.py`
3. Once you push all your progress on the main branch, GitHub Actions will be ran


## Local Usage
1. Run ``java -jar selenium-server-4.8.1.jar standalone`` command on one terminal
2. Run your script with the command ``python3 test_<browser of your choice>.py`` on another terminal in the same directory
NOTE: Make sure both terminals are in the same directory
3. Once the script has ran, you can terminate the server via ``ctrl + c`` on the terminal from step 1. 
