from dependencies import start_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait


def tiktok_video():

    driver = start_driver()
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.tiktok.com/@khaby.lame")

    # login_button = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div/div/div[3]/div/div[2]/div'))
    # )
    # login_button.click()

    three_column_container = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-1qb12g8-DivThreeColumnContainer.eegew6e2'))
    )

    time.sleep(3)

    item_containers = three_column_container.find_element(By.CLASS_NAME, 'css-x6y88p-DivItemContainerV2.e19c29qe8')
    item_containers.click()

    p_element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/p'))
    )

    video_url = p_element.text.strip()
    print(f"Video URL: {video_url}")
    driver.close()

    return video_url