import time
from selenium import webdriver

def scrapeBalance(cosmosWalletAddress):

    #Your choice of webdriver.
    #Here using Firefox webdriver.
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    browser = webdriver.Firefox(
        executable_path="Your Firefox Web Driver Path",
        options=op)

    url =  "https://likecoin.bigdipper.live/account/" + cosmosWalletAddress

    browser.get(url)

    time.sleep(3)

    balance = browser.find_elements_by_xpath("//div[@class='value text-right col-8']")[5].text

    browser.quit()

    return balance
