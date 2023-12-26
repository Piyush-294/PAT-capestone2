import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Test_data import data
from Test_locators import locators


class Test_Piyush:

    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_forget_password(self, booting_function):
        self.driver.get(data.TestData().URL)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().forget_password).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username).send_keys(data.TestData.USER_NAME)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().reset_password).click()
        reset_msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().reset_text)
        assert reset_msg.text == "A reset password link has been sent to you via email."
        print(reset_msg.text)

    def test_login(self, booting_function):
        self.driver.get(data.TestData().URL)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username).send_keys(data.TestData.USER_NAME)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().password).send_keys(data.TestData.PASSWORD)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        assert self.driver.title == "OrangeHRM"

    def test_admin_validation(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.TestData().URL)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username).send_keys(data.TestData.USER_NAME)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().password).send_keys(data.TestData.PASSWORD)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value="//ul[@class='oxd-main-menu']/li[1]").click()

        user_management = self.driver.find_element(by=By.XPATH, value=locators.Locators().user_management)
        assert user_management.text == "User Management"
        print(user_management.text)

        job = self.driver.find_element(by=By.XPATH, value=locators.Locators().job)
        assert job.text == "Job"
        print(job.text)

        organisation = self.driver.find_element(by=By.XPATH, value=locators.Locators().organization)
        assert organisation.text == "Organization"
        print(organisation.text)

        qualification = self.driver.find_element(by=By.XPATH, value=locators.Locators().qualification)
        assert qualification.text == "Qualifications"
        print(qualification.text)

        nationalities = self.driver.find_element(by=By.XPATH,
                                                 value="//div[@class='oxd-topbar-body']/nav/ul/li[5]/a").text
        print(nationalities)

        corporate_banking = self.driver.find_element(by=By.XPATH, value=locators.Locators().corporate_banking)
        assert corporate_banking.text == "Corporate Branding"
        print(corporate_banking.text)

        configuration = self.driver.find_element(by=By.XPATH, value=locators.Locators().configuration)
        assert configuration.text == "Configuration"
        print(configuration.text)

    def test_admin_side_pane(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.TestData().URL)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username).send_keys(data.TestData.USER_NAME)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().password).send_keys(data.TestData.PASSWORD)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()

        admin = self.driver.find_element(by=By.XPATH, value=locators.Locators().admin)
        assert admin.text == "Admin"
        print(admin.text)

        PIM = self.driver.find_element(by=By.XPATH, value=locators.Locators().PIM)
        assert PIM.text == "PIM"
        print(PIM.text)

        Leave = self.driver.find_element(by=By.XPATH, value=locators.Locators().Leave)
        assert Leave.text == "Leave"
        print(Leave.text)

        Time = self.driver.find_element(by=By.XPATH, value=locators.Locators().Time)
        assert Time.text == "Time"
        print(Time.text)

        Recruitment = self.driver.find_element(by=By.XPATH, value=locators.Locators().Recruitment)
        assert Recruitment.text == "Recruitment"
        print(Recruitment.text)

        Myinfo = self.driver.find_element(by=By.XPATH, value=locators.Locators().MyInfo)
        assert Myinfo.text == "My Info"
        print(Myinfo.text)

        Performance = self.driver.find_element(by=By.XPATH, value=locators.Locators().Performance)
        assert Performance.text == "Performance"
        print(admin.text)

        Dashboard = self.driver.find_element(by=By.XPATH, value=locators.Locators().Dashboard)
        assert Dashboard.text == "Dashboard"
        print(Dashboard.text)

        Directory = self.driver.find_element(by=By.XPATH, value=locators.Locators().Directory)
        assert Directory.text == "Directory"
        print(Directory.text)

        Maintenance = self.driver.find_element(by=By.XPATH, value=locators.Locators().Maintenance)
        assert Maintenance.text == "Maintenance"
        print(Maintenance.text)

        Buzz = self.driver.find_element(by=By.XPATH, value=locators.Locators().Buzz)
        assert Buzz.text == "Buzz"
        print(Buzz.text)
