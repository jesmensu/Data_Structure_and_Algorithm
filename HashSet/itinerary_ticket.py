ticket = {
    "Chennai": "Bengaluru",
    "Mumbai": "Delhi",
    "Goa": "Chennai",
    "Delhi": "Goa"
}

rev_ticket = {}

for k, v in ticket.items():
    rev_ticket[v] = k

for k in ticket:
    if k not in rev_ticket:
        print(k)