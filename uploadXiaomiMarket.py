import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import threading
from selenium.webdriver.common.keys import Keys  

def uploadXiaomi():
	name="你的小米应用市场账号"
	pwd="你的密码"
	apkPath="你的本地apk完整路径"
	changeLog="你的更新日志"
	versionCode="你的最新版本号"
	# chromedriver完整路径
	driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
	# 管理台登录
	driver.get("https://dev.mi.com/console/")
	time.sleep(1)
	driver.find_element_by_link_text("登录").click()
	time.sleep(1)
	driver.find_element_by_id("username").send_keys(name)
	driver.find_element_by_id("pwd").send_keys(pwd)
	time.sleep(1)
	driver.find_element_by_id("login-button").click()
	time.sleep(1)
	driver.find_element_by_link_text("管理控制台").click()
	time.sleep(1)
	driver.find_element_by_link_text("应用和游戏").click()
	time.sleep(1)
	# 你要上传的应用在第几个，小标0开始
	driver.find_elements_by_link_text("管理")[1].click()
	time.sleep(1)
	driver.find_elements_by_tag_name("button")[1].click()
	time.sleep(1)
	# 开始上传apk
	driver.find_elements_by_tag_name("input")[0].send_keys(apkPath)
	time.sleep(5)
	# 检测上传是否完成
	while 1:
		try:
			driver.find_element_by_class_name("ant-progress-inner")
			time.sleep(5)
		except:
			break;
	element = driver.find_element_by_id("AppBasicInfo_changeLog")
	element.clear()
	time.sleep(1)
	element.send_keys(changeLog)
	version = driver.find_element_by_id("AppBasicInfo_versionName")
	version.clear()
	time.sleep(1)
	version.send_keys(versionCode)
	# 发布时间选择审核通过后立即上线
	div = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[4]/div[2]/form/div[5]/div/div[2]")
	js4 = "arguments[0].scrollIntoView();" 
	driver.execute_script(js4, div)  
	time.sleep(2)
	div.click()
	time.sleep(2)
	driver.find_element_by_xpath("//li[contains(text(),'审核通过后立即上线')]").click()
	time.sleep(2)
	# 提交发布
	publish = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[8]/div[2]/div/div/button[2]")
	driver.execute_script(js4, publish)
	time.sleep(2)
	publish.click()
	time.sleep(10)
	driver.quit()


if __name__ == '__main__':
	threads=[
		threading.Thread(target=uploadXiaomi)
	]
	for t in threads:
		t.start()
