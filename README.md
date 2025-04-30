# Google Form Automation Tool

Created by **Gabriel Wambura (Gabriel Jumanne)**

A powerful and flexible automation tool designed to streamline the submission of Google Forms. Leveraging the power of Selenium WebDriver, this tool intelligently detects form elements, supports multi-page forms, and automates form submissions with randomized responses. Whether you're testing, collecting data, or automating repetitive tasks, this tool is an invaluable resource.

---

![Google Forms Automation](https://img.shields.io/badge/Automation-Google%20Forms-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![Selenium](https://img.shields.io/badge/Framework-Selenium-orange)

---

## Key Features

- **Multi-Page Form Support**: Seamlessly handles forms with multiple sections or pages.
- **Intelligent Question Detection**: Uses XPath to locate form elements, even if IDs are dynamically generated.
- **Randomized Response Submission**: Fills out forms with random answers based on predefined options for testing or automated data collection.
- **Retry Mechanism**: Recovers from errors automatically and retries to ensure form completion.
- **Anti-Detection Measures**: Incorporates browser fingerprinting countermeasures to avoid detection and blocking.
- **Detailed Logging**: Generates comprehensive logs with timestamps and error details for easy debugging.
- **Configurable Submissions**: Adjust the number of submissions and timing intervals to suit your requirements.

---

## Requirements

To run this tool, ensure you have the following prerequisites:

- **Python**: Version 3.6 or higher
- **Chrome Browser**: The latest version of Google Chrome
- **ChromeDriver**: Automatically managed by the script using `webdriver-manager`
- **Internet Connection**

---

## Installation

1. **Clone the Repository**  
   Open a terminal and execute the following command:
   ```bash
   git clone https://github.com/gabrieljumanne/Google_form_automation.git
   cd Google_form_automation
   ```

2. **Install Required Packages**  
   Install the necessary dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Step 1: Configure the Form URL  
Set the target Google Form URL in the script by modifying the `FORM_URL` variable:
```python
FORM_URL = "https://forms.gle/example_form_url"
```

### Step 2: Customize Questions and Answers  
Define the questions and corresponding answer options in the `QUESTIONS` dictionary:
```python
QUESTIONS = {
    "Question 1 Text": ["Option 1", "Option 2", "Option 3"],
    "Question 2 Text": ["Option A", "Option B", "Option C"]
}
```

### Step 3: Run the Script  
Execute the program in your terminal:
```bash
python main.py or python3 mainfilename.py
```

---

## Configuration Options

You can customize the tool's behavior by modifying these parameters in the `main()` function:

- **Number of Submissions**: Control how many times the form is submitted.
- **Timing**: Adjust the interval between submissions to avoid detection.
- **Headless Mode**: Enable or disable headless mode in the ChromeDriver settings.
- **Window Size**: Change the browser window dimensions for better compatibility.
- **Chrome Profiles**: Use an existing Chrome profile for more advanced configurations.

---

## Troubleshooting

- **Form Detection Issues**: The tool saves screenshots of errors in the root directory for easier debugging.
- **XPath Errors**: If form elements are not detected, inspect the form structure and update the XPath selectors in the script.
- **Button Detection Failures**: The script includes multiple fallback methods for locating buttons, but you may need to adjust these if the form structure changes.

---

## Advanced Features

- **Google Account Integration**: The script includes commented-out code for logging into a Google account. Uncomment and configure this section if required.
- **Multi-Pass Question Answering**: Ensures all questions are completed by revisiting partially filled forms.
- **Error Recovery**: Implements robust mechanisms to recover from unexpected browser or form issues.

---

## Example Workflow

1. Start by setting up the script and providing the form URL.
2. Define the questions and predefined answers in the script.
3. Run the script and observe the logs for details about the submission process.
4. Review screenshots and logs if any issues arise.

---

## Contribution

Contributions, suggestions, and bug reports are welcome! Feel free to open an issue or submit a pull request to enhance the tool.

---



---

With this tool, automating Google Form submissions has never been easier. Whether you're a developer, tester, or researcher, the **Google Form Automation Tool** will save you time and effort while providing powerful and reliable automation capabilities.
JavaScript execution fallbacks for complex form interactions
License
This project is available for personal and educational use.

© 2025 Gabriel Wambura (Gabriel Jumanne)
