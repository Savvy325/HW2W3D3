# 1. Python Sets Adventure

# Task 1: Destinations that both airlines fly to.
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
same_destinations = our_routes.intersection(competitor_routes)
print(same_destinations)

# Task 2: Destinations unique to your airline.
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
unique = our_routes.difference(competitor_routes)
print(unique)

# Task 3: Whether there are any destinations that neither airline shares.
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
differences = our_routes.symmetric_difference(competitor_routes)
print(differences)

# 2. Set Operations in Data Analysis

#Task 1: Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
customer_ids_set = set(customer_ids)
print(customer_ids_set)
