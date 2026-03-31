def run_playoffs():
    print("===== PLAYOFFS =====\n")

    venues = {
        "Qualifier 1": input("Enter stadium for Qualifier 1: "),
        "Eliminator":  input("Enter stadium for Eliminator: "),
        "Qualifier 2": input("Enter stadium for Qualifier 2: "),
        "Final":       input("Enter stadium for the Final: "),
    }

    teams = []
    for i in range(1, 5):
        teams.append(input(f"Enter team in position {i} of points table: "))

    # Qualifier 1: 1st vs 2nd
    print(f"\nQualifier 1: {teams[0]} vs {teams[1]} at {venues['Qualifier 1']} | 7:30 pm")
    q1_winner = input("Winner: ")
    q1_loser = teams[1] if q1_winner == teams[0] else teams[0]

    # Eliminator: 3rd vs 4th
    print(f"\nEliminator: {teams[2]} vs {teams[3]} at {venues['Eliminator']} | 7:30 pm")
    elim_winner = input("Winner: ")

    # Qualifier 2: Q1 loser vs Eliminator winner
    print(f"\nQualifier 2: {q1_loser} vs {elim_winner} at {venues['Qualifier 2']} | 7:30 pm")
    q2_winner = input("Winner: ")

    # Final
    print(f"\nIPL Final: {q1_winner} vs {q2_winner} at {venues['Final']} | 7:30 pm")
    champion = input("Winner: ")

    if champion == "RCB":
        print(f"\nCongratulations to Kohli and Co! Finally {champion} have won the IPL!")
    else:
        print(f"\nThe IPL Champion is {champion}! 🏆")