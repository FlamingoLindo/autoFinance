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

def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)
    
    soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)
    
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def valida_cpf(cpf):
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]
    
    if len(cpf_numeros) != 11:
        return False
    
    # Validar primeiro dígito
    soma1 = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    if cpf_numeros[9] != digito1:
        return False
    
    # Validar segundo dígito
    soma2 = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    if cpf_numeros[10] != digito2:
        return False
    
    return True

def gera_e_valida_cpf():
    while True:
        cpf = gera_cpf()
        if valida_cpf(cpf):
            return cpf


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

cli_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaWaDaD1')
                                                  )
                       ).click()

user_amount_str = get_user_input("How many users?")
user_amount_int = int(user_amount_str)
num = 1
for _ in range(user_amount_int):
    
    new_cli_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaYaFb'))).click()
    
    cpf_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.baTaHzaD')
        )).send_keys(gera_e_valida_cpf())
    
    name_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.baTaHzaP')
        )).send_keys(f"Name {num}")
    
    email_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.baTaHzz')
        )).send_keys(f"autoemail{num}@gmail.com")
    
    rand_phone = random.randint(11111111111, 99999999999)
    phone_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.baTaIaAaL')
        )).send_keys(rand_phone)
    
    create = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaHvq'))).click()
    
    time.sleep(1.5)
    
    num += 1
        
get_user_input("DONE")

# Close the browser
driver.quit()
     
    
    
    
