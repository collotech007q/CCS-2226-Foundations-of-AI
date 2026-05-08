# NAME: COLLINS KIPKIRUI
# REG NO: CIT-227-065/2024
# UNIT: FOUNDATIONS OF AI
# TASK: Task 2(b) - Nairobi Map Coloring (17 Sub-counties)

def is_valid(region, color, assignment, adjacency):
    """Check if the current color assignment is consistent with neighbors."""
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, adjacency):
    """Solve the CSP using backtracking search."""
    if len(assignment) == len(regions):
        return assignment

    # Select the next unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, adjacency):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, adjacency)
            if result:
                return result
            # Backtrack if no solution found
            del assignment[region]
    return None

# List of 17 Nairobi Sub-counties
sub_counties = [
    "Westlands", "Dagoretti North", "Dagoretti South", "Lang'ata", "Kibra", 
    "Roysambu", "Kasarani", "Ruaraka", "Embakasi South", "Embakasi North", 
    "Embakasi Central", "Embakasi East", "Embakasi West", "Makadara", 
    "Kamkunji", "Starehe", "Mathare"
]

# Adjacency clusters based on a simulative map of Nairobi
adj_list = {
    "Starehe": ["Mathare", "Kamkunji", "Makadara", "Westlands"],
    "Mathare": ["Starehe", "Ruaraka", "Kamkunji"],
    "Westlands": ["Starehe", "Dagoretti North", "Roysambu"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
    "Dagoretti South": ["Dagoretti North", "Lang'ata"],
    "Kibra": ["Dagoretti North", "Lang'ata", "Starehe"],
    "Lang'ata": ["Dagoretti South", "Kibra", "Embakasi South"],
    "Roysambu": ["Westlands", "Kasarani", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North"],
    "Ruaraka": ["Mathare", "Roysambu", "Kasarani"],
    "Embakasi South": ["Lang'ata", "Makadara", "Embakasi East"],
    "Embakasi North": ["Kasarani", "Embakasi Central", "Embakasi West"],
    "Embakasi Central": ["Embakasi North", "Embakasi West", "Embakasi East"],
    "Embakasi East": ["Embakasi South", "Embakasi Central"],
    "Embakasi West": ["Embakasi North", "Embakasi Central", "Makadara"],
    "Makadara": ["Starehe", "Kamkunji", "Embakasi South", "Embakasi West"],
    "Kamkunji": ["Starehe", "Mathare", "Makadara"]
}

def solve_nairobi():
    # Attempt to solve with the minimum number of colors starting from 1
    for k in range(1, 18):
        test_colors = [f"Color_{i+1}" for i in range(k)]
        solution = backtrack({}, sub_counties, test_colors, adj_list)
        if solution:
            return k, solution

# Execute and Print results
min_colors, result = solve_nairobi()
print(f"Minimum colors required for Nairobi's 17 sub-counties: {min_colors}")
print("Sample Assignment:", result)
