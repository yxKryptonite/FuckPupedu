import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time

LOGIN_URL = "http://www.pupedu.cn/app/login/login.do"
SHORT_INTERVAL = 1
MID_INTERVAL   = 5
LONG_INTERVAL  = 120
ONE_MINUTE     = 60

class FuckPupedu(object):
    def __init__(self, cfg):
        self.id = cfg['ID']
        self.password = cfg['PASSWORD']
        mobile_emulation = {"deviceName": "iPhone 6"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(options=options)

        
    def login(self):
        self.driver.get(LOGIN_URL)
        self.driver.find_element(By.XPATH, "//*[@id=\"login\"]/div[2]/div[4]/span[2]").click()
        self.driver.implicitly_wait(MID_INTERVAL)
        self.driver.find_element(By.ID, "user_name").send_keys(self.id)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "logon_button").click()
        self.driver.implicitly_wait(MID_INTERVAL)
    
    def learn(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"my_list\"]/div/div/div/div/div[2]/div[2]/div[1]/div").click()
        self.driver.implicitly_wait(LONG_INTERVAL)
        container = self.driver.find_element(By.ID, "step2")
        chapters = container.find_elements(By.CLASS_NAME, "chapters")
        for chapter in chapters:
            chapter.click()
            self.driver.implicitly_wait(SHORT_INTERVAL)
            titles = chapter.find_elements(By.CLASS_NAME, "titleName")
            for idx, title in enumerate(titles):
                if idx < 2 or idx == len(titles) - 1: # 不包括PPT和测试
                    # print("PPT自己随便翻翻就行了")
                    continue
                else:
                    self.learn_video(title)
        
    def learn_video(self, title):
        print("next one")
        title.click()
        self.driver.implicitly_wait(LONG_INTERVAL)
        btn = self.driver.find_element(By.CLASS_NAME, "outter")
        btn.click()
        self.watch()
        
        
    def watch(self):
        time.sleep(MID_INTERVAL)
        duration_div = self.driver.find_element(By.CLASS_NAME, "duration").text # e.g 19:15
        duration_div = duration_div.split(":")
        duration = int(duration_div[0]) * ONE_MINUTE + int(duration_div[1])
        # print(duration)
        start_time = time.time()
        while True:
            curr_time = time.time()
            if curr_time - start_time > duration + ONE_MINUTE:
                break
            try:
                cont_btn = self.driver.find_element(By.CLASS_NAME, "el-button")
                cont_btn.click()
            except:
                pass
                    
                
            
        