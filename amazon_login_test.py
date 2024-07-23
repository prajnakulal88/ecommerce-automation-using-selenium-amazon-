import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import csv

class AmazonSearchTest(unittest.TestCase):
    def setUp(self):
        self.service = Service("C:/Users/prajna/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.amazon.com")  # Amazon homepage URL

    def test_search(self):
        driver = self.driver
        file_path = os.path.abspath(r"C:\Users\prajna\Desktop\ST MINIPROJECT\login_data.csv")
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                username = row['username']
                password = row['password']
                
                # Click on the signin button
                signin_button = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.ID, "nav-link-accountList"))
                )
                signin_button.click()
                
                # Enter the email or phone number
                email_field = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "ap_email"))
                )
                email_field.clear()
                email_field.send_keys(username)
                
                # Click continue
                continue_button = driver.find_element(By.ID, "continue")
                continue_button.click()
                
                # Enter the password
                password_field = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "ap_password"))
                )
                password_field.clear()
                password_field.send_keys(password)
                
                # Click the login button
                login_button = driver.find_element(By.ID, "signInSubmit")
                login_button.click()
                
                # Check if login was successful
                self.assertIn("Hello", driver.page_source)  # Adjust based on the actual content after login
                
                # Logout and prepare for the next iteration
                driver.get("https://www.amazon.com/ap/signin")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()