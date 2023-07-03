'''
This script stores all the common functions between the 3 test files. Including setup the drivers and the tests itself
In theory, you don't need to change anything on this script except adding your link to the driver.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to set the same options for each browser
def set_options(driver_options):
        # Uncomment the line below if you want to run your tests on headless
        #driver_options.add_argument("--headless")
        driver_options.add_argument("--ignore-certificate-errors")
        driver_options.add_argument("--kiosk")


# Function to configure settings for each driver
def setup_driver(driver_options):
        driver = webdriver.Remote( 
        command_executor="http://localhost:4444",
        options=driver_options
        )

        # Make sure you paste your URL in the line below
        driver.get('''INSERT URL HERE''')
        return driver

# Function to run the UI tests
def ui_test(driver):
        try:
                print("Tests will be ran")
                # Write all your tests in the line below, make sure your code is indented correctly.







                # But above this line :)
        finally:
                #prints the url that was last loaded
                print(driver.current_url)
                driver.quit()


