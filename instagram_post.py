from dependencies import start_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait


def post_video_insta():

    
    driver = start_driver()
    wait = WebDriverWait(driver, 20)

    driver.get('https://www.instagram.com/') 

    input_insta_email = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    input_insta_email.send_keys('YOUR INSTA USERNAME HERE')


    input_insta_pass = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
    )
    input_insta_pass.send_keys('YOUR INSTA PASSWORD HERE')

    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
    )
    login_btn.click()

     # Wait for the desired button to become clickable after login
    desired_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, '_ac8f'))
    )
    desired_button.click()

    time.sleep(2)
    
    driver.find_element(By.XPATH, '//*[contains(text(),"Not Now")]').click()

    time.sleep(3)
   
    driver.find_element(By.XPATH, "//*[contains(text(), 'Create')]").click()
    time.sleep(3)

    button = driver.find_element(By.XPATH, "//button[contains(text(),'Select from computer') and @class=' _acan _acap _acas _aj1- _ap30']")
    button.click()


    '''path where downloaded video is placed'''
    video_path = r'E:\vscode\Selenium\Project\Downloads\video.mp4'

    pyperclip.copy(video_path)
    time.sleep(2) 

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)  
    pyautogui.press('enter')  

    time.sleep(3)


    driver.find_element(By.XPATH, "//button[contains(text(), 'OK') and @class=' _acan _acap _acaq _acas _acav _aj1- _ap30']").click()

    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button/div").click()


    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div").click()

    time.sleep(10)

    driver.close()

    return True

