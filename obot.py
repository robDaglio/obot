#!/usr/bin/env python

from bs4 import BeautifulSoup
from classes import Pause
from functions import get_driver, run
from sys import exit

if __name__ == '__main__':

    sleep_duration = Pause()
    counter = 0

    # Navigate to website
    omegle = "https://www.omegle.com/"
    print(f"[*] Navigating to {omegle}")

    while True:
        driver = get_driver(omegle)
        driver = run(driver, sleep_duration)
        driver.get_screenshot_as_file(f'./screen_shots/run_{counter}.png')
        
        print(f"[*] Iteration {counter} complete | Image: run_{counter}.png")

        counter += 1
        driver.quit()

        sleep_duration.reset()


        
        





