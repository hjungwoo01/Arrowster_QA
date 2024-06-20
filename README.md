# README.md

## Installation and Setup

### Step 1: Clone the Repository

First, clone the repository to your local machine using Git.

```sh
git clone https://github.com/hjungwoo01/Arrowster_QA.git
cd Arrowster_QA
```

### Step 2: Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Requirements

Install the necessary packages listed in `requirements.txt`.

```sh
pip install -r requirements.txt
```

### Step 4: Download and Set Up ChromeDriver

Download the ChromeDriver from the [official site](https://sites.google.com/chromium.org/driver/) and place it in a known directory.

Update the `chromedriver_path` variable in the test scripts with the path to the ChromeDriver executable.

```python
chromedriver_path = "/path/to/chromedriver"
```

## Running the Tests

### Step 1: Run Functional Tests

To run the functional tests, use the following command:

```sh
python3 -m unittest functional_tests.py
```

### Step 2: Run UI/UX Tests

To run the UI/UX tests, use the following command:

```sh
python3 -m unittest uiux_tests.py
```

### Functional Tests

The functional tests in this project are designed to verify that the core functionalities of the web application are working correctly. The tests are organized under different epics to cover various aspects of the application.

#### EPIC 1: Data Integrity Tests

1. **User Login Test**:
   - **Test Case**: `test_epic1_user_login`
   - **Description**: Verifies the login functionality by navigating to the login page, entering valid credentials, and checking for successful redirection to the connections page.

2. **User Profile Update Test**:
   - **Test Case**: `test_epic1_user_profile_update`
   - **Description**: Ensures the user can navigate to and update their profile page. It assumes the user is already logged in and verifies the navigation from the connections page to the student profile page.

#### EPIC 3: User Flow Efficiency

3. **Login Process Efficiency Test**:
   - **Test Case**: `test_epic3_login_process_efficiency`
   - **Description**: Measures the efficiency of the login process by timing it. The test ensures the login completes within 2 seconds by navigating to the login page, entering credentials, clicking the login button, and checking for successful redirection to the connections page.

4. **Access Search Page Test**:
   - **Test Case**: `test_epic3_access_search`
   - **Description**: Checks the time taken to access the search page. After logging in, the test navigates to the advanced search page and ensures it loads within 2 seconds.

#### EPIC 4: Performance and Security

5. **Page Load Times Test**:
   - **Test Case**: `test_epic4_page_load_times`
   - **Description**: Measures the load times for critical pages like the student profile and advanced search pages. The test ensures these pages load within 2 seconds, verifying the application's performance and speed.

#### Other Functional Tests

6. **Recommendation Form Test**:
   - **Test Case**: `test_recommendation_form`
   - **Description**: Tests the functionality of the recommendation form by navigating to the main page, entering GPA, selecting Grade Level, Location, Budget, and Course Preference, and running the recommendation engine. The test verifies if the recommendation results are displayed correctly.

These functional tests ensure that the application's main features, user flow efficiency, and performance meet the expected standards, providing confidence in the application's readiness for deployment.

## UI/UX Tests

The UI/UX tests in this project are designed to ensure that the user interface is intuitive, accessible, and consistent across different devices and resolutions. They also verify that key features and navigation elements are functional and accessible to all users.

### EPIC 2: UI/UX Design

1. **Main Navigation Menu Test**:
   - **Test Case**: `test_epic2_main_navigation_menu`
   - **Description**: Ensures that the main navigation menu is present and functional on various pages, including login, student signup, school recommendation, and advanced search. The test checks for the expected items "Search" and "Comparisons," along with the presence of the company logo.

2. **Key Features Accessibility Test**:
   - **Test Case**: `test_epic2_key_features_accessibility`
   - **Description**: Verifies the presence and accessibility of key features such as navigation items and the company logo on the login, student signup, school recommendation, and advanced search pages. Ensures that the navigation items "Search" and "Comparisons" are displayed correctly.

3. **Design Elements Consistency Test**:
   - **Test Case**: `test_epic2_design_elements_consistency`
   - **Description**: Checks that design elements like font, color, and button style are consistent across different pages, including login, student signup, school recommendation, and advanced search.

4. **Layout Consistency Test**:
   - **Test Case**: `test_epic2_layout_consistency`
   - **Description**: Ensures the layout structure, including headers, footers, and sidebars, is consistent on different pages such as login, student signup, school recommendation, and advanced search.

5. **Form Field Accessibility Test**:
   - **Test Case**: `test_form_field_accessibility`
   - **Description**: Verifies the presence and functionality of form fields on the student signup page, specifically the "Phone Number" field, to ensure it is accessible and functional.

6. **Button Visibility and Functionality Test**:
   - **Test Case**: `test_button_visibility_and_functionality`
   - **Description**: Ensures that important buttons like "Save" and "Continue" are visible and functional on the student signup page.

### EPIC 5: Usability

7. **Accessibility Compliance Test**:
   - **Test Case**: `test_accessibility_compliance`
   - **Description**: Checks for the presence of elements with aria-label and tabindex attributes to ensure accessibility compliance on pages such as login, student signup, school recommendation, and advanced search.

8. **Responsive Design Test**:
   - **Test Case**: `test_responsive_design`
   - **Description**: Verifies that the website is responsive and functions correctly at various screen resolutions (1920x1080, 1366x768, 375x667, 768x1024) on pages like login, student signup, school recommendation, and advanced search.

These tests ensure that the user interface is intuitive, accessible, and consistent across different devices and resolutions. They also verify that key features and navigation elements are functional and accessible to all users.

By following these steps and descriptions, you should be able to set up, run, and understand the tests provided in this repository.
