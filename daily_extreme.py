from driver_set_up import set_up_driver
from quordle_bot import enter_words
from html_scraper import extract_answers
# from google_sheets_append import g_sheets_quordle


def extreme_answer():

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
    # g_sheets_quordle(answers,"Extreme")
    # driver.quit()

    return answers
