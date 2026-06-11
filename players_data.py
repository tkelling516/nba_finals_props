# Centralized database of player stats for Regular Season, Playoffs, and Finals matchups.
# Used by app.py, generate_grid.py, and extrapolate.py.

players_data = [
    {
        'Name': 'Jalen Brunson', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 35.0, 'PTS': 26.0, 'REB': 3.3, 'AST': 6.8, 'STL': 0.8, '3PM': 2.6 },
        'Playoffs': { 'MIN': 36.2, 'PTS': 27.1, 'REB': 2.8, 'AST': 6.3, 'STL': 0.9, '3PM': 2.2 },
        'Finals': [
            { 'MIN': 37.1, 'PTS': 30.0, 'REB': 3.0, 'AST': 2.0, 'STL': 0.0, '3PM': 2.0 },
            { 'MIN': 37.7, 'PTS': 20.0, 'REB': 5.0, 'AST': 6.0, 'STL': 5.0, '3PM': 2.0 },
            { 'MIN': 35.5, 'PTS': 32.0, 'REB': 5.0, 'AST': 5.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 44.5, 'PTS': 36.0, 'REB': 5.0, 'AST': 7.0, 'STL': 3.0, '3PM': 3.0 }
        ]
    },
    {
        'Name': 'Victor Wembanyama', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 29.2, 'PTS': 25.0, 'REB': 11.5, 'AST': 3.1, 'STL': 1.0, '3PM': 1.9 },
        'Playoffs': { 'MIN': 34.8, 'PTS': 23.3, 'REB': 10.8, 'AST': 3.0, 'STL': 1.1, '3PM': 1.8 },
        'Finals': [
            { 'MIN': 37.8, 'PTS': 26.0, 'REB': 12.0, 'AST': 2.0, 'STL': 1.0, '3PM': 2.0 },
            { 'MIN': 40.0, 'PTS': 29.0, 'REB': 9.0, 'AST': 2.0, 'STL': 2.0, '3PM': 2.0 },
            { 'MIN': 38.7, 'PTS': 32.0, 'REB': 8.0, 'AST': 6.0, 'STL': 2.0, '3PM': 2.0 },
            { 'MIN': 43.9, 'PTS': 24.0, 'REB': 13.0, 'AST': 1.0, 'STL': 0.0, '3PM': 2.0 }
        ]
    },
    {
        'Name': 'Karl-Anthony Towns', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 31.0, 'PTS': 20.1, 'REB': 11.9, 'AST': 3.0, 'STL': 0.9, '3PM': 1.5 },
        'Playoffs': { 'MIN': 33.7, 'PTS': 17.0, 'REB': 10.7, 'AST': 5.7, 'STL': 1.2, '3PM': 1.5 },
        'Finals': [
            { 'MIN': 34.4, 'PTS': 18.0, 'REB': 12.0, 'AST': 4.0, 'STL': 0.0, '3PM': 0.0 },
            { 'MIN': 33.9, 'PTS': 21.0, 'REB': 13.0, 'AST': 4.0, 'STL': 1.0, '3PM': 3.0 },
            { 'MIN': 38.0, 'PTS': 11.0, 'REB': 8.0, 'AST': 1.0, 'STL': 3.0, '3PM': 0.0 },
            { 'MIN': 25.8, 'PTS': 13.0, 'REB': 10.0, 'AST': 2.0, 'STL': 0.0, '3PM': 1.0 }
        ]
    },
    {
        'Name': 'OG Anunoby', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 33.2, 'PTS': 16.7, 'REB': 5.2, 'AST': 2.2, 'STL': 1.6, '3PM': 2.3 },
        'Playoffs': { 'MIN': 33.7, 'PTS': 19.7, 'REB': 6.9, 'AST': 1.9, 'STL': 1.6, '3PM': 2.4 },
        'Finals': [
            { 'MIN': 31.1, 'PTS': 17.0, 'REB': 3.0, 'AST': 0.0, 'STL': 1.0, '3PM': 3.0 },
            { 'MIN': 36.8, 'PTS': 17.0, 'REB': 4.0, 'AST': 3.0, 'STL': 2.0, '3PM': 2.0 },
            { 'MIN': 38.0, 'PTS': 28.0, 'REB': 5.0, 'AST': 1.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 41.5, 'PTS': 33.0, 'REB': 4.0, 'AST': 1.0, 'STL': 1.0, '3PM': 7.0 }
        ]
    },
    {
        'Name': 'Stephon Castle', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 27.4, 'PTS': 14.7, 'REB': 3.7, 'AST': 4.1, 'STL': 1.1, '3PM': 1.2 },
        'Playoffs': { 'MIN': 33.5, 'PTS': 19.1, 'REB': 5.1, 'AST': 6.5, 'STL': 0.9, '3PM': 1.6 },
        'Finals': [
            { 'MIN': 34.5, 'PTS': 17.0, 'REB': 8.0, 'AST': 3.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 27.7, 'PTS': 14.0, 'REB': 4.0, 'AST': 4.0, 'STL': 1.0, '3PM': 2.0 },
            { 'MIN': 38.0, 'PTS': 23.0, 'REB': 5.0, 'AST': 5.0, 'STL': 1.0, '3PM': 2.0 },
            { 'MIN': 25.9, 'PTS': 13.0, 'REB': 5.0, 'AST': 5.0, 'STL': 0.0, '3PM': 1.0 }
        ]
    },
    {
        'Name': 'Julian Champagnie', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 27.6, 'PTS': 11.1, 'REB': 5.8, 'AST': 1.5, 'STL': 0.8, '3PM': 1.5 },
        'Playoffs': { 'MIN': 29.5, 'PTS': 11.5, 'REB': 6.0, 'AST': 1.5, 'STL': 1.1, '3PM': 2.5 },
        'Finals': [
            { 'MIN': 31.2, 'PTS': 16.0, 'REB': 10.0, 'AST': 1.0, 'STL': 0.0, '3PM': 5.0 },
            { 'MIN': 36.0, 'PTS': 8.0, 'REB': 4.0, 'AST': 1.0, 'STL': 0.0, '3PM': 2.0 },
            { 'MIN': 26.6, 'PTS': 12.0, 'REB': 1.0, 'AST': 3.0, 'STL': 1.0, '3PM': 3.0 },
            { 'MIN': 33.0, 'PTS': 5.0, 'REB': 5.0, 'AST': 3.0, 'STL': 4.0, '3PM': 1.0 }
        ]
    },
    {
        'Name': 'Dylan Harper', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 23.5, 'PTS': 11.8, 'REB': 3.4, 'AST': 3.9, 'STL': 1.1, '3PM': 0.9 },
        'Playoffs': { 'MIN': 25.7, 'PTS': 13.2, 'REB': 5.5, 'AST': 2.5, 'STL': 1.1, '3PM': 0.9 },
        'Finals': [
            { 'MIN': 27.5, 'PTS': 16.0, 'REB': 8.0, 'AST': 1.0, 'STL': 1.0, '3PM': 1.0 },
            { 'MIN': 32.3, 'PTS': 15.0, 'REB': 6.0, 'AST': 3.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 32.0, 'PTS': 13.0, 'REB': 9.0, 'AST': 4.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 32.3, 'PTS': 21.0, 'REB': 4.0, 'AST': 3.0, 'STL': 0.0, '3PM': 3.0 }
        ]
    },
    {
        'Name': 'Landry Shamet', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 23.2, 'PTS': 9.3, 'REB': 1.8, 'AST': 1.4, 'STL': 0.7, '3PM': 1.9 },
        'Playoffs': { 'MIN': 15.0, 'PTS': 6.0, 'REB': 0.8, 'AST': 0.6, 'STL': 0.5, '3PM': 1.2 },
        'Finals': [
            { 'MIN': 33.3, 'PTS': 13.0, 'REB': 1.0, 'AST': 0.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 30.2, 'PTS': 13.0, 'REB': 2.0, 'AST': 2.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 23.4, 'PTS': 3.0, 'REB': 4.0, 'AST': 2.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 20.5, 'PTS': 0.0, 'REB': 2.0, 'AST': 1.0, 'STL': 0.0, '3PM': 0.0 }
        ]
    },
    {
        'Name': 'De\'Aaron Fox', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 31.0, 'PTS': 18.6, 'REB': 3.8, 'AST': 6.2, 'STL': 1.5, '3PM': 1.6 },
        'Playoffs': { 'MIN': 34.5, 'PTS': 15.9, 'REB': 4.0, 'AST': 5.9, 'STL': 1.2, '3PM': 1.4 },
        'Finals': [
            { 'MIN': 38.0, 'PTS': 7.0, 'REB': 4.0, 'AST': 5.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 33.8, 'PTS': 20.0, 'REB': 3.0, 'AST': 5.0, 'STL': 1.0, '3PM': 2.0 },
            { 'MIN': 36.7, 'PTS': 12.0, 'REB': 3.0, 'AST': 8.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 37.4, 'PTS': 18.0, 'REB': 5.0, 'AST': 7.0, 'STL': 2.0, '3PM': 4.0 }
        ]
    },
    {
        'Name': 'Josh Hart', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 35.0, 'PTS': 12.0, 'REB': 7.4, 'AST': 4.8, 'STL': 1.1, '3PM': 1.1 },
        'Playoffs': { 'MIN': 33.0, 'PTS': 11.4, 'REB': 8.6, 'AST': 4.6, 'STL': 1.8, '3PM': 1.4 },
        'Finals': [
            { 'MIN': 26.8, 'PTS': 3.0, 'REB': 15.0, 'AST': 6.0, 'STL': 4.0, '3PM': 0.0 },
            { 'MIN': 18.2, 'PTS': 0.0, 'REB': 6.0, 'AST': 4.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 34.9, 'PTS': 16.0, 'REB': 9.0, 'AST': 5.0, 'STL': 0.0, '3PM': 4.0 },
            { 'MIN': 32.8, 'PTS': 6.0, 'REB': 8.0, 'AST': 6.0, 'STL': 2.0, '3PM': 1.0 }
        ]
    },
    {
        'Name': 'Devin Vassell', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 30.5, 'PTS': 13.9, 'REB': 4.0, 'AST': 2.5, 'STL': 0.9, '3PM': 2.5 },
        'Playoffs': { 'MIN': 34.2, 'PTS': 13.0, 'REB': 4.9, 'AST': 2.7, 'STL': 1.4, '3PM': 2.3 },
        'Finals': [
            { 'MIN': 36.0, 'PTS': 9.0, 'REB': 9.0, 'AST': 3.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 38.1, 'PTS': 14.0, 'REB': 9.0, 'AST': 5.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 38.1, 'PTS': 11.0, 'REB': 4.0, 'AST': 0.0, 'STL': 0.0, '3PM': 3.0 },
            { 'MIN': 40.4, 'PTS': 18.0, 'REB': 5.0, 'AST': 4.0, 'STL': 1.0, '3PM': 5.0 }
        ]
    },
    {
        'Name': 'Mikal Bridges', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 32.8, 'PTS': 14.4, 'REB': 3.8, 'AST': 3.7, 'STL': 1.1, '3PM': 1.9 },
        'Playoffs': { 'MIN': 31.5, 'PTS': 14.2, 'REB': 3.1, 'AST': 2.5, 'STL': 1.1, '3PM': 1.1 },
        'Finals': [
            { 'MIN': 28.2, 'PTS': 9.0, 'REB': 3.0, 'AST': 3.0, 'STL': 2.0, '3PM': 0.0 },
            { 'MIN': 40.9, 'PTS': 20.0, 'REB': 6.0, 'AST': 6.0, 'STL': 1.0, '3PM': 4.0 },
            { 'MIN': 28.7, 'PTS': 2.0, 'REB': 5.0, 'AST': 2.0, 'STL': 0.0, '3PM': 0.0 },
            { 'MIN': 28.1, 'PTS': 7.0, 'REB': 2.0, 'AST': 2.0, 'STL': 0.0, '3PM': 1.0 }
        ]
    },
    {
        'Name': 'Miles McBride', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 26.3, 'PTS': 12.0, 'REB': 2.4, 'AST': 2.6, 'STL': 0.9, '3PM': 2.7 },
        'Playoffs': { 'MIN': 19.1, 'PTS': 6.9, 'REB': 1.4, 'AST': 1.1, 'STL': 0.6, '3PM': 2.2 },
        'Finals': [
            { 'MIN': 19.5, 'PTS': 6.0, 'REB': 1.0, 'AST': 4.0, 'STL': 0.0, '3PM': 2.0 },
            { 'MIN': 18.4, 'PTS': 5.0, 'REB': 2.0, 'AST': 2.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 8.7, 'PTS': 0.0, 'REB': 0.0, 'AST': 0.0, 'STL': 0.0, '3PM': 0.0 },
            { 'MIN': 7.2, 'PTS': 0.0, 'REB': 0.0, 'AST': 0.0, 'STL': 0.0, '3PM': 0.0 }
        ]
    },
    {
        'Name': 'Keldon Johnson', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 23.3, 'PTS': 13.2, 'REB': 5.4, 'AST': 1.4, 'STL': 0.6, '3PM': 1.2 },
        'Playoffs': { 'MIN': 18.1, 'PTS': 8.4, 'REB': 3.2, 'AST': 0.9, 'STL': 0.6, '3PM': 1.4 },
        'Finals': [
            { 'MIN': 8.0, 'PTS': 3.0, 'REB': 0.0, 'AST': 0.0, 'STL': 0.0, '3PM': 1.0 },
            { 'MIN': 15.7, 'PTS': 3.0, 'REB': 4.0, 'AST': 2.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 16.8, 'PTS': 7.0, 'REB': 2.0, 'AST': 0.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 18.0, 'PTS': 2.0, 'REB': 4.0, 'AST': 1.0, 'STL': 1.0, '3PM': 0.0 }
        ]
    },
    {
        'Name': 'Mitchell Robinson', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 19.6, 'PTS': 5.7, 'REB': 8.8, 'AST': 0.9, 'STL': 0.9, '3PM': 0.0 },
        'Playoffs': { 'MIN': 14.2, 'PTS': 5.3, 'REB': 5.5, 'AST': 0.3, 'STL': 0.5, '3PM': 0.0 },
        'Finals': [
            { 'MIN': 13.2, 'PTS': 2.0, 'REB': 6.0, 'AST': 0.0, 'STL': 0.0, '3PM': 0.0 },
            { 'MIN': 14.1, 'PTS': 7.0, 'REB': 3.0, 'AST': 0.0, 'STL': 1.0, '3PM': 0.0 },
            { 'MIN': 7.1, 'PTS': 5.0, 'REB': 4.0, 'AST': 0.0, 'STL': 0.0, '3PM': 0.0 },
            { 'MIN': 13.0, 'PTS': 2.0, 'REB': 5.0, 'AST': 1.0, 'STL': 0.0, '3PM': 0.0 }
        ]
    }
]
