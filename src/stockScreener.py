from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

class Screener:
    def __init__(self) -> None:
        self.URL = "https://www.tradingview.com/chart/npVh6Wmg/"
        self.portNumber = 9999
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("debuggerAddress", f"localhost:{self.portNumber}")
        self.driver = webdriver.Chrome(options=ops)
        self.driver.maximize_window()
    
    def stochasticScreen(self) -> list:
        filtered_stocks = self.__stoch_driver_filter()
        return filtered_stocks
        
    def simpleScreen(self)-> list:
        filtered_stocks = self.__simple_filter()
        return filtered_stocks
    
    def simpleSell(self):
        six_month_low_stocks = self.__simple_filter_sell()
        return six_month_low_stocks
    
    def __simple_filter_sell(self):
        self.__getURL()
        self.driver.find_element('xpath', '//*[@id="bottom-area"]/div[4]/div[2]/div[11]').click()
        time.sleep(1)
        self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[7]/div[2]/div/span/i').click()
        self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[1]/input').send_keys('ru')
        self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[3]/div[1]/div[27]/label').click()
        element = self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[78]/div[2]/label/label/input')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[1]/div[3]').click()
        time.sleep(1)
        tableHTML = self.driver.find_elements(By.CLASS_NAME, 'tv-data-table__tbody')
        return self.__getTickersOnly(tableHTML)
        #self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[1]/input').send_keys('ru')
        #self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[3]/div[1]/div[27]').click()
        #self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[1]/div[3]').click()

        #self.driver.find_element('xpath', '//*[@id="bottom-area"]/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[20]/label/label/input').click()
        #self.driver.find_element('xpath', '//*[@id="bottom-area"]/div[4]/div[3]/table/thead/tr/th[13]/div/i').click()

    def __simple_filter(self):                          #need to send backspace keys to russell 1000 and add ytd performance
        self.__getURL()
        self.driver.find_element("xpath", '//*[@id="bottom-area"]/div[4]/div[3]/table/thead/tr/th[1]/div/div/div[3]/input').send_keys("russell 1000")
        self.driver.find_element("xpath",'//*[@id="bottom-area"]/div[4]/div[2]/div[11]').click()
        time.sleep(1)
        element = self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[95]/div[2]/label[2]/span/i')         #moving average
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div/div[1]/span[5]').click()
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[1]/div[3]').click()
        time.sleep(1)
        elements = self.driver.find_elements(By.CLASS_NAME, 'tv-screener-table__symbol-container-description')
        russell_in_elements = False
        for tooltip in elements:
            soup = BeautifulSoup(tooltip.get_attribute('innerHTML'), "html.parser")
            if "vone dvanguard russell 1000" in soup.get_text().lower():
                russell_in_elements = True
        if russell_in_elements:
            for x in range(12):
                self.driver.find_element("xpath", '//*[@id="bottom-area"]/div[4]/div[3]/table/thead/tr/th[1]/div/div/div[3]/input').send_keys(Keys.BACK_SPACE)
            time.sleep(1)
            self.driver.find_element('xpath', '//*[@id="bottom-area"]/div[4]/div[3]/div/div[1]').click()                                                #clicks 3 dot
            time.sleep(1)
            element = self.driver.find_element('xpath', '//*[@id="bottom-area"]/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[255]/label/label/input')
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            time.sleep(1)
            self.driver.find_element("xpath",'//*[@id="bottom-area"]/div[4]/div[2]/div[11]').click()                    #clicks filter
            time.sleep(1)
            self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[5]/div[2]/label[2]/span/i').click()
            self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div/div[1]/span[1]').click()
            time.sleep(1)
            self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[8]/div[2]/div/span/span').click()
            self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[1]/input').send_keys('rus')
            self.driver.find_element('xpath', '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[3]/div[1]/div[27]/label').click()
            time.sleep(1)
            element = self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[76]/div[2]/label/label/input')
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[1]/div[3]').click()
            time.sleep(1)
            self.driver.find_element("xpath", '//*[@id="bottom-area"]/div[4]/div[3]/table/thead/tr/th[13]/div/div/div/div').click()
            time.sleep(1)
            tableHTML = self.driver.find_elements(By.CLASS_NAME, 'tv-data-table__tbody')
            return self.__getTickers(tableHTML)
        else:   
            return []
        
    def __getURL(self):
        self.driver.get(self.URL)
        time.sleep(5)

    def __del__(self):
        self.driver.quit()

    def __stoch_driver_filter(self):
        self.__getURL()
        self.driver.find_element("xpath",'//*[@id="bottom-area"]/div[4]/div[2]/div[11]').click()
        time.sleep(1)
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[7]/div[2]/div/span/i').click()
        element = self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div[3]/div[1]/div[27]/label')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(1)
        element = self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[96]/div[2]/label[2]/span/i')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[4]/div/div[1]/span[5]').click()
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[3]/div[1]/div/div/div[97]/div[2]/input[1]').send_keys("5")
        time.sleep(1)
        self.driver.find_element("xpath", '//*[@id="overlap-manager-root"]/div/div/div/div[1]/div[3]').click()
        tableHTML = self.driver.find_elements(By.CLASS_NAME, 'tv-data-table__tbody')
        return self.__getTickers(tableHTML)

    def __getTickers(self, tableHTML)->dict:
        ret_dict = dict()
        soup = BeautifulSoup(tableHTML[1].get_attribute('innerHTML'), "html.parser")
        count = 0
        for item in soup.children:
            if len(tuple(soup.stripped_strings))>1:
                if count == 20:
                    break
                tables = item.find_all_next()
                ticker = tables[8].get_text()
                price = re.sub(r'[^0-9.]','',tables[14].get_text())
                ret_dict[ticker] = {'price': price, 'rank': count}
                count +=1
        return ret_dict
    
    def __getTickersOnly(self, tableHTML)->dict:
        ret_set = set()
        soup = BeautifulSoup(tableHTML[1].get_attribute('innerHTML'), "html.parser")
        for item in soup.children:
            if len(tuple(soup.stripped_strings))>1:
                tables = item.find_all_next()
                ticker = tables[8].get_text()
                ret_set.add(ticker)
        return ret_set
