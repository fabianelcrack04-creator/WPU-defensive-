import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image

try:
    from streamlit_drawable_canvas import st_canvas
except ImportError:
    st_canvas = None

# Set page configurations
st.set_page_config(
    page_title="WPU Defensive Scouting Assistant v3",
    page_icon="⚽",
    layout="wide",
)

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

# ----------------- BRANDING HEADER -----------------
# Let's check for WPU Logo and Sunset Background
logo_path = "WPU Men's Soccer Logo.png"
sunset_path = "Game Field (3).jpeg"

# Apply a clean, professional dark CSS style with support for a dark sunset background if it exists
if os.path.exists(sunset_path):
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: linear-gradient(rgba(12, 35, 64, 0.85), rgba(12, 35, 64, 0.85)), url("app/static/{sunset_path}");
                background-size: cover;
                background-position: center;
                color: #ffffff;
            }}
            .card {{
                background-color: rgba(26, 54, 93, 0.9);
                border: 2px solid #c5a059;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
                color: white;
            }}
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                background-color: #0c2340;
                color: #ffffff;
            }
            .card {
                background-color: #1a365d;
                border: 2px solid #c5a059;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 20px;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Main Title Grid
title_col1, title_col2 = st.columns([4, 1])
with title_col1:
    st.title("⚽ WPU Defensive Scouting Playbook")
    st.subheader("NCAA D1 / MLS-Grade Match Preparation vs. Concordia (NE)")
with title_col2:
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)

st.markdown("---")

# ----------------- SIDEBAR CONTROLS -----------------
st.sidebar.markdown("### 🛠️ Match-Day Settings")

formation = st.sidebar.selectbox(
    "Set Concordia's Formation",
    ["4-4-2 (Fake Rotation)", "4-3-3 (Wide Overload)", "4-4-1-1 (Compact Midfield)"]
)

match_phase = st.sidebar.selectbox(
    "Set Current Match State",
    ["0-20 mins (Aggressive Press)", "20-65 mins (Mid-Block Control)", "65-90 mins (Exploit Fatigue)"]
)

# Live Set-Piece Signal Box
st.sidebar.markdown("### ⚠️ Corner Kick Alert")
st.sidebar.warning(
    "**SIGNAL:** #8 Hugo Garrote raises his **LEFT HAND**.\n\n"
    "**TARGET:** 6'5\" senior center-back **#4 Niko Nareike** at the back post.\n\n"
    "**OUR ACTION:** Double-team #4 instantly and block his jumping lane physically!"
)

# ----------------- TACTICAL ENGINE (MATPLOTLIB) -----------------
def draw_soccer_pitch(formation):
    fig, ax = plt.subplots(figsize=(8, 5.5))
    fig.patch.set_facecolor('#0c2340')  # Match our navy background
    ax.set_facecolor('#1e4620')  # Green grass

    # Draw Pitch Markings
    plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], color="white", linewidth=2)  # Outer boundary
    plt.plot([50, 50], [0, 100], color="white", linewidth=2)  # Midfield line
    center_circle = plt.Circle((50, 50), 10, color="white", fill=False, linewidth=2)
    ax.add_patch(center_circle)

    # Penalty Areas (Left & Right)
    plt.plot([0, 16.5, 16.5, 0], [22, 22, 78, 78], color="white", linewidth=2)  # Left Box
    plt.plot([100, 83.5, 83.5, 100], [22, 22, 78, 78], color="white", linewidth=2)  # Right Box (Our Goal)

    # Plot WPU Defenders in solid Navy circles with Gold borders
    # Standard compact zonal back four defending the right box (goal on right)
    wpu_players = {
        'LB': (75, 15),
        'LCB': (78, 38),
        'RCB': (78, 62),
        'RB': (75, 85)
    }
    for label, pos in wpu_players.items():
        circle = plt.Circle(pos, 3.5, color='#0c2340', ec='#c5a059', lw=2.5, zorder=5)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], label, color='white', ha='center', va='center', fontweight='bold', fontsize=9, zorder=6)

    # Plot Concordia Attackers in White circles with Muted borders based on selected formation
    if formation == "4-4-2 (Fake Rotation)":
        cune_players = {
            '#13': (65, 25),  # Montino pushes high
            '#20': (60, 50),  # Hofland drops deep to pull CB
            '#8': (45, 30),
            '#11': (45, 70),
            '#12': (30, 15),
            '#4': (25, 38),
            '#27': (25, 62),
            '#24': (30, 85)
        }
        # Draw dotted line showing rotation
        plt.annotate("", xy=(82, 30), xytext=(65, 25), arrowprops=dict(arrowstyle="->", color="#c5a059", lw=2, ls="--"))
        plt.annotate("", xy=(50, 50), xytext=(60, 50), arrowprops=dict(arrowstyle="->", color="#ffffff", lw=2, ls="--"))
        ax.text(67, 34, "#13 runs deep", color="#c5a059", fontsize=9, ha='center', fontweight='bold')
        ax.text(53, 54, "#20 drops", color="white", fontsize=9, ha='center', fontweight='bold')

    elif formation == "4-3-3 (Wide Overload)":
        cune_players = {
            '#16': (70, 15),  # Wide Left
            '#9': (80, 50),   # Central Target
            '#7': (70, 85),   # Wide Right
            '#8': (55, 30),
            '#11': (48, 50),
            '#20': (55, 70),
            '#4': (30, 35),
            '#27': (30, 65)
        }
    else:  # 4-4-1-1
        cune_players = {
            '#9': (82, 50),   # Central striker
            '#16': (70, 50),  # Shadow striker
            '#13': (55, 15),
            '#8': (55, 35),
            '#11': (55, 65),
            '#7': (55, 85),
            '#4': (30, 35),
            '#27': (30, 65)
        }

    for label, pos in cune_players.items():
        circle = plt.Circle(pos, 3.5, color='white', ec='#0c2340', lw=2, zorder=5)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], label, color='#0c2340', ha='center', va='center', fontweight='bold', fontsize=9, zorder=6)

    plt.xlim(-5, 105)
    plt.ylim(-5, 105)
    plt.axis('off')
    return fig

# ----------------- MAIN PRESENTATION TABS -----------------
tab1, tab2, tab3 = st.tabs(["🛡️ Tactical Pitch Board", "✏️ Interactive Chalkboard", "👤 Player Profiles"])

with tab1:
    col_pitch, col_phase_info = st.columns([3, 1.5])
    
    with col_pitch:
        st.markdown(f"### Live Field Alignment ({formation})")
        fig = draw_soccer_pitch(formation)
        st.pyplot(fig)
        
    with col_phase_info:
        st.markdown("### ⏱️ Phase Strategy")
        
        if match_phase == "0-20 mins (Aggressive Press)":
            st.info(
                "**OBJECTIVE:** CUNE gets highly panicked and nervous early in games. "
                "In their opening matches, they committed an own goal and conceded a red card under a heavy press within the first half-hour.\n\n"
                "**ACTION:** Our strikers and midfielders must press them aggressively from kickoff. Do not let them breathe!"
            )
        elif match_phase == "20-65 mins (Mid-Block Control)":
            st.info(
                "**OBJECTIVE:** Hold a disciplined central defensive structure. "
                "Concordia has no aerial threats taller than 6'0\". They rely strictly on quick, ground-based passing to penetrate the box.\n\n"
                "**ACTION:** Clog the central passing lanes. Force their play outside to the sidelines and invite high crosses. Our tall CBs will win every ball easily."
            )
        else:  # Exploit Fatigue
            st.info(
                "**OBJECTIVE:** CUNE loses their physical stamina and defensive discipline after the 65th minute, "
                "leading to desperate challenges and card accumulation (conceded 12 yellow cards and 1 red card overall this season).\n\n"
                "**ACTION:** Keep high-tempo possession to stretch their shape, force them to chase, and attack their tired lines aggressively."
            )

with tab2:
    st.markdown("### ✏️ Interactive Coaching Chalkboard")
    st.write("Use your finger or an Apple Pencil on your iPad to draw custom runs, passes, or defensive lines directly on top of the drawing board!")
    
    if st_canvas is None:
        st.error("Please add `streamlit-drawable-canvas` to your `requirements.txt` file on GitHub to enable the interactive whiteboard feature.")
    else:
        # Draw controls
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            drawing_mode = st.selectbox("Drawing tool:", ["freedraw", "line", "rect", "circle", "transform"])
        with col_c2:
            stroke_color = st.color_picker("Ink Color:", "#FFD700")  # Default Gold
        with col_c3:
            stroke_width = st.slider("Brush Size:", 1, 15, 3)

        # Create the canvas using the tactical pitch as a background if available
        canvas_result = st_canvas(
            fill_color="rgba(255, 215, 0, 0.2)",  # Translucent gold
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color="#1e4620",  # Soccer Field Green
            height=450,
            width=800,
            drawing_mode=drawing_mode,
            key="chalkboard_canvas",
        )
        st.write("💡 *Tip: Switch tools to draw clean lines/circles, or select 'transform' to resize and move your drawings on the screen.*")

with tab3:
    st.markdown("### 👤 Player Profile Scout Matrix")
    
    selected_player = st.selectbox(
        "Select an opponent to inspect:",
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
    
    # Fully-grounded physical and tactical profiles
    player_data = {
        "#9 Kai Olbrich": {
            "hometown": "Bennington, Nebraska",
            "height": "6'0\" (183 cm)",
            "danger": "Main physical runner. Scored vs Bellevue on Sept 2nd. Highly direct and active inside the box.",
            "rule": "Drop 2 steps early. Do not get caught in flat-out sprints. Use your physical size to block his running track early.",
            "photo": "IMG_2465.jpeg"
        },
        "#16 Joao Pedro Moreira": {
            "hometown": "Sao Paulo, Brazil",
            "height": "5'10\" (178 cm)",
            "danger": "Highly technical Brazilian playmaker/dribbler. Likes step-overs and quick diagonal combinations on the floor.",
            "rule": "Do not dive in! Stand him up in a low-jockey stance, keep your eyes on the ball, and wait for helper double-team support.",
            "photo": "IMG_2466.jpeg"
        },
        "#13 Sebastian Montino": {
            "hometown": "Vina Del Mar, Chile",
            "height": "5'7\" (170 cm)",
            "danger": "Extremely fast, high-workrate wing-back who runs the flank to form their 4-4-2 attacking rotation.",
            "rule": "Force him wide to the corner flag. Prevent him from cutting inside to look for diagonal ground passes.",
            "photo": "No photo on roster"
        },
        "#20 Jasper Hofland": {
            "hometown": "Papendrecht, Netherlands",
            "height": "6'0\" (183 cm)",
            "danger": "Senior linking playmaker. Provided the critical assist against Bellevue on Sept 2nd.",
            "rule": "Our holding midfielders must step up and press him. Do not let him drag our center-backs out of the defensive line.",
            "photo": "No photo on roster"
        },
        "#11 Joe McCarroll": {
            "hometown": "Liverpool, England",
            "height": "6'1\" (185 cm)",
            "danger": "Active transitional midfielder. Runs their horizontal passing lanes.",
            "rule": "Block his left-side passing lanes and show him to his weaker right side.",
            "photo": "No photo on roster"
        },
        "#7 Milo Hegarty": {
            "hometown": "St. Albans, England",
            "height": "5'10\" (178 cm)",
            "danger": "Smart support connector. Plays wide and looks for quick one-twos in the half-spaces.",
            "rule": "Protect the inside channel. Cut off his horizontal return passes.",
            "photo": "IMG_2464.jpeg"
        },
        "#18 Karlo Rodriguez": {
            "hometown": "Omaha, Nebraska",
            "height": "6'0\" (183 cm)",
            "danger": "Athletic returning striker. Played solid minutes in their 2-0 win over Bellevue.",
            "rule": "Maintain our zonal structure. Stay tight on him to close down his turning spaces if he enters off the bench.",
            "photo": "IMG_2467.jpeg"
        },
        "#21 Elijah Fulton": {
            "hometown": "Gretna, Nebraska",
            "height": "5'11\" (180 cm)",
            "danger": "Strong, aggressive freshman substitute forward.",
            "rule": "Play very physical. Use our size advantage to cleanly push him off the ball.",
            "photo": "IMG_2468.jpeg"
        },
        "#6 William Preston": {
            "hometown": "Gretna, Nebraska",
            "height": "5'9\" (175 cm)",
            "danger": "Small, extremely quick change-of-pace substitute forward.",
            "rule": "Close him down immediately. Do not let him turn with the ball in front of our line.",
            "photo": "IMG_2463.jpeg"
        }
    }
    
    info = player_data[selected_player]
    
    col_p1, col_p2 = st.columns([1, 2])
    
    with col_p1:
        # Strict roster photo matching with fail-safe Fallbacks (No AI fakes)
        if info['photo'] != "No photo on roster" and os.path.exists(info['photo']):
            st.image(info['photo'], caption=f"{selected_player} Bio Headshot", use_container_width=True)
        elif info['photo'] != "No photo on roster":
            st.info(f"📸 {selected_player} Headshot\n\n(Upload `{info['photo']}` to GitHub to display their face)")
        else:
            st.warning("⚠️ No official headshot available on roster.")
            
    with col_p2:
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<h4>👤 {selected_player}</h4>", unsafe_allow_html=True)
        st.write(f"📏 **Height:** {info['height']}")
        st.write(f"📍 **Hometown:** {info['hometown']}")
        
        # Interactive dominant foot editor
        current_foot = st.session_state['preferred_feet'][selected_player]
        edited_foot = st.text_input(f"✍️ Confirmed Dominant Foot:", value=current_foot)
        st.session_state['preferred_feet'][selected_player] = edited_foot
        
        st.write(f"⚠️ **Key Danger:** {info['danger']}")
        st.warning(f"🛡️ **WPU Guarding Rule:** {info['rule']}")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚽ *WPU Defensive Unit - Keep high-tempo possession, maintain zonal compactness, and lock down our roles!*")
