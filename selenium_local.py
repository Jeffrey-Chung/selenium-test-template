'''
Write all your tests in this script and they will be imported to selenium_action.py. 
This script will only be ran  on your local machine and not run on GitHub Actions
Make sure you have Firefox on your machine.
Feel free to change any settings here
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



firefox_options = webdriver.FirefoxOptions()


#Headless option for github action
#firefox_options.add_argument("--headless")

firefox_options.add_argument("--kiosk")


#Configure the driver
firefox_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=firefox_options
)

#Make sure you paste your URL in the line below
firefox_driver.get('''INSERT URL HERE''') 


# Run deez tests!
def ui_test(driver):
        try:
                print("Tests will be ran")
                #Write all your tests in the line below, make sure your code is indented correctly.







                #But above this line :)
        finally:
                #prints the url that was last loaded
                print(driver.current_url)
                #Quits the browser, hence finishing the session
                driver.quit()

if __name__ == "__main__":
        ui_test(firefox_driver)

