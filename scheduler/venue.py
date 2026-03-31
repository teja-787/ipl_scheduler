def assign_venues(n, team_names, matches):
    """
    If n stadiums: home team's city is the venue.
    If fewer stadiums: rotate through available stadiums.
    """
    n_stadiums = 0
    while n_stadiums < 1 or n_stadiums > n:
        n_stadiums = int(input(f"Enter number of stadiums (1 to {n}): "))

    venues = []

    if n_stadiums == n:
        home_cities = []
        for name in team_names:
            city = input(f"Enter home city for {name}: ")
            home_cities.append(city)
        for (a, b) in matches:
            venues.append(home_cities[a - 1])
    else:
        stadium_names = []
        for i in range(n_stadiums):
            s = input(f"Enter name for Stadium {i+1}: ")
            stadium_names.append(s)
        for i in range(len(matches)):
            venues.append(stadium_names[i % n_stadiums])

    return venues