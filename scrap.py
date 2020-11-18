#Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#function to select option
def select(driver, element_id, label):
    el = driver.find_element_by_id(element_id)
    for option in el.find_elements_by_tag_name('option'):
        if option.text == label:
            option.click()

#function to change the date
def date(driver, element_id, day, month, year):
    el = driver.find_element_by_id(element_id)
    el.clear()
    send = f"{year}-{month}-{day}"
    el.send_keys(send)
    el.send_keys(Keys.RETURN)

#Separate data by commas
def separate(data):
    data = data.replace(" m ", " ")
    data = data.replace(" ", ",")
    return data

#Clean data
#Make sure we don't have data that messes the values up
#Remove Moon fases and header
def clean(data):
    if "Lua" in data:
        pass
    elif "Fenómeno" in data:
        pass
    elif "Quarto" in data:
        pass
    else:
        return separate(data)

#Write data to the file
def to_csv(data):
    data = clean(data)
    
    if data != None:
        print(data)
        store = open("WORK\SCHOOL\data.csv", "a")
        store.write(str(data))
        store.write("\n")
        store.close()
        


#Get data from the tables
def get_data(driver, element_id):
    tb = driver.find_element_by_tag_name('tbody')
    tr = tb.find_elements_by_tag_name('tr')
    for data in tr:
        to_csv(data.text)

#Query one time
def query(driver, day, month, year):
    date(driver, "dd", day, month, year)
    select(driver, "country-list", "Portugal")
    select(driver, "port-list", "Leixões")
    select(driver, "nd", "7")
    time.sleep(5)
    get_data(driver, "table table-striped")
    time.sleep(5)

#Query 1 month
def query_month(driver, day, month, year):
    query(driver, day, month, year)
    day += 7
    query(driver, day, month, year)
    day += 7
    query(driver, day, month, year)
    day += 7
    query(driver, day, month, year)
    day += 7
    query(driver, day, month, year)


#Main function
if __name__ == "__main__":
    #Setup browser
    PATH="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.hidrografico.pt/m.mare")
    #Important stuff LOL
    query_month(driver, 1, 10, 2020)
    

