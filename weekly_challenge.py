from driver_set_up import set_up_driver
from quordle_bot import enter_words
from html_scraper import extract_answers
from daily_classic import daily_answer
import time
from datetime import datetime

def weekly_answer():
    
    try:
            
        daily_url = "https://www.merriam-webster.com/games/quordle/#/"

        daily_answers = daily_answer()

        time.sleep(5)

        driver = set_up_driver()
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Driver has been reset.")
        driver.get(daily_url)

        current_url = driver.current_url

        # Check if the URL contains '?modal-open' and strip it if necessary
        if "?" in current_url:
            print(f"Removing modal from the URL... - {current_url}")
            fixed_url = current_url.split('?')[0]
            driver.get(fixed_url)

        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Entering today's answers into today's grid")
        html_content = enter_words(driver, "Daily", daily_answers)

        weekly_url = "https://www.merriam-webster.com/games/quordle/#/weekly"

        driver.get(weekly_url)
        time.sleep(5)
        current_url = driver.current_url

        if current_url != weekly_url:
            print("Updating driver URL again...")
            driver.execute_script(f"window.location.href = '{weekly_url}';")

            driver.get(weekly_url)
            time.sleep(10)

            current_url = driver.current_url

        # Check if the URL contains '?modal-open' and strip it if necessary
        if "?" in current_url:
            print(f"Removing modal from the URL... - {current_url}")
            fixed_url = current_url.split('?')[0]
            driver.get(fixed_url)

        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Now finding weekly answers on {driver.current_url}")
        html_content = enter_words(driver, "Weekly")
        answers = extract_answers(html_content)

    except Exception as e: 
        print(f"An error occurred: {e}")

    return answers