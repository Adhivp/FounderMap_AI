import streamlit as st
from gemini_app import get_gemini_data
from mind_map import create_mind_map
from options import get_startup_options, get_customization_options
import os

st.set_page_config(page_title="Team Structure", page_icon="👥")
st.title("👥 Team Structure Mind Map")

st.write("""
This mind map helps you organize your team structure by considering key components such as:
- Team Roles
- Responsibilities
- Reporting Lines
- Key Skills
- Departmental Structure
- Team Dynamics
- Recruitment Needs
- Performance Metrics
""")

startup_options = get_startup_options()
option_names = list(startup_options.keys())

selected_option = st.selectbox("Choose a mind map structure:", option_names)
selected_structure = startup_options[selected_option]

st.write(f"Selected Option: {selected_option} - {selected_structure['description']}")

user_input = st.text_area("💡 Describe your startup idea:")

customization_options = get_customization_options()
selected_layout = st.selectbox("Choose layout:", customization_options['Layouts'])
selected_color = st.selectbox("Choose color scheme:", customization_options['Colors'])
additional_features = st.multiselect("Additional Features:", customization_options['Additional Features'])
model_choice = st.selectbox(
    "Choose the model type:",
    options=["Fast (Gemini 1.5 Flash)", "Quality (Gemini 1.5 Pro)"],
    index=0
)
if "Fast" in model_choice:
    selected_model = 'fast'
else:
    selected_model = 'quality'

if st.button("Generate Mind Map"):
    if user_input:
        context = (
            "This mind map helps you organize your team structure by considering key components such as:\n"
            "- Team Roles\n"
            "- Responsibilities\n"
            "- Reporting Lines\n"
            "- Key Skills\n"
            "- Departmental Structure\n"
            "- Team Dynamics\n"
            "- Recruitment Needs\n"
            "- Performance Metrics"
        )
        mind_map_data = get_gemini_data(user_input, context, selected_structure,selected_model)
        if isinstance(mind_map_data, dict) and 'nodes' in mind_map_data and 'edges' in mind_map_data:
            fig = create_mind_map(mind_map_data, layout_option=selected_layout, color_scheme=selected_color)
            st.plotly_chart(fig)
        else:
            st.error(mind_map_data or "Failed to generate a structured response from the Gemini API.")
    else:
        st.warning("Please enter some data or a rough idea.")

logo_path = "https://i.ibb.co/4YbJCtd/Founder-Map-AI.jpg"

st.sidebar.image(
    logo_path, 
    use_column_width=False,
    width=200
)
