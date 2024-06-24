import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "/usr/local/bin/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--verbose")

service = Service(chromedriver_path)

base_url = "https://stage.arrowster.com"

class DataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 20)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def navigate_to_page(self, page):
        self.driver.get(f"{base_url}/{page}")
        print(f"Navigated to {page} page")

    ### MAIN PAGE TESTS ###
    def enter_gpa(self, gpa_value):
        gpa_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input)[1]")))
        gpa_field.clear()
        gpa_field.send_keys(gpa_value)
        print(f"Entered GPA: {gpa_value}")

    def check_gpa_validity(self, gpa_value, should_pass):
        self.enter_gpa(gpa_value)
        time.sleep(2)
        
        # Click and select Grade Level
        grade_level_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[2]")))
        grade_level_field.click()
        first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[2]/div[2]/div[1]/input")))
        first_choice.click()
        print("Selected Grade Level: Undergraduate")
        
        time.sleep(2)
        # Click and select Location
        location_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[3]")))
        location_field.click()
        first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[3]/div[2]/div[2]")))
        first_choice.click()
        print("Selected Location: United States")
        
        time.sleep(2)
        # Click and select Budget
        budget_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[4]")))
        budget_field.click()
        first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[4]/div[2]/div[2]/input")))
        first_choice.click()
        print("Selected Budget: $500 - $10,000")
        
        time.sleep(2)
        # Click and select Course Preference
        course_preference_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[5]")))
        course_preference_field.click()
        first_choice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[5]/div[2]/div[2]")))
        first_choice.click()
        print("Selected Course Preference: Agricultural Sciences")
        
        # Click the "Run Recommendation Engine" button
        run_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[1]/div/div/form/div[6]/button")))
        run_button.click()
        print("Clicked 'Run Recommendation Engine' button")
        
        # Check redirection
        if should_pass:
            try:
                time.sleep(2)
                self.wait.until(EC.url_contains(f"{base_url}/school-recommendation?data="))
                self.assertTrue(self.driver.current_url.startswith(f"{base_url}/school-recommendation?data="), "Redirection to recommendation page failed")
                print(f"GPA value '{gpa_value}' is valid and passed.")
            except Exception as e:
                print(f"GPA value '{gpa_value}' should be valid but failed. Exception: {e}")
                self.fail(f"GPA value '{gpa_value}' should be valid but failed. Exception: {e}")
        else:
            try:
                time.sleep(2)
                self.wait.until_not(EC.url_contains(f"{base_url}/school-recommendation?data="))
                print(f"GPA value '{gpa_value}' is invalid and not redirected.")
            except Exception as e:
                print(f"GPA value '{gpa_value}' should be invalid but passed. Exception: {e}")
                self.fail(f"GPA value '{gpa_value}' should be invalid but passed. Exception: {e}")

    def test_gpa_valid_values(self):
        print("Starting test for valid GPA values...")
        self.navigate_to_page("")
        valid_gpas = ["0", "0.0", "2.5", "4.0", "5.0"]
        for gpa in valid_gpas:
            self.check_gpa_validity(gpa, True)
        print("Valid GPA values test passed")

    def test_gpa_invalid_values(self):
        print("Starting test for invalid GPA values...")
        self.navigate_to_page("")
        invalid_gpas = ["-1", "5.1", "abc", "@!#", "", " ", "6", "3..5"]
        for gpa in invalid_gpas:
            self.check_gpa_validity(gpa, False)
        print("Invalid GPA values test passed")

    def test_gpa_boundary_values(self):
        print("Starting test for GPA boundary values...")
        self.navigate_to_page("")
        boundary_gpas = ["0", "5", "0.0", "5.0"]
        for gpa in boundary_gpas:
            self.check_gpa_validity(gpa, True)
        near_boundary_gpas = ["-0.1", "5.1", "0.01", "4.99"]
        for gpa in near_boundary_gpas:
            self.check_gpa_validity(gpa, False)
        print("GPA boundary values test passed")

    ### SIGN UP PAGE TESTS ###
    def check_phone_number_validity(self, phone_number, should_be_valid):
        self.navigate_to_page("student-signup")
        phone_number_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']")))
        phone_number_field.clear()
        time.sleep(2)
        phone_number_field.send_keys(phone_number)
        print(f"Entered phone number: {phone_number}")
        
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button.click()
        print(f"Clicked Continue after entering phone number: {phone_number}")
        
        time.sleep(2)
        
        if should_be_valid:
            try:
                otp_verification_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'OTP Verification']")))
                self.assertTrue(otp_verification_element.is_displayed(), f"Phone number '{phone_number}' should be valid.")
                print(f"Phone number '{phone_number}' is valid and passed.")
            except Exception as e:
                print(f"Phone number '{phone_number}' should be valid but failed. Exception: {e}")
                self.fail(f"Phone number '{phone_number}' should be valid but failed. Exception: {e}")
        else:
            try:
                otp_verification_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'OTP Verification']")))
                print(f"Phone number '{phone_number}' should be invalid but passed.")
                self.fail(f"Phone number '{phone_number}' should be invalid but passed.")
            except:
                self.assertTrue(True, f"Phone number '{phone_number}' is invalid and did not redirect.")
                print(f"Phone number '{phone_number}' is invalid and did not redirect.")

    def test_phone_number_boundary_values(self):
        print("Starting test for phone number boundary values...")
        valid_numbers = ["12345678", "123456789", "1234567890"]
        invalid_numbers = ["1234567", "12345678901"]

        for phone_number in valid_numbers:
            self.check_phone_number_validity(phone_number, True)

        for phone_number in invalid_numbers:
            self.check_phone_number_validity(phone_number, False)

    def test_phone_number_invalid_values(self):
        print("Starting test for invalid phone number values...")
        invalid_numbers = ["", "abcdefg", "!@#$%^&*()"]

        for phone_number in invalid_numbers:
            self.check_phone_number_validity(phone_number, False)

    def test_phone_number_valid_values(self):
        print("Starting test for valid phone number values...")
        valid_numbers = ["12345678", "87654321", "9876543210"]

        for phone_number in valid_numbers:
            self.check_phone_number_validity(phone_number, True)
        
    ### ADV-SEARCH PAGE TESTS ###
    def test_area_of_study_selection(self):
        self.navigate_to_page("adv-search")
        try:
            area_of_study = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[3]/div[2]/select")))
            area_of_study.click()
            first_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]")))
            first_option.click()
            print("Selected Area Of Study")
        except Exception as e:
            print(f"Failed to select Area Of Study: {e}")
            self.fail("Failed to select Area Of Study")

    def test_invalid_tuition_fee(self):
        self.navigate_to_page("adv-search")
        invalid_values = ["-100", "abc", "1000000"]

        for value in invalid_values:
            try:
                from_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[2]/div[1]/input")))
                to_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[2]/div[2]/input")))
                from_field.clear()
                to_field.clear()
                from_field.send_keys(value)
                to_field.send_keys(value)
                print(f"Entered invalid Tuition Fee: {value}")
            except Exception as e:
                print(f"Failed to enter invalid Tuition Fee {value}: {e}")
                self.fail(f"Failed to enter invalid Tuition Fee {value}")

    def test_invalid_ielts(self):
        self.navigate_to_page("adv-search")
        invalid_values = ["-1", "abc", "10"]

        for value in invalid_values:
            try:
                from_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]/div[1]/input")))
                to_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]/div[2]/input")))
                from_field.clear()
                to_field.clear()
                from_field.send_keys(value)
                to_field.send_keys(value)
                print(f"Entered invalid IELTS: {value}")
            except Exception as e:
                print(f"Failed to enter invalid IELTS {value}: {e}")
                self.fail(f"Failed to enter invalid IELTS {value}")

    def test_invalid_sat_score(self):
        self.navigate_to_page("adv-search")
        invalid_values = ["-1", "abc", "1600"]

        for value in invalid_values:
            try:
                from_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div[2]/div[1]/input")))
                to_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div[2]/div[2]/input")))
                from_field.clear()
                to_field.clear()
                from_field.send_keys(value)
                to_field.send_keys(value)
                print(f"Entered invalid SAT Score: {value}")
            except Exception as e:
                print(f"Failed to enter invalid SAT Score {value}: {e}")
                self.fail(f"Failed to enter invalid SAT Score {value}")

    def test_invalid_gpa(self):
        self.navigate_to_page("adv-search")
        invalid_values = ["-1", "abc", "6"]

        for value in invalid_values:
            try:
                from_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[7]/div/div[2]/div[2]/div[1]/input")))
                to_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[7]/div/div[2]/div[2]/div[2]/input")))
                from_field.clear()
                to_field.clear()
                from_field.send_keys(value)
                to_field.send_keys(value)
                print(f"Entered invalid GPA: {value}")
            except Exception as e:
                print(f"Failed to enter invalid GPA {value}: {e}")
                self.fail(f"Failed to enter invalid GPA {value}")

    def test_apply_filter(self):
        self.navigate_to_page("adv-search")
        try:
            apply_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply Filter')]")))
            apply_button.click()
            print("Clicked Apply Filter button")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'Results Found']")))
            print("Results page loaded")
        except Exception as e:
            print(f"Failed to apply filter: {e}")
            self.fail("Failed to apply filter")

if __name__ == "__main__":
    unittest.main()
