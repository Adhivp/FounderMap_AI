import streamlit as st
from gemini_app import get_gemini_data
from mind_map import create_mind_map
from options import get_startup_options, get_customization_options
import os

st.set_page_config(page_title="Go-To-Market Strategy", page_icon="🛫")
st.title("🛫 Go-To-Market Strategy Mind Map")

st.write("""
This mind map helps you formulate a go-to-market strategy by considering key elements such as:
- Target Market
- Value Proposition
- Distribution Channels
- Sales Strategy
- Marketing Tactics
- Pricing Strategy
- Customer Acquisition
- Partnerships
- Metrics and KPIs
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
            "This mind map helps you formulate a go-to-market strategy by considering key elements such as:\n"
            "- Target Market\n"
            "- Value Proposition\n"
            "- Distribution Channels\n"
            "- Sales Strategy\n"
            "- Marketing Tactics\n"
            "- Pricing Strategy\n"
            "- Customer Acquisition\n"
            "- Partnerships\n"
            "- Metrics and KPIs"
        )
        mind_map_data = get_gemini_data(user_input, context, selected_structure,selected_model)
        if isinstance(mind_map_data, dict) and 'nodes' in mind_map_data and 'edges' in mind_map_data:
            
            fig = create_mind_map(mind_map_data, layout_option=selected_layout, color_scheme=selected_color)
            st.plotly_chart(fig)
        else:
            st.error(mind_map_data or "Failed to generate a structured response from the Gemini API.")
    else:
        st.warning("Please enter some data or a rough idea.")

logo_path = 'https://i.ibb.co/4YbJCtd/Founder-Map-AI.jpg'

st.sidebar.image(
    logo_path, 
    use_column_width=False,
    width=200
)
