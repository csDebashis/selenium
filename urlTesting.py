from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support import expected_conditions as EC

import time



chrome_options = Options()  
chrome_options.add_argument("--headless")  
#chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`    

#driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),   chrome_options=chrome_options)  
driver = webdriver.Chrome(chrome_options=chrome_options)

 
#driver = webdriver.Chrome()
driver.get("https://google.com")

#checking if it is error page or not
try:
	element = driver.find_element_by_id("main-frame-error")
	print("This site can’t be reached")
except NoSuchElementException:
	print("Able to open the website")
except:
	print("some other exception")	

	
	
#filling the form
try:
	inputbox = driver.find_element_by_id("lst-ib")
	inputbox.clear()  
	inputbox.send_keys("some text")
	print("keys passed to input box")
	
	btn = driver.find_element_by_name('btnK')
	btn.click()
	print("clicked on search button")
	try:
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.Class, "LC20lb")))
	except:
		print("don't know")
	results = driver.find_elements_by_class_name("LC20lb")
	for elem in results:
		print(elem.text)
	
	
except NoSuchElementException:
	print ("Unable to find element")
	
finally:
	driver.quit()
	

	