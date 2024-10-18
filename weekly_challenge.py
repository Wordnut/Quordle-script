from driver_set_up import set_up_driver
from quordle_bot import enter_words
from html_scraper import extract_answers
from daily_classic import daily_answer
# from google_sheets_append import g_sheets_quordle
import time

def weekly_answer():
    daily_url = "https://www.merriam-webster.com/games/quordle/#/"

    daily_answers = daily_answer()

    time.sleep(10)

    driver = set_up_driver()
    print("Driver has been reset.")
    driver.get(daily_url)

    current_url = driver.current_url

    # Check if the URL contains '?modal-open' and strip it if necessary
    if "?" in current_url:
        print(f"Removing modal from the URL... - {current_url}")
        fixed_url = current_url.split('?')[0]
        driver.get(fixed_url)

    print("Entering today's answers into today's grid")
    html_content = enter_words(driver, "Daily", daily_answers)

    weekly_url = "https://www.merriam-webster.com/games/quordle/#/weekly"

    driver.get(weekly_url)
    time.sleep(10)
    current_url = driver.current_url

    print("Checking URL...")
    print(current_url)

    if current_url != weekly_url:
        print("Updating driver URL again...")
        print("Trying to use execute_script")
        driver.execute_script(f"window.location.href = '{weekly_url}';")

        driver.get(weekly_url)
        time.sleep(10)

        print("Checking weekly URL once again...")
        current_url = driver.current_url
        print(current_url)

    # Check if the URL contains '?modal-open' and strip it if necessary
    if "?" in current_url:
        print(f"Removing modal from the URL... - {current_url}")
        fixed_url = current_url.split('?')[0]
        driver.get(fixed_url)

    print("One last check for URL before checking for finding weekly answers: ", driver.current_url)
    print("Now finding weekly answers...")
    html_content = enter_words(driver, "Weekly")
    answers = extract_answers(html_content)
    print(answers)
    # g_sheets_quordle(answers,"Weekly")

    # driver.quit()

    return answers