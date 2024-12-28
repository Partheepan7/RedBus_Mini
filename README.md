# RedBus_Mini
Redbus Data Scraping with Selenium &amp; Dynamic Filtering using Streamlit
Sure! Below is a **README.md** file that you can use for your GitHub repository.

---

# Redbus Data Scraping and Filtering with Streamlit Application

## Overview

The **"Redbus Data Scraping and Filtering with Streamlit Application"** is a project designed to automate the collection, analysis, and visualization of bus travel data from Redbus. The project leverages **Selenium** for web scraping and **Streamlit** for creating an interactive user interface for filtering and displaying the bus data.

This application provides a comprehensive solution to collect, filter, and visualize bus route information, including bus types, schedules, prices, seat availability, and ratings, allowing transportation professionals to make data-driven decisions and improve operational efficiency.

---

## Features

- **Automated Data Collection**: Scrapes bus details such as bus name, type, departure time, duration, arrival time, rating, price, and seat availability from Redbus.
- **Real-Time Data Filtering**: Use Streamlit to filter the bus data by bus type, route name, price range, and star rating.
- **Interactive User Interface**: Allows users to easily interact with the data and make informed decisions.
- **MySQL Integration**: Stores the scraped data in a MySQL database for further querying and analysis.

---

## Technologies Used

- **Selenium**: For automating web scraping from Redbus.
- **Streamlit**: For building the interactive user interface.
- **pymysql**: For connecting to and interacting with the MySQL database.
- **pandas**: For data manipulation and analysis.
- **MySQL**: For storing and managing the scraped data.

---

## Installation

### Prerequisites

Before running the project, you need to install the following dependencies:

1. **Selenium**: For scraping data.
   ```bash
   pip install selenium
   ```

2. **Streamlit**: For building the web app.
   ```bash
   pip install streamlit
   ```

3. **pymysql**: For connecting to MySQL.
   ```bash
   pip install pymysql
   ```

4. **pandas**: For data manipulation.
   ```bash
   pip install pandas
   ```

5. **ChromeDriver**: Selenium requires a browser driver to interact with web pages. Make sure you have the correct version of **ChromeDriver** installed. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

---

## How to Use

### 1. **Web Scraping Script**

The scraping script automatically collects bus data from Redbus. To use it:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/redbus-data-scraping.git
   cd redbus-data-scraping
   ```

2. Run the scraping script:
   ```bash
   python scrape_redbus_data.py
   ```

   This will scrape the bus data from Redbus and store it in a MySQL database.

### 2. **Streamlit Application**

To interact with the scraped data and apply filters using Streamlit:

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser (usually `http://localhost:8501`) to view the app.

3. **Filters**: You can filter bus routes by:
   - **Bus Type**
   - **Route Name**
   - **Price Range**
   - **Star Rating**

4. **Display**: The filtered results will be displayed in a table on the app. You can also click on "Show Detailed View" to see the raw data.

---

## Data Structure

The scraped data is stored in a MySQL database with the following structure:

- **Table Name**: `bus_routes`

### Table Columns:

| Column Name        | Description                                      |
|--------------------|--------------------------------------------------|
| `route_name`       | Name of the bus route                           |
| `route_link`       | Link to the specific route page                  |
| `bus_name`         | Name of the bus                                 |
| `bustype`          | Type of bus (e.g., Sleeper, Seater)              |
| `departing_time`   | Time when the bus departs                       |
| `duration`         | Duration of the trip                            |
| `reaching_time`    | Time when the bus arrives                       |
| `star_rating`      | Star rating of the bus (if available)           |
| `price`            | Price of the bus ticket                         |
| `seats_available`  | Number of seats available                       |
| `route_id`         | Unique identifier for the route                 |

---

## Code Explanation

### **Web Scraping with Selenium**

1. **Initialize the WebDriver**: The script uses Selenium to initialize a Chrome WebDriver and navigate to the Redbus webpage.
2. **Locate Bus Elements**: The script extracts the bus listing elements using XPath and stores them in a list.
3. **Extract Data**: For each bus, the following details are extracted: bus name, type, departure time, duration, arrival time, star rating, price, and seat availability.
4. **Store Data in MySQL**: The extracted data is stored in a MySQL database using the `pymysql` library.

### **Streamlit App for Data Visualization**

1. **Connect to MySQL**: The app connects to the MySQL database to retrieve the stored bus data.
2. **Filters**: The app allows users to filter the bus data by bus type, route name, price range, and star rating.
3. **Display Data**: The filtered data is displayed in a table format using Streamlit's `st.dataframe()` function.
4. **Styling**: Custom CSS is used to enhance the user interface, with background images, animations, and colors.

---

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. You can also open issues to report bugs or suggest new features.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [Redbus](https://www.redbus.in/) for providing the data we scrape.
- [Selenium](https://www.selenium.dev/) for browser automation.
- [Streamlit](https://streamlit.io/) for building the interactive web application.
- [pymysql](https://pymysql.readthedocs.io/en/latest/) for MySQL connectivity.

---

## Contact

For any questions or inquiries, please contact me at [partheepan.bluesky@gmail.com].

---

**End of README**

---

This **README.md** file provides an overview of your project, installation instructions, usage guidelines, and other relevant information for contributors and users. Make sure to replace the placeholders like `partheepan` and `partheepan.bluesky@gmail.com` with your actual GitHub username and contact details.
