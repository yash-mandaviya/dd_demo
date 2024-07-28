import streamlit as st

# Set the page configuration to allow wide mode
st.set_page_config(
    page_title="Education and the Mismatch in the Labor Market",
    page_icon=":mortar_board:",
    layout="wide"
)

# Define the URLs for the modules
modules = {
    "Income Levels by Education": "https://adt-data-dynamos-wageseducation.streamlit.app",
    "Employment Trends and Insights": "https://adt-data-dynamos-employmentforecast.streamlit.app",
    "Geographic Education Distribution": "https://adt-data-dynamos-education.streamlit.app"
}

# Custom CSS for sidebar
st.markdown("""
    <style>
        .css-18e3th9 {
            font-size: 24px; /* Adjust the font size as needed */
            font-weight: bold;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.image("graphics/logo.png", use_column_width=True)  # Display the logo in the sidebar
st.sidebar.title("Dashboard")
selection = st.sidebar.radio("Go to module:", list(modules.keys()))

# Main section
st.title("Education and the Mismatch in the Labor Market: Considerations for Improving Job-Skill Alignment")

# Display content based on selection
if selection in modules:
    st.subheader(f"Module: {selection}")
    st.markdown(f'Click [here]({modules[selection]}) to view the {selection} module.', unsafe_allow_html=True)

# Footer section
st.markdown("---")
st.markdown("### Group Name : Data Dynamos")
st.markdown("&copy; 2024 Summer (Dr. Shafaq Khan) Advanced Database Topics, All rights reserved.")