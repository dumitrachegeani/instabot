import random
import time

import pytesseract as pytesseract
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver
# open the driver
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument("profile-directory=Profile 1")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Navigate to Instagram login page
# driver.get('https://www.instagram.com/accounts/login/')

# Enter login credentials and click the login button
time.sleep(10)
# button = driver.find_element(By.XPATH, "//button[text()='Allow essential and optional cookies']").click()
# username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
# password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
# username.send_keys('geanigdumitrache')
# password.send_keys('Mazal.com2001!')
# login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
# login_button.click()

# Wait for the user to enter their OTP or complete two-factor authentication
# time.sleep(10)

# Navigate to messages page and select conversation with first person
driver.get('https://www.instagram.com/direct/inbox/')
driver.maximize_window()

# Click on the first conversation
pyautogui.moveTo(x=52, y=318)
pyautogui.click(x=52, y=318)

# Loop to check for new messages and generate responses
while True:
    # Move the mouse to the last received message (if any)
    latest_message = pyautogui.screenshot(region=(821, 824, 963, 863))
    # Convert the image to grayscale
    latest_message = latest_message.convert('L')

    # Perform OCR on the image and extract the text
    message_text = pytesseract.image_to_string(latest_message)
    print(message_text)

    # Send the message to the ChatGPT API to generate a response
    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                             json={
                                 'moodel': 'gpt-3.5-turbo',
                                 'prompt': latest_message,
                             },
                             headers={
                                 'Content-Type': 'application/json',
                                 'Authorization': 'Bearer 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'
                             })
    response_text = response.json()['choices'][0]['text']

    # Send the generated response to the user
    pyautogui.click(x=500, y=1000)  # click on the message input box
    pyautogui.write(response_text)  # write the response
    pyautogui.press('enter')  # press the enter key

    # Wait for a random amount of time before checking for new messages again
    time.sleep(random.randint(3, 10) * 60)
