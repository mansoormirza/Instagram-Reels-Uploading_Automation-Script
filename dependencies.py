import undetected_chromedriver as uc

'''
download_dir is the path where chrome will download the tiktok video
'''
download_dir = r'E:\vscode\Selenium\Project\Downloads'


def start_driver():
    options = uc.ChromeOptions()
    prefs = {
        'download.default_directory': download_dir,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option('prefs', prefs)
    options.headless = False 
    options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(options=options)

    return driver