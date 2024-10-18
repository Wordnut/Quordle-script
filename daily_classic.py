from driver_set_up import set_up_driver
from quordle_bot import enter_words
from html_scraper import extract_answers
from google_sheets import sheet_append


def daily_answer():
    # driver.quit()
    driver = set_up_driver()

    try: 
        driver.get("https://www.merriam-webster.com/games/quordle/#/")
        
        current_url = driver.current_url

        # Check if the URL contains '?modal-open' and strip it if necessary
        if "?" in current_url:
            print(f"Removing modal from the URL... - {current_url}")
            fixed_url = current_url.split('?')[0]
            driver.get(fixed_url)

        html_content = enter_words(driver, "Daily")
        answers = extract_answers(html_content)
        sheet_append(answers,"Daily")
    
    except Exception as e: 
        # Handle any potential errors and print them
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

    return answers