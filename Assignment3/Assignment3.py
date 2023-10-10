# Importing required libraries
from threading import Thread



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(5)

# Navigating to the puma.ca homepage
driver.get("https://ca.puma.com/ca/en")
time.sleep(3)

# Clicking on search bar
search = driver.find_element("xpath",
                                  "/html/body/div[1]/div[1]/div[1]/nav/div/div/button[1]/div[2]/div")
search.click()
time.sleep(3)

# Searching for product in search bar
search_bar = driver.find_element("id", "react-aria-7")
search_bar.send_keys("Shoes")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Shoes" in driver.title
time.sleep(5)

#Select the product
product_link = driver.find_element("xpath",
                                  "/html/body/div[2]/div[1]/main/div/section/section/ul/li[13]/a/div/div[1]/div/div[1]/img")
product_link.click()
time.sleep(3)

#Select the product size
select_size = driver.find_element("xpath",
                                  "/html/body/div[2]/div[1]/main/div/section/div[1]/section[1]/div/div[5]/div[2]/div[1]/label[9]/span/span[2]")
time.sleep(3)

#Add the product to wishlist
add_to_wishlist = driver.find_element("xpath",
                                  "/html/body/div[2]/div[1]/main/div/section/div[1]/section[1]/div/div[7]/div[2]/button[2]/div[2]/div")
add_to_wishlist.click()
time.sleep(3)


# Closing the webdriver
driver.close()