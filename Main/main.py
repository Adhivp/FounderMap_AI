import streamlit as st
import os 

st.set_page_config(page_title="FounderMap AI", page_icon="🧠🗺️")

st.title("Welcome to FounderMap AI 🧠🗺️")

st.write("""
FounderMap AI is designed to help startup founders visualize and organize their business ideas effectively. With a range of interactive tools and features, you can create detailed mind maps and gain valuable insights to drive your startup’s success.
""")

st.write("### Key Features")

st.write("""
- **Interactive Mind Mapping**: Build and customize mind maps tailored to various aspects of your startup journey.
- **Customizable Templates**: Choose from predefined templates and structures to fit your specific needs.
- **AI-Powered Insights**: Utilize advanced AI to generate and refine your mind maps based on your input.
- **Real-Time Visualization**: See your ideas come to life with real-time updates and visualizations.
- **Comprehensive Customization**: Adjust layouts, colors, and features to suit your preferences and enhance clarity.
""")

st.write("### How It Works")

st.write("""
1. **Select a Template**: Choose from various templates to structure your mind map.
2. **Input Your Ideas**: Start by describing your startup ideas or key aspects you want to explore.
3. **Customize**: Apply different layouts, colors, and features to tailor your mind map.
4. **Generate and View**: Generate your mind map with the click of a button and view it in real-time.
5. **Refine and Save**: Make any adjustments needed and save or export your mind map for future reference.
""")

st.write("### Get Started")

st.write("""
Begin by exploring the interactive features and tools available in FounderMap AI. Enter your ideas and start creating mind maps that will guide your startup towards success.
""")

logo_path = "https://i.ibb.co/4YbJCtd/Founder-Map-AI.jpg"

st.sidebar.image(
    logo_path, 
    use_column_width=False,
    width=200
)

