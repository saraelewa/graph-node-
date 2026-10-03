from state.travel_state import TravelState


def itinerary_agent(state: TravelState):
    itinerary = [
        "Day 1: Arrival and city tour",
        "Day 2: Visit historical sites",
        "Day 3: Food and shopping",
        "Day 4: Nature and parks",
        "Day 5: Departure"
    ]

    return {
        "itinerary": itinerary
    }