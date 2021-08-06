### Dictionaries, Nesting and the Secret Auction

## Dictionaries
Here are my dictionary notes:
https://www.notion.so/2ade684e759c44aebfe0344fc402c161?v=967010a9f1ac4418ad7c9bbb1eb6734e&p=8fd7d37116f040f6a83e95236beca4f4

## Nesting
You can nest lists or dictionaries in another dictionary

    # Dictionary with nested list
    travel_log = {
        "France": ["Paris", "Lille", "Dijon"]
    }

    # List in a list
    nested_list = ["A", "B", ["C", "D"]]

    #Dictionary with nested dictionary
    cities_visited = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3},
    }

    #Dictionary in a list
    travel_log = [
        {
            "country": "France",
            "cities_visited": ["Paris", "Lille", "Dijon"],
            "total_visits": 12
        },
        {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3
        },
    ]

    for item in travel_log:
        for key, value in item.items():
            print(item)
