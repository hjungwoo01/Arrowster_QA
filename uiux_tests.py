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

class UIUXTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 20)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def navigate_to_page(self, page):
        print(f"Navigating to {base_url}/{page}")
        self.driver.get(f"{base_url}/{page}")
        print(f"Navigated to {page} page")
        time.sleep(2)

    def get_menu_items(self):
        nav_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//nav")))
        return nav_menu.find_elements(By.XPATH, ".//a")

    def check_navigation_items(self, expected_items):
        menu_items = self.get_menu_items()
        print("Retrieved menu items:")
        for item in menu_items:
            print(f"Menu item text: '{item.text}'")
        
        for item, expected in zip(menu_items, expected_items):
            print(f"Checking menu item: '{item.text}' against expected: '{expected}'")
            self.assertEqual(item.text.strip(), expected)
        
        logo = self.wait.until(EC.presence_of_element_located((By.XPATH, "//nav//img[@alt='Arrowster']")))
        self.assertIsNotNone(logo)
        print("Company logo found")
    
    #### EPIC 2: UI/UX Design
    def test_epic2_main_navigation_menu(self):
        print("Starting EPIC 2: UI/UX Design")
        print("Starting main navigation menu test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        expected_items = ["Search", "Comparisons"]
        
        for page in pages:
            self.navigate_to_page(page)
            try:
                self.check_navigation_items(expected_items)
                print(f"Main navigation menu test passed on {page} page")
            except Exception as e:
                print(f"Main navigation menu test failed on {page} page: {e}")
                self.fail(f"Main navigation menu test failed on {page} page")
    
    def test_epic2_key_features_accessibility(self):
        print("Starting key features accessibility test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        expected_items = ["Search", "Comparisons"]
        
        for page in pages:
            self.navigate_to_page(page)
            try:
                logo = self.wait.until(EC.presence_of_element_located((By.XPATH, "//nav//img[@alt='Arrowster']")))
                self.assertIsNotNone(logo)
                print("Company logo found")
                
                for item_text in expected_items:
                    nav_item = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, item_text)))
                    self.assertTrue(nav_item.is_displayed())
                    print(f"Navigation item {item_text} is displayed")
                
                print(f"Key features accessibility test passed on {page} page")
            except Exception as e:
                print(f"Key features accessibility test failed on {page} page: {e}")
                self.fail(f"Key features accessibility test failed on {page} page")
    
    def test_epic2_design_elements_consistency(self):
        print("Starting design elements consistency test...")
        self.navigate_to_page("")
        
        try:
            design_elements = {
                "font": self.driver.find_element(By.TAG_NAME, "body").value_of_css_property("font-family"),
                "color": self.driver.find_element(By.TAG_NAME, "body").value_of_css_property("color"),
                "button_style": self.driver.find_element(By.TAG_NAME, "button").get_attribute("class")
            }
            print(f"Captured design elements: {design_elements}")
            
            pages = ["login", "student-signup", "school-recommendation", "adv-search"]
            for page in pages:
                self.navigate_to_page(page)
                self.assertEqual(design_elements["font"], self.driver.find_element(By.TAG_NAME, "body").value_of_css_property("font-family"))
                self.assertEqual(design_elements["color"], self.driver.find_element(By.TAG_NAME, "body").value_of_css_property("color"))
                self.assertEqual(design_elements["button_style"], self.driver.find_element(By.TAG_NAME, "button").get_attribute("class"))
                print(f"Design elements are consistent on {page}")
            
            print("Design elements consistency test passed")
        except Exception as e:
            print(f"Design elements consistency test failed: {e}")
            self.fail("Design elements consistency test failed")
    
    def test_epic2_layout_consistency(self):
        print("Starting layout consistency test...")
        self.navigate_to_page("")
        
        try:
            layout_structure = {
                "header": self.driver.find_element(By.TAG_NAME, "header").get_attribute("class") if self.driver.find_elements(By.TAG_NAME, "header") else None,
                "footer": self.driver.find_element(By.TAG_NAME, "footer").get_attribute("class") if self.driver.find_elements(By.TAG_NAME, "footer") else None,
                "sidebar": self.driver.find_element(By.TAG_NAME, "aside").get_attribute("class") if self.driver.find_elements(By.TAG_NAME, "aside") else None
            }
            print(f"Captured layout structure: {layout_structure}")
            
            pages = ["login", "student-signup", "school-recommendation", "adv-search"]
            for page in pages:
                self.navigate_to_page(page)
                if layout_structure["header"]:
                    self.assertEqual(layout_structure["header"], self.driver.find_element(By.TAG_NAME, "header").get_attribute("class"))
                if layout_structure["footer"]:
                    self.assertEqual(layout_structure["footer"], self.driver.find_element(By.TAG_NAME, "footer").get_attribute("class"))
                if layout_structure["sidebar"]:
                    self.assertEqual(layout_structure["sidebar"], self.driver.find_element(By.TAG_NAME, "aside").get_attribute("class"))
                print(f"Layout structure is consistent on {page}")
            
            print("Layout consistency test passed")
        except Exception as e:
            print(f"Layout consistency test failed: {e}")
            self.fail("Layout consistency test failed")

    def test_form_field_accessibility(self):
        print("Starting form field accessibility test...")
        self.navigate_to_page("student-signup")
        
        try:
            form_fields = {
                "Phone Number": (By.XPATH, "//input[@type='tel']")
            }
            
            for field_name, locator in form_fields.items():
                field = self.wait.until(EC.presence_of_element_located(locator))
                self.assertTrue(field.is_displayed())
                field.send_keys("test")
                print(f"{field_name} field is accessible and functional")
            
            print("Form field accessibility test passed")
        except Exception as e:
            print(f"Form field accessibility test failed: {e}")
            self.fail("Form field accessibility test failed")
    
    def test_button_visibility_and_functionality(self):
        print("Starting button visibility and functionality test...")
        self.navigate_to_page("student-signup")
        
        try:
            buttons = ["Save", "Continue"]
            for button_text in buttons:
                button = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{button_text}')]")))
                self.assertTrue(button.is_displayed())
                print(f"Button '{button_text}' is visible")
            
            print("Button visibility and functionality test passed")
        except Exception as e:
            print(f"Button visibility and functionality test failed: {e}")
            self.fail("Button visibility and functionality test failed")

    def test_accessibility_compliance(self):
        print("Starting accessibility compliance test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        for page in pages:
            self.navigate_to_page(page)
            try:
                accessible_elements = self.driver.find_elements(By.XPATH, "//*[@aria-label]")
                self.assertGreater(len(accessible_elements), 0)
                print("Found elements with aria-label")
                
                focusable_elements = self.driver.find_elements(By.XPATH, "//*[@tabindex]")
                self.assertGreater(len(focusable_elements), 0)
                print("Found elements with tabindex")
                
                print(f"Accessibility compliance test passed on {page} page")
            except Exception as e:
                print(f"Accessibility compliance test failed on {page} page: {e}")
                self.fail(f"Accessibility compliance test failed on {page} page")

    def test_responsive_design(self):
        print("Starting responsive design test...")
        
        pages = ["login", "student-signup", "school-recommendation", "adv-search"]
        for page in pages:
            self.navigate_to_page(page)
            try:
                sizes = [(1920, 1080), (1366, 768), (375, 667), (768, 1024)]
                for width, height in sizes:
                    self.driver.set_window_size(width, height)
                    time.sleep(2)
                    body = self.driver.find_element(By.TAG_NAME, "body")
                    self.assertTrue(body.is_displayed())
                    print(f"Page {page} is responsive at {width}x{height}")
                
                print(f"Responsive design test passed on {page} page")
            except Exception as e:
                print(f"Responsive design test failed on {page} page: {e}")
                self.fail(f"Responsive design test failed on {page} page")

if __name__ == "__main__":
    unittest.main()
