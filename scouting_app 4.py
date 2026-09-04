import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image

# Set Page Configuration for iPad (Widescreen landscape)
st.set_page_config(
    page_title="WPU Defensive Scouting Unit",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Theme Styling (WPU Navy & Gold)
# Using completely safe triple-quoted string styling to prevent NameErrors in Python
st.markdown("""
    <style>
        .reportview-container {
            background-color: #0c2340;
            color: #ffffff;
        }
        .main-title {
            color: #c5a059;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .subtitle {
            color: #ffffff;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .scout-card {
            background-color: #1a365d;
            border: 2px solid #c5a059;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .wpu-badge {
            background-color: #0c2340;
            border: 1px solid #c5a059;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            color: #c5a059;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. LAYOUT HEADER WITH LOGO (Top Right Placement)
# ---------------------------------------------------------
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown("<div class='main-title'>🛡️ WILLIAM PENN DEFENSIVE UNIT</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Elite System-Based Scouting Assistant vs. Concordia (NE)</div>", unsafe_allow_html=True)

with header_col2:
    # Safely load the WPU Logo if it exists, otherwise use fallback text
    logo_filename = "WPU Men's Soccer Logo.png"
    if os.path.exists(logo_filename):
        try:
            logo_img = Image.open(logo_filename)
            st.image(logo_img, width=100)
        except Exception:
            st.markdown("<div class='wpu-badge'>WPU CREST</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='wpu-badge'>WPU CREST</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# 2. INITIALIZE EDITABLE DATABASE IN SESSION STATE
# ---------------------------------------------------------
if 'preferred_feet' not in st.session_state:
    st.session_state['preferred_feet'] = {
        '#9 Kai Olbrich': 'Left Foot (Confirmed)',
        '#16 Joao Pedro Moreira': 'Right Foot (Confirmed)',
        '#13 Sebastian Montino': 'Right Foot (Confirmed)',
        '#20 Jasper Hofland': 'Right Foot (Confirmed)',
        '#11 Joe McCarroll': 'Left Foot (Confirmed)',
        '#7 Milo Hegarty': 'Right Foot (Confirmed)',
        '#18 Karlo Rodriguez': 'Right Foot (Confirmed)',
        '#21 Elijah Fulton': 'TBD (Watch Warm-up)',
        '#6 William Preston': 'TBD (Watch Warm-up)',
    }

# ---------------------------------------------------------
# 3. SIDEBAR CONFIGURATIONS & CRITICAL TRIGGERS
# ---------------------------------------------------------
st.sidebar.markdown("### 🛠️ Match Controls")

# Formation selector (Fluid changes are key!)
selected_formation = st.sidebar.selectbox(
    "Set Concordia's Shape:",
    ["4-4-2 (Fake Rotation)", "4-3-3 (Wide Overload)", "4-4-1-1 (Compact Mid-Block)"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚠️ Corner-Kick Trigger")
st.sidebar.warning(
    "**SIGNAL:** #8 Hugo Garrote raises his **LEFT HAND**.\n\n"
    "**TARGET:** 6'5\" center-back **#4 Niko Nareike** at the back post.\n\n"
    "**WPU ACTION:** Immediately **double-team #4**, get physical, and disrupt his jumping stride."
)

# ---------------------------------------------------------
# 4. MAIN INTERACTIVE VIEWS (Columns)
# ---------------------------------------------------------
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown(f"### 🏟️ Concordia Shape: {selected_formation}")
    
    # ---------------------------------------------------------
    # DRAW THE SOCCER PITCH USING MATPLOTLIB (iPad-Proof!)
    # ---------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('#0c2340')  # Match WPU Navy
    ax.set_facecolor('#1e4620')        # Pitch Green
    
    # Draw simple soccer lines
    ax.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], color="white", linewidth=2)  # Outer boundary
    ax.plot([50, 50], [0, 100], color="white", linewidth=2)                        # Midline
    center_circle = plt.Circle((50, 50), 15, color="white", fill=False, linewidth=2)
    ax.add_patch(center_circle)
    
    # Penalty boxes
    ax.plot([0, 16.5, 16.5, 0], [25, 25, 75, 75], color="white", linewidth=2)      # Left box
    ax.plot([100, 83.5, 83.5, 100], [25, 25, 75, 75], color="white", linewidth=2)  # Right box
    
    # Define team positions based on selected formation
    # Concordia in WHITE (moving Left to Right), WPU in NAVY/GOLD
    if selected_formation == "4-4-2 (Fake Rotation)":
        # Attacking Strikers (Montino #13 and Hofland #20)
        ax.scatter([75, 75], [35, 65], color="white", edgecolor="#c5a059", s=400, zorder=5)
        ax.text(75, 35, "13", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        ax.text(75, 65, "20", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        ax.text(75, 28, "Montino", color="white", fontsize=8, ha="center")
        ax.text(75, 71, "Hofland", color="white", fontsize=8, ha="center")
        ax.text(82, 50, "Rotation Trigger:\n#20 drops deep, #13 runs behind", color="#c5a059", fontsize=9, ha="center", style="italic")
        
        # WPU Backline (Navy with Gold borders)
        ax.scatter([85, 85, 85, 85], [15, 38, 62, 85], color="#0c2340", edgecolor="#c5a059", s=450, zorder=5)
        ax.text(85, 15, "RB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 38, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 62, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 85, "LB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        
    elif selected_formation == "4-3-3 (Wide Overload)":
        # Strikers
        ax.scatter([78, 80, 78], [15, 50, 85], color="white", edgecolor="#c5a059", s=400, zorder=5)
        ax.text(78, 15, "16", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        ax.text(80, 50, "9", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        ax.text(78, 85, "7", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        
        # WPU Backline (Wider spacing)
        ax.scatter([85, 85, 85, 85], [10, 36, 64, 90], color="#0c2340", edgecolor="#c5a059", s=450, zorder=5)
        ax.text(85, 10, "RB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 36, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 64, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(85, 90, "LB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(70, 50, "Force Wide:\nShow them sidelines!", color="#c5a059", fontsize=10, ha="center", style="italic")
        
    else:  # 4-4-1-1
        # Striker and Shadow
        ax.scatter([80, 72], [50, 50], color="white", edgecolor="#c5a059", s=400, zorder=5)
        ax.text(80, 50, "9", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        ax.text(72, 50, "16", color="#0c2340", fontsize=10, ha="center", va="center", weight="bold", zorder=6)
        
        # WPU Backline
        ax.scatter([88, 88, 88, 88], [15, 38, 62, 85], color="#0c2340", edgecolor="#c5a059", s=450, zorder=5)
        ax.text(88, 15, "RB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(88, 38, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(88, 62, "CB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(88, 85, "LB", color="white", fontsize=9, ha="center", va="center", weight="bold", zorder=6)
        ax.text(76, 30, "Drop 2 steps early", color="#c5a059", fontsize=10, ha="center", style="italic")
        
    ax.set_xlim(-2, 102)
    ax.set_ylim(-2, 102)
    ax.axis("off")
    
    # Render the drawn matplotlib pitch cleanly
    st.pyplot(fig)
    st.write("⚽ *Matplotlib pitch is fully rendering and optimized for iPad landscape display.*")

with col_right:
    st.markdown("### 👤 Selected Striker Profile")
    
    # Dropdown matrix
    selected_player = st.selectbox(
        "Choose an Attacker to Inspect:",
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
    
    # Core Grounded Database
    player_data = {
        "#9 Kai Olbrich": {
            "height": "6'0\" (183 cm)",
            "hometown": "Bennington, Nebraska",
            "foot_default": "Left Foot (Confirmed)",
            "danger": "Main physical runner. Scored vs Bellevue on Sept 2nd. Extremely direct and aggressive inside the penalty box.",
            "rule": "Drop 2 yards early to cover the run behind. Do not get caught in flat-out sprints. Use your body to disrupt his acceleration path.",
            "photo": "IMG_2465.jpeg"
        },
        "#16 Joao Pedro Moreira": {
            "height": "5'10\" (178 cm)",
            "hometown": "Sao Paulo, Brazil",
            "foot_default": "Right Foot (Confirmed)",
            "danger": "Highly technical Brazilian dribbler. Uses step-overs and fast ground combinations.",
            "rule": "Do not dive in! Stand him up in your jockey stance, watch the ball (not his body), and wait for helper double-team.",
            "photo": "IMG_2466.jpeg"
        },
        "#13 Sebastian Montino": {
            "height": "5'7\" (170 cm)",
            "hometown": "Vina Del Mar, Chile",
            "foot_default": "Right Foot (Confirmed)",
            "danger": "Fast, high-stamina wing-back who pushes high to form their 4-4-2 shape.",
            "rule": "Force him wide to the corner flag; protect inside spaces and prevent him from cutting in.",
            "photo": "No photo on roster"
        },
        "#20 Jasper Hofland": {
            "height": "6'0\" (183 cm)",
            "hometown": "Papendrecht, Netherlands",
            "foot_default": "Right Foot (Confirmed)",
            "danger": "Senior playmaker. Got the assist against Bellevue on Sept 2nd.",
            "rule": "Midfielders must pick him up when he drops. Do not let him drag center-backs out of the defensive line.",
            "photo": "No photo on roster"
        },
        "#11 Joe McCarroll": {
            "height": "6'1\" (185 cm)",
            "hometown": "Liverpool, England",
            "foot_default": "Left Foot (Confirmed)",
            "danger": "Active transition midfielder who connects their forward runs.",
            "rule": "Block his left passing lanes; show him to his weaker right side.",
            "photo": "No photo on roster"
        },
        "#7 Milo Hegarty": {
            "height": "5'10\" (178 cm)",
            "hometown": "St. Albans, England",
            "foot_default": "Right Foot (Confirmed)",
            "danger": "Smart connector. Plays wide and looks for quick one-twos in the central channel.",
            "rule": "Protect the inside channel and cut off his horizontal return passes.",
            "photo": "IMG_2464.jpeg"
        },
        "#18 Karlo Rodriguez": {
            "height": "6'0\" (183 cm)",
            "hometown": "Omaha, Nebraska",
            "foot_default": "Right Foot (Confirmed)",
            "danger": "Athletic forward who played solid minutes against Bellevue on Sept 2nd.",
            "rule": "Enforce our tight zonal block. Stay tight and close down his turning space inside the box.",
            "photo": "IMG_2467.jpeg"
        },
        "#21 Elijah Fulton": {
            "height": "5'11\" (180 cm)",
            "hometown": "Gretna, Nebraska",
            "foot_default": "TBD (Watch Warm-up)",
            "danger": "Strong, highly aggressive freshman sub.",
            "rule": "Play very physical. Use our size advantage to cleanly push him off the ball.",
            "photo": "IMG_2468.jpeg"
        },
        "#6 William Preston": {
            "height": "5'9\" (175 cm)",
            "hometown": "Gretna, Nebraska",
            "foot_default": "TBD (Watch Warm-up)",
            "danger": "Small, very fast change-of-pace substitute forward.",
            "rule": "Close him down immediately. Do not let him turn with the ball in tight spaces.",
            "photo": "IMG_2463.jpeg"
        }
    }
    
    info = player_data[selected_player]
    
    # Display the Profile Card
    st.markdown("<div class='scout-card'>", unsafe_allow_html=True)
    st.markdown(f"<h4>👤 {selected_player}</h4>", unsafe_allow_html=True)
    st.write(f"📏 **Height:** {info['height']}")
    st.write(f"📍 **Hometown:** {info['hometown']}")
    
    # EDITABLE DOMINANT FOOT (Saves dynamically in state)
    current_foot = st.session_state['preferred_feet'][selected_player]
    new_foot = st.text_input("✍️ Dominant Foot:", value=current_foot)
    st.session_state['preferred_feet'][selected_player] = new_foot
    
    st.write(f"⚠️ **Key Danger:** {info['danger']}")
    st.warning(f"🛡️ **WPU Zonal Guarding Rule:** {info['rule']}")
    
    # Render official bio photo if it exists, otherwise leave space (No fake AI faces!)
    if info['photo'] != "No photo on roster":
        photo_path = info['photo']
        if os.path.exists(photo_path):
            try:
                img = Image.open(photo_path)
                st.image(img, caption=f"Official Bio Photo: {selected_player}", width=180)
            except Exception:
                st.markdown("🖼️ *Verified bio photo found but could not load—ensure image is uploaded.*")
        else:
            st.markdown(f"🖼️ *Official bio photo placeholder:* `{photo_path}` (Upload file to see face)")
    else:
        st.info("⚠️ *No official bio photo on CUNE roster—photo space left blank.*")
        
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚽ **Game Management (65th Minute Drop-off):** Concordia collapses physically late in halves, leading to desperation challenges (12 yellows, 1 red overall). Keep high-tempo possession to run them out of shape.")
