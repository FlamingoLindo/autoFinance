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

team_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaKaXj')
                                                  )
                       ).click()

team_amount_str = get_user_input("How many")
team_amount_int = int(team_amount_str)
num = 1
for _ in range(team_amount_int):
    
    time.sleep(1.2)
    
    new = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVfs0'))).click()
    
    first_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVhk0')
                                                  )
                       ).send_keys(f"Name {num}")
    
    sur_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVhp0')
                                                  )
                       ).send_keys(f"Surname {num}")
    
    email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVhr0')
                                                  )
                       ).send_keys(f"email{num}@gmail.com")
    
    password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVhv0')
                                                  )
                       ).send_keys(f"12345678")
    
    cost_center = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.select2-MultiDropdown')
                                                  )
                       ).click()
    
    a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='abc']")
                        )).click()
    
    done = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaVhx0')
                                                  )
                       ).click()
    
    time.sleep(1.2)
    
    close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.iziToast-body')
                                                  )
                       ).click()
    
    num += 1
    
    
    
get_user_input("DONE")

# Close the browser
driver.quit()
     
    
    
    
