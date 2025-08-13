import streamlit as st
from amadeus import ResponseError
from config import amadeus

airport_to_city = {
    "JFK": "NYC", "LGA": "NYC", "EWR": "NYC",
    "LAX": "LAX", "SFO": "SFO", "ORD": "CHI",
    "DFW": "DFW", "MIA": "MIA", "ATL": "ATL"
}

def get_hotels(city_code, check_in, check_out):
    city_code = airport_to_city.get(city_code.upper(), city_code.upper())
    try:
        hotels_in_city = amadeus.reference_data.locations.hotels.by_city.get(cityCode=city_code)
        hotel_ids = [hotel["hotelId"] for hotel in hotels_in_city.data[:10]]

        offers = []
        for hid in hotel_ids:
            try:
                offer_resp = amadeus.shopping.hotel_offers_search.get(
                    hotelIds=hid,
                    checkInDate=check_in,
                    checkOutDate=check_out,
                    adults=1,
                    roomQuantity=1
                )
                if offer_resp.data:
                    offers.extend(offer_resp.data)
            except ResponseError:
                continue

        return offers
    except ResponseError as e:
        st.error(f"Hotel API error: {e}")
        return []
