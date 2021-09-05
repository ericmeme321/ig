from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

path = f"C:\\temp\chromedriver.exe"

class ig():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path=path)
        self.username = username
        self.password = password

    def login(self):

        url = f'https://www.instagram.com/'
        self.driver.get(url)


        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')

        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        login.click()
        time.sleep(3)


    # def search(self, keyword):

    #     self.driver.get(f'https://www.instagram.com/')
    #     search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    #     )
    #     search.send_keys(keyword)
    #     time.sleep(1)
    #     search.send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     search.send_keys(Keys.RETURN)

    def follow(self, keyword):

        self.driver.get(f'https://www.instagram.com/{keyword}')

        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))
        ) 
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        print(followers.text)
        followers.click()

        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]'))
        )  
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)
            time.sleep(1)

        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li button"))
        )
        followers_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in followers_buttons:
            button.click()
            time.sleep(1)


    def downloadimg(self, keyword):

        self.driver.get(f'https://www.instagram.com/{keyword}')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span'))
        )

        imgnums = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span')
        t = int(imgnums.text) // 40
        for _ in range(t+1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
        )
        imgs = self.driver.find_elements_by_class_name("FFVAD")

        path = os.path.join(keyword)
        os.mkdir(path)

        count = 0
        for img in imgs:
            save_as = os.path.join(path, keyword + '_' +str(count) + '.jpg')
            wget.download(img.get_attribute("src"), save_as)
            count += 1
        
        print(count)



if __name__ == '__main__':
    username = 'justtest0812'
    password = 'allenisme123'
    keyword = 'pyy_3'
    
    # username = input("input username:")
    # password = input("input password:")
    # keyword = input("input searchusername:")

    allen = ig(username, password)
    allen.login()
    # allen.follow(keyword)
    # allen.downloadimg(keyword)