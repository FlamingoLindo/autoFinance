import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('URL'))

wait = WebDriverWait(driver, 5)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/button[1]')
                                                  )
                       ).click()

email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/input')
                                                    )
                         ).send_keys(os.getenv("PERSONAL_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]')
                                                       )
                            ).send_keys(os.getenv("PERSONAL_PASSWORD"))

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/button')
                                                  )
                       ).click()

options1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaWaDaN1')
                                                  )
                       ).click()

options2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaHaPm')
                                                  )
                       ).click()

categ_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaKaXv')
                                                  )
                       ).click()

time.sleep(1.4)

users_amount = driver.find_elements(By.CSS_SELECTOR, '.baTaKiu')
quantity = len(users_amount)

for _ in range(quantity):
    delete1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaKjaA')
                                                  )
                       ).click()
    
    delete2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaYaHx')
                                                  )
                       ).click()
    
    delete3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaOaFt')
                                                  )
                       ).click()
    
    close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.iziToast-message')
                                                  )
                       ).click()
    
     
get_user_input("DONE")

# Close the browser
driver.quit()
     
    
    
    
