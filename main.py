import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Load data from CSV file
data = pd.read_csv('C:/Users/rahim/Downloads/Sample Dataset.csv')

# Configure the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open the web app
driver.get("https://staging-scweb.arcapps.org/")
time.sleep(5)  # Allow time for the page to load

# Log in
driver.find_element_by_name("username").send_keys("tester")
driver.find_element_by_name("password").send_keys("tester2023!")
driver.find_element_by_name("province").send_keys("Lusaka")
driver.find_element_by_name("district").send_keys("Lusaka")
driver.find_element_by_name("login").click()
time.sleep(3)  # Allow time for the login to complete

# Navigate to the form page
driver.find_element_by_link_text("Add Vital").click()
time.sleep(3)  # Allow time for the page to load

# Fill out the form with data from the CSV file
for index, row in data.iterrows():
    driver.find_element_by_name("date").send_keys(row['Date'])
    driver.find_element_by_name("time").send_keys(row['Time'])
    driver.find_element_by_name("weight").send_keys(row['Weight'])
    driver.find_element_by_name("length").send_keys(row['Length'])
    driver.find_element_by_name("temperature").send_keys(row['Temperature'])
    driver.find_element_by_name("systolic").send_keys(row['Systolic'])
    driver.find_element_by_name("diastolic").send_keys(row['Diastolic'])
    driver.find_element_by_name("pulseRate").send_keys(row['PulseRate'])
    driver.find_element_by_name("respiratoryRate").send_keys(row['RespiratoryRate'])
    driver.find_element_by_name("oxygenSaturation").send_keys(row['OxygenSaturation'])
    driver.find_element_by_name("muac").send_keys(row['MUAC'])
    driver.find_element_by_name("headCircumference").send_keys(row['HeadCircumference'])
    driver.find_element_by_name("abdominalCircumference").send_keys(row['AbdominalCircumference'])
    driver.find_element_by_name("bpUnrecordable").send_keys(row['BPUnrecordable'])
    driver.find_element_by_name("note").send_keys(row['Note'])

    # Submit the form
    driver.find_element_by_name("save").click()
    time.sleep(5)

driver.quit()
