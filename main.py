from scheduler.matches import generate_matches
from scheduler.days import schedule_days, schedule_time
from scheduler.venue import assign_venues
from scheduler.display import print_schedule
from scheduler.playoffs import run_playoffs

def main():
    print("Welcome to the IPL Scheduler!")
    n = int(input("Enter the number of teams: "))

    print("\nEnter starting day:")
    days_map = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
    for k, v in days_map.items():
        print(f"  {k}. {v}")
    day_one = int(input("Enter the day number: "))

    team_names = []
    for i in range(n):
        name = input(f"Enter name of team {i+1}: ")
        team_names.append(name)

    matches = generate_matches(n)
    days = schedule_days(day_one, len(matches), n)
    times = schedule_time(days)
    venues = assign_venues(n, team_names, matches)

    print_schedule(matches, days, times, venues, team_names)

    reschedule = input("\nDid all matches go smoothly? (yes/no): ").strip().lower()
    while reschedule == "no":
        start = int(input(f"Enter match number to reschedule from (1-{len(matches)}): ")) - 1
        new_day = int(input("Enter new starting day number (1-7): "))
        new_days = schedule_days(new_day, len(matches) - start, n)
        days[start:] = new_days
        times = schedule_time(days)
        print_schedule(matches, days, times, venues, team_names, modified_from=start)
        reschedule = input("\nDid all matches go smoothly? (yes/no): ").strip().lower()

    print("\nGreat! Proceeding to Playoffs...\n")
    run_playoffs()

if __name__ == "__main__":
    main()