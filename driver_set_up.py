import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import random

# Automatically install the appropriate chromedriver
chromedriver_autoinstaller.install()

def set_up_driver():
    
    print("Calling set_up_driver")
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Ensure headless mode is enabled if needed
    chrome_options.add_argument('--no-sandbox')  # Required in some environments, but be cautious
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
    chrome_options.add_argument('--window-size=1920,1080')  # Set window size
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    random_port = random.randint(10000, 11000)
    chrome_options.add_argument(f'--remote-debugging-port={random_port}')  # Prevent DevToolsActivePort error

    print("Selected port = ", random_port)

    # Optionally set a random user-agent
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    ]
    selected_user_agent = random.choice(user_agents_list)
    chrome_options.add_argument(f'user-agent={selected_user_agent}')
    print("Selected user-agent = ", selected_user_agent)

    # Set up the Chrome driver
    service = Service()
    driver = webdriver.Chrome(service=service,options=chrome_options)

    # Stealth browsing
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": selected_user_agent})
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
      "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    # params = { # ignore this for now. Do NOT use this!
    #     "latitude": -36.8588062,
    #     "longitude": 174.3764706,
    #     "accuracy": 100
    # }
    # driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

    # Override the browser's timezone
    # driver.execute_cdp_cmd(
    #     'Emulation.setTimezoneOverride',
    #     {"timezoneId": "Pacific/Auckland"}
    # )

    print("Driver reset done.")

    return driver

# driver = set_up_driver()

# # Automatically install the appropriate chromedriver
# chromedriver_autoinstaller.install()

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# # Set up the Chrome driver
# service = Service()
# driver = webdriver.Chrome(service=service, options=chrome_options)
