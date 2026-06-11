import json
import numpy as np

# Import unified player database and filter for the 9 key players with betting lines
from players_data import players_data
key_player_names = {
    'Jalen Brunson', 'Victor Wembanyama', 'Karl-Anthony Towns', 
    'OG Anunoby', 'Stephon Castle', 'De\'Aaron Fox', 
    'Josh Hart', 'Devin Vassell', 'Mikal Bridges'
}
players = [p for p in players_data if p['Name'] in key_player_names]

# Typical betting lines (estimated based on Game 5 markets)
betting_lines = {
    'Jalen Brunson': {'PTS': 26.5, 'REB': 3.5, 'AST': 5.5, 'STL': 1.5, '3PM': 2.5},
    'Victor Wembanyama': {'PTS': 25.5, 'REB': 10.5, 'AST': 2.5, 'STL': 1.5, '3PM': 1.5},
    'Karl-Anthony Towns': {'PTS': 18.5, 'REB': 11.5, 'AST': 4.5, 'STL': 0.5, '3PM': 1.5},
    'OG Anunoby': {'PTS': 17.5, 'REB': 5.5, 'AST': 1.5, 'STL': 1.5, '3PM': 2.5},
    'Stephon Castle': {'PTS': 15.5, 'REB': 4.5, 'AST': 4.5, 'STL': 1.5, '3PM': 1.5},
    'De\'Aaron Fox': {'PTS': 16.5, 'REB': 3.5, 'AST': 5.5, 'STL': 1.5, '3PM': 1.5},
    'Josh Hart': {'PTS': 8.5, 'REB': 8.5, 'AST': 4.5, 'STL': 1.5, '3PM': 0.5},
    'Devin Vassell': {'PTS': 13.5, 'REB': 5.5, 'AST': 3.5, 'STL': 1.5, '3PM': 2.5},
    'Mikal Bridges': {'PTS': 14.5, 'REB': 3.5, 'AST': 3.5, 'STL': 1.5, '3PM': 1.5}
}

output_lines = []
output_lines.append("# Player Prop Analysis & Extrapolation for Game 5")
output_lines.append("\nThis analysis calculates expected player prop outcomes for tonight's Game 5 of the NBA Finals by blending historical baselines and current series trends:")
output_lines.append("1. **Season Baseline**: Blends 2025-26 Regular Season and 2026 Playoff baselines (using 70% Playoff / 30% Regular Season weight).")
output_lines.append("2. **Finals Average**: Actual performance average across Game 1, Game 2, Game 3, and Game 4 of this series.")
output_lines.append("3. **Blended Projection**: A 50% Season Baseline and 50% Finals Average blend model, capturing both depth and matchup adjustments.\n")


playoff_w = 0.7
finals_w = 0.5

for p in players:
    name = p['Name']
    team = p['Team']
    reg = p['Regular_Season']
    playoff = p['Playoffs']
    finals = p['Finals']
    
    # Calculate Baseline MIN
    baseline_min = (1.0 - playoff_w) * reg['MIN'] + playoff_w * playoff['MIN']
    # Calculate Finals MIN
    finals_min = np.mean([g['MIN'] for g in finals])
    # Blended Proj MIN
    proj_min = (1.0 - finals_w) * baseline_min + finals_w * finals_min
    
    output_lines.append(f"## {name} ({team})")
    output_lines.append(f"- **Season Baseline MIN**: {baseline_min:.1f} | **Finals Avg MIN**: {finals_min:.1f} | **Game 5 Projected MIN**: {proj_min:.1f}")
    output_lines.append("\n| Metric | Season Baseline | Finals Avg | Blended Proj | Betting Line | Recommendation |")
    output_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
    
    lines = betting_lines.get(name, {})
    
    for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
        # Baseline stat
        reg_rate = reg[stat] / reg['MIN']
        playoff_rate = playoff[stat] / playoff['MIN']
        blend_rate = (1.0 - playoff_w) * reg_rate + playoff_w * playoff_rate
        stat_baseline = blend_rate * baseline_min
        
        # Finals Avg stat
        stat_finals = np.mean([g[stat] for g in finals])
        
        # Blended Proj stat
        stat_proj = (1.0 - finals_w) * stat_baseline + finals_w * stat_finals
        
        line = lines.get(stat, 0.0)
        
        # Recommendation logic
        diff = stat_proj - line
        if diff > 0.5:
            rec = f"**OVER** (+{diff:.2f})"
        elif diff < -0.5:
            rec = f"**UNDER** ({diff:.2f})"
        else:
            rec = "Neutral"
            
        output_lines.append(f"| {stat} | {stat_baseline:.2f} | {stat_finals:.2f} | {stat_proj:.2f} | {line:.1f} | {rec} |")
    output_lines.append("\n")

with open('player_props_analysis.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Analysis successfully written to player_props_analysis.md")
