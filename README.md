Google Form Automation Tool
Created by Gabriel Wambura (Gabriel Jumanne)
A powerful, flexible automation tool for submitting Google Forms with intelligent form detection and multi-page support. This tool uses Selenium WebDriver to automate form submissions with randomized responses.

<img alt="Google Forms Automation" src="https://img.shields.io/badge/Automation-Google Forms-blue">
<img alt="Python" src="https://img.shields.io/badge/Language-Python-green">
<img alt="Selenium" src="https://img.shields.io/badge/Framework-Selenium-orange">
Features
Multi-page form support: Handles forms with multiple pages/sections
Intelligent question detection: Uses XPath to find form elements even with dynamic IDs
Randomized responses: Submits random answers from predefined options
Retry mechanism: Automatically attempts to recover from errors
Anti-detection measures: Implements browser fingerprinting countermeasures
Detailed logging: Comprehensive logging with timestamps and error tracking
Configurable submissions: Control the number and timing of form submissions
Requirements
Python 3.6+
Chrome browser
ChromeDriver (automatically managed)
Internet connection
Installation
Clone this repository:
Install required packages:
Usage
Configure the form URL in the script by setting the FORM_URL variable:
Customize the questions and possible answers in the QUESTIONS dictionary:
Run the script:
Configuration Options
Adjust these parameters in the main() function to customize behavior:

Additional options in the Chrome settings section:

Enable/disable headless mode
Change window size
Configure existing Chrome profiles
Troubleshooting
Form detection issues: The script saves screenshots of errors in the root directory
XPath errors: Check the form structure and update the XPath selectors if needed
Button detection failures: The script includes multiple fallback methods for finding buttons
Advanced Features
Google account integration (commented out in the code)
Multi-pass question answering to ensure all questions are completed
JavaScript execution fallbacks for complex form interactions
License
This project is available for personal and educational use.

© 2025 Gabriel Wambura (Gabriel Jumanne)
