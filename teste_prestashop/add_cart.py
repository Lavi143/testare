from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait




class TestAddtocart():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_addtocart(self):
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        product_container = self.driver.find_element(By.CLASS_NAME, 'h3')
        product_name = product_container.get_attribute('innerText')
        self.driver.find_element(By.ID,"group_1").click()
        dropdown = self.driver.find_element(By.ID, "group_1")
        dropdown.find_element(By.XPATH,"//option[. = 'XL']").click()
        sleep(3)
        self.driver.find_element(By.ID,"group_2")
        check= self.driver.find_element(By.ID, "group_2")
        check.find_element(By.XPATH, "//input[@title='Black']").click()
        sleep(3)
        self.driver.find_element(By.CLASS_NAME,"bootstrap-touchspin-up").click()
        self.driver.find_element(By.CLASS_NAME,"bootstrap-touchspin-up").click()
        self.driver.find_element(By.CLASS_NAME,"bootstrap-touchspin-up").click()
        self.driver.find_element(By.CLASS_NAME,"bootstrap-touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        element = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
        time.sleep(3)
        element.click()
        assert product_name.lower() in self.driver.page_source.lower()
        time.sleep(30)


