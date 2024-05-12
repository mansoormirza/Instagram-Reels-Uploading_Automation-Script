from get_tiktok_video import tiktok_video
from instagram_post import post_video_insta
from download_tiktok_video import download_tiktok_video
import time

def main():

    url = tiktok_video()
    result = download_tiktok_video(url)
    if result is True:
        print("Video has already been posted")
    else:
        status = post_video_insta()
        if status:
            print("Instagram video posted..")
            time.sleep(5)

if __name__ == "__main__":
    while True: 
        main()
        input("Press Enter to exit and close the browser or script will run again...")
        time.sleep(10)

      
