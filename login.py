import time

from selenium.webdriver.common.by import By

RETRY = 5
RETRY_TIMEOUT = 120


def login(browser, username, password):
    for retry in range(RETRY):
        print(f'第{retry}次尝试登陆')

        try:
            browser.get('https://selfreport.shu.edu.cn/Default.aspx')
            browser.find_element(By.ID, 'username').send_keys(username)
            browser.find_element(By.ID, 'password').send_keys(password)
            browser.find_element(By.ID, 'submit-button').click()
        except Exception as e:
            print(e)

        browser.get('https://selfreport.shu.edu.cn/DayReport.aspx')
        time.sleep(1)
        if browser.current_url == 'https://selfreport.shu.edu.cn/DayReport.aspx':
            return True

        time.sleep(RETRY_TIMEOUT)

    return False
