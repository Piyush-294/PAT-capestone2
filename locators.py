"""Locators"""


class Locators:
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    login_button = "//button[@type='submit']"
    forget_password = '//div[@class="orangehrm-login-forgot"]/p'
    reset_password = "//button[@type='submit']"
    reset_text = "//p[text()='A reset password link has been sent to you via email.']"

    """Admin validation"""
    user_management = "//div[@class='oxd-topbar-body']/nav/ul/li[1]/span"
    job = "//div[@class='oxd-topbar-body']/nav/ul/li[2]/span"
    organization = "//div[@class='oxd-topbar-body']/nav/ul/li[3]/span"
    qualification = "//div[@class='oxd-topbar-body']/nav/ul/li[4]/span"
    nationalities = "//div[@class='oxd-topbar-body']/nav/ul/li[5]/a"
    corporate_banking = "//div[@class='oxd-topbar-body']/nav/ul/li[6]/a"
    configuration = "//div[@class='oxd-topbar-body']/nav/ul/li[7]/span"

    """Side pane validation"""
    admin = "//ul[@class='oxd-main-menu']/li[1]/a/span"
    PIM = "//ul[@class='oxd-main-menu']/li[2]/a/span"
    Leave = "//ul[@class='oxd-main-menu']/li[3]/a/span"
    Time = "//ul[@class='oxd-main-menu']/li[4]/a/span"
    Recruitment = "//ul[@class='oxd-main-menu']/li[5]/a/span"
    MyInfo = "//ul[@class='oxd-main-menu']/li[6]/a/span"
    Performance = "//ul[@class='oxd-main-menu']/li[7]/a/span"
    Dashboard = "//ul[@class='oxd-main-menu']/li[8]/a/span"
    Directory = "//ul[@class='oxd-main-menu']/li[9]/a/span"
    Maintenance = "//ul[@class='oxd-main-menu']/li[10]/a/span"
    Buzz = "//ul[@class='oxd-main-menu']/li[12]/a/span"

