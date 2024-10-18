from driver_set_up import set_up_driver
from quordle_bot import enter_words
from html_scraper import extract_answers

def extreme_answer():

    try:

        driver = set_up_driver()
        driver.get("https://www.merriam-webster.com/games/quordle/#/extreme")

        current_url = driver.current_url

        # Check if the URL contains '?modal-open' and strip it if necessary
        if "?" in current_url:
            print(f"Removing modal from the URL... - {current_url}")
            fixed_url = current_url.split('?')[0]
            driver.get(fixed_url)

        html_content = enter_words(driver, "Extreme")
        answers = extract_answers(html_content)

    except Exception as e: 
        print(f"An error occurred: {e}")

    return answers
