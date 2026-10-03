from orchestrator.travel_graph import travel_graph


def main():

    result = travel_graph.invoke(
        {
            "destination": "Japan",
            "days": 5,
            "budget": 1500,
        }
    )

    print("\n=== FINAL STATE ===\n")

    print(result)


if __name__ == "__main__":
    main()