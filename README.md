# Selenium-Test-Template

This is a template that can run your Selenium tests locally and/or on GitHub Actions.
* src/test_firefox.py will run the tests on FireFox
* src/test_chrome.py will run the tests on Chrome
* src/test_edge.py will run the tests on Edge

You can either Fork/Clone my repository. Instructions are down below

## Usage (GitHub Actions)

1. Fork/Clone the Repository linked above
2. In the directory, go to the src folder and find `utilities.py`
3. Add the link of your website to test on the `'''INSERT URL HERE'''` prompt in `utilities.py`
4. Write all your tests in the try block on the `ui_test` function in `utilities.py`
5. Once you push/PR all your progress on the main branch, GitHub Actions will be ran
6. Tests will be ran on each browser simultaneously on GitHub Actions (Edge, Chrome and Firefox) via Docker Compose


## Local Usage (via Docker Compose) 

1. Fork/Clone the Repository linked above
2. In the directory, go to the src folder and find `utilities.py`
3. Add the link of your website to test on the `'''INSERT URL HERE'''` prompt in `utilities.py`
4. Write all your tests in the try block on the `ui_test` function in `utilities.py`
5. Run the docker-compose file with the command to spin up the containers for the Selenium Grid Server: ``docker-compose -f docker-compose.yaml up -d``
6. Run a Python script based on the browser that you want to test on: ``python src/test_<browser>.py``
7. Go to the link http://localhost:4444/ui to access the Selenium Grid Server
8. Then click on “Sessions” and then click on the session you want to access. Each session will run each instance of an UI test.
9. Type “secret” as the password for that session (each session will have this as the password regardless)
10. Let the test run. 
11. Once you finish testing, run the docker-compose file again with this command to deactivate the containers: ``docker-compose -f docker-compose.yaml down``

## Local Usage

1. Fork/Clone the Repository linked above
2. In the directory, go to the src folder and find `utilities.py`
3. Inside the `'''INSERT URL HERE'''` comment, replace it with the URL you want to conduct your UI tests in.
4. Inside the try block of the ui_test function, write your UI tests for your URL. 
5. Run this command on one terminal to start the Selenium Grid server (make sure the terminal is in the same directory as the repository): ``java -jar selenium-server-4.8.1.jar standalone``
6. On another terminal, run a Python script based on the browser that you want to test on (once again make sure that this terminal is in the same directory as the repository): ``python src/test_<browser>.py``
 7. The tests will pop out automatically based on the browser of your choice
 8. Once the script has ran, you can terminate the server via `ctrl + c` on the terminal from step 5.