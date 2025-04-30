from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('form_automation')

# 1) Setup Chrome options
chrome_opts = Options()
#chrome_opts.add_argument("--headless")
#Add these lines to use your existing Chrome profile
# user_data_dir = "/home/i-castorosa-098/.config/google-chrome"  # Path to Chrome user data
# profile_directory = "Default"  # Usually "Default" or "Profile 1", "Profile 2", etc.
# chrome_opts.add_argument(f"user-data-dir={user_data_dir}")
# chrome_opts.add_argument(f"profile-directory={profile_directory}")

chrome_opts.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_opts.add_experimental_option("useAutomationExtension", False)
chrome_opts.add_argument("--disable-blink-features=AutomationControlled")
chrome_opts.add_argument("--window-size=1920,1080")
chrome_opts.add_argument("--disable-gpu")
chrome_opts.add_argument("--no-sandbox")
chrome_opts.add_argument("--disable-dev-shm-usage")

# Add random user-agent
user_agents = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
chrome_opts.add_argument(f"user-agent={random.choice(user_agents)}")

# Initialize webdriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_opts
)

# Form URL
FORM_URL = ""

# 2) sample questions with there possible ans
QUESTIONS  = {
    "What is your profession?": [
        "Student",
        "Teacher",
        "Administrator",
        "Other (please specify)"
    ],
    "Have you ever used a biometric attendance system before?": [
        "Yes",
        "No"
    ],
    "If yes, what kind of system did you use?": [
        "Fingerprint-based",
        "Facial recognition",
        "Card-based",
        "Other (please specify)"
    ],
    "How do you currently track attendance at your institution?": [
        "Manual attendance sheets",
        "Digital attendance register",
        "Biometric systems",
        "Other (please specify)"
    ],
    "Do you feel the current attendance system is accurate and reliable?": [
        "Yes",
        "No"
    ],
    "What challenges do you face with the current attendance tracking method?": [
        "Inaccurate records",
        "Time-consuming process",
        "Lack of security",
        "Inability to scale",
        "Other (please specify)"
    ],
    "Would you be interested in using an AI-based attendance system that uses facial recognition technology?": [
        "Yes",
        "No"
    ],
    "What features do you think are most important in an AI-based attendance system?": [
        "Real-time face recognition",
        "Automatic attendance logging",
        "Mobile accessibility",
        "Data security",
        "User-friendly interface"
    ],
    "How do you currently manage and monitor attendance records?": [
        "Manually recorded",
        "Digital records",
        "Through a third-party software",
        "Not monitored regularly"
    ],
    "How often do you have access to a computer or mobile device for managing attendance?": [
        "Daily",
        "Weekly",
        "Rarely",
        "Never"
    ]
}

def wait_for_page_load():
    """Wait for the form to fully load with better error handling"""
    try:
        # Try multiple possible form elements
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 
                "form, div[role='form'], div.freebirdFormviewerViewFormCard"))
        )
        logger.info("Form page loaded successfully")
        time.sleep(random.uniform(1.0, 2.5))
        return True
    except Exception as e:
        logger.error(f"Error waiting for page to load: {str(e)}")
        # Take a screenshot for debugging
        try:
            driver.save_screenshot("page_load_error.png")
            logger.info("Screenshot saved as page_load_error.png")
        except:
            pass
        return False

def find_question_container(question_text):
    """Find the container div for a specific question"""
    try:
        # Try exact match first
        container = driver.find_element(
            By.XPATH,
            f"//div[contains(., '{question_text}') and .//div[@role='listitem']]"
        )
        return container
    except:
        # Try partial match if exact match fails
        try:
            # Look for parts of the question text
            words = question_text.split()
            if len(words) > 3:
                search_text = ' '.join(words[:3])  # Use first 3 words
                containers = driver.find_elements(
                    By.XPATH,
                    f"//div[contains(., '{search_text}') and .//div[@role='listitem']]"
                )
                if containers:
                    return containers[0]
            
            # If still not found, get all question containers and return the one that seems most relevant
            all_containers = driver.find_elements(
                By.XPATH,
                "//div[.//div[@role='listitem']]"
            )
            if all_containers:
                return all_containers[0]  # Return the first question container
            
            raise Exception("Could not find question container")
        except Exception as e:
            logger.error(f"Error finding question container for '{question_text}': {str(e)}")
            return None

def select_radio_option(container, option_text):
    """Select a radio button option within a question container"""
    try:
        # Try to find the option by its text
        radio_options = container.find_elements(
            By.XPATH,
            ".//div[@role='radio']"
        )
        
        # Get all label texts
        option_labels = []
        for option in radio_options:
            try:
                label = option.find_element(By.XPATH, ".//div[contains(@class, 'docssharedWizToggleLabeledContainer')]").text
                option_labels.append((option, label))
            except:
                continue
        
        # Try to match option text
        for option, label in option_labels:
            if option_text.lower() in label.lower():
                option.click()
                time.sleep(random.uniform(0.3, 0.7))  # Small delay after click
                return True
        
        # If no match found, pick a random option
        if radio_options:
            random.choice(radio_options).click()
            time.sleep(random.uniform(0.3, 0.7))
            return True
        
        return False
    except Exception as e:
        logger.error(f"Error selecting option '{option_text}': {str(e)}")
        return False

def submit_form():
    """Click the submit button with enhanced button detection"""
    try:
        # Look for the Submit button using multiple possible selectors
        # submit_xpaths = [
        #     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span',
            
        #  ]
        
        submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'
        
        # for xpath in submit_xpaths:
        #     submit_buttons = driver.find_elements(By.XPATH, xpath)
        #     if submit_buttons:
        #         # Try scrolling to the button first
        #         driver.execute_script("arguments[0].scrollIntoView(true);", submit_buttons[0])
        #         time.sleep(0.5)
        #         submit_buttons[0].click()
        #         logger.info("Form submitted successfully")
        #         time.sleep(random.uniform(2.0, 4.0))
        #         return True
        
        submit_button = driver.find_element(By.XPATH, submit_xpath)
        if submit_button:
            # Try scrolling to the button first
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(0.5)
            submit_button.click()
            logger.info("Form submitted successfully")
            time.sleep(random.uniform(2.0, 4.0))
            return True
            
        else:
            # Try using JavaScript as a last resort
            logger.info("Trying JavaScript click for submit")
            driver.execute_script(
                "document.querySelector('div[role=\"button\"]').click();"
            )
            time.sleep(2)
            return True
    except Exception as e:
        logger.error(f"Error submitting form: {str(e)}")
        return False
    
    
def do_one_submission():
    """Complete one form submission with retries"""
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        try:
            logger.info(f"Submission attempt {attempt}/{max_attempts}")
            driver.get(FORM_URL)
            
            if not wait_for_page_load():
                logger.warning(f"Page load failed on attempt {attempt}, retrying...")
                continue
                
            # Track answers and unanswered questions
            answers = {}
            unanswered_questions = []
            
            # First pass - try to answer all questions
            for question, options in QUESTIONS.items():
                container = find_question_container(question)
                if not container:
                    unanswered_questions.append(question)
                    logger.warning(f"Could not find container for: {question}")
                    continue
                
                selected_option = random.choice(options)
                answers[question] = selected_option
                
                if not select_radio_option(container, selected_option):
                    unanswered_questions.append(question)
                    logger.warning(f"Failed to select option for: {question}")
            
            # Second pass - retry unanswered questions
            if unanswered_questions:
                logger.info(f"Retrying {len(unanswered_questions)} unanswered questions")
                
                for question in unanswered_questions[:]:  # Work on a copy
                    container = find_question_container(question)
                    if container:
                        selected_option = random.choice(QUESTIONS[question])
                        answers[question] = selected_option
                        
                        if select_radio_option(container, selected_option):
                            unanswered_questions.remove(question)
                            logger.info(f"Successfully answered on retry: {question}")
            
            # Check if all questions are answered
            if unanswered_questions:
                logger.warning(f"Still have {len(unanswered_questions)} unanswered questions")
                if attempt < max_attempts:
                    continue  # Try the entire form again
            else:
                logger.info("✅ All questions have been answered")
            
            # Submit the form
            if submit_form():
                logger.info(f"✅ Submission successful: {answers}")
                return True
            else:
                logger.error(f"❌ Submission failed on attempt {attempt}")
                if attempt < max_attempts:
                    time.sleep(2)
                
        except Exception as e:
            logger.error(f"❌ Error during submission attempt {attempt}: {str(e)}")
            if attempt < max_attempts:
                time.sleep(2)
    
    return False

# def sign_in_explicitly():
#     """Sign in to Google explicitly before submitting forms"""
#     try:
#         logger.info("Explicitly signing in to Google...")
#         driver.get("https://accounts.google.com")
#         time.sleep(5)  # Give time to check if already signed in
        
#         # Check if we need to sign in
#         if "myaccount.google.com" not in driver.current_url:
#             logger.info("Need to sign in - please enter credentials manually")
#             # Wait for manual sign-in
#             input("Press Enter after you've signed in to your Google account...")
#         else:
#             logger.info("Already signed in to Google")
            
#         return True
#     except Exception as e:
#         logger.error(f"Error during explicit sign-in: {str(e)}")
#         return False


    
    # Rest of your main function...
def main():
    """Main function to run multiple submissions"""
    # sign_in_explicitly()
    NUM_SUBMISSIONS = 1    # Number of submissions
    MIN_DELAY = 5               # Minimum seconds between submissions
    MAX_DELAY = 15              # Maximum seconds between submissions
    
    successful = 0
    
    try:
        logger.info(f"Starting form automation: {NUM_SUBMISSIONS} submissions planned")
        
        for i in range(NUM_SUBMISSIONS):
            logger.info(f"Starting submission {i+1}/{NUM_SUBMISSIONS}")
            
            if do_one_submission():
                successful += 1
            
            # Add random delay between submissions to appear more human-like
            if i < NUM_SUBMISSIONS - 1:  # Don't wait after the last submission
                delay = random.uniform(MIN_DELAY, MAX_DELAY)
                logger.info(f"Waiting {delay:.2f} seconds before next submission...")
                time.sleep(delay)
                
        logger.info(f"Form automation completed: {successful} successful out of {NUM_SUBMISSIONS} attempts")
    
    finally:
        # Always quit the driver
        driver.quit()

if __name__ == "__main__":
    main()

#https://docs.google.com/forms/d/e/1FAIpQLSdglCU2izjBj_-X9asnjguCQEtnY64e1PKrGi-76q0bw0CRZg/viewform?usp=pp_url&entry.927270234=Parent/Guardian&entry.2098028729=Yes&entry.472046235=Community-based+programs&entry.1253466392=Local+clinics+or+healthcare+centers&entry.1711734882=No&entry.2023486554=Lack+of+knowledge+about+dietary+diversity&entry.362848299=Yes&entry.1359096553=Multilingual+support&entry.1450209950=Regular+visits+to+healthcare+centers&entry.1387712863=Occasionally

#&entry.22322330=Teacher&entry.145887383=Yes&entry.1653129520=Fingerprint-based&entry.1129766213=Manual+attendance+sheets&entry.2104621186=Yes&entry.2013631848=Inaccurate+records&entry.199592298=Yes&entry.854302400=Real-time+face+recognition&entry.1492864480=Manually+recorded&entry.1902448988=Daily