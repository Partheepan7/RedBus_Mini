from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import mysql.connector
import pymysql



# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
#KIS to JAI
url = 'https://www.redbus.in/bus-tickets/kishangarh-to-jaipur?fromCityId=1353&toCityId=807&fromCityName=Kishangarh%20(Rajasthan)&toCityName=Jaipur&busType=Any&srcCountry=IND&destCountry=null&onward=22-Dec-2024'
driver.get(url)

# Wait for the page to load (adjust time.sleep as needed)
time.sleep(15)

# Locate all bus listing elements
bus_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'clearfix bus-item-details')]")

bus_data = []
bus_elements
# Iterate through each bus element and extract details
for bus in bus_elements:
    try:
#         # Bus Name
        bus_name = bus.find_element(By.XPATH, ".//div[contains(@class, 'travels lh-24 f-bold d-color')]").text
        
#         # Bus Type
        bus_type = bus.find_element(By.XPATH, ".//div[contains(@class, 'bus-type f-12 m-top-16 l-color evBus')]").text
        
#         # Departure Time
        departure_time = bus.find_element(By.XPATH, ".//div[contains(@class, 'dp-time f-19 d-color f-bold')]").text
        
#         # Duration
        duration = bus.find_element(By.XPATH, ".//div[contains(@class, 'dur l-color lh-24')]").text
        
#         # Arrival Time
        arrival_time = bus.find_element(By.XPATH, ".//div[contains(@class, 'bp-time f-19 d-color disp-Inline')]").text
        
#         # Star Rating
        try:
            rating = bus.find_element(By.XPATH, ".//div[contains(@class, 'lh-18 rating rat-green')]//span").text
        except:
            rating = "No rating"
        
#         # Price
        price = bus.find_element(By.XPATH, ".//div[contains(@class, 'fare d-block')]//span").text
        
#         # Seat Availability
        seats_available = bus.find_element(By.XPATH, ".//div[contains(@class, 'column-eight w-15 fl')]").text
        
#         # Print the extracted details
        # print(f"Bus Name: {bus_name}, Bus Type:{bus_type}, Departure Time:{departure_time}, Duration:{duration}, Arrival Time: {arrival_time}, Rating:{rating},Price:{price},Seat Availability:{seats_available}")
        bus_data.append({
            "Route Name":"test",
            "Route Link":"test",
            "Bus Name": bus_name,
            "Bus Type": bus_type,
            "Departure Time": departure_time,
            "Duration": duration,
            "Arrival Time": arrival_time,
            "Rating": rating,
            "Price": price,
            "Seats Available": seats_available,
            "route_id":"98"
        })
    
    except Exception as e:
        print(f"Error extracting details for a bus: {e}")

# # Close the WebDriver
driver.quit()

df = pd.DataFrame(bus_data)

# print(df)
try:

    connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'mdt41'
    )
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO bus_routes (route_name,route_link,busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available, route_id)
    VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for bus in bus_data:
        data_tuple = (
            bus["Route Name"],
            bus["Route Link"],
            bus["Bus Name"],
            bus["Bus Type"],
            bus["Departure Time"],
            bus["Duration"],
            bus["Arrival Time"],
            bus["Rating"],
            bus["Price"],
            bus["Seats Available"],
            bus["route_id"]
        )
        
        cursor.execute(insert_query, data_tuple)
        connection.commit()
    
except Exception as err:
    print (str(err))

