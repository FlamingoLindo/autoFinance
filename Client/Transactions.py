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
import pyautogui
import sys
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

transaction_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.baTaWaCq1')
                                                  )
                       ).click()


def new_transac():
    num = 1
    transac_amount_str = get_user_input("How many?")
    transac_amount_int = int(transac_amount_str)
    for _ in range(transac_amount_int):
        
        desc = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.baTaIpaO')))
        
        desc.click()
        desc.send_keys(f"Description {num}")
        
        rand_phone = random.randint(11111111111, 99999999999)
        phone = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cont"]'))
                            ).send_keys(rand_phone)
        
        cost_center_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="receb"]/div[1]/div/div[5]/select[1]'))
                            ).click()
        
        find1 = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, ".Dropdown:nth-child(4)")
                            )
                           ).click()

        find2 = wait.until(EC.presence_of_element_located
                        ((By.XPATH, "//option[text()='a']")
                        )
                        ).click()
            
        recived_from_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="receb"]/div[1]/div/div[5]/div[2]/div'))
                            ).click()
        time.sleep(1)
        recived_from_dropdown2 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[2]/select'))
                            )
        recived_from_dropdown2.click()
        recived_from_dropdown2.click()
        
        recived_from_dropdown2.send_keys("a")
        
        categ_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="receb"]/div[1]/div/div[5]/div[3]/div'))
                            ).click()
        time.sleep(1)
        categ_dropdown2 = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.baTaYcaN > .Dropdown'))
                            )
        categ_dropdown2.click()
        categ_dropdown2.click()
        
        categ_dropdown2.send_keys("a")
        
        rand_value = random.randint(1, 99999999)
        value = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="receb"]/div[1]/div/div[5]/input[3]'))
                            ).send_keys(rand_value)
        
        a = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='receb']/div/div/div[5]/select[2]")
        )
                             ).click()
        
        b = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='receb']/div/div/div[5]/select[2]")
        )
                             ).click()
        
        rand_shit = random.randint(1, 3)
        if rand_shit == 2:
            # Installments
            c = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".Dropdown:nth-child(8)")
            )
                                ).click()
            
            d = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, ".Dropdown:nth-child(8)")
                            )
                           ).click()

            e = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//option[text()='Parcelado']")
                            )
                           ).click()
            
            f = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, ".baTaSaDf")
                            )
                           )
            f.click()
            rand_install = random.randint(1, 12)
            f.send_keys(rand_install)
            
            payed_btn = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//div[@id='receb']/div/div/div[5]/div[6]/input")
                            )
                           ).click()

            confirm_btn = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, '.baTaIpaT')
                                )
                            ).click()
            
            time.sleep(rand_install + 9)
            
        elif rand_shit == 1:
            # IN cash
            payed_btn = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//div[@id='receb']/div/div/div[5]/div[6]/input")
                            )
                           ).click()

            confirm_btn = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, '.baTaIpaT')
                                )
                            ).click()
            time.sleep(0.5)
        
        else:
            # Recurrent
            c = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".Dropdown:nth-child(8)")
            )
                                ).click()
            
            d = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, ".Dropdown:nth-child(8)")
                            )
                           ).click()
            
            e = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//option[text()='Recorrente']")
                            )
                           ).click()
            
            f = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, ".baTaSaDf")
                            )
                           )
            f.click()
            rand_install = random.randint(1, 12)
            f.send_keys(rand_install)
            
            payed_btn = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//div[@id='receb']/div/div/div[5]/div[6]/input")
                            )
                           ).click()

            confirm_btn = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, '.baTaIpaT')
                                )
                            ).click()
            
            time.sleep(rand_install +9)
        num +=1     
        

        
                
        
        
        

rand_transac_type = 2 #random.randint(1, 5)
if rand_transac_type == 1:
    new_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="receb"]/div[1]/div/div[4]/div'))
                            ).click()
    new_transac()

elif rand_transac_type == 2:
    # Expenses
    expenses = wait.until(EC.presence_of_element_located
                            ((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[2]')
                                )
                            ).click()
    
    new_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div'))
                            ).click()
    
    new_transac()


# Close the browser
driver.quit()
