# README.md

## Installation and Setup

### Step 1: Clone the Repository

First, clone the repository to your local machine using Git.

```sh
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
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
python -m unittest functional_tests.py
```

### Step 2: Run UI/UX Tests

To run the UI/UX tests, use the following command:

```sh
python -m unittest uiux_tests.py
```

## Functional Tests

### Test Cases Included

1. **User Login (EPIC 1)**: Tests the login functionality by entering an email and password, clicking the sign-in button, and verifying redirection to the connections page.
2. **User Profile Update (EPIC 1)**: Ensures the user can navigate to the student profile page after logging in.
3. **Main Navigation Menu (EPIC 2)**: Checks the presence and functionality of the main navigation menu on various pages.
4. **Key Features Accessibility (EPIC 2)**: Verifies the presence of key navigation items and the company logo on different pages.
5. **Design Elements Consistency (EPIC 2)**: Ensures that design elements such as font, color, and button style remain consistent across different pages.
6. **Layout Consistency (EPIC 2)**: Checks that the layout structure, including headers, footers, and sidebars, is consistent across different pages.
7. **Login Process Efficiency (EPIC 3)**: Measures the time taken for the login process to ensure it completes within acceptable limits.
8. **Access Search (EPIC 3)**: Ensures that accessing the advanced search page is quick and efficient.
9. **Sign-Up Process Efficiency (EPIC 3)**: Tests the sign-up process by entering all required fields and verifying the redirection to the completion page within an acceptable time.

## UI/UX Tests

### Test Cases Included

1. **Main Navigation Menu (EPIC 2)**: Ensures the main navigation menu is present and functional on various pages.
2. **Key Features Accessibility (EPIC 2)**: Verifies the presence and accessibility of key features such as navigation items and the company logo.
3. **Design Elements Consistency (EPIC 2)**: Checks that design elements like font, color, and button style are consistent across different pages.
4. **Layout Consistency (EPIC 2)**: Ensures the layout structure, including headers, footers, and sidebars, is consistent on different pages.
5. **Form Field Accessibility (EPIC 2)**: Verifies the presence and functionality of form fields on the sign-up page.
6. **Button Visibility and Functionality (EPIC 2)**: Ensures that important buttons like "Save" and "Continue" are visible and functional on the sign-up page.
7. **Accessibility Compliance (EPIC 5)**: Checks for the presence of elements with aria-label and tabindex attributes to ensure accessibility compliance.
8. **Responsive Design (EPIC 5)**: Verifies that the website is responsive and functions correctly at various screen resolutions.

By following these steps and descriptions, you should be able to set up, run, and understand the tests provided in this repository.