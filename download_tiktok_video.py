from dependencies import start_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait



def rename():

    '''path where tiktok video is downloaded and can be renamed'''
    
    directory = r'E:\vscode\Selenium\Project\Downloads'
    
    new_file_name = 'video.mp4'
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if files:

        first_file = files[0]
        old_file_path = os.path.join(directory, first_file)
        new_file_path = os.path.join(directory, new_file_name)

        if not os.path.exists(new_file_path):
            os.rename(old_file_path, new_file_path)
            print(f"{first_file} has been renamed to {new_file_name}")
        else:
            print("A file named 'video.mp4' already exists. Please handle this case!")
    else:
        print("No files found in the directory.")



def download_tiktok_video(video_url):

    cleaned_video_url = video_url.split('?')[0]
    file_path = './downloaded_url.txt'

    with open(file_path, 'r') as file:
        saved_urls = file.readlines()
        saved_urls = [url.strip() for url in saved_urls]

    if cleaned_video_url in saved_urls:
        print("The URL is already in the file.")
        return True
    else:
        print("The URL is not in the file.")
        with open(file_path, 'a') as file:
            file.write(cleaned_video_url + '\n')
        print("URL has been added to the file.")

        driver = start_driver()
        wait = WebDriverWait(driver, 20)
 
        driver.get("https://ssstik.io/")

        input_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main_page_text"]'))
        )

        input_element.send_keys(video_url)
        time.sleep(2)
        input_element.send_keys(Keys.RETURN)

        download_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dl_btns"]/a[1]'))
        )

        download_url = download_button.get_attribute("href")
        print(f"Download URL: {download_url}")  

        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(download_url) 
        
        time.sleep(4)

        driver.close()

        time.sleep(5)
        rename()

        return False

