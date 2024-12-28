import streamlit as st
import pandas as pd
import pymysql
from datetime import datetime

# Connect to the MySQL database
def get_data_from_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='mdt41'
    )
    query = """
        SELECT 
            route_name, 
            busname, 
            bustype, 
            departing_time, 
            duration, 
            reaching_time, 
            star_rating, 
            price, 
            seats_available 
        FROM bus_routes
    """
    df = pd.read_sql(query, connection)
    connection.close()
    
    # Ensure 'price' and 'star_rating' are numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Convert 'price' to numeric
    df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')  # Convert 'star_rating' to numeric
    
    # Normalize string columns to ensure consistent filtering
    df['bustype'] = df['bustype'].str.strip().str.lower()
    df['route_name'] = df['route_name'].str.strip().str.lower()
    
    return df

# Streamlit App
def run_streamlit_app():
    # Path to your local image
    image_path = "background.jpg"  # Replace with your local image file path

    # Add custom CSS for UI design
    st.markdown(
        f"""
        <style>
            body {{
                background-image: url('file://{image_path}');
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .header {{
                text-align: center;
                font-size: 30px;
                color: white;
                font-weight: bold;
                margin-top: 20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
                transition: transform 0.3s, color 0.3s;
            }}
            .header:hover {{
                transform: scale(1.1);
                color: #FFD700;
            }}
            .welcome-note {{
                background-color: #008080;
                color: white;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }}
            .announcement {{
                background-color: #FF5733;
                color: white;
                text-align: center;
                font-size: 15px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }}
            .subheader {{
                font-size: 30px;
                color: #FFD700;
                font-weight: 600;
                margin-top: 20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
                transition: color 0.3s ease-in-out;
            }}
            .subheader:hover {{
                color: #4CAF50;
            }}
            .scrolling-text {{
                color: red;
                font-size: 20px;
                font-weight: bold;
                padding: 15px;
                text-align: center;
                white-space: nowrap;
                overflow: hidden;
                animation: scroll 10s linear infinite;
                font-family: 'Poppins', sans-serif;
            }}
            @keyframes scroll {{
                0% {{ transform: translateX(100%); }}
                100% {{ transform: translateX(-100%); }}
            }}
            .filter-header {{
                font-size: 18px;
                font-weight: bold;
                color: white;
                background-color: #4CAF50;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }}
            .filter-location {{
                color: black;
                font-size: 14px;
                margin-top: 5px;
            }}
            .filter-time {{
                color: black;
                font-size: 14px;
                margin-top: 5px;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Load data
    df = get_data_from_db()

    # Welcome Note
    st.markdown('<div class="welcome-note">🌟 Welcome to RedBus! Discover routes, compare prices, and enjoy your journey with exclusive offers. 🌟</div>', unsafe_allow_html=True)

    # Header
    st.markdown('<h3 class="header">Travel Route Information</h3>', unsafe_allow_html=True)
    
    # Diwali Announcement
    st.markdown('<div class="announcement">🎉 Diwali Special Offer: Get up to 50% off on selected routes! Book now! 🎉</div>', unsafe_allow_html=True)

    # Running Note (Scrolling Text)
    st.markdown('<div class="scrolling-text">🚨 Exciting offers available this Diwali! Book your journey now and save big! 🚨</div>', unsafe_allow_html=True)

    # Sidebar Filters Section
    st.sidebar.markdown('<div class="filter-header">Filters</div>', unsafe_allow_html=True)

    # # Date and Location
    # current_time = datetime.now().strftime("%dth %b- %Y %I:%M %p")
    # st.sidebar.markdown(f'<div class="filter-time">{current_time}</div>', unsafe_allow_html=True)
    # st.sidebar.markdown('<div class="filter-location">Location: Tamil Nadu, India</div>', unsafe_allow_html=True)
    
    # Filter by Bus Type
    bus_types = df['bustype'].unique()
    selected_bus_type = st.sidebar.selectbox("Select Bus Type", options=bus_types, format_func=lambda x: x.capitalize())
    
    # Filter by Route Name
    route_names = df['route_name'].unique()
    selected_route_name = st.sidebar.selectbox("Select Route Name", options=route_names, format_func=lambda x: x.capitalize())
    
    # Price Range Filter
    min_price, max_price = df['price'].min(), df['price'].max()
    selected_price_range = st.sidebar.slider(
        "Select Price Range", min_value=float(min_price), max_value=float(max_price),
        value=(float(min_price), float(max_price))
    )
    
    # Star Rating Filter
    min_rating, max_rating = df['star_rating'].min(), df['star_rating'].max()
    selected_rating = st.sidebar.slider(
        "Select Star Rating", min_value=float(min_rating), max_value=float(max_rating),
        value=(float(min_rating), float(max_rating))
    )
    
    # Apply Filters
    filtered_df = df[
        (df['bustype'] == selected_bus_type.lower()) &
        (df['route_name'] == selected_route_name.lower()) &
        (df['price'] >= selected_price_range[0]) &
        (df['price'] <= selected_price_range[1]) &
        (df['star_rating'] >= selected_rating[0]) &
        (df['star_rating'] <= selected_rating[1])
    ]

    # Display Filtered Data
    if not filtered_df.empty:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("No results match the selected filters.")

    # Detailed View Button
    if st.button("Show Detailed View of Filtered Data"):
        st.write(filtered_df)

# Run the Streamlit app
if __name__ == "__main__":
    run_streamlit_app()
