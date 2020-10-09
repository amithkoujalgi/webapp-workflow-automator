from selenium import webdriver


class WebappAutomatorAPI:
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

    def search(self, query):
        self.driver.get(f"https://www.google.com/search?q={query}&tbm=isch")
        img_src = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div/img')
        val = img_src.get_attribute("src")
        return val

    def close(self):
        self.driver.close()
