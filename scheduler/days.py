def next_day(day):
    return (day % 7) + 1

def schedule_days(day_one, total, n):
    """
    Assign a day number (1=Mon ... 7=Sun) to each match.
    - n >= 8: two matches on weekends, one on weekdays
    - n < 8:  one match every other day (gap of 1)
    """
    days = []
    current = day_one

    if n >= 8:
        i = 0
        while i < total:
            days.append(current)
            if current in (6, 7) and i + 1 < total:  # Weekend double-header
                days.append(current)
                i += 2
            else:
                i += 1
            current = next_day(current)
    else:
        # 1 day gap between matches
        for i in range(total):
            days.append(current)
            current = next_day(next_day(current))  # skip one day

    return days[:total]

def schedule_time(days):
    """
    Assign time slots:
    - Weekdays: always 7:30 pm
    - First match on weekend: 3:30 pm, second: 7:30 pm
    """
    times = []
    for i, day in enumerate(days):
        if day in (6, 7):
            if i == 0 or days[i - 1] != day:
                times.append("3:30 pm")
            else:
                times.append("7:30 pm")
        else:
            times.append("7:30 pm")
    return times