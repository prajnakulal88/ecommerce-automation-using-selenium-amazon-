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
        file_path = os.path.abspath(r"C:\Users\prajna\Desktop\ST MINIPROJECT\search_data.csv")
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = row['product']
                
                # Locate the search bar and search for the product
                wait = WebDriverWait(driver, 60)
                search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#twotabsearchtextbox")))
                
                search_bar.clear()
                search_bar.send_keys(product)
                
                # Click the search button
                search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
                search_button.click()
                
                # Verify the search results page contains the product name
                wait.until(EC.url_contains("s?k=" + product))
                
                self.assertIn(product, driver.page_source)
                
                # Navigate back to the homepage for the next iteration
                driver.get("https://www.amazon.com")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()