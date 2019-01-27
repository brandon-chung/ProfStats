from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True
profile = webdriver.ChromeOptions()

def averagePassing(firstName, lastName):
    browser = webdriver.Chrome('C:/Users/Andrew/Desktop/chromedriver.exe', options = opts)
    url = 'https://slacknotes.com/professors?first_name=' + firstName.lower() + '&last_name=' + lastName.lower()
    browser.get(url)
    time.sleep(1)
    average = ((str(browser.page_source.encode("utf-8")).partition('<div class="class-header-info center" data-reactid=".0.0.1.1.0.0"><h2 class="center" data-reactid=".0.0.1.1.0.0.0">')[2]).partition('</h2><div class="class-header-label center" data-reactid=".0.0.1.1.0.0.1">aggregated average')[0])
    passing = ((str(browser.page_source.encode("utf-8")).partition('<div class="class-header-info center" data-reactid=".0.0.1.1.1.0"><h2 class="center" data-reactid=".0.0.1.1.1.0.0">')[2]).partition('</h2><div class="class-header-label center" data-reactid=".0.0.1.1.1.0.1">students pass')[0])
    print(average)
    print(passing)
    return average, passing

averagePassing('gregor', 'kiczales')