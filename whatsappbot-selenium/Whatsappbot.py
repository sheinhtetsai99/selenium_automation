from lib2to3.pgen2 import driver
from matplotlib.pyplot import text
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Whatsappbot:

    def __init__(self):
        self.WPP_URL = "https://web.whatsapp.com/"
        self.SEARCH_CONTACT = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        self.FIRST_CONTACT = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div'
        self.OPTION_BTN = "(//div[contains(@class, 'message-out')]//div[@class='_22Msk'])[last()]"
        self.OPTION_DELETE = "(//div[contains(@class, '_2oldI')])[last()]"
        self.DIALOG_CLICK = "(//div[@class='_3e9My'])"
        self.OK_BTN = "(//div[contains(@class, '_2Zdgs')])"
        self.DELETE_FOR_EVERYONE = "(//div[contains(@class, '_1zOyO')])"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.WPP_URL)

    def delete_message(self, contato):
        """
         This function will delete the last message sent.
        Parameters
        ----------
        contato : Enter the name of the contact or group
            Enter the name of the contact or group you want to send the message to, you can use a for or while for more than one group or contact
        Returns
        -------
        None.
        """

        # Click on search contact bar
        new_msg_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_CONTACT)))
        new_msg_button.click()
        sleep(1)

        # type contact name into search contact bar
        new_msg_button.send_keys(str(contato))
        sleep(1)

        # click on first contact
        first_contact = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.FIRST_CONTACT)))
        first_contact.click()
        sleep(1)

        # Hover over last message sent by you
        btn_option = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.OPTION_BTN)))
        hover = ActionChains(self.driver).move_to_element(btn_option)
        hover.perform()

        # Click drop down menu on message
        dialog_click = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.DIALOG_CLICK)))
        dialog_click.click()
        sleep(1.5)

        # Then select Delete message option by clicking on it
        btn_option_delete = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.OPTION_DELETE)))
        btn_option_delete.click()
        sleep(1.5)

        # select the delete for everybody option
        delete_for_everybody = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.DELETE_FOR_EVERYONE)))
        delete_for_everybody.click()
        sleep(0.5)

        # click ok in the popup that appeared
        ok_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.OK_BTN)))
        ok_button.click()
        sleep(2)
