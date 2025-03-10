#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 8 17:30:59 2025
@author: madisonskinner
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Blackboard login credentials (replace with actual login details)
USERNAME = ""
PASSWORD = ""
# Set up Selenium WebDriver
driver = webdriver.Chrome() # Ensure you have the correct ChromeDriver
driver.get("https://blackboard.ncat.edu/ultra/course")
# Wait for page to load
time.sleep(3)
# Find and fill in the username and password fields
driver.find_element(By.ID, "user_id").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "entry-login").click()
# Wait for login to complete

body = driver.find_element(By.XPATH, "//*[@id='main-content-inner']")
body.send_keys(Keys.PAGE_DOWN)  # Scrolls down one page
body.send_keys(Keys.END)  # Scrolls to the bottom

time.sleep(15)
# Wait for instructors section to appear
try:
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "instructors"))
)
except:
    print("Instructor section not found.")
    driver.quit()
    exit()
# Scrape instructor names
instructors = []
course_elements = driver.find_elements(By.CLASS_NAME, "instructors")

for course in course_elements:
    try:
        professor_name = course.text
        if professor_name == 'Multiple Instructors':
            pass
        instructors.append(professor_name)
    except:
        print("Error extracting instructor name.")
        continue # Skip if no professor name found

# Save to a file
print("Extracted Instructors:", instructors)

# Save to a file
with open("professors.txt", "w", encoding="utf-8") as f:  # Added encoding for safety
    for instructor in instructors:
        if instructor:  # Ensure it's not None
            f.write(str(instructor) + "\n")
  # Correct newline
print("Extraction complete! Check professors.txt")

driver.quit()