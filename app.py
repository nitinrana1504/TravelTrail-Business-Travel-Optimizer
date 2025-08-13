import streamlit as st
from datetime import date
from flights import get_flights
from hotels import get_hotels
from utils import rank_travel_options

st.title("✈️ TravelTrail - Business-Travel Optimizer")
st.write("Search the best flights + hotels using Amadeus API")

with st.form(key="search_form"):
    origin = st.text_input("From (IATA Airport Code)", "JFK")
    destination = st.text_input("To (IATA City Code or Airport Code)", "LAX")
    start_date = st.date_input("Start Date", date(2025, 9, 1))
    end_date = st.date_input("End Date", date(2025, 9, 6))
    submit = st.form_submit_button("Search")

if submit:
    flights = get_flights(origin, destination, str(start_date), str(end_date))
    hotels = get_hotels(destination, str(start_date), str(end_date))

    if not flights or not hotels:
        st.warning("No flights or hotels found. Try adjusting search.")
    else:
        ranked = rank_travel_options(flights, hotels)
        st.dataframe(ranked)
