from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getDriverInstance(self):
        baseURL = "https://www.coppel.com/"
        # baseURL = "https://prodauth.coppel.com/"
        # baseURL = "https://qaauth.coppel.com/"
        opts = Options()

        # opts.binary_location = "chromedriver.exe"
        opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        opts.add_argument("--user-data-dir=/Users/rene.cortes/Library/Application Support/Google/Chrome/Default")
        opts.add_argument('--disable-blink-features')
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])

        """
        
        opts.add_argument('--profile-directory=Default')
        opts.add_argument("--disable-web-security")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--incognito")
        opts.add_argument('--ignore-certificate-errors')
        
        opts.add_experimental_option('useAutomationExtension', False)
        # Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
        """
        if(self.browser.upper() == "CHROME"):

            # driver = uc.Chrome()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
            driver.delete_all_cookies()
            '''
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
            print(driver.execute_script("return navigator.userAgent;"))
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            })
            '''
            driver.get(baseURL)
        else:
            print("Please enter a valid option")
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

