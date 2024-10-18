# better method for enter_words function

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def set_max_count(sheet):
    max_counts = {
        "Sequence": 10,
        "Daily": 9,
        "Weekly": 9,
        "Chill": 12,
        "Extreme": 8
    }
    return max_counts.get(sheet, 0)  # Default to 0 if sheet is not found

def enter_words(driver, sheet, words=None):

    url = driver.current_url

    print(url)

    # Define the default words to enter
    default_words = [
        "APPLE", "BANCO", "CRANE", "DRONE", "EAGLE",
        "FLAKE", "GRAPE", "HOUSE", "IVORY", "BRAKE",
        "ADIEU", "STORY"
    ]

    # Use the provided words if available; otherwise, use the default list
    words = words if words is not None else default_words

    # Determine the number of words to enter based on the game type
    # max_count = 10 if sheet == "Sequence" else 9  # old logic - please delete
    max_count = set_max_count(sheet)
    max_attempts = 5  # Maximum number of attempts to avoid infinite loop

    attempt = 0
    while attempt < max_attempts:
        count = 0
        # Iterate through the words and enter them into the game
        for word in words:
            try:
                # Simulate typing each letter
                body = driver.find_element(By.TAG_NAME, 'body')
                for letter in word:
                    body.send_keys(letter)
                    time.sleep(1)  # Small delay to ensure letter is entered

                # Simulate pressing 'Enter' to submit the guess
                body.send_keys(Keys.ENTER)
                print(f"Entered word: {word}")

                # Wait for the result to be processed
                time.sleep(2)  # Adjust timing if needed

                count += 1
                if count >= max_count:
                    break

                # Check if "quordle-extras" is visible
                try:
                    extras = driver.find_element(By.ID, 'quordle-extras')
                    html_content = extras.get_attribute('outerHTML')
                    print("quordle-extras is visible.")
                    print(driver.current_url)
                    return html_content
                except:
                    # "quordle-extras" not visible, continue to next word
                    pass

            except Exception as e:
                print(f"An error occurred while entering word '{word}': {e}")
                continue

        # Increment attempt count and check again
        attempt += 1
        print(f"Attempt {attempt} completed. Checking visibility again.")

    # If the maximum number of attempts is reached, raise an error
    print("Maximum number of attempts reached. 'quordle-extras' not found.")
    return None
