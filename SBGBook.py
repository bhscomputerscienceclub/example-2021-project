from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import re

#pls dont use this

driver = Chrome()
driver.get("https://www.sbgbook.xyz/gbook/login/")
username = '' 
password = '' 
driver.find_element_by_class_name("btn-success").click()
time.sleep(1)
driver.find_element_by_id('id_LogIn-username').send_keys(username)
driver.find_element_by_id('id_LogIn-password').send_keys(password)
driver.find_element_by_id('lgnbtn').click()
url = driver.current_url

# courser = driver.find_element_by_class_name('dropdown-menu')

# course_regex = re.search('student(.*)-(.*)">(.*)<\/a>', courser.get_attribute('innerHTML'), re.IGNORECASE)
# a,b,course = course_regex.groups()
# print(a,b,course)

# grading_period = driver.find_elements_by_class_name('dropdown-menu')[1]
# print(grading_period.get_attribute('innerHTML'))



cookies=driver.get_cookies()
driver.quit()

s = requests.Session()
for c in cookies:
    s.cookies[c['name']]= c['value']

title_search = re.search('student(.*)-(.*)-(.*)\/([0-9]*)', url, re.IGNORECASE)
student_id,useless,collection_id,section_id = title_search.groups()


r  = s.post('https://www.sbgbook.xyz/gbook/studentgradeframe/?section_id=' + section_id +'&student_id='+ student_id + '&scollection_id=' + collection_id)
sbg_grades = r.content.decode()
print(sbg_grades)