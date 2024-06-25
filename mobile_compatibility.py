import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/usr/local/bin/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--window-size=375,812")

service = Service(chromedriver_path)

base_url = "https://stage.arrowster.com"

class MobileCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 20)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def navigate_to_page(self, page=""):
        url = f"{base_url}/{page}" if page else base_url
        print(f"Navigating to {url}")
        self.driver.get(url)
        print(f"Navigated to {url}")
        time.sleep(2)

    def test_mobile_home_page(self):
        print("Starting mobile home page test...")
        self.navigate_to_page("")
        try:
            # Check for mobile layout elements
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[1]/input").is_displayed(), "GPA input is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[2]").is_displayed(), "Grade Level dropdown is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[3]").is_displayed(), "Location dropdown is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[4]").is_displayed(), "Budget dropdown is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[5]").is_displayed(), "Course Preference dropdown is not visible.")     
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[6]/button").is_displayed(), "Run Recommendation Engine button is not visible.")
            print("Mobile home page test passed")
        except Exception as e:
            print(f"Mobile home page test failed: {e}")
            self.fail("Mobile home page test failed")

    def test_mobile_login_page(self):
        print("Starting mobile login page test...")
        self.navigate_to_page("login")
        try:
            # Check for mobile layout elements
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/div[1]/input").is_displayed(), "Email input is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/div[2]/input").is_displayed(), "Password input is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/button").is_displayed(), "Sign in button is not visible.")
            print("Mobile login page test passed")
        except Exception as e:
            print(f"Mobile login page test failed: {e}")
            self.fail("Mobile login page test failed")

    def test_mobile_signup_page(self):
        print("Starting mobile signup page test...")
        self.navigate_to_page("student-signup")
        try:
            # Check for mobile layout elements
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/input").is_displayed(), "Phone number input is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[2]/input").is_displayed(), "Check box is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").is_displayed(), "Continue button is not visible.")
            print("Mobile signup page test passed")
        except Exception as e:
            print(f"Mobile signup page test failed: {e}")
            self.fail("Mobile signup page test failed")
            
    def test_mobile_navigation(self):
        print("Starting mobile navigation test...")
        self.navigate_to_page("")
        try:
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/nav/div/div/div[1]/ul/li[1]/a").is_displayed(), "Search on nav bar is not visible.")
            self.assertTrue(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/nav/div/div/div[1]/ul/li[2]/a").is_displayed(), "Comparisons on nav bar is not visible.")
            print("Mobile navigation test passed")
        except Exception as e:
            print(f"Mobile navigation test failed: {e}")
            self.fail("Mobile navigation test failed")

    def test_mobile_responsiveness(self):
        print("Starting mobile responsiveness test...")
        pages = ["", "login", "student-signup"]
        try:
            for page in pages:
                self.navigate_to_page(page)
                self.driver.set_window_size(375, 812)
                time.sleep(1)
                self.assertTrue(self.driver.find_element(By.TAG_NAME, "body").is_displayed(), f"Page {page} is not responsive at 375x812")
                print(f"Page {page} is responsive at 375x812")
            print("Mobile responsiveness test passed")
        except Exception as e:
            print(f"Mobile responsiveness test failed: {e}")
            self.fail("Mobile responsiveness test failed")

if __name__ == "__main__":
    unittest.main()
