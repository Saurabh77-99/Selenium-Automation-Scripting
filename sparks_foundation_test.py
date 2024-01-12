from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import  TimeoutException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wd = driver
print(wd.current_url)
driver.get("https://www.thesparksfoundationsingapore.org/")
print("\nTest Cases:")

# TestCase 1: Title
print("\nTestCase 1:")
if driver.title:
    print("\nTitle Verified Successfully: ", wd.title)
else:
    print("\nTitle Verification Failed!\n")

# TestCase 2: To find logo of the webpage
print("\nTestCase 2:")
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Success! The logo is present\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo is present!\n')

# TestCase 3: Check if navbar appears
print("\nTestCase 3:")
try:
    navbar_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "navbar"))
    )
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")


# TestCase 4: Home button
print("TestCase 4:")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
    print("Home link is working!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")
    
print("TestCase 4:")
try:
    home_link = driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation")
    home_link.click()
    print("Home link is clicked!\n")
    # Wait for a condition after the click
    time.sleep(5)
    print("Delay after click!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 5: About Us Pages
print("TestCase 5:")
try:
    driver.find_element(By.LINK_TEXT, 'About Us').click()
    print("'About Us' link is clicked!\n")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Corporate Partners').click()
    print("Corporate Partners link is clicked!\n")
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("'About Us' Link Doesn't Work!\n")

# TestCase 6: Policy page
print('TestCase 6:')
try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    print("Policies and code link is clicked!\n")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Policies").click()
    print("Policies link is clicked!\n")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Code of Ethics and Conduct').click()
    print("Code of Ethics and Conduct link is clicked!\n")
    time.sleep(3)
    print('Policy Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Programs page
print('TestCase 7:')
try:
    driver.find_element(By.LINK_TEXT,'Student Scholarship Program').click()
    print('Student Scholarship Program clicked!\n')
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Student Mentorship Program").click()
    print('Student Mentorship Program clicked!\n')
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Student SOS Program').click()
    print('Student SOS Program Clicked!\n')
    time.sleep(3)
    print('Programs Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 8: Check the Contact us Page
print("TestCase 8:")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(3)
    info = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Incorrect!')
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")

# TestCase 9: Links Page
print("TestCase 9:")
try:
    driver.find_element(By.LINK_TEXT,'LINKS').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Software & App').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'AI in Education').click()
    time.sleep(3)
    print('LINKS Verfication Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

print("TestCase 10:")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    driver.find_element(By.NAME,'Name').send_keys('Saurabh Davda')
    time.sleep(3)
    driver.find_element(By.NAME,'Email').send_keys('saurabhmelophile@gmail.com')
    time.sleep(3)

    dropdown_element = driver.find_element(By.CLASS_NAME, 'form-control')
    select = Select(dropdown_element)
    time.sleep(2)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)
finally:
    driver.quit()