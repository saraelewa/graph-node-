from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.budget_agent import budget_agent


def create_travel_plan(destination, days, budget):
    flight_result = flight_agent(destination, days)
    hotel_result = hotel_agent(destination, days)
    budget_result = budget_agent(budget)

    return {
        "flight": flight_result,
        "hotel": hotel_result,
        "budget": budget_result,
    }