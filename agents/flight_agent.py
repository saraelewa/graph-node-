from state.travel_state import TravelState


def flight_agent(state: TravelState):
    return {
        "flight_info": (
            f"Searching for flights to "
            f"{state['destination']} "
            f"for {state['days']} days."
        )
    }