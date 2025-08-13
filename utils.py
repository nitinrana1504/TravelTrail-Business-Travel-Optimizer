import random

def rank_travel_options(flights, hotels):
    results = []
    for f in flights:
        try:
            airline_codes = [seg['carrierCode'] for seg in f['itineraries'][0]['segments']]
            flight_airline = ', '.join(set(airline_codes))
            flight_price = float(f['price']['total'])

            flight_duration = 0
            for seg in f['itineraries'][0]['segments']:
                dur = seg['duration'].replace("PT", "")
                hours, mins = 0, 0
                if "H" in dur:
                    parts = dur.split("H")
                    hours = int(parts[0])
                    mins = int(parts[1].replace("M", "")) if "M" in parts[1] else 0
                else:
                    mins = int(dur.replace("M", ""))
                flight_duration += hours * 60 + mins

            for h in hotels:
                hotel_price = float(h['offers'][0]['price']['total'])
                hotel_rating = h['hotel'].get('rating', 'N/A')
                total_cost = flight_price + hotel_price
                loyalty_score = random.uniform(0, 1)

                results.append({
                    "Flight Airline": flight_airline,
                    "Flight Price": flight_price,
                    "Flight Duration (min)": flight_duration,
                    "Hotel Name": h['hotel']['name'],
                    "Hotel Rating": hotel_rating,
                    "Hotel Price": hotel_price,
                    "Total Cost": total_cost,
                    "Loyalty Score": round(loyalty_score, 2)
                })
        except Exception:
            continue

    results.sort(key=lambda x: x["Total Cost"])
    return results[:5]
