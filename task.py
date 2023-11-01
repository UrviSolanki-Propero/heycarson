
"""Template robot with Python."""

from time import sleep
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

web = browser.get(
    "https://www.heycarson.com/task-catalog-browse/task-types/development")


def open_task_card():
    sleep(5)

    # get number of elements
    card_path = f'//*[@id="page-results"]/div[1]/div/div/div/div/div[1]/a/h2'
    card = browser.find_elements("xpath", card_path)
    tag = len(card)

    # set loop for all elements
    for var in range(1, tag+1):

        sleep(3)
        ele_path = f'//*[@id="page-results"]/div[1]/div/div[{var}]/div/div/div[1]/a/h2'
        ele_card = browser.find_element("xpath", ele_path)
        ele_card.is_displayed()
        ele_card.click()
        print(var, "card")
        # sleep(2)

        # getting name of the card
        path = f'//*[@id="root"]/div[4]/div[1]/div[2]/div/div[1]/h1'
        name = browser.find_element(By.XPATH, path).text
        name1 = [name]
        print(var, "card")
        print(name1)
        sleep(2)

        # getting summary of the card
        attrib_s = f'//*[@id="root"]/div[4]/div[1]/div[1]/div[4]/div[2]'
        sa = browser.find_element(
            By.XPATH, attrib_s).text
        sa1 = [sa]
        print(var, "summary")
        print(sa1)

        # updating data into excel sheet
        workbook(name1, sa1)
        sleep(3)
        browser.back()
        # sleep(5)


def workbook(heading, list):

    df1 = pd.read_excel(r'output/data.xlsx', index_col=[0])
    df2 = pd.DataFrame(zip(heading, list), columns=[
        'Tasks cards', 'summary'])
    data = pd.concat([df1, df2])
    data.to_excel(r'output/data.xlsx')


def pages():

    next = browser.find_element(By.LINK_TEXT, 'Next')
    # sleep(10)
    while next.is_displayed():
        sleep(3)
        if next.is_displayed():
            open_task_card()
            sleep(10)
            next = browser.find_element(By.LINK_TEXT, 'Next')
            next.click()
            print("page", "copied")
            sleep(10)

        else:
            break


def main():
    try:
        pages()

    finally:
        browser.close()


if __name__ == "__main__":
    main()
