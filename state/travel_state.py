from typing import TypedDict


class TravelState(TypedDict):
    destination: str
    days: int
    budget: int

    flight_info: str
    hotel_info: str
    budget_info: str

    itinerary: list[str]