import pytest
import pdb # pdb.set_trace()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import allure
from allure_commons.types import AttachmentType

@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    @allure.feature('Open page')
    @allure.story('open page')
    @allure.severity('blocker')
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//*[@name='li1']").click()
        self.driver.find_element(By.XPATH, "//*[@name='li2']").click()

        title = "Sample page1 - lambdatest.com"
        with allure.step("Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name='Open page', attachment_type=AttachmentType.PNG)
        assert title == self.driver.title

    @allure.feature('Add text')
    @allure.story('check adding text')
    @allure.severity('critical') # normal minor trivial
    def test_add_text(self):
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = self.driver.find_element(By.XPATH, "//*[@id='sampletodotext']")
        email_text_field.send_keys(sample_text)
        self.driver.find_element(By.XPATH, "//*[@id='addbutton']").click()

        output_str = self.driver.find_element(By.XPATH, "//*[@class='list-unstyled']/li[6]").text
        sys.stderr.write(output_str)
        assert output_str == sample_text








# @pytest.mark.usefixtures("chrome_driver_init")
# class BasicTest:
#     pass
#
#
# class Test_URL(BasicTest):
#     def test_open_url(self):
#         self.driver.get('https://www.google.com/')
#         self.driver.maximize_window()
#         title = "Google"
#         assert title == self.driver.title
#
#         search_text = "LambdaTest"
#         search_box = self.driver.find_element(By.XPATH, "//textarea[@name='q']")
#         search_box.send_keys(search_text)
#         search_box.submit()

        # search_box.send_keys(Keys.ARROW_DOWN)
        # search_box.send_keys(Keys.ARROW_UP)
        # search_box.send_keys(Keys.RETURN)