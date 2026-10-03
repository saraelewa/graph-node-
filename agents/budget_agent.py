from state.travel_state import TravelState


def budget_agent(state: TravelState):
    return {
        "budget_info": (
            f"Available budget: "
            f"${state['budget']}"
        )
    }