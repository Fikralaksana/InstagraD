from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

service = FirefoxService(executable_path=GeckoDriverManager().install())

options = FirefoxOptions()
driver = webdriver.Firefox(service=service,options=options)
driver.set_window_size(1000, 800)

def find_a(driver):
    return driver.execute_script('''
var elements=document.getElementsByTagName('a')
var posts=[]
for (i=0;i<elements.length;i++){
    if (elements[i].href.includes('/p/')){
        posts.push(elements[i])
    }
}
window.scrollTo(0, document.body.scrollHeight)
return posts.length
    ''')
def scroll(driver):
    return driver.execute_script('''
window.scrollTo(0, document.body.scrollHeight)
    ''')


driver.get("http://www.instagram.com")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("fikralaksanaputra")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("F1kr41997!%(#%&")
password = driver.find_element(By.ID, "loginForm").submit()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Not Now']")))
not_now = driver.find_element(By.XPATH,"//*[text()='Not Now']").click()
driver.get("https://www.instagram.com/noerilisnaini/")
old_posts=0
new_posts=1
while new_posts>old_posts:
    print('before',new_posts,old_posts)
    temp=new_posts
    new_posts=find_a(driver)
    time.sleep(5)
    old_posts=temp
    scroll(driver)
    print('after',new_posts,old_posts)

# driver.quit()
  
