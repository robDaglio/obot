#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sys import exit

SYSTEM_MESSAGES = {
    'importing_message': '[*] Importing message...',
    'initializing_driver': '[*] Initializing chrome driver...',
    'starting_chat': '[*] Starting chat...',
    'sending_message': '[*] Sending message...',
    'importing_interests': '[*] Importing interests...',
}

def get_message():

    print(SYSTEM_MESSAGES['importing_message'])

    try:
        with open('./message.txt') as message:
            m = "".join(message.readlines())
    except:
        print("[x] Unable to read file...")
        exit(0)
    else:
        message.close()
        return m

def get_interests():

    print(SYSTEM_MESSAGES['importing_interests'])

    try:
        with open('./interests.txt') as interests:
            i = interests.readlines()
    except:
        print("[x] Unable to read file...")
        exit(0)
    else:
        interests.close()
        return [x.strip("\n") for x in i]
        
def get_driver(url):

    print(SYSTEM_MESSAGES['initializing_driver'])

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    return driver

def enter_interests(driver):

    interests = get_interests()

    # Enter interests
    interests_text_input = driver.find_element_by_class_name('newtopicinput')
    
    for i in interests:
        interests_text_input.send_keys(i)
    
    return driver

def start_chat(driver):

    # Click text chat button
    text_chat_button = driver.find_element_by_id('textbtn')
    text_chat_button.click()

    return driver

def send_message(driver, message, p):

    print(SYSTEM_MESSAGES['sending_message'])

    # find text area and type greeting
    text_area_entry = driver.find_element_by_class_name("chatmsg")
    text_area_entry.send_keys(message)
    text_area_entry.send_keys(Keys.ENTER)

    p.small()
    return driver

def run(driver, p):

    message = get_message()

    driver = enter_interests(driver)
    p.small()

    print(SYSTEM_MESSAGES['starting_chat'])

    driver = start_chat(driver)
    p.medium()

    driver = send_message(driver, message, p)

    return driver

