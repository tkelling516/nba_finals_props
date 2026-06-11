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

# Define static player statistical profiles (Regular Season vs Playoff Averages vs Finals actuals)
from players_data import players_data

# ----------------- SIDEBAR CONTROLS -----------------
st.sidebar.markdown("### ⚙️ App Controls")

# Mode selection weighting
playoff_weight = st.sidebar.slider(
    "Playoff Weight (%)",
    min_value=0,
    max_value=100,
    value=70,
    step=5,
    help="0% uses purely 2025-26 Regular Season averages. 100% uses purely 2026 Playoff averages. Intermediate values blend both."
) / 100.0

finals_weight = st.sidebar.slider(
    "Finals Matchup Weight (%)",
    min_value=0,
    max_value=100,
    value=50,
    step=5,
    help="0% relies purely on the Season Baseline (Regular Season + Playoffs). 100% projects performance purely based on the average of Games 1, 2, 3, and 4 actuals."
) / 100.0

# ----------------- DATA PROCESSING -----------------
def calculate_predictions(players, playoff_w, finals_w):
    rows = []
    for p in players:
        name = p['Name']
        team = p['Team']
        reg = p['Regular_Season']
        playoff = p['Playoffs']
        finals = p['Finals']
        
        # Calculate Season Baseline (B)
        baseline_min = (1.0 - playoff_w) * reg['MIN'] + playoff_w * playoff['MIN']
        
        baseline_stats = {}
        for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
            reg_rate = reg[stat] / reg['MIN']
            playoff_rate = playoff[stat] / playoff['MIN']
            blend_rate = (1.0 - playoff_w) * reg_rate + playoff_w * playoff_rate
            baseline_stats[stat] = blend_rate * baseline_min
            
        # Calculate Finals Matchup Trend (M) - average of Finals actuals
        finals_min = np.mean([g['MIN'] for g in finals])
        finals_stats = {}
        for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
            finals_stats[stat] = np.mean([g[stat] for g in finals])
            
        # Final Blend Projections
        proj_min = (1.0 - finals_w) * baseline_min + finals_w * finals_min
        
        player_row = {
            'Name': name,
            'Team': team,
            'Proj_MIN': proj_min
        }
        
        for stat in ['PTS', 'REB', 'AST', 'STL', '3PM']:
            val_baseline = baseline_stats[stat]
            val_finals = finals_stats[stat]
            proj_val = (1.0 - finals_w) * val_baseline + finals_w * val_finals
            player_row[f'{stat}_Proj'] = round(proj_val, 2)
            
        # Calculate expected combos
        player_row['PRA_Proj'] = round(player_row['PTS_Proj'] + player_row['REB_Proj'] + player_row['AST_Proj'], 2)
        player_row['PA_Proj'] = round(player_row['PTS_Proj'] + player_row['AST_Proj'], 2)
        player_row['PR_Proj'] = round(player_row['PTS_Proj'] + player_row['REB_Proj'], 2)
        player_row['RA_Proj'] = round(player_row['REB_Proj'] + player_row['AST_Proj'], 2)
            
        rows.append(player_row)
        
    return pd.DataFrame(rows)

df_predictions = calculate_predictions(players_data, playoff_weight, finals_weight)

# ----------------- MAIN APP CONTENT -----------------
st.markdown('<div class="main-title">🏀 NBA Finals Game 5 Prop Extrapolator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Extrapolating points, rebounds, assists, steals, and 3-pointers by blending regular season, playoff, and actual Finals Game 1, 2, 3, & 4 averages.</div>', unsafe_allow_html=True)

# Top level metrics overview
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.markdown("""
    <div class="card">
        <h4 style="margin: 0; color: #EC9F05;">🏀 Game 5 Matchup</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">San Antonio Spurs vs. New York Knicks</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">June 13, 2026 | Frost Bank Center, San Antonio, Texas</span>
    </div>
    """, unsafe_allow_html=True)
with col_info2:
    st.markdown("""
    <div class="card">
        <h4 style="margin: 0; color: #FF4E50;">🏆 Series Status</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">Knicks lead 3 - 1</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">Game 1: NYK 105-95 | Game 2: NYK 105-104 | Game 3: SAS 115-111 | Game 4: NYK 107-106</span>
    </div>
    """, unsafe_allow_html=True)

with col_info3:
    st.markdown(f"""
    <div class="card">
        <h4 style="margin: 0; color: #4D96FF;">⚡ Weight Configuration</h4>
        <p style="margin: 5px 0 0 0; font-size: 1.1rem; font-weight: 500;">{int(finals_weight*100)}% Matchup / {int((1-finals_weight)*100)}% Baseline</p>
        <span style="font-size: 0.85rem; color: #8E9AAF;">Blends baseline projections with actual Finals stats</span>
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
    st.subheader("📰 Matchup & Rotation Analyst Insights (Leading into Game 5)")
    st.write("Recent trends, injury reports, and strategic notes compiled from NBA analysts following Game 4 at Madison Square Garden.")
    
    col_ins1, col_ins2 = st.columns(2)
    
    with col_ins1:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #FF4E50;">
            <h4 style="margin: 0 0 5px 0; color: #FF4E50;">🩹 Injury Updates & Status</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Stephon Castle (Spurs - Guard)</strong>: Castle played a reduced 25.9 minutes in Game 4, putting up 13 PTS and 5 AST. While his ankle is physically healthy, his lateral mobility was tested heavily by Jalen Brunson's high-tempo pick-and-rolls, leading to some rotation adjustments.</li>
                <li><strong>Karl-Anthony Towns (Knicks - Center)</strong>: Faced significant foul trouble in Game 4, playing only 25.8 minutes but contributing 13 PTS and 10 REB. His defensive discipline against Wembanyama's drives will dictate his floor time in Game 5.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="border-left: 5px solid #EC9F05;">
            <h4 style="margin: 0 0 5px 0; color: #EC9F05;">🎯 Key Matchups & Offensive Adjustments</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Victor Wembanyama Post Presence</strong>: Wembanyama logged 43.9 minutes in Game 4, recording 24 PTS and 13 REB but only 1 AST as the Knicks successfully denied his passing lanes. Look for SA to run more handoffs to free him up in Game 5.</li>
                <li><strong>Jalen Brunson's Playmaking</strong>: Brunson dominated Game 4 with 36 PTS and 7 AST in 44.5 minutes. He was the key driver in the Knicks' 29-point comeback. Denying him middle penetration remains the Spurs' top defensive priority.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_ins2:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #4D96FF;">
            <h4 style="margin: 0 0 5px 0; color: #4D96FF;">⏱️ Minutes & Rotation Trends</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>Josh Hart (Knicks)</strong>: Played 32.8 minutes in Game 4, contributing 6 PTS, 8 REB, and 6 AST. Hart's physical presence and transition push were critical in the second-half rally.</li>
                <li><strong>Dylan Harper (Spurs)</strong>: Harper played a massive 32.3 minutes off the bench in Game 4, scoring 21 PTS (3-6 3PM). His hot hand kept the Spurs in the game late, making him a potential starter candidate for Game 5.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="border-left: 5px solid #2ecc71;">
            <h4 style="margin: 0 0 5px 0; color: #2ecc71;">🔥 Perimeter Spacing & Shooters</h4>
            <ul style="margin: 5px 0 0 0; padding-left: 20px; font-size: 0.95rem; line-height: 1.5;">
                <li><strong>OG Anunoby (Knicks)</strong>: Delivered a legendary Game 4, scoring 33 PTS with 7-10 shooting from deep and tipping in the game-winner with 1.2s left. His gravity is the single most important factor spacing the floor for Brunson.</li>
                <li><strong>Landry Shamet (Knicks)</strong>: Shamet went scoreless in 20.5 minutes (0-2 FG) in Game 4 as his role contracted slightly in favor of Hart's defensive hustle.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

