### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.projects
import pages.rewards
import pages.skills

import resources.ast as ast


PAGES = {
    "About Me": pages.about,
    "Projects" : pages.projects,
    "Skill": pages.skills,
    "Rewards": pages.rewards,

}

def main():
    """Main function of App"""
    
    
#     st.sidebar.title("Navigation")
#     selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    st.title("Navigation")
    selection = st.selectbox("Go to", list(PAGES.keys()))
    st.write("***")
    
    
    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are want to contract me, 
        [email me](mailto:nrtp.boon@gmail.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/naratip-boonbanyen-86778717b/)
""")
    
    
#     app.run()


if __name__ == "__main__":
    main()
    