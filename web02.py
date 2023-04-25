from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Web():
    def __init__(self) -> None:
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-2022'
        self.map = {
            'sorteio': {
            'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[%num%]'
                        
            },
            'data': {
            'xpath': ''
            },
            'numero': {
            'xpath': '/html/body/main/div[2]/div/div/div[1]/span[%num%]'
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def abrir_site(self):
        sleep(2)
        self.driver.get(self.site)
        sleep(2)
        k = 0
        for i in range(110):
            print()
            print(self.driver.find_element(By.XPATH, self.map['sorteio']['xpath'].replace("%num%", f'{i+4}')).text)

            for j in range(6):
                print(self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace("%num%", f'{k+1}')).text, end="  ")
                k+=1
            print()
               
        sleep(2)