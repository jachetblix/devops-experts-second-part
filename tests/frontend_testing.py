import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def frontend_testings_func(user_id):
    get_user_name = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(service=Service("../sets/chromedriver"), options=options)

        test_browser_url = f"http://127.0.0.1:5001/users/get_user_data/{user_id}"

        driver.get(test_browser_url)

        driver.implicitly_wait(10)

        get_user_name = driver.find_element(By.ID, value="user").text
        print(get_user_name)

    except selenium.common.exceptions.WebDriverException as webDriverErr:
        print(webDriverErr)
    except selenium.common.exceptions.NoSuchWindowException as winException:
        print(winException)
    except Exception as exception:
        print(exception)
    finally:
        driver.close()
    return get_user_name

if __name__ == '__main__':
    frontend_testings_func(7)

