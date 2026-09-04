import streamlit as st
import pandas as pd

# Set page configurations
st.set_page_config(
    page_title="WPU Defensive Scouting Assistant",
    page_icon="⚽",
    layout="wide",
)

# Custom Styling (WPU Navy & Gold Theme)
st.markdown("""
    <style>
        .main {
            background-color: #0c2340; /* Navy Blue */
            color: #ffffff;
        }
        .stButton>button {
            background-color: #c5a059; /* Gold */
            color: #0c2340;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #dcb873;
            color: #0c2340;
        }
        .card {
            background-color: #1a365d;
            border: 2px solid #c5a059;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .pitch-container {
            background-color: #1e4620;
            border: 4px solid #ffffff;
            border-radius: 15px;
            padding: 30px;
            position: relative;
            min-height: 450px;
            text-align: center;
        }
        .player-node {
            display: inline-block;
            background-color: #0c2340;
            color: #ffffff;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
            cursor: pointer;
        }
        .opponent-node {
            display: inline-block;
            background-color: #ffffff;
            color: #0c2340;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.title("⚽ WPU Defensive Scouting Assistant")
st.subheader("Interactive Match-Day Preparation vs. Concordia (NE)")
st.markdown("---")

# Initialize Session State for Preferred Feet to make it editable and saveable!
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
st.sidebar.image("WPU Men's Soccer Logo.png", caption="William Penn Men's Soccer", width=120)
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

# Main Screen Layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(f"### 🛡️ Defensive Unit Alignment vs. CUNE {formation}")
    
    # Render an interactive, styled tactile pitch based on the selected formation
    st.markdown("<div class='pitch-container'>", unsafe_allow_html=True)
    
    if formation == "4-4-2 (Fake Rotation)":
        st.write("⚽ **Concordia in White (4-4-2) | WPU Zonal Block in Navy**")
        st.markdown("<br>", unsafe_allow_html=True)
        # Strikers
        st.markdown("<div><span class='opponent-node'>#13</span> <span class='opponent-node'>#20</span></div>", unsafe_allow_html=True)
        st.write("⬇️ *#20 Hofland drops deep to pull our CBs. #13 Montino runs behind.*")
        # Midfield
        st.markdown("<div><span class='opponent-node'>#8</span> <span class='opponent-node'>#11</span></div>", unsafe_allow_html=True)
        # Defense
        st.markdown("<div><span class='opponent-node'>#12</span> <span class='opponent-node'>#4</span> <span class='opponent-node'>#27</span> <span class='opponent-node'>#24</span></div>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)
        st.write("**WPU Zonal Back Four (Compact Line):**")
        st.markdown("<div><span class='player-node'>LB</span> <span class='player-node'>CB</span> <span class='player-node'>CB</span> <span class='player-node'>RB</span></div>", unsafe_allow_html=True)
        st.write("ℹ️ **Zonal Rule:** CBs stay compact, protect the **'D'**, and pass #20 to our defensive midfielders. **Do not chase deep.**")

    elif formation == "4-3-3 (Wide Overload)":
        st.write("⚽ **Concordia in White (4-3-3) | WPU Zonal Block in Navy**")
        st.markdown("<br>", unsafe_allow_html=True)
        # Strikers
        st.markdown("<div><span class='opponent-node'>#16</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='opponent-node'>#9</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='opponent-node'>#7</span></div>", unsafe_allow_html=True)
        # Midfield
        st.markdown("<div><span class='opponent-node'>#8</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='opponent-node'>#11</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='opponent-node'>#20</span></div>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)
        st.write("**WPU Zonal Back Four (Forcing Outside):**")
        st.markdown("<div><span class='player-node'>LB</span> &nbsp;&nbsp;&nbsp;&nbsp; <span class='player-node'>CB</span> &nbsp;&nbsp;&nbsp;&nbsp; <span class='player-node'>CB</span> &nbsp;&nbsp;&nbsp;&nbsp; <span class='player-node'>RB</span></div>", unsafe_allow_html=True)
        st.write("ℹ️ **Zonal Rule:** Force their wingers wide to the sidelines and invite high crosses. Our tall CBs will win 100% of headers.")

    else:  # 4-4-1-1
        st.write("⚽ **Concordia in White (4-4-1-1) | WPU Zonal Block in Navy**")
        st.markdown("<br>", unsafe_allow_html=True)
        # Striker
        st.markdown("<div><span class='opponent-node'>#9</span></div>", unsafe_allow_html=True)
        # Shadow Striker
        st.markdown("<div><span class='opponent-node'>#16</span></div>", unsafe_allow_html=True)
        # Midfield
        st.markdown("<div><span class='opponent-node'>#13</span> <span class='opponent-node'>#8</span> <span class='opponent-node'>#11</span> <span class='opponent-node'>#7</span></div>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)
        st.write("**WPU Zonal Back Four:**")
        st.markdown("<div><span class='player-node'>LB</span> <span class='player-node'>CB</span> <span class='player-node'>CB</span> <span class='player-node'>RB</span></div>", unsafe_allow_html=True)
        st.write("ℹ️ **Zonal Rule:** Maintain depth. CBs drop 2 steps early to block vertical balls behind.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("✏️ *You can adjust their positions by selecting different tactical formations in the sidebar menu!*")

with col2:
    st.markdown("### 👤 Player Profile Scout Matrix")
    
    # Dropdown to select and inspect any specific opponent
    selected_player = st.selectbox(
        "Click a player's name to see their scouting profile:",
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
    st.write(f"📏 **Height:** {info['height']}")
    st.write(f"📍 **Hometown:** {info['hometown']}")
    
    # Editable Preferred Foot (Saves in Session State!)
    current_foot = st.session_state['preferred_feet'][selected_player]
    edited_foot = st.text_input(f"✍️ Preferred Foot (Edit and press Enter):", value=current_foot)
    st.session_state['preferred_feet'][selected_player] = edited_foot
    
    st.write(f"⚠️ **Key Danger:** {info['danger']}")
    st.warning(f"🛡️ **Our WPU Guarding Action:** {info['rule']}")
    
    # Reference their actual bio picture filename
    if info['photo'] != "No photo on roster":
        st.markdown(f"🖼️ **Official Bio Photo:** `{info['photo']}` (Face photo verified from roster)")
    else:
        st.markdown("⚠️ *No bio photo on official roster - leave photo area blank.*")
        
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚽ *WPU Defenders - Keep high-tempo possession to target their **65th-minute physical drop-off window**. Stay focused and win!*")
