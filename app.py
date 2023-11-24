import streamlit as st
from PIL import Image
import pandas as pd

st.title("Jefforson Ewing Peter")
st.subheader("Its not who i am underneath, Its what I do that defines me")

col1, col2 = st.columns([3,1])
with col1:
        st.subheader("About Me")
        st.text("Extremely organized with the ability to work both\n independently or as part of a team")
with col2:
    image = Image.open('21.jpeg')
    st.image(image,width = 250)
st.sidebar.caption('wish to connect?')
st.sidebar.write('jeffyewing1991@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('resume.pdf','rb')
st.sidebar.download_button('Download Resume', pdf_file,file_name='resume.pdf',mime='pdf')

#Experience
st.subheader("relevant Experience")
experience_table = pd.DataFrame({
        "Job Title":["Product Process Specialist"],
        "company" :["Best buy"],
        "Job description":["packing and processing the online orders in warehouse"],
})
experience_table = experience_table.set_index('Job Title')
st.table(experience_table)

with tab_pro:
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    bar_chart = alt.Chart(titanic_data).mark_bar().encode(
        x = 'sum(Survived):Q',
        y = 'Pclass:N',
        color = 'Pclass:N',
    ).properties(
        width = 300
    )
    scatter_plot = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age:Q',
        y = 'Fare:Q',
        color = alt.condition(interval, 'Sex', alt.value('lightgray')),
    ).properties(
        width = 500,
        height = 400
    ).add_selection(
        interval
    ).interactive()
    # Define a selection to filter the scatter plot based on the selected passenger 
    selection = alt.selection_single(fields=['Pclass'], empty = 'none')
    bar_chart = bar_chart.add_selection(selection)
    scatter_plot = scatter_plot.transform_filter(selection)
    #put any jupiter chart in streamlit just add st.altair_chart()
    st.altair_chart(bar_chart | scatter_plot)

with tab_skills:
    #Skills section in the form of bar chart

    skill_data=pd.DataFrame(
        {
            "Skills level":[90,60,60,90],
            "Skills":["Python","Tableau","mySQL","Rstudio"]
        }
    )
    skill_data=skill_data.set_index('Skills')
    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
    with st.expander("See More Skills"):
        st.write("...")

with tab_pic:
    #take a picture
    picture = st.camera_input("Take a picture with me")
    if picture:
        st.image(picture)