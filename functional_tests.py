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

service = Service(chromedriver_path)

base_url = "https://stage.arrowster.com"

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 20)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test_recommendation_form(self):
        print("Starting recommendation form test...")
        self.driver.get(base_url)
        print("Navigated to main page")
        
        try:
            # Enter GPA
            gpa_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='GPA']")))
            gpa_field.send_keys("4.0")
            print("Entered GPA")
            time.sleep(2)
            
            # Click and select Grade Level
            grade_level_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Grade Level')]")))
            grade_level_field.click()
            first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][1]")))
            first_choice.click()
            print("Selected Grade Level: Undergraduate")
            time.sleep(2)
            
            # Click and select Location
            location_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Location')]")))
            location_field.click()
            first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][1]")))
            first_choice.click()
            print("Selected Location: United States")
            time.sleep(2)
            
            # Click and select Budget
            budget_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Budget')]")))
            budget_field.click()
            first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][1]")))
            first_choice.click()
            print("Selected Budget: $500 - $10,000")
            time.sleep(2)
            
            # Click and select Course Preference
            course_preference_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Course Preference')]")))
            course_preference_field.click()
            first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem'][1]")))
            first_choice.click()
            print("Selected Course Preference: Agricultural Sciences")
            time.sleep(2)
            
            # Click the "Run Recommendation Engine" button
            run_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Run Recommendation Engine')]")))
            run_button.click()
            print("Clicked 'Run Recommendation Engine' button")
            
            # Wait for the next page to load 
            self.wait.until(EC.url_contains("/school-recommendation"))
            print("Recommendation successful, redirected to recommendation page")
            self.assertTrue("/school-recommendation" in self.driver.current_url)
            
            print("Recommendation form test passed")
        except Exception as e:
            print(f"Recommendation form test failed: {e}")
            self.fail("Recommendation form test failed")
            
    #### EPIC 1: Data Integrity Tests
    def test_epic1_user_login(self):
        print("Starting EPIC 1: Data Integrity Tests")
        print("Starting login test...")
        self.driver.get(f"{base_url}/login")
        print("Navigated to login page")
        
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            time.sleep(2)
            email_field.send_keys("testuser@example.com")
            print("Entered email")
            
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_field.send_keys("password123")
            print("Entered password")
            
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']")))
            login_button.click()
            print("Clicked login button")
            
            self.wait.until(EC.url_to_be(f"{base_url}/connection"))
            print("Login successful, redirected to connections page")
            self.assertEqual(self.driver.current_url, f"{base_url}/connection")
            print("Login test passed")
        except Exception as e:
            print(f"Login failed: {e}")
            self.fail("Login test failed")
    
    def test_epic1_user_profile_update(self):
        print("Starting profile update test...")
        self.driver.get(f"{base_url}/connection")
        print("Navigated to connections page") # Ensure user is logged in
        
        try:
            self.driver.get(f"{base_url}/student-profile")
            print("Navigated to student profile page")
            name_field = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
            name_field.clear()
            name_field.send_keys("Updated User")
            print("Updated name field")
            
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
            save_button.click()
            print("Clicked Save button")
            
            # Verify update
            self.driver.refresh()
            updated_name = self.wait.until(EC.presence_of_element_located((By.ID, "name"))).get_attribute("value")
            self.assertEqual(updated_name, "Updated User")
            print("Profile update test passed")
        except Exception as e:
            print(f"Profile update test failed: {e}")
            self.fail("Profile update test failed")

    #### EPIC 3: User Flow Efficiency
    def test_epic3_login_process_efficiency(self):
        print("Starting login process efficiency test...")
        start_time = time.time()
        self.driver.get(f"{base_url}/login")
        print("Navigated to login page")
        
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email']")))
            email_field.send_keys("testuser@example.com")
            print("Entered email")
            
            password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
            password_field.send_keys("password123")
            print("Entered password")
            
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]")))
            login_button.click()
            print("Clicked Sign in button")
            
            self.wait.until(EC.url_to_be(f"{base_url}/connection"))
            end_time = time.time()
            print("Login successful, redirected to connections page")
            self.assertTrue(end_time - start_time < 2, "Login process took too long")
            print("Login process efficiency test passed")
        except Exception as e:
            print(f"Login process efficiency test failed: {e}")
            self.fail("Login process efficiency test failed")

    def test_epic3_access_search(self):
        print("Starting access search test...")
        self.test_epic1_user_login()  # Ensure the user is logged in
        
        start_time = time.time()
        self.driver.get(f"{base_url}/adv-search")
        print("Navigated to search page")
        
        try:
            end_time = time.time()
            self.assertTrue(end_time - start_time < 2, "Accessing search page took too long")
            print("Access search page test passed")
        except Exception as e:
            print(f"Access search page test failed: {e}")
            self.fail("Access search page test failed")

    ### Sign up changed to phone number and OTP verification
    # def test_epic3_sign_up_process_efficiency(self):
    #     print("Starting sign up process efficiency test...")
    #     start_time = time.time()
    #     self.driver.get(f"{base_url}/signup")
    #     print("Navigated to sign up page")
        
    #     try:
    #         # Full Name
    #         fullname_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text'][1]")))
    #         time.sleep(2)
    #         fullname_field.send_keys("New User")
    #         print("Entered fullname")
            
    #         # Email Address
    #         email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email'][1]")))
    #         time.sleep(2)
    #         email_field.send_keys("newuser@example.com")
    #         print("Entered email")
            
    #         # Password
    #         password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
    #         time.sleep(2)
    #         password_field.send_keys("password123")
    #         print("Entered password")
            
    #         # Confirm Password
    #         password_confirm_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[2]")))
    #         time.sleep(2)
    #         password_confirm_field.send_keys("password123")
    #         print("Entered confirm password")
            
    #         # Phone Number
    #         phone_number_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='tel']")))
    #         time.sleep(2)
    #         phone_number_field.send_keys("1234567890")
    #         print("Entered phone number")
            
    #         # Click the Save button
    #         save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]")))
    #         save_button.click()
    #         print("Clicked save button")
            
    #         continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
    #         continue_button.click()
    #         print("Clicked continue button")
            
    #         self.wait.until(EC.url_to_be(f"{base_url}/signup/complete"))
    #         end_time = time.time()
    #         self.assertTrue(end_time - start_time < 2, "Registration process took too long")
    #         print("Registration process efficiency test passed")
    #     except Exception as e:
    #         print(f"Registration process efficiency test failed: {e}")
    #         self.fail("Registration process efficiency test failed")

    #### EPIC 4: Performance and Security
    def test_epic4_page_load_times(self):
        print("Starting page load times test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        for page in pages:
            start_time = time.time()
            self.driver.get(f"{base_url}/{page}")
            print(f"Navigated to {page} page")
            
            try:
                self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                end_time = time.time()
                self.assertTrue(end_time - start_time < 2, f"Page load time for {page} took too long")
                print(f"Page load times test passed for {page} page")
            except Exception as e:
                print(f"Page load times test failed for {page} page: {e}")
                self.fail(f"Page load times test failed for {page} page")

    #### EPIC 5: Usability
    def test_epic5_help_resources(self):
        print("Starting help resources test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        for page in pages:
            print(f"Navigating to {base_url}/{page}")
            self.driver.get(f"{base_url}/{page}")
            print(f"Navigated to {page} page")
            
            try:
                time.sleep(2)
                help_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Help")))
                help_link.click()
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Help']")))
                print(f"Help resources are accessible on {page} page")
                
                print(f"Help resources test passed on {page} page")
            except Exception as e:
                print(f"Help resources test failed on {page} page: {e}")
                self.fail(f"Help resources test failed on {page} page")
    
    def test_epic5_instructions_clarity(self):
        print("Starting instructions clarity test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        for page in pages:
            print(f"Navigating to {base_url}/{page}")
            self.driver.get(f"{base_url}/{page}")
            print(f"Navigated to {page} page")
            
            try:
                time.sleep(2)
                instructions = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'instructions')]")
                for instruction in instructions:
                    self.assertTrue(instruction.is_displayed(), "Instruction text is not clear or visible")
                    print(f"Instruction text: {instruction.text}")
                
                print(f"Instructions clarity test passed on {page} page")
            except Exception as e:
                print(f"Instructions clarity test failed on {page} page: {e}")
                self.fail(f"Instructions clarity test failed on {page} page")
    
if __name__ == "__main__":
    unittest.main()
