import numpy as np

# Import unified player database
from players_data import players_data as players

playoff_weight = 0.7
finals_weight = 0.5

print("## Unified Extrapolated Stat Projections Grid (Blended model)")
print("This table displays each player's blended expected stat lines for Game 5 under the default 70% Playoff Weight / 50% Finals Matchup Weight blend model.")

print("\n| Player (Team) | Expected MIN | Points (PTS) | Rebounds (REB) | Assists (AST) | Steals (STL) | 3-Pointers (3PM) | PTS + REB + AST | PTS + AST | PTS + REB | REB + AST |")
print("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

for p in players:
    name = p['Name']
    team = p['Team']
    reg = p['Regular_Season']
    playoff = p['Playoffs']
    finals = p['Finals']
    
    # Calculate Season Baseline (B)
    baseline_min = (1.0 - playoff_weight) * reg['MIN'] + playoff_weight * playoff['MIN']
    
    baseline_stats = {}
    for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
        reg_rate = reg[stat] / reg['MIN']
        playoff_rate = playoff[stat] / playoff['MIN']
        blend_rate = (1.0 - playoff_weight) * reg_rate + playoff_weight * playoff_rate
        baseline_stats[stat] = blend_rate * baseline_min
        
    # Calculate Finals Matchup Trend (M)
    finals_min = np.mean([g['MIN'] for g in finals])
    finals_stats = {}
    for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
        finals_stats[stat] = np.mean([g[stat] for g in finals])
        
    # Blended expected minutes
    expected_min = (1.0 - finals_weight) * baseline_min + finals_weight * finals_min
    
    proj_vals = {}
    for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
        val_baseline = baseline_stats[stat]
        val_finals = finals_stats[stat]
        proj_vals[stat] = (1.0 - finals_weight) * val_baseline + finals_weight * val_finals
        
    proj_pts = round(proj_vals['PTS'], 2)
    proj_reb = round(proj_vals['REB'], 2)
    proj_ast = round(proj_vals['AST'], 2)
    proj_stl = round(proj_vals['STL'], 2)
    proj_3pm = round(proj_vals['3PM'], 2)
    
    # Calculate combo projections matching app.py logic
    proj_pra = round(proj_pts + proj_reb + proj_ast, 2)
    proj_pa = round(proj_pts + proj_ast, 2)
    proj_pr = round(proj_pts + proj_reb, 2)
    proj_ra = round(proj_reb + proj_ast, 2)
    
    cells = [
        f"{name} ({team})",
        f"{expected_min:.1f}",
        f"{proj_pts:.2f}",
        f"{proj_reb:.2f}",
        f"{proj_ast:.2f}",
        f"{proj_stl:.2f}",
        f"{proj_3pm:.2f}",
        f"{proj_pra:.2f}",
        f"{proj_pa:.2f}",
        f"{proj_pr:.2f}",
        f"{proj_ra:.2f}"
    ]
    
    print("| " + " | ".join(cells) + " |")
