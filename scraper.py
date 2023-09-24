from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#TODO: Add maybe banard dining halls. Also maybe pring allergen information?

class FoodScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.diningHalls = {
            "John Jay Dining Hall": "content/john-jay-dining-hall",     
            "Ferris Booth Commons": "content/ferris-booth-commons-0", 
            "JJ's Place": "content/jjs-place-0",
            "Chef Mike's Sub Shop": "chef-mikes",
            "Chef Don's Pizza Pi": "content/chef-dons-pizza-pi",
            "Grace Dodge Dining Hall": "content/grace-dodge-dining-hall-0",
            "The Fac Shack": "content/fac-shack"}
    
    #Checks all of the dining halls are open and adjusts accordingly
    def checkOpen(self):
        self.driver.get("https://dining.columbia.edu/")
        wait = WebDriverWait(self.driver, 20)
        #This has div with class = col-xs-12 col-md-6
        wrapperContainer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cu_dining_open_now-19925"]/div/div/div[2]/div/div[1]')))
        print("Wrapper" )
        locations = wrapperContainer.find_elements(By.XPATH, './/div[@class="location"]') 
        print("locations" + str(locations))
        for location in locations:
            status_open = location.find_elements(By.XPATH, './/span[@class="status open"]')
            print("One status")
            if status_open:
                print(status_open[0].text)



    def getMenu(self, diningHall: str):
        diningHallUrl = self.diningHalls[diningHall]
        self.driver.get(f"https://dining.columbia.edu/{diningHallUrl}")
        #self.driver.implicitly_wait(5)

        sleep(100)

    #def run: This calls checkOPen then getMenu


if __name__ == "__main__":
    diningScraper = FoodScraper()
    diningScraper.checkOpen()
