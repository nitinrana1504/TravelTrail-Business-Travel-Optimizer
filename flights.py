import streamlit as st
from amadeus import ResponseError
from config import amadeus

def get_flights(origin, destination, departure_date, return_date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            returnDate=return_date,
            adults=1,
            max=3
        )
        return response.data
    except ResponseError as e:
        st.error(f"Flight API error: {e}")
        return []
