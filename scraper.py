from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



#TODO: Add maybe banard dining halls. Also maybe pring allergen information?

class FoodScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        #Each dining hall has a dictionary with link and whether it is open or not
        self.diningHalls = {
            "John Jay Dining Hall": {"link": "content/john-jay-dining-hall", "open" : False, "menu":[]},     
            "Ferris Booth Commons": {"link": "content/ferris-booth-commons-0", "open" : False, "menu":[]}, 
            "JJ's Place": {"link":"content/jjs-place-0", "open" : False, "menu":[]},
            "Chef Mike's Sub Shop": {"link": "chef-mikes", "open" : False, "menu":[]},
            "Chef Don's Pizza Pi": {"link": "content/chef-dons-pizza-pi", "open" : False, "menu":[]} ,
            "Grace Dodge Dining Hall": {"link": "content/grace-dodge-dining-hall-0", "open" : False, "menu":[]},
            "The Fac Shack": {"link": "content/fac-shack", "open" : False, "menu":[]},
            "Faculty House": {"link": "content/fac-shack", "open" : False, "menu":[]},
            }
    
    #Checks all of the dining halls are open and adjusts accordingly
    def checkOpen(self):
        self.driver.get("https://dining.columbia.edu/")
        wait = WebDriverWait(self.driver, 20)
        wrapperContainer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cu_dining_open_now-19925"]/div/div/div[2]/div/div[1]')))
        locations = wrapperContainer.find_elements(By.XPATH, './/div[@class="location"]')  
        #Get dining hall information for each of the locations
        for location in locations:
            status_open = location.find_elements(By.XPATH, './/span[@class="status open"]')
            name = location.find_elements(By.XPATH, './/span[@class="name"]')[0]
            if name.text == "Robert F. Smith Dining Hall":
                continue
            elif status_open:
                print(name.text + " is open")
                self.diningHalls[name.text]["open"] = True
            else:
                print(name.text + " is closed")



    def getMenus(self):
        for hall in self.diningHalls:
            #In main.py, if dining halls are closed, the information is not printed
            if self.diningHalls[hall]["open"] == False:
                print(f"{hall} is closed")
            else:
                diningHallUrl = self.diningHalls[hall]["link"]
                self.driver.get(f"https://dining.columbia.edu/{diningHallUrl}")
                wait = WebDriverWait(self.driver, 5)

                #Note that div1 represents the first chunk of food information(i.e. action station, main line). Need a for loop over all of them for certain dining halls
                #All dining halls ahve this element below, even if they don't have a visible menu
                

                #If dining hall does not have a menu available, then element will not be found
                try:
                    wrapperContainer = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cu-dining-meals"]/div/div/div[1]/div/div')))
                except TimeoutException:
                    print("Timed out")
                    #Mention tha the menu is not currently available
                    self.diningHalls[hall]["menu"].append("Not Available")
                    continue

                packagedMenuItems = wrapperContainer[0].find_elements(By.XPATH, './/div[@class="meal-item angular-animate ng-trans ng-trans-fade-down ng-scope"]')
                print(diningHallUrl + str(len(packagedMenuItems)))
                for item in packagedMenuItems:
                    #Gets the text of the item
                    #Doesn't find it?
                    itemName =item.find_elements(By.XPATH, './/h5[@class="meal-title ng-binding"]')[0].text
                    #Add to the menu
                    self.diningHalls[hall]["menu"].append(itemName)

                #Add if ferris, so that you also get the action line item
        
        self.printDict()
    
    def printDict(self):
        for hall in self.diningHalls:
            if self.diningHalls[hall]["open"] == False:
                status = "closed"
            else:
                status = "open"
            print(f"{hall} is currently {status}")
            print(f"Menu: \t {self.diningHalls[hall]['menu']}\n")

    def run(self):
        self.checkOpen()
        self.getMenus()



    #def run: This calls checkOPen then getMenu


if __name__ == "__main__":
    diningScraper = FoodScraper()
    diningScraper.run()



#Formatting to print
"""
Dining Hall (Hours)
Lunch: Chunky Monkey waffles food1, food2, food3, etc
Dinner
"""
"""
Maybe activated via a text to a certain number as "I'm hungry"
"""