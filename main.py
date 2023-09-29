from scraper import FoodScraper
from texter import Texter

def sendFoodOptions():
    diningScraper = FoodScraper()
    texter = Texter()
    information = diningScraper.run()

    texter.text(information)


sendFoodOptions()

    

