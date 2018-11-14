import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):
	def equal(self, v1, v2):
		self.assertEqual(v1, v2)
        
test = Test()

driver = webdriver.Firefox()
driver.get("http://localhost:5005/")
time.sleep(2)

e1 = driver.find_element_by_id("t1")
e2 = driver.find_element_by_id("t2")
b1 = driver.find_element_by_id("b1")
resultBox = driver.find_element_by_id("resultBox")
time.sleep(2)

def myTest(e1, e2, b1, value_1, value_2, right_answer):
	e1.clear()
	e2.clear()
	time.sleep(2)
	e1.send_keys(value_1)
	time.sleep(2)
	e2.send_keys(value_2)
	time.sleep(2)
	b1.click()
	time.sleep(2)
	s1 = e1.get_attribute('value')
	s2 = e2.get_attribute('value')
	s3 = resultBox.text
	print(s1 + "  " + s2 + "  " + s3)
	time.sleep(2)
	test.equal(s3, right_answer)
	print("OK")
	time.sleep(1)

myTest(e1, e2, b1, "25", "17", "42")
myTest(e1, e2, b1, "100", "200", "300")
myTest(e1, e2, b1, "-30", "17", "-13")

driver.close()
