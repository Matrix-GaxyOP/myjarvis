from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open("accountinfo.txt",'r') as f:
        info=f.read().split()
        email=info[0]
        password=info[1]
    return email,password
def callthebot(tweet):
    email,password=account_info()
    # tweet="hello world,this is jarvis here..."
    print(tweet)
    options=Options()
    options.add_argument("start-maximized")
    driver=webdriver.Chrome(options=options)

    driver.get("https://twitter.com/login")
    # email_xpath="//input[@name="session[username_or_email]"]"
    # password_xpath="//input[@name="session[password]"]"
    # login_xpath="//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div"
    email_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    password_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'
    time.sleep(4)
    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(login_xpath).click()

    # tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg/g/path'
    message_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    post_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span'
    time.sleep(4)

    # driver.find_element_by_xpath(tweet_xpath).click()
    # time.sleep(0.5)
    driver.find_element_by_xpath(message_xpath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(post_xpath).click()