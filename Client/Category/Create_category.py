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

categ_amount_str = get_user_input("How many")
categ_amount_int = int(categ_amount_str)
num = 1
for _ in range(categ_amount_int):
    
    new_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaKip')
                                                  )
                       ).click()
    
    name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaKpaY')
                                                  )
                       ).send_keys(f"Category {num}")
    
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[37]/div/select")
                                                  )
                       ).click()
    
    d = wait.until(EC.presence_of_element_located
                   ((By.CSS_SELECTOR, ".Dropdown")
                    )).click()
    
    random_shit = random.randint(1, 5)
    if random_shit == 1:
        a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='Recebimentos']")
                        )).click()
    elif random_shit == 2:
        a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='Despesas fixas']")
                        )).click()
    elif random_shit == 3:
        a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='Despesas variáveis']")
                        )).click()
    elif random_shit == 4:
        a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='Pessoas']")
                        )).click()
    elif random_shit == 5:
        a = wait.until(EC.presence_of_element_located
                    ((By.XPATH, "//option[text()='Impostos']")
                        )).click()
        
    create = wait.until(EC.presence_of_element_located
                    ((By.CSS_SELECTOR, ".baTaKpaZ")
                        )).click()
    
    time.sleep(0.5)
    
    num += 1
    
    
        
get_user_input("DONE")

# Close the browser
driver.quit()
     
    
    
    
