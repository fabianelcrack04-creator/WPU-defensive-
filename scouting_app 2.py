import streamlit as st
import pandas as pd
import os
import base64

# Set page configurations
st.set_page_config(
    page_title="WPU Defensive Scouting Assistant",
    page_icon="⚽",
    layout="wide",
)

# Helper function to convert local image to base64 for background image styling
def get_image_base64(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
        except Exception:
            return None
    return None

# Attempt to load Game Field (3).jpeg as background sunset
bg_image = get_image_base64("Game Field (3).jpeg")

if bg_image:
    # Beautiful sunset background with overlay for high text readability
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(12, 35, 64, 0.88), rgba(12, 35, 64, 0.88)), url("data:image/jpeg;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #ffffff;
        }}
        .main-header {{
            color: #c5a059; /* Gold */
            font-weight: bold;
        }}
        .stMarkdown, p, h1, h2, h3, h4, h5, h6 {{
            color: #ffffff !important;
        }}
        .stSelectbox label, .stTextInput label {{
            color: #c5a059 !important;
            font-weight: bold !important;
        }}
        .card {{
            background-color: rgba(26, 54, 93, 0.85); /* Transparent Navy */
            border: 2px solid #c5a059;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }}
        .pitch-container {{
            background-color: rgba(30, 70, 32, 0.85); /* Transparent Field Green */
            border: 4px solid #ffffff;
            border-radius: 15px;
            padding: 30px;
            position: relative;
            min-height: 450px;
            text-align: center;
        }}
        .player-node {{
            display: inline-block;
            background-color: #0c2340;
            color: #ffffff !important;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
        }}
        .opponent-node {{
            display: inline-block;
            background-color: #ffffff;
            color: #0c2340 !important;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    # High-quality fallback gradient if the background file isn't uploaded yet
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #0c2340 0%, #1a365d 100%);
            background-attachment: fixed;
            color: #ffffff;
        }
        .main-header {
            color: #c5a059;
            font-weight: bold;
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
            color: #ffffff !important;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
        }
        .opponent-node {
            display: inline-block;
            background-color: #ffffff;
            color: #0c2340 !important;
            border: 2px solid #c5a059;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 41px;
            font-weight: bold;
            text-align: center;
            margin: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

# Top Bar Layout with WPU Branding and Logo placement in top right
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown("<h1 style='color: #c5a059; margin-bottom: 0px;'>⚽ WPU Defensive Scouting Assistant</h1>", unsafe_allow_html=True)
    st.subheader("Interactive Match-Day Preparation vs. Concordia (NE)")
    
with header_col2:
    if os.path.exists("WPU Men's Soccer Logo.png"):
        st.image("WPU Men's Soccer Logo.png", width=110)
    else:
        # Graceful placeholder to prevent app crash if logo file is missing on GitHub
        st.markdown("<div style='text-align: right; font-weight: bold; color: #c5a059; border: 2px solid #c5a059; padding: 10px; border-radius: 8px; margin-top: 15px;'>🏆 WPU SOCCER</div>", unsafe_allow_html=True)

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
        '#21 Elijah Fulton': 'TBD (Observe in Play)',
        '#6 William Preston': 'TBD (Observe in Play)',
    }

# Sidebar - Main Controls
st.sidebar.markdown("### 🛠️ Match-Day Configurations")

# Formation Selector
formation = st.sidebar.selectbox(
    "Select Concordia's System Shape",
    ["4-4-2 (Fake Rotation)", "4-3-3 (Wide Overload)", "4-4-1-1 (Compact Midfield)"]
)

# Set-Piece Info Card
st.sidebar.markdown("### ⚠️ Set-Piece Trigger (Corners)")
st.sidebar.info(
    "**SIGNAL:** #8 Hugo Garrote raises his **LEFT HAND**.\n\n"
    "**TARGET:** 6'5\" center-back **#4 Niko Nareike** at the back post.\n\n"
    "**ACTION:** Immediately **double-team #4** and physically block his jump stride cleanly."
)

# App hosting helper message for when images are missing
with st.sidebar.expander("📂 Missing Images? Read Here"):
    st.write(
        "If you see warning boxes about missing images, simply upload the matching PNG or JPEG files "
        "into the exact same directory on GitHub where your `scouting_app.py` is hosted. "
        "Once uploaded, they will appear in your app automatically!"
    )

# Main Screen Layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(f"### 🛡️ Defensive Unit Alignment vs. CUNE {formation}")
    
    # Render interactive tactile pitch map
    st.markdown("<div class='pitch-container'>", unsafe_allow_html=True)
    
    if formation == "4-4-2 (Fake Rotation)":
        st.write("⚽ **Concordia in White (4-4-2) | WPU Zonal Block in Navy**")
        st.markdown("<br>", unsafe_allow_html=True)
        # Strikers
        st.markdown("<div><span class='opponent-node'>#13</span> <span class='opponent-node'>#20</span></div>", unsafe_allow_html=True)
        st.write("⬇️ *#20 Hofland drops deep to pull our CBs out. #13 Montino runs behind.*")
        # Midfield
        st.markdown("<div><span class='opponent-node'>#8</span> <span class='opponent-node'>#11</span></div>", unsafe_allow_html=True)
        # Defense
        st.markdown("<div><span class='opponent-node'>#12</span> <span class='opponent-node'>#4</span> <span class='opponent-node'>#27</span> <span class='opponent-node'>#24</span></div>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)
        st.write("**WPU Zonal Back Four (Compact Line):**")
        st.markdown("<div><span class='player-node'>LB</span> <span class='player-node'>CB</span> <span class='player-node'>CB</span> <span class='player-node'>RB</span></div>", unsafe_allow_html=True)
        st.write("ℹ️ **Zonal Rule:** CBs stay compact, protect the **'D'**, and pass #20 to midfielders. **Do not chase deep.**")

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
        st.write("ℹ️ **Zonal Rule:** Force their wingers wide to the sidelines and invite high crosses. Our tall CBs win 100% of headers.")

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
    st.write("✏️ *Change CUNE's formation shape in the sidebar to see how our zonal block shifts!*")

with col2:
    st.markdown("### 👤 Player Profile Scout Matrix")
    
    # Dropdown to select and inspect players
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
    
    # Roster data
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
            "rule": "Do not dive in! Stand him up, keep your knees bent, watch the ball (not his shoulders), and wait for helper coverage.",
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
    
    info = player_data[selected_player]
    
    # Render Profile Card
    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<h4>👤 {selected_player}</h4>", unsafe_allow_html=True)
    
    # Load player headshot image defensively
    if info['photo'] != "No photo on roster":
        if os.path.exists(info['photo']):
            st.image(info['photo'], width=180, caption=f"Official Roster Face: {selected_player}")
        else:
            # Helpful fallback warning instead of breaking the app with a MediaFileStorageError
            st.info(f"ℹ️ **Official Bio Photo:** Upload `{info['photo']}` to your GitHub repository to display his face here.")
    else:
        st.markdown("⚠️ *No official bio photo available on roster.*")
        
    st.write(f"📏 **Height:** {info['height']}")
    st.write(f"📍 **Hometown:** {info['hometown']}")
    
    # Editable Preferred Foot (Saves in Session State!)
    current_foot = st.session_state['preferred_feet'][selected_player]
    edited_foot = st.text_input(f"✍️ Preferred Foot (Edit & press Enter):", value=current_foot)
    st.session_state['preferred_feet'][selected_player] = edited_foot
    
    st.write(f"⚠️ **Key Danger:** {info['danger']}")
    st.markdown(f"<div style='border-left: 4px solid #c5a059; padding-left: 10px; margin: 10px 0;'>🛡️ **Our WPU Guarding Action:** <br><i>{info['rule']}</i></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚽ *WPU Defenders - Keep high-tempo possession to target their **65th-minute physical drop-off window**. Stay focused and win!*")
