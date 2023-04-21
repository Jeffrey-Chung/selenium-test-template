'''
This script will be ran on Github Actions. It will run the tests on Firefox, Chrome and Edge respectively.
In theory, you don't need to change anything on this script except adding your link to the driver.
'''
from selenium import webdriver
from selenium_local import ui_test

# define ze options
firefox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

#chrome_options.add_argument("--disable-dev-shm-usage")

#function to set the same options for each browser
def set_options(driver_options):
        #Uncomment the line below if you want to run your tests on headless
        #driver_options.add_argument("--headless")
        driver_options.add_argument("--ignore-certificate-errors")
        driver_options.add_argument("--kiosk")

set_options(firefox_options)
set_options(chrome_options)
set_options(edge_options)

#Function to configure settings for each driver
def setup_driver(driver_options):
        driver = webdriver.Remote( 
        command_executor="http://localhost:4444",
        options=driver_options
        )

        #Make sure you paste your URL in the line below
        driver.get('''INSERT URL HERE''')
        return driver

firefox_driver = setup_driver(firefox_options)
chrome_driver = setup_driver(chrome_options)
edge_driver = setup_driver(edge_options)


if __name__ == "__main__":
        ui_test(firefox_driver)
        ui_test(chrome_driver)
        ui_test(edge_driver)
