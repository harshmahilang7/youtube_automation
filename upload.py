# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date: 23-03-2024 06:29:41 PM 18:29:41
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 25-03-2024 01:31:05 AM       01:31:05
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
    
def vido_upload(t):
    title = t
    # Path to the video you want to upload
    video_path = "C:\\Users\\harsh\\OneDrive\\Desktop\\youtube_automation\\DONE.mp4"
    
    # URL for YouTube Studio
    youtube_studio_url = "https://studio.youtube.com"
    
    # Your YouTube login credentials
    # email = "harshmahilang9@gmail.com"
    # password = "1gq2Pe62bob4F42g"
    
    email = "d80976269@gmail.com"
    password = "title_input.clear()"
    
    # Configure Firefox browser options
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--log-level=3")  # suppress logging
    
    # Initialize Firefox WebDriver
    driver = webdriver.Firefox(options=firefox_options)
    
    # Open YouTube Studio
    driver.get(youtube_studio_url)
    time.sleep(3)
    
    # Fill in email and click "Next"
    email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # Fill in password and click "Next"
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)
    
    # Check if there is a "Continue" button
    try:
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue-button"]')
        continue_button.click()
        time.sleep(3)
    except NoSuchElementException:
        pass  # If there is no "Continue" button, continue with the next steps
    
    # Wait for the "Upload video" button to be clickable
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="upload-icon"]')))
    upload_button.click()
    time.sleep(3)
    
    # Select the video file to upload
    file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    file_input.send_keys(video_path)
    time.sleep(7)
    
    # Add video details (if required)
    # For example:
    title_input = driver.find_element(By.XPATH, '//*[@id="textbox"]')
    title_input.clear()
    title_input.send_keys(title)
    time.sleep(2)
    
    # Find and click on the checkbox "No, it's not made for kids"
    try:
        checkboxes = driver.find_elements(By.XPATH, '//*[contains(text(), "No, it\'s not made for kids")]')
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(2)
    except NoSuchElementException:
        print("Checkbox for 'No, it's not made for kids' not found.")
    time.sleep(4)
    
    # Click on the "Next" button
    next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
    next_button.click()
    time.sleep(3)
    
    # Click on the "Next" button
    next_button2 = driver.find_element(By.XPATH, '//*[@id="next-button"]')
    next_button2.click()
    time.sleep(3)
    
    # Click on the "Next" button
    next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
    next_button.click()
    time.sleep(3)
        
    # Choose video visibility: Public
    try:
        # Find the third radio label (assuming "Public" is the third option)
        visibility_public = driver.find_elements(By.XPATH, '//*[@id="radioLabel"]')[2]
        
        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", visibility_public)
        time.sleep(1)  # Add a small delay to ensure the element is fully scrolled into view
        
        # Click on the "Public" visibility option
        visibility_public.click()
        time.sleep(2)
        
    except (NoSuchElementException, IndexError):
        print("Public visibility option not found")
        
        # Set as instant Premiere
    premiere_checkbox = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/div[2]/ytcp-checkbox-lit/div/div[2]')
    premiere_checkbox.click()
    time.sleep(2)
    
    # Save or publish
    save_button = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div')
    save_button.click()
    time.sleep(5)
    
    # save_button = driver.find_element(By.XPATH, '/html/body/ytcp-video-share-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button/div')
    # save_button.click()
    # time.sleep(5)
    
    # Close the browser
    driver.quit()
    
    
# vido_upload("hero")
