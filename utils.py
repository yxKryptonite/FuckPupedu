import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import eventlet
eventlet.monkey_patch()

LOGIN_URL      = "http://www.pupedu.cn/app/login/login.do"
IMMED_INTERVAL = 0.1
SHORT_INTERVAL = 1
MID_INTERVAL   = 5
HALF_MINUTE    = 30
LONG_INTERVAL  = 1200
ONE_MINUTE     = 60

class FuckPupedu(object):
    def __init__(self, cfg):
        self.cfg = cfg
        mobile_emulation = {"deviceName": "iPhone 6"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument('-mute-audio')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.actions = ActionChains(self.driver)

        
    def login(self):
        self.driver.get(LOGIN_URL)
        self.driver.find_element(By.XPATH, "//*[@id=\"login\"]/div[2]/div[4]/span[2]").click()
        self.driver.implicitly_wait(MID_INTERVAL)
        self.driver.find_element(By.ID, "user_name").send_keys(self.cfg['ID'])
        self.driver.find_element(By.ID, "password").send_keys(self.cfg['PASSWORD'])
        self.driver.find_element(By.ID, "logon_button").click()
        self.driver.implicitly_wait(MID_INTERVAL)
        print("登录成功")
        
        
    def search(self):
        '''在最初始界面上搜寻章节和标题'''
        container = self.driver.find_element(By.ID, "step2")
        chapters = container.find_elements(By.CLASS_NAME, "chapters")
        courses = []
        for chapter in chapters:
            self.driver.execute_script("arguments[0].scrollIntoView();", chapter)
            self.driver.implicitly_wait(LONG_INTERVAL)
            chapter.click()
            self.driver.implicitly_wait(LONG_INTERVAL)
            titles = chapter.find_elements(By.CLASS_NAME, "titleName")
            courses.append(titles[2:-1]) # 去掉前两个和最后一个
            
        return courses # len(courses) 为 chapter 数，courses[i] 为第 i 个 chapter 的所有 title 的 list
    
    
    def get_idx(self, count, courses):
        '''返回当前应该学习的章节和标题的索引'''
        chapter_idx = 0
        title_idx = 0
        for chapter in courses:
            if count < len(chapter):
                title_idx = count
                break
            else:
                chapter_idx += 1
                count -= len(chapter)
                
        return chapter_idx, title_idx
    
    
    def learn(self):
        # 当前页面：用户课程列表，下面点击劳动教育课程
        self.driver.find_element(By.XPATH, "//*[@id=\"my_list\"]/div/div/div/div/div[2]/div[2]/div[1]/div").click()
        self.driver.implicitly_wait(LONG_INTERVAL)
        current_url = self.driver.current_url
        courses = self.search() # [[title1, title2, ...], [title1, title2, ...], ...]
        total_num = sum([len(chapter) for chapter in courses])
        
        count = 0
        for i in range(self.cfg['START_CHAPTER'] - 1):
            count += len(courses[i])
        count += self.cfg['START_TITLE'] - 1   
            
        while count < total_num:
            chapter_idx, title_idx = self.get_idx(count, courses)
            print("开始学习第 {} 讲的第 {} 个视频".format(chapter_idx + 1, title_idx + 1))
            self.play_video(courses[chapter_idx][title_idx])
            count += 1
            print("学习完毕，正在加载下一个视频")
            
            self.driver.get(current_url)
            self.driver.implicitly_wait(LONG_INTERVAL)
            time.sleep(MID_INTERVAL)
            courses = self.search()
            while sum(len(chapter) for chapter in courses) < total_num:
                self.driver.refresh()
                time.sleep(MID_INTERVAL)
                courses = self.search()
                
        
    def play_video(self, title):
        '''播放视频'''
        self.driver.execute_script("arguments[0].scrollIntoView();", title)
        title.click()
        self.driver.implicitly_wait(LONG_INTERVAL)
        btn = self.driver.find_element(By.CLASS_NAME, "outter")
        btn.click()
        start_time = time.time()
        
        time.sleep(MID_INTERVAL) # wait for the duration to be loaded
        duration_div = self.driver.find_element(By.CLASS_NAME, "duration").text # e.g 19:25
        duration_div = duration_div.split(":")
        duration = int(duration_div[0]) * ONE_MINUTE + int(duration_div[1])
        
        for sec in tqdm(range(duration + HALF_MINUTE - MID_INTERVAL)):
            time.sleep(SHORT_INTERVAL)
            curr_time = time.time()
            if curr_time - start_time > duration + HALF_MINUTE:
                break
            
            if sec % ONE_MINUTE == ONE_MINUTE - 1:
                # 每分钟检查一下有无弹窗（如果一直检查会严重阻塞）、并且刷新一次页面（使 driver 取得“控制权”）
                self.driver.refresh()
                self.driver.implicitly_wait(MID_INTERVAL)
                self.driver.find_element(By.CLASS_NAME, "outter").click()
                try:
                    with eventlet.Timeout(IMMED_INTERVAL, False):
                        cont_btn = self.driver.find_element(By.CLASS_NAME, "el-button")
                        cont_btn.click()
                except:
                    pass
                    