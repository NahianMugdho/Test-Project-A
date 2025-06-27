import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestA(BaseClass):
    def test_e2e(self):
        driver= self.driver
        homePage = HomePage(driver)
        homePage.shopItems().click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        #//div[@class='card h-100']/div/h4/a
        for product in products:
            productName=product.find_element(By.XPATH, ".//div/h4/a").text
            if productName == "Blackberry":
                #//div[@class='card h-100']/div[2]/button
                product.find_element(By.XPATH, "div[2]/button").click()
        driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # //button[normalize-space()='Checkout']
        #//button[@class='btn btn-success']
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        #//input[@id='country']
        driver.find_element(By.ID, "country").send_keys("bang")
        wait = WebDriverWait(driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Bangladesh')))
        driver.find_element(By.LINK_TEXT, "Bangladesh").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        print(driver.find_element(By.CLASS_NAME, "alert-success").text)
        driver.get_screenshot_as_file("screenshot.png")
