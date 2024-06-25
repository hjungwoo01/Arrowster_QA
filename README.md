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

### Step 3: Run Data Tests

To run the data tests, use the following command:

```sh
python3 -m unittest data_tests.py
```

### Step 4: Run Mobile Compatibility Tests

To run the mobile compatibility tests, use the following command:

```sh
python3 -m unittest mobile_compatibility_tests.py
```

## Functional Tests

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

## Data Tests

The data tests in this project are designed to verify the handling of various data inputs in the application. The tests ensure that input fields validate data correctly and that the application responds appropriately to different types of input.

### GPA Field Tests

1. **Valid GPA Values Test**:
   - **Test Case**: `test_gpa_valid_values`
   - **Description**: Tests valid GPA values to ensure they are accepted by the application.

2. **Invalid GPA Values Test**:
   - **Test Case**: `test_gpa_invalid_values`
   - **Description**: Tests invalid GPA values to ensure they are rejected by the application.

3. **GPA Boundary Values Test**:
   - **Test Case**: `test_gpa_boundary_values`
   - **Description**: Tests GPA boundary values to ensure the application handles edge cases correctly.

### Phone Number Field Tests

4. **Phone Number Boundary Values Test**:
   - **Test Case**: `test_phone_number_boundary_values`
   - **Description**: Tests phone numbers at the boundary of valid and invalid lengths.

5. **Invalid Phone Number Values Test**:
   - **Test Case**: `test_phone_number_invalid_values`
   - **Description**: Tests various invalid phone numbers to ensure they are rejected by the application.

6. **Valid Phone Number Values Test**:
   - **Test Case**: `test_phone_number_valid_values`
   - **Description**: Tests valid phone numbers to ensure they are accepted by the application.

### Advanced Search Page Tests

7. **Area of Study Selection Test**:
   - **Test Case**: `test_area_of_study_selection`
   - **Description**: Tests the selection of the area of study dropdown on the advanced search page.

8. **Invalid Tuition Fee Values Test**:
   - **Test Case**: `test_invalid_tuition_fee`
   - **Description**: Tests various invalid tuition fee values to ensure they are rejected by the application.

9. **Invalid IELTS Values Test**:
   - **Test Case**: `test_invalid_ielts`
   - **Description**: Tests various invalid IELTS values to ensure they are rejected by the application.

10. **Invalid SAT Score Values Test**:
    - **Test Case**: `test_invalid_sat_score`
    - **Description**: Tests various invalid SAT score values to ensure they are rejected by the application.

11. **Invalid GPA Values Test**:
    - **Test Case**: `test_invalid_gpa`
    - **Description**: Tests various invalid GPA values to ensure they are rejected by the application.

12. **Apply Filter Test**:
    - **Test Case**: `test_apply_filter`
    - **Description**: Tests the apply filter functionality on the advanced search page.

## Mobile Compatibility Tests

The mobile compatibility tests in this project are designed to ensure that the user interface is mobile-friendly and works correctly on mobile devices.

1. **Mobile Home Page Test**:
   - **Test Case**: `test_mobile_home_page`
   - **Description**: Verifies the visibility of key elements on the mobile home page.

2. **Mobile Login Page Test**:
   - **Test Case**: `test_mobile_login_page`
   - **Description**: Verifies the visibility of key elements on the mobile login page.

3. **Mobile Signup Page Test**:
   - **Test Case**: `test_mobile_signup_page`
   - **Description**: Verifies the visibility of key elements on the mobile signup page.

4. **Mobile Navigation Test**:
   - **Test Case**: `test_mobile_navigation`
   - **Description**: Verifies the visibility of navigation elements on the mobile version of the site.

5. **Mobile Responsiveness Test**:
   - **Test Case**: `test_mobile_responsiveness`
   - **Description**: Ensures that the application is responsive on a mobile device with a screen size of 375x812.

By following these steps and descriptions, you should be able to set up, run, and understand the tests provided in this repository.
