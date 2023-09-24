from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#TODO: Add maybe banard dining halls. Also maybe pring allergen information?

class FoodScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        #Each dining hall has a dictionary with link and whether it is open or not
        self.diningHalls = {
            "John Jay Dining Hall": {"link": "content/john-jay-dining-hall", "open" : False, "menu":},     
            "Ferris Booth Commons": {"link": "content/ferris-booth-commons-0", "open" : False}, 
            "JJ's Place": {"link":"content/jjs-place-0", "open" : False},
            "Chef Mike's Sub Shop": {"link": "chef-mikes", "open" : False},
            "Chef Don's Pizza Pi": {"link": "content/chef-dons-pizza-pi", "open" : False} ,
            "Grace Dodge Dining Hall": {"link": "content/grace-dodge-dining-hall-0", "open" : False},
            "The Fac Shack": {"link": "content/fac-shack", "open" : False}}
    
    #Checks all of the dining halls are open and adjusts accordingly
    def checkOpen(self):
        self.driver.get("https://dining.columbia.edu/")
        wait = WebDriverWait(self.driver, 20)
        
        wrapperContainer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cu_dining_open_now-19925"]/div/div/div[2]/div/div[1]')))
        locations = wrapperContainer.find_elements(By.XPATH, './/div[@class="location"]') 
        #Get dining hall information for each of the locations
        for location in locations:
            status_open = location.find_elements(By.XPATH, './/span[@class="status open"]')
            name = location.find_elements(By.XPATH, './/span[@class="name"]')
            if status_open:
                print(name[0].text + " is open")
                self.diningHalls[name[0].text]["open"] = True
            else:
                print(name[0].text + " is closed")
        
        print(self.diningHalls)



    def getMenus(self):
        for hall in self.diningHalls:
            if hall["open"] == False:
                print("Dining Hall Closed")

        diningHallUrl = self.diningHalls[diningHall]
        self.driver.get(f"https://dining.columbia.edu/{diningHallUrl}")
        #self.driver.implicitly_wait(5)

        sleep(100)

    #def run: This calls checkOPen then getMenu


if __name__ == "__main__":
    diningScraper = FoodScraper()
    diningScraper.checkOpen()
