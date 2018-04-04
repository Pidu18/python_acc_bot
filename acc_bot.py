import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import random
import random


restart = True
def start():
    optiuni = input("\n \n1.Facebook Account\n \n2.Instagram Account\n \n-:")
    if optiuni == "1":
        web = webdriver.Firefox()
        web.get("https://facebook.com/")
       	print("Openned facebook.com")
       	time.sleep(5)
       	print("Sleep time (5s)")
       	x = web.find_element_by_name("firstname")
       	x.send_keys("Pidle")
       	print("Name inserted succesfully")
       	y = web.find_element_by_name("lastname")
       	y.send_keys("Jhon")
       	print("Last Name inserted succesfully")
       	z = web.find_element_by_name("reg_email__")
       	rae = random.randint(1111,9999)
       	z.send_keys("mrpidu" + str(rae) + "jhon@gmail.com")
       	print("Email inserted succesfully")
       	print("Sleep time (5s)")
       	print(rae)
       	time.sleep(5)
       	a = web.find_element_by_name("reg_email_confirmation__")
       	a.send_keys("mrpidu" + str(rae) + "jhon@gmail.com")
       	email = "mrpidu" + str(rae) + "jhon@gmail.com"
       	print(rae)
       	print("Email inserted succesfully")
       	b =  web.find_element_by_name("reg_passwd__")
       	b.send_keys("Piduaswor123")
       	password = "Piduaswor123"
       	c = web.find_element_by_id("year")
       	c.click()
       	d = web.find_element_by_name("sex")
       	d.click()
       	d.send_keys(Keys.ENTER)
       	print("Submited")
       	print("Email: " + email + "\n" + "Password: " + password)
       	time.sleep(10)
       	web.quit()
    
        pass
    elif optiuni == "2":
        web = webdriver.Firefox()
       	web.get("https://www.instagram.com/?hl=en")
       	print("Openned instagram.com")
       	print("Sleep time (5s)")
       	time.sleep(5)
       	x = web.find_element_by_name("emailOrPhone")
       	rae = random.randint(1111, 9999)
       	x.send_keys("mrpidu" + str(rae) + "jhon@gmail.com")
       	email = "mrpidu" + str(rae) + "jhon@gmail.com"
       	print(rae)
       	print("Email inserted succesfully")
       	y = web.find_element_by_name("fullName")
       	y.send_keys("Pidu Jhonson")
       	print("Full name inserted succesfully")
       	z = web.find_element_by_name("username")
       	ra = random.randint(11111, 99999)
       	z.send_keys("mrpidu" + str(ra))
       	print("Username inserted succesfully")
       	print("Sleep time (5s)")
       	time.sleep(5)
       	a = web.find_element_by_name("password")
       	a.send_keys("Piduaswor123")
       	password = "Piduaswor123"
       	a.send_keys(Keys.ENTER)
       	print("Submited")
       	print("Email: " + email + "\n" + "Password: " + password)
       	time.sleep(10)
       	web.quit()
  

while restart :
    start()