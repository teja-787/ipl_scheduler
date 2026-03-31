def generate_matches(n):
    """Generate all home & away match combinations for n teams."""
    matches = []
    # Round robin: every team plays every other team twice (home & away)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                matches.append((i, j))
    return matches