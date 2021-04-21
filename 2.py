from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
driver = webdriver.Firefox()
driver.get(url)

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),"南昌")   
)

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element_value((By.ID,"toStationText"),"南京")   
)

btn_area = driver.find_element_by_id("query_ticket")
btn_area.click()
