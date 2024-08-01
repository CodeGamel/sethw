our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

intersect = our_routes.intersection(competitor_routes)
print(intersect)

print(our_routes.difference(competitor_routes))
print(our_routes.difference(competitor_routes))

diff_destinations = our_routes.symmetric_difference(competitor_routes)
print(diff_destinations)

print('='*50)


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def find_duplicates(customer_ids):
    seen = set()
    duplicates = set()
    for id in customer_ids:
        if id in seen:
            duplicates.add(id)
        else:
            seen.add(id)
    return list(duplicates)

print("Duplicates:", find_duplicates(customer_ids))