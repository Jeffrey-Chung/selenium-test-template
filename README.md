# Selenium-Test-Template

This is a template that can run your Selenium tests locally and on GitHub Actions.
`selenium_local.py`: Runs your tests locally (make sure Firefox is installed)
`selenium_global.py`: Runs your test on GitHub Actions

You can either Fork/Clone my repository. Instructions are down below

## Fork Repository

1. Simply click on the Fork button at the top right of my repo on Github
2. Make sure you keep the "Copy the master branch only" option ticked so that you can add your own branches later on
3. Copy the SSH URL of the repo (i.e.: `git@github.com:Jeffrey-Chung/<repo name>.git`)
4. Run the command `git clone <SSH URL>` on your terminal 


## Clone Repository
Assuming that you have created a SSH key already 

1. Copy the SSH URL of the repo (i.e.: `git@github.com:Jeffrey-Chung/<repo name>.git`)
2. Run the command `git clone <SSH URL>` on your terminal
3. Move to the directory and run `git remote rm origin` so that your progress doesn't affect my repo
4. Create a new repo on GitHub and add your origin to your directory


## Usage
Follow this once you either fork/clone my repo

1. Add the link of your website to test on the `'''INSERT YOUR URL'''` prompts in both scripts
2. Write all your tests in the try block on the `ui_test` function in `selenium_local.py`
3. Once you push all your progress on the main branch, GitHub Actions will be ran