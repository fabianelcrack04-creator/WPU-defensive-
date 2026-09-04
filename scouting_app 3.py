import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set page configurations
st.set_page_config(
    page_title="WPU Defensive Scouting Assistant",
    page_icon="⚽",
    layout="wide",
)

# Custom Styling (WPU Navy & Gold Theme + Glassmorphism Cards)
# Uses the sunset background image if it exists, otherwise falls back to solid Navy
background_style = ""
if os.path.exists("Game Field (3).jpeg"):
    background_style = """
        .main {
            background-image: linear-gradient(rgba(12, 35, 64, 0.9), rgba(12, 35, 64, 0.9)), url("Game Field (3).jpeg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #ffffff;
        }
    """
else:
    background_style = """
        .main {
            background-color: #0c2340; /* Navy Blue fallback */
            color: #ffffff;
        }
    """

st.markdown(f"""
    <style>
        {background_style}
        .stButton>button {{
            background-color: #c5a059; /* Gold */
            color: #0c2340;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            width: 100%;
        }}
        .stButton>button:hover {{
            background-color: #dcb873;
            color: #0c2340;
        }}
        .card {{
            background-color: rgba(26, 54, 93, 0.85); /* Semitransparent Glass */
            border: 2px solid #c5a059;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }}
        .logo-header {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# Application Header & Logo
# Top Right Logo Placement (Clean HTML layout to prevent overlapping)
logo_col1, logo_col2 = st.columns([4, 1])
with logo_col1:
    st.title("⚽ WPU Defensive Scouting Assistant")
    st.subheader("Interactive Match-Day Preparation vs. Concordia (NE)")
with logo_col2:
    if os.path.exists("WPU Men's Soccer Logo.png"):
        st.image("WPU Men's Soccer Logo.png", width=120)
    else:
        st.markdown("<div style='text-align: right; color: #c5a059; font-weight: bold;'>[ WPU MEN'S SOCCER ]</div>", unsafe_allow_html=True)

st.markdown("---")

# Initialize Session State for Preferred Feet to make it editable and saveable
if 'preferred_feet' not in st.session_state:
    st.session_state['preferred_feet'] = {
        '#9 Kai Olbrich': 'Left Foot (Confirmed)',
        '#16 Joao Pedro Moreira': 'Right Foot (Confirmed)',
        '#13 Sebastian Montino': 'Right Foot (Confirmed)',
        '#20 Jasper Hofland': 'Right Foot (Confirmed)',
        '#11 Joe McCarroll': 'Left Foot (Confirmed)',
        '#7 Milo Hegarty': 'Right Foot (Confirmed)',
        '#18 Karlo Rodriguez': 'Right Foot (Confirmed)',
        '#21 Elijah Fulton': 'TBD',
        '#6 William Preston': 'TBD',
    }

# Sidebar - Main Controls
st.sidebar.markdown("### 🛠️ Match-Day Configurations")

# Formation Select
formation = st.sidebar.selectbox(
    "Select Concordia's Formation",
    ["4-4-2 (Fake Rotation)", "4-3-3 (Wide Overload)", "4-4-1-1 (Compact Midfield)"]
)

# Tactical Overview Card
st.sidebar.markdown("### ⚠️ Set-Piece Trigger (Corners)")
st.sidebar.info(
    "**SIGNAL:** #8 Hugo Garrote raises his **LEFT HAND**.\n\n"
    "**TARGET:** 6'5\" center-back **#4 Niko Nareike** at the back post.\n\n"
    "**ACTION:** Immediately **double-team #4** and physically block his jump."
)

# --- MATPLOTLIB SOCCER PITCH DRAWING (Top Tier, iPad Compatible) ---
def draw_tactical_pitch(formation_name):
    # Set up figure and axis style matching WPU Navy
    fig, ax = plt.subplots(figsize=(10, 6.5))
    fig.patch.set_facecolor('#0c2340') # WPU Navy background
    ax.set_facecolor('#1e4620') # Soccer green grass
    
    # Boundary Lines
    ax.plot([0, 100, 100, 0, 0], [0, 0, 60, 60, 0], color="white", linewidth=2.5) # Outer
    ax.plot([50, 50], [0, 60], color="white", linewidth=2.5) # Halfway Line
    
    # Center Circle
    center_circle = patches.Circle((50, 30), 9.15, edgecolor="white", facecolor="none", linewidth=2.5)
    ax.add_patch(center_circle)
    ax.scatter([50], [30], color="white", s=25) # Center Spot
    
    # Left Penalty Area (WPU Defensive Zone)
    ax.plot([0, 16.5, 16.5, 0], [13.2, 13.2, 46.8, 46.8], color="white", linewidth=2.5)
    ax.plot([0, 5.5, 5.5, 0], [22, 22, 38, 38], color="white", linewidth=2.5) # Goal Box
    ax.scatter([11], [30], color="white", s=25) # Penalty Spot
    
    # Right Penalty Area (CUNE Defensive Zone)
    ax.plot([100, 83.5, 83.5, 100], [13.2, 13.2, 46.8, 46.8], color="white", linewidth=2.5)
    ax.plot([100, 94.5, 94.5, 100], [22, 22, 38, 38], color="white", linewidth=2.5) # Goal Box
    ax.scatter([89], [30], color="white", s=25) # Penalty Spot
    
    # Visual Dimensions
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 65)
    ax.axis('off')
    
    # Color Palette for Players
    wpu_color = '#0c2340' # WPU Navy
    wpu_edge = '#c5a059'  # WPU Gold
    cune_color = '#ffffff' # CUNE White
    cune_edge = '#0c2340'  # CUNE Dark Border
    
    # --- Plot WPU Zonal Defensive Line (Stays Solid in Back Four) ---
    wpu_positions = {
        'LB': (28, 10),
        'LCB': (25, 23),
        'RCB': (25, 37),
        'RB': (28, 50),
        'LCM': (38, 20),
        'RCM': (38, 40)
    }
    
    for label, pos in wpu_positions.items():
        ax.scatter(pos[0], pos[1], color=wpu_color, edgecolors=wpu_edge, s=600, zorder=5, lw=2)
        ax.text(pos[0], pos[1], label, color='white', ha='center', va='center', fontweight='bold', fontsize=9, zorder=6)
        
    # Highlight the Protected Zone ("The D")
    the_d = patches.Arc((16.5, 30), 18.3, 18.3, theta1=270, theta2=90, color="white", linewidth=2, linestyle="dashed")
    ax.add_patch(the_d)
    ax.text(14, 30, 'Protected D', color='gold', ha='center', va='center', fontsize=8, fontweight='bold', style='italic', bbox=dict(facecolor='#0c2340', alpha=0.6, boxstyle='round,pad=0.3'))
    
    # --- Plot Concordia attacking positions dynamically ---
    if formation_name == "4-4-2 (Fake Rotation)":
        # #20 drops deep to pull out LCB, #13 sprints behind from deep right flank
        # #20 Hofland position
        ax.scatter([34], [29], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(34, 29, '#20', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        # Arrow showing Hofland dropping
        ax.annotate('Drops Deep', xy=(34, 29), xytext=(48, 24),
                    arrowprops=dict(facecolor='#c5a059', edgecolor='#c5a059', width=2, headwidth=8, shrink=0.1),
                    color='white', fontsize=8, fontweight='bold', ha='center', va='bottom', bbox=dict(facecolor='#0c2340', alpha=0.7, boxstyle='round,pad=0.2'))
        
        # #13 Sebastian Montino position
        ax.scatter([18], [15], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(18, 15, '#13', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        # Arrow showing Montino running behind
        ax.annotate('Runs Behind', xy=(18, 15), xytext=(42, 8),
                    arrowprops=dict(facecolor='red', edgecolor='red', width=2, headwidth=8, shrink=0.1),
                    color='white', fontsize=8, fontweight='bold', ha='center', va='bottom', bbox=dict(facecolor='#0c2340', alpha=0.7, boxstyle='round,pad=0.2'))
        
        # Other CUNE players
        ax.scatter([48, 48], [35, 52], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(48, 35, '#8', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(48, 52, '#11', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
    elif formation_name == "4-3-3 (Wide Overload)":
        # #16 wide left, #9 central, #7 wide right
        ax.scatter([20], [8], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(20, 8, '#16', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
        ax.scatter([22], [30], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(22, 30, '#9', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
        ax.scatter([20], [52], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(20, 52, '#7', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
        # Arrows showing width
        ax.annotate('', xy=(15, 6), xytext=(20, 8), arrowprops=dict(arrowstyle="->", color="white", lw=2, ls="--"))
        ax.annotate('', xy=(15, 54), xytext=(20, 52), arrowprops=dict(arrowstyle="->", color="white", lw=2, ls="--"))
        
        # Midfielders
        ax.scatter([42, 42, 42], [20, 30, 40], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(42, 20, '#11', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(42, 30, '#8', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(42, 40, '#20', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
    else: # 4-4-1-1 Compact
        # #9 target forward, #16 shadow striker underneath
        ax.scatter([18], [30], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(18, 30, '#9', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
        ax.scatter([28], [30], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(28, 30, '#16', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        
        # Midfield 4
        ax.scatter([45, 45, 45, 45], [10, 23, 37, 50], color=cune_color, edgecolors=cune_edge, s=600, zorder=5, lw=2)
        ax.text(45, 10, '#13', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(45, 23, '#11', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(45, 37, '#8', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)
        ax.text(45, 50, '#7', color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=10, zorder=6)

    plt.tight_layout()
    return fig

# Main Screen Layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(f"### 🛡️ Defensive Unit Zonal Alignment vs. CUNE {formation}")
    
    # Render Matplotlib Pitch - Always works perfectly on iPads and mobile!
    tactical_board = draw_tactical_pitch(formation)
    st.pyplot(tactical_board)
    
    # Formatting legend card below pitch
    st.markdown("""
    <div class='card'>
        <strong>Visual Legend:</strong><br>
        🔵 <span style='color: #c5a059; font-weight: bold;'>Navy Circles:</span> WPU Defensive Unit (Zonal Shape)<br>
        ⚪ <span>White Circles:</span> Concordia (CUNE) Attacking Threat Numbers
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 👤 Player Profile Scout Matrix")
    
    # Dropdown to select and inspect any specific opponent
    selected_player = st.selectbox(
        "Select an attacker or midfielder to inspect:",
        [
            "#9 Kai Olbrich",
            "#16 Joao Pedro Moreira",
            "#13 Sebastian Montino",
            "#20 Jasper Hofland",
            "#11 Joe McCarroll",
            "#7 Milo Hegarty",
            "#18 Karlo Rodriguez",
            "#21 Elijah Fulton",
            "#6 William Preston"
        ]
    )
    
    # Detailed data dictionary for every scouted player
    player_data = {
        "#9 Kai Olbrich": {
            "hometown": "Bennington, Nebraska",
            "height": "6'0\" (183 cm)",
            "danger": "Main physical runner. Scored vs Bellevue on Sept 2nd. Very aggressive in the box.",
            "rule": "Drop 2 yards early. Do not get caught in flat-out sprints. Use your body to disrupt his run path before he accelerates.",
            "photo": "IMG_2465.jpeg"
        },
        "#16 Joao Pedro Moreira": {
            "hometown": "Sao Paulo, Brazil",
            "height": "5'10\" (178 cm)",
            "danger": "Highly technical Brazilian dribbler. Loves step-overs and quick ground combinations.",
            "rule": "Do not dive in! Stand him up, keep your knees bent, watch the ball (not his shoulders), and wait for help.",
            "photo": "IMG_2466.jpeg"
        },
        "#13 Sebastian Montino": {
            "hometown": "Vina Del Mar, Chile",
            "height": "5'7\" (170 cm)",
            "danger": "Extremely fast wing-back who runs the sideline to form their 4-4-2 attacking shape.",
            "rule": "Force him to the corner flag; do not let him cut inside.",
            "photo": "No photo on roster"
        },
        "#20 Jasper Hofland": {
            "hometown": "Papendrecht, Netherlands",
            "height": "6'0\" (183 cm)",
            "danger": "Senior playmaker. Got the game-winning assist against Bellevue on Sept 2nd.",
            "rule": "Midfielders must step up to press him. Do not let him drag our center-backs deep.",
            "photo": "No photo on roster"
        },
        "#11 Joe McCarroll": {
            "hometown": "Liverpool, England",
            "height": "6'1\" (185 cm)",
            "danger": "Active transitional midfielder. Runs their forward passing lanes.",
            "rule": "Block his left-side passing lanes and force him to play backward or to his right.",
            "photo": "No photo on roster"
        },
        "#7 Milo Hegarty": {
            "hometown": "St. Albans, England",
            "height": "5'10\" (178 cm)",
            "danger": "Smart support forward. Plays wide and looks for quick one-twos.",
            "rule": "Protect the inside channel. Cut off his horizontal return passes.",
            "photo": "IMG_2464.jpeg"
        },
        "#18 Karlo Rodriguez": {
            "hometown": "Omaha, Nebraska",
            "height": "6'0\" (183 cm)",
            "danger": "Athletic returning striker. Played solid minutes in their 2-0 win over Bellevue.",
            "rule": "Enforce our zonal block. Stay alert if he enters late; close his turning spaces.",
            "photo": "IMG_2467.jpeg"
        },
        "#21 Elijah Fulton": {
            "hometown": "Gretna, Nebraska",
            "height": "5'11\" (180 cm)",
            "danger": "Strong, highly aggressive freshman substitute forward.",
            "rule": "Play very physical. Use our size advantage to cleanly push him off the ball.",
            "photo": "IMG_2468.jpeg"
        },
        "#6 William Preston": {
            "hometown": "Gretna, Nebraska",
            "height": "5'9\" (175 cm)",
            "danger": "Small, very quick change-of-pace substitute forward.",
            "rule": "Close him down immediately. Do not let him turn with the ball.",
            "photo": "IMG_2463.jpeg"
        }
    }
    
    # Retrieve data for selected player
    info = player_data[selected_player]
    
    # Display Profile Card
    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<h4>👤 {selected_player}</h4>", unsafe_allow_html=True)
    
    # Display official image safely if it exists, otherwise use fallback
    image_loaded = False
    if info['photo'] != "No photo on roster":
        if os.path.exists(info['photo']):
            st.image(info['photo'], caption=f"Verified face of {selected_player}", width=220)
            image_loaded = True
        else:
            st.warning(f"⚠️ Image file `{info['photo']}` is registered but not uploaded to GitHub yet.")
    
    if not image_loaded and info['photo'] != "No photo on roster":
        st.info("ℹ️ Roster image is selected but cannot render because the image file is missing from your repository.")
    elif info['photo'] == "No photo on roster":
        st.markdown("<div style='background-color: #0c2340; border: 1px dashed #c5a059; border-radius: 8px; padding: 15px; text-align: center; font-style: italic;'>No photo available on official roster.</div>", unsafe_allow_html=True)
        st.write("")

    st.write(f"📏 **Height:** {info['height']}")
    st.write(f"📍 **Hometown:** {info['hometown']}")
    
    # Editable Preferred Foot (Saves in Session State)
    current_foot = st.session_state['preferred_feet'][selected_player]
    edited_foot = st.text_input(f"✍️ Preferred Foot (Edit and press Enter):", value=current_foot)
    st.session_state['preferred_feet'][selected_player] = edited_foot
    
    st.write(f"⚠️ **Key Danger:** {info['danger']}")
    st.warning(f"🛡️ **Our WPU Guarding Action:** {info['rule']}")
    
    st.markdown("</div> division", unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚽ *WPU Defenders - Keep high-tempo possession to target their **65th-minute physical drop-off window**. Stay focused and win!*")
