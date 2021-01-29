import logging
from selenium import webdriver
import time
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format = '%(asctime)s - %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.INFO)


class GoogleMeetBot():
    def __init__(self, meet_url):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--disable-infobars")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--window-size=800,800")
        #  chromeOptions.add_argument("--window-size=1920,1080")
        #  to make the bot headless, uncomment the below line
        # chromeOptions.add_argument('--headless')
        chromeOptions.add_argument("--incognito")
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                        "profile.default_content_setting_values.media_stream_camera": 2,
                                                        "profile.default_content_setting_values.notifications": 2
                                                        })
        chromeOptions.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 1})
        chromeOptions.add_argument("user-agent=User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        self.driver = webdriver.Chrome('./chromedriver', options = chromeOptions)
        self.google_login_url = "https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        self.email_input_xpath = "//*[@id='identifierId']"
        self.pass_input_xpath = "//*[@id='password']/div[1]/div/div[1]/input"
        self.next_button_1_xpath = "//*[@id='identifierNext']/div/button/div[2]"
        self.next_button_2_xpath = "//*[@id='passwordNext']/div/button/div[2]"
        self.meet_url = meet_url
        self.dismiss_btn_xpath = "//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span"
        self.ask_to_join_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span"

    def google_login(self, email_id, password):
        self.driver.get(self.google_login_url)
        logging.info("[Gmail Login]")
        logging.info("[Entering Gmail Address]")
        email_input_field = self.driver.find_element_by_xpath(self.email_input_xpath)
        email_input_field.send_keys(email_id)
        next_btn_1 = self.driver.find_element_by_xpath(self.next_button_1_xpath)
        next_btn_1.click()
        time.sleep(2)
        logging.info("[Entering Password]")
        password_input_field = self.driver.find_element_by_xpath(self.pass_input_xpath)
        password_input_field.send_keys(password)
        logging.info("[Logging in to Google]")
        next_btn_2 = self.driver.find_element_by_xpath(self.next_button_2_xpath)
        next_btn_2.click()
        logging.info("[Google Login Successful]")
        time.sleep(2)

    def join_meeting(self):
        self.driver.get(self.meet_url)
        logging.info("[Opening Google Meet Link]")
        time.sleep(2)
        dismiss_btn = self.driver.find_element_by_xpath(self.dismiss_btn_xpath)
        dismiss_btn.click()
        time.sleep(2)
        ask_to_join_btn = self.driver.find_element_by_xpath(self.ask_to_join_xpath)
        ask_to_join_btn.click()
        logging.info("[Joined the meeting]")

    def leave_meeting(self):
        self.driver.refresh()
        time.sleep(5)
        self.driver.close()