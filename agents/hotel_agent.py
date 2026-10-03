from state.travel_state import TravelState


def hotel_agent(state: TravelState):
    return {
        "hotel_info": (
            f"Searching hotels in "
            f"{state['destination']} "
            f"for {state['days']} nights."
        )
    }