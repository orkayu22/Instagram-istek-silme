from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput =self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def getFollowers(self):
        url= 'https://www.instagram.com/accounts/access_tool/current_follow_requests?hl=tr'
        self.browser.get(url)
        try:
            while True:
                daha_fazlasini_gor = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button').click()
                time.sleep(2)

                isimlistesi= self.browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/main/section')

                linkler = []
                
                for isim in isimlistesi:
                    link =  isim.text
                    print(link)
                    linkler.append(link)
                
                with open ("istek_silme.txt", "w", encoding="UTF-8")as file:
                    for user in linkler:
                        file.write(user)                

        except (NoSuchElementException, StaleElementReferenceException):
            print("LİSTE SONLANDI!")
            self.browser.quit()
       
    def tektek(self):
        
        listkullanici = open("istek_silme.txt").read().splitlines()
        for item in listkullanici:
            print(f'{item} adlı kişiye gönderilen istek siliniyor...')
            self.browser.get('https://www.instagram.com/' + item)          
            time.sleep(0.5)
            istegi_sil = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            istegi_sil_dogrulama = self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            time.sleep(0.2)

instagrm = Instagram(username, password)
instagrm.signIn()
instagrm.getFollowers()
# instagrm.tektek()