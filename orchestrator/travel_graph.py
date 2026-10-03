from agents.itinerary_agent import itinerary_agent

from langgraph.graph import StateGraph, END

from state.travel_state import TravelState
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.budget_agent import budget_agent


builder = StateGraph(TravelState)

builder.add_node("flight_agent", flight_agent)
builder.add_node("hotel_agent", hotel_agent)
builder.add_node("budget_agent", budget_agent)
builder.add_node("itinerary_agent", itinerary_agent)
builder.set_entry_point("flight_agent")

builder.add_edge("flight_agent", "hotel_agent")
builder.add_edge("hotel_agent", "budget_agent")
builder.add_edge("budget_agent", "itinerary_agent")
builder.add_edge("itinerary_agent", END)

travel_graph = builder.compile()