DAY_NAMES = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}

def print_schedule(matches, days, times, venues, team_names, modified_from=None):
    print("\n===== IPL SCHEDULE =====\n")
    for i, (a, b) in enumerate(matches):
        if modified_from is not None and i == modified_from:
            print("\n--- MODIFIED SCHEDULE FROM HERE ---\n")
        team_a = team_names[a - 1]
        team_b = team_names[b - 1]
        day = DAY_NAMES.get(days[i], "Unknown")
        time = times[i]
        venue = venues[i]
        print(f"Match {i+1:>3} | {day:<10} | {time} | {team_a} vs {team_b} | {venue}")