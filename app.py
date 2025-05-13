import streamlit as st
from main import TripCrew
import time
from datetime import datetime, timedelta
import json

# Page config
st.set_page_config(
    page_title="Trip Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stSelectbox>div>div>select {
        border-radius: 5px;
    }
    .travel-plan {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
        color: #222 !important;
    }
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #222 !important;
    }
    .stDataFrame, .stTable, .stText, .stMarkdown {
        color: #222 !important;
    }
    .css-1cpxqw2, .css-ffhzg2, .css-1d391kg {
        color: #222 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("✈️ Smart Travel Planner")
st.markdown("""
    Plan your perfect trip with our AI-powered travel assistant. 
    Just fill in your preferences and let our experts create a personalized travel plan for you!
    """)

# Sidebar for user inputs
with st.sidebar:
    st.header("Your Travel Preferences")
    
    # Origin input
    origin = st.text_input("Where are you traveling from?", 
                          placeholder="e.g., New York, USA")
    
    # Cities input
    cities = st.text_input("Which cities would you like to visit? (comma-separated)", 
                          placeholder="e.g., Paris, London, Rome")
    
    # Date range
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", 
                                 min_value=datetime.now(),
                                 value=datetime.now() + timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", 
                               min_value=datetime.now(),
                               value=datetime.now() + timedelta(days=37))
    
    # Interests
    interests = st.multiselect(
        "What are your interests?",
        ["Adventure", "Culture", "Food", "Nature", "History", "Shopping", "Relaxation", "Nightlife"],
        default=["Culture", "Food"]
    )
    
    # Additional interests
    other_interests = st.text_input("Other interests (optional)", 
                                   placeholder="e.g., Photography, Hiking")

# Main content area
if st.button("Generate Travel Plan"):
    if not origin or not cities:
        st.error("Please fill in your origin and desired cities.")
    else:
        # Combine interests
        all_interests = interests
        if other_interests:
            all_interests.append(other_interests)
        
        # Format date range
        date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        
        # Show loading state
        with st.spinner("Our travel experts are working on your perfect itinerary..."):
            # Initialize and run the trip crew
            trip_crew = TripCrew(origin, cities, date_range, ", ".join(all_interests))
            result = trip_crew.run()
            
            # Display the result
            st.markdown("## ✨ Your Personalized Travel Plan")
            st.markdown("---")
            
            # Create a container for the travel plan
            with st.container():
                st.markdown(f"""
                    <div class="travel-plan">
                        {result}
                    </div>
                """, unsafe_allow_html=True)
            
            # Add a download button for the plan
            st.download_button(
                label="Download Travel Plan",
                data=result,
                file_name="travel_plan.md",
                mime="text/markdown"
            )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Powered by AI Travel Experts | Made with ❤️ for travelers</p>
    </div>
    """, unsafe_allow_html=True) 