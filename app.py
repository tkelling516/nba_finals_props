import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set page config for a premium wide layout
st.set_page_config(
    page_title="2026 NBA Finals Prop Extrapolator",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern premium styling (dark-mode friendly)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

.main-title {
    background: linear-gradient(135deg, #EC9F05 0%, #FF4E50 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    font-size: 2.8rem;
    margin-bottom: 0.2rem;
}

.sub-title {
    color: #8E9AAF;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}

.card {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
</style>
""", unsafe_allow_html=True)

# Define static player statistical profiles (Regular Season vs Playoff Averages)
players_data = [
    {
        'Name': 'Jalen Brunson', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 35.0, 'PTS': 26.0, 'REB': 3.3, 'AST': 6.8, 'STL': 0.8, '3PM': 2.6 },
        'Playoffs': { 'MIN': 36.2, 'PTS': 27.1, 'REB': 2.8, 'AST': 6.3, 'STL': 0.9, '3PM': 2.2 }
    },
    {
        'Name': 'Victor Wembanyama', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 29.2, 'PTS': 25.0, 'REB': 11.5, 'AST': 3.1, 'STL': 1.0, '3PM': 1.9 },
        'Playoffs': { 'MIN': 34.8, 'PTS': 23.3, 'REB': 10.8, 'AST': 3.0, 'STL': 1.1, '3PM': 1.8 }
    },
    {
        'Name': 'Karl-Anthony Towns', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 31.0, 'PTS': 20.1, 'REB': 11.9, 'AST': 3.0, 'STL': 0.9, '3PM': 1.5 },
        'Playoffs': { 'MIN': 33.7, 'PTS': 17.0, 'REB': 10.7, 'AST': 5.7, 'STL': 1.2, '3PM': 1.5 }
    },
    {
        'Name': 'OG Anunoby', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 33.2, 'PTS': 16.7, 'REB': 5.2, 'AST': 2.2, 'STL': 1.6, '3PM': 2.3 },
        'Playoffs': { 'MIN': 33.7, 'PTS': 19.7, 'REB': 6.9, 'AST': 1.9, 'STL': 1.6, '3PM': 2.4 }
    },
    {
        'Name': 'Stephon Castle', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 27.4, 'PTS': 14.7, 'REB': 3.7, 'AST': 4.1, 'STL': 1.1, '3PM': 1.2 },
        'Playoffs': { 'MIN': 33.5, 'PTS': 19.1, 'REB': 5.1, 'AST': 6.5, 'STL': 0.9, '3PM': 1.6 }
    },
    {
        'Name': 'Julian Champagnie', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 27.6, 'PTS': 11.1, 'REB': 5.8, 'AST': 1.5, 'STL': 0.8, '3PM': 1.5 },
        'Playoffs': { 'MIN': 29.5, 'PTS': 11.5, 'REB': 6.0, 'AST': 1.5, 'STL': 1.1, '3PM': 2.5 }
    },
    {
        'Name': 'Dylan Harper', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 23.5, 'PTS': 11.8, 'REB': 3.4, 'AST': 3.9, 'STL': 1.1, '3PM': 0.9 },
        'Playoffs': { 'MIN': 25.7, 'PTS': 13.2, 'REB': 5.5, 'AST': 2.5, 'STL': 1.1, '3PM': 0.9 }
    },
    {
        'Name': 'Landry Shamet', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 23.2, 'PTS': 9.3, 'REB': 1.8, 'AST': 1.4, 'STL': 0.7, '3PM': 1.9 },
        'Playoffs': { 'MIN': 15.0, 'PTS': 6.0, 'REB': 0.8, 'AST': 0.6, 'STL': 0.5, '3PM': 1.2 }
    },
    {
        'Name': 'De\'Aaron Fox', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 31.0, 'PTS': 18.6, 'REB': 3.8, 'AST': 6.2, 'STL': 1.5, '3PM': 1.6 },
        'Playoffs': { 'MIN': 34.5, 'PTS': 15.9, 'REB': 4.0, 'AST': 5.9, 'STL': 1.2, '3PM': 1.4 }
    },
    {
        'Name': 'Josh Hart', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 35.0, 'PTS': 12.0, 'REB': 7.4, 'AST': 4.8, 'STL': 1.1, '3PM': 1.1 },
        'Playoffs': { 'MIN': 33.0, 'PTS': 11.4, 'REB': 8.6, 'AST': 4.6, 'STL': 1.8, '3PM': 1.4 }
    },
    {
        'Name': 'Devin Vassell', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 30.5, 'PTS': 13.9, 'REB': 4.0, 'AST': 2.5, 'STL': 0.9, '3PM': 2.5 },
        'Playoffs': { 'MIN': 34.2, 'PTS': 13.0, 'REB': 4.9, 'AST': 2.7, 'STL': 1.4, '3PM': 2.3 }
    },
    {
        'Name': 'Mikal Bridges', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 32.8, 'PTS': 14.4, 'REB': 3.8, 'AST': 3.7, 'STL': 1.1, '3PM': 1.9 },
        'Playoffs': { 'MIN': 31.5, 'PTS': 14.2, 'REB': 3.1, 'AST': 2.5, 'STL': 1.1, '3PM': 1.1 }
    },
    {
        'Name': 'Miles McBride', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 26.3, 'PTS': 12.0, 'REB': 2.4, 'AST': 2.6, 'STL': 0.9, '3PM': 2.7 },
        'Playoffs': { 'MIN': 19.1, 'PTS': 6.9, 'REB': 1.4, 'AST': 1.1, 'STL': 0.6, '3PM': 2.2 }
    },
    {
        'Name': 'Keldon Johnson', 'Team': 'SAS',
        'Regular_Season': { 'MIN': 23.3, 'PTS': 13.2, 'REB': 5.4, 'AST': 1.4, 'STL': 0.6, '3PM': 1.2 },
        'Playoffs': { 'MIN': 18.1, 'PTS': 8.4, 'REB': 3.2, 'AST': 0.9, 'STL': 0.6, '3PM': 1.4 }
    },
    {
        'Name': 'Mitchell Robinson', 'Team': 'NYK',
        'Regular_Season': { 'MIN': 19.6, 'PTS': 5.7, 'REB': 8.8, 'AST': 0.9, 'STL': 0.9, '3PM': 0.0 },
        'Playoffs': { 'MIN': 14.2, 'PTS': 5.3, 'REB': 5.5, 'AST': 0.3, 'STL': 0.5, '3PM': 0.0 }
    }
]

# ----------------- SIDEBAR CONTROLS -----------------
st.sidebar.markdown("### ⚙️ App Controls")

# Mode selection weighting
blend_weight = st.sidebar.slider(
    "Playoff Weight (%)",
    min_value=0,
    max_value=100,
    value=70,
    step=5,
    help="0% uses purely 2025-26 Regular Season averages. 100% uses purely 2026 Playoff averages. Intermediate values blend both."
) / 100.0

# ----------------- DATA PROCESSING -----------------
def calculate_predictions(players, weight):
    rows = []
    for p in players:
        name = p['Name']
        team = p['Team']
        reg = p['Regular_Season']
        playoff = p['Playoffs']
        
        # Expected minutes is a blend of Regular Season and Playoff averages
        expected_min = (1.0 - weight) * reg['MIN'] + weight * playoff['MIN']
        
        player_row = {
            'Name': name,
            'Team': team,
            'Proj_MIN': expected_min
        }
        
        for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
            reg_rate = reg[stat] / reg['MIN']
            playoff_rate = playoff[stat] / playoff['MIN']
            
            # Weighted Rate
            blend_rate = (1.0 - weight) * reg_rate + weight * playoff_rate
            extrap_val = blend_rate * expected_min
            
            player_row[f'{stat}_Proj'] = round(extrap_val, 2)
            player_row[f'{stat}_Reg_Rate'] = round(reg_rate * expected_min, 2)
            player_row[f'{stat}_Playoff_Rate'] = round(playoff_rate * expected_min, 2)
            
        # Calculate expected combos
        player_row['PRA_Proj'] = round(player_row['PTS_Proj'] + player_row['REB_Proj'] + player_row['AST_Proj'], 2)
        player_row['PA_Proj'] = round(player_row['PTS_Proj'] + player_row['AST_Proj'], 2)
        player_row['PR_Proj'] = round(player_row['PTS_Proj'] + player_row['REB_Proj'], 2)
        player_row['RA_Proj'] = round(player_row['REB_Proj'] + player_row['AST_Proj'], 2)
            
        rows.append(player_row)
        
    return pd.DataFrame(rows)

df_predictions = calculate_predictions(players_data, blend_weight)

# ----------------- MAIN APP CONTENT -----------------
st.markdown('<div class="main-title">🏀 NBA Finals Game 2 Prop Extrapolator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Extrapolating points, rebounds, assists, steals, and 3-pointers by blending regular season and playoff averages.</div>', unsafe_allow_html=True)

# Top level metrics overview
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.markdown("""
    <div class="card">
        <h4 style="margin: 0; color: #EC9F05;">🏀 Game 2 Matchup</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">New York Knicks vs. San Antonio Spurs</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">June 5, 2026 | Frost Bank Center, San Antonio</span>
    </div>
    """, unsafe_allow_html=True)
with col_info2:
    st.markdown("""
    <div class="card">
        <h4 style="margin: 0; color: #FF4E50;">🏆 Series Status</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">Knicks lead 1 - 0</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">Game 1: Knicks won 105 - 95</span>
    </div>
    """, unsafe_allow_html=True)
with col_info3:
    st.markdown(f"""
    <div class="card">
        <h4 style="margin: 0; color: #4D96FF;">⚡ Weight Configuration</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">{int(blend_weight*100)}% Playoff / {int((1-blend_weight)*100)}% Regular Season</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">Expected minutes and stat rates are dynamically blended</span>
    </div>
    """, unsafe_allow_html=True)

# Tabs for organization
tab_raw_data, tab_by_prop, tab_insights = st.tabs([
    "📋 Consolidated Projections Grid", 
    "📊 Predictions by Prop Category", 
    "📰 Analyst Insights & Context"
])

# ----------------- TAB: CONSOLIDATED GRID VIEW -----------------
with tab_raw_data:
    st.subheader("📋 Consolidated Projections Grid")
    st.write("A master matrix showing all players and their expected stat lines based on blended minutes.")
    
    # Create consolidated table including combo metrics
    df_display_grid = df_predictions[['Name', 'Team', 'Proj_MIN', 'PTS_Proj', 'REB_Proj', 'AST_Proj', 'STL_Proj', '3PM_Proj', 'PRA_Proj', 'PA_Proj', 'PR_Proj', 'RA_Proj']].copy()
    df_display_grid.columns = ['Player', 'Team', 'Expected Minutes', 'Points', 'Rebounds', 'Assists', 'Steals', '3-Pointers Made', 'PTS + REB + AST', 'PTS + AST', 'PTS + REB', 'REB + AST']
    
    # Configure columns to force right justification (both header and data cells)
    st.dataframe(
        df_display_grid.style.format({
            'Expected Minutes': '{:.1f}',
            'Points': '{:.2f}',
            'Rebounds': '{:.2f}',
            'Assists': '{:.2f}',
            'Steals': '{:.2f}',
            '3-Pointers Made': '{:.2f}',
            'PTS + REB + AST': '{:.2f}',
            'PTS + AST': '{:.2f}',
            'PTS + REB': '{:.2f}',
            'REB + AST': '{:.2f}'
        }),
        use_container_width=True,
        hide_index=True,
        column_config={
            col: st.column_config.NumberColumn(col, alignment="left") for col in df_display_grid.columns if col not in ['Player', 'Team']
        } | {
            col: st.column_config.TextColumn(col, alignment="left") for col in ['Player', 'Team']
        }
    )
    st.caption("Projections calculated by applying the blended per-minute rate to the blended expected minutes.")

# ----------------- TAB: BY PROP CATEGORY -----------------
with tab_by_prop:
    st.subheader("📊 Predictions by Prop Category")
    st.write("Rank and compare players across specific stats (including combo metrics).")
    
    selected_stat = st.radio(
        "Select Stat to View:",
        [
            'PTS (Points)', 
            'REB (Rebounds)', 
            'AST (Assists)', 
            'STL (Steals)', 
            '3PM (3-Pointers Made)',
            'PTS+REB+AST (PRA)', 
            'PTS+AST (PA)', 
            'PTS+REB (PR)', 
            'REB+AST (RA)'
        ],
        horizontal=True
    )
    
    # Map selected options to dataframe column keys and pretty display names
    stat_mapping = {
        'PTS (Points)': ('PTS_Proj', 'Projected Points'),
        'REB (Rebounds)': ('REB_Proj', 'Projected Rebounds'),
        'AST (Assists)': ('AST_Proj', 'Projected Assists'),
        'STL (Steals)': ('STL_Proj', 'Projected Steals'),
        '3PM (3-Pointers Made)': ('3PM_Proj', 'Projected 3-Pointers Made'),
        'PTS+REB+AST (PRA)': ('PRA_Proj', 'Projected PTS + REB + AST'),
        'PTS+AST (PA)': ('PA_Proj', 'Projected PTS + AST'),
        'PTS+REB (PR)': ('PR_Proj', 'Projected PTS + REB'),
        'REB+AST (RA)': ('RA_Proj', 'Projected REB + AST')
    }
    
    stat_col, pretty_name = stat_mapping[selected_stat]
    
    # Create clean data slice
    df_stat = df_predictions[['Name', 'Team', stat_col]].copy()
    df_stat.columns = ['Player', 'Team', pretty_name]
    
    # Sort by Projection
    df_stat = df_stat.sort_values(by=pretty_name, ascending=False)
    
    st.dataframe(
        df_stat.style.format({
            pretty_name: '{:.2f}'
        }),
        use_container_width=True,
        hide_index=True,
        column_config={
            pretty_name: st.column_config.NumberColumn(pretty_name, alignment="left"),
            'Player': st.column_config.TextColumn('Player', alignment="left"),
            'Team': st.column_config.TextColumn('Team', alignment="left")
        }
    )

# ----------------- TAB: ANALYST INSIGHTS -----------------
with tab_insights:
    st.subheader("📰 Matchup & Rotation Analyst Insights")
    st.write("Recent trends, injury reports, and strategic notes compiled from NBA analysts leading into Game 2.")
    
    col_ins1, col_ins2 = st.columns(2)
    
    with col_ins1:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #FF4E50;">
            <h4 style="margin: 0 0 5px 0; color: #FF4E50;">🩹 Injury Updates & Status</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Mitchell Robinson (Knicks - Center)</strong>: Listed as <strong>Probable</strong> despite a fractured right-hand metacarpal. Played 13 minutes in Game 1, showing strong rebounding (6 REB) but limited offensive capabilities. Will play through a protective wrap.</li>
                <li><strong>Spurs Clean Health Report</strong>: San Antonio has zero players listed on the injury report, allowing coach Mitch Johnson a full roster to implement tactical changes after the Game 1 loss.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="border-left: 5px solid #EC9F05;">
            <h4 style="margin: 0 0 5px 0; color: #EC9F05;">🎯 Key Matchups & Ball Security</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Victor Wembanyama Turnover Focus</strong>: Had a strong double-double in Game 1 (26 PTS, 12 REB) but committed 6 turnovers against New York's half-court double-teams. Look for San Antonio to establish him at the high-post and use pick-and-pop actions in Game 2 to give him more breathing room.</li>
                <li><strong>De'Aaron Fox Perimeter Pressure</strong>: Struggled in Game 1 (7 PTS on 3-13 FG) due to the smothering perimeter defense of OG Anunoby and Mikal Bridges. Adjustments must be made to get Fox running in transition before the Knicks' half-court defense sets.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_ins2:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #4D96FF;">
            <h4 style="margin: 0 0 5px 0; color: #4D96FF;">⏱️ Minutes & Rotation Trends</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Landry Shamet (Knicks)</strong>: Logged a massive 33 minutes off the bench in Game 1 (well above his regular season/playoff baseline of ~15-20 MIN) after scoring 13 points (3 3PM). His shooting and spacing are currently prioritized by coach Mike Brown, making his high minutes projection for Game 2 very sticky.</li>
                <li><strong>Dylan Harper (Spurs)</strong>: Played 28 minutes in Game 1, compiling 16 PTS and 8 REB. He became the youngest player in Finals history to score 15+ points. His rebounding from the guard position is crucial for the Spurs' bench units.</li>
                <li><strong>Josh Hart (Knicks)</strong>: Minutes dropped to 26.8 in Game 1 (average is ~33-35) due to Shamet's hot shooting, but he still grabbed 15 rebounds. Expect coach Brown to increase Hart's minutes in Game 2 if the Spurs push the transition game.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="border-left: 5px solid #2ecc71;">
            <h4 style="margin: 0 0 5px 0; color: #2ecc71;">🔥 Streaky Perimeter Spacing</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Julian Champagnie (Spurs)</strong>: Exploded for 16 points in Game 1 on 5-of-6 shooting from deep in the first half, but went scoreless in the second half. Analysts highlight his streaky nature; maintaining ball movement to feed him open looks will be a key Spurs focus.</li>
                <li><strong>OG Anunoby (Knicks)</strong>: Scored 12 of his 17 points in the 4th quarter of Game 1 to seal the game. Shows elite conditioning despite recovering from a recent hamstring strain.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
