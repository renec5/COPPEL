from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getDriverInstance(self):
        baseURL = "https://www.coppel.com/"
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        opts.add_argument("--user-data-dir=/Users/rene.cortes/Library/Application Support/Google/Chrome/Default")
        opts.add_argument('--profile-directory=Default')
        opts.add_argument("--disable-web-security")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--incognito")
        opts.add_argument('--ignore-certificate-errors')
        # Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
        if(self.browser.upper() == "CHROME"):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
            driver.delete_all_cookies()
            driver.get(baseURL)
        else:
            print("Please enter a valid option")
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

