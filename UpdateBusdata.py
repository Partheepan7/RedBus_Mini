from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import mysql.connector
import pymysql

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get('https://www.redbus.in/online-booking/rajasthan-state-road-transport-corporation')

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# List to store all route names
all_routes = []
all_links  = []

# Iterate through all the pages
for page_number in range(1, 6):  # Assuming there are 5 pages
    
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "route")))
    
    
    route_elements = driver.find_elements(By.CLASS_NAME, "route")
    link =[i.get_attribute('href') for i in route_elements]
    for l in link:
        all_links.append(l)
    for route in route_elements:
        route_name = route.text
        
        if route_name not in all_routes:
            all_routes.append(route_name)
        
    if page_number < 5:
        try:
            next_page = driver.find_element(By.XPATH, f"//div[text()='{page_number + 1}']")
            next_page.click()
            time.sleep(2)  # Allow the page to load
        except Exception as e:
            print(f"Error navigating to page {page_number + 1}: {e}")
            break
        
# print(all_routes[0])
# for route in all_routes:
#     print(route)

# print(all_links)
# print(all_routes)
# exit

driver.quit()

df_routes = pd.DataFrame(all_routes)
df_links = pd.DataFrame(all_links)

try:
    # Establish connection
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='mdt41'
    )
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Assuming 'all_routes' is a Python list and you want the first element
    new_route_name = all_routes[9]
    new_route_link = all_links[9]
    
    # Prepare the update query
    update_query1 = """
    UPDATE bus_routes
    SET route_name = %s
    WHERE route_name = 'test'
    """
    
    update_query2 = """
    UPDATE bus_routes
    SET route_link = %s
    WHERE route_link = 'test'
    """
    
    # Execute the query with the new route name
    cursor.execute(update_query1, (new_route_name))
    cursor.execute(update_query2, (new_route_link))
    
    # Commit the changes
    connection.commit()
    
except Exception as err:
    print("Error:", str(err))
    
finally:
    # Close the cursor and connection
    if connection.open:
        cursor.close()
        connection.close()
