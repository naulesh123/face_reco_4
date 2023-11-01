import streamlit as st


st.set_page_config(layout="wide")
st.header("My all projects combined in this single project")


with st.form("my_form"):
    st.write("")
    slider_val = st.slider("Use the number in the CV to slide in this sliding bar")
    # checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        pass
        # st.write("slider", slider_val)

###########################################################
###########################################################

placeholder=st.empty()









############################################################
############################################################
if slider_val==99:


    st.write(" ")
    st.write(" " )

    col1, col2 = st.columns(2, gap='small')
    with col1:
        pass

        col11,col12=st.columns(2,gap="small")
        with col11:
            st.write("**NAME : NIKHIL KUMAR**")
            st.write("**BRANCH : CHEMICAL ENGINEERING**")
            st.write("**ROLL NUMBER : 120CH0099**")
            st.write("**PROGRAMME : B.TECH.**")
            st.write("**COLLEGE NAME : NIT ROURKELA**")
        with col12:
            st.image("reference_3.jpeg",width=200)





    with col2:
        # st.write("hello")
        pass

    st.write(" ")
    st.write(" ")
    col41,col42,col43,col44=st.columns(4,gap="small")
    with col41:
        # st.write("gg")
        st.write("***Movie Recommendation system***")
        # st.image()

        st.write("A full stack website developed using streamlit framework python’s natural language toolkit module , which recommends movie based on the keywords provided by user and similar type of movies, developed using")
        # st.write("")
        st.image("movie_wala.png")
        st.write("**python, Natural language toolkit, Streamlit, Pandas, Numpy**")
        # st.write("")

        gg11,gg12=st.columns(2,gap="small")

        with gg11:
            st.link_button("Project Link", "https://3qsge4wbxubs98lmkttpbt.streamlit.app/")
        with gg12:
            st.link_button("Github repo Link","https://github.com/naulesh123/hope_1")


        pass
    with col42:
        # st.write("gg")
        st.write("***Continent analysis***")

        st.write("Build a website for analysis of continents on the basis of GDP per capita , GDP growth rate , population etc")
        st.image("continent_analysis.png")
        st.write("**python, pandas, Streamlit,plotly_chart**")
        gg21,gg22=st.columns(2,gap="small")
        with gg21:
            st.link_button("Project Link","https://countriesdashboardusingapp-9y5uqe8ejvgllqcuur7jvw.streamlit.app/")
        with gg22:
            st.link_button("Github repo Link","https://github.com/naulesh123/countries_dashboard_using_streamlit")





        pass
    with col43:
        # st.write("gg")
        st.write("***House price prediction using Flask & Decision Tree***")
        st.write("Developed a fullstack website for house price prediction using **python's scikit learn** flask framework , bootstrap , used axios for data transfer between frontend and backend")
        st.image("hp_pred.png")
        st.write("**Python, Flask, Scikit‐learn’s Decision Tree, Numpy, Pandas, axios, HTML, CSS,Javascript**")
        gg31,gg32=st.columns(2,gap="small")
        with gg31:
            st.link_button("Github repo Link","https://github.com/naulesh123/house_price_predict2")


        pass
    with col44:
        # st.write("gg")
        st.write("***Marketing intern in IOCL Divisional office Barauni***")
        st.write("Worked as a marketing analyst intern at Indian Oil corporation(IOCL), managed IOCL Barauni divisional audits under Assistant Manager of Begusarai division")
        st.image("iocl_barauni_do.png",width=150)

        gg41,gg42=st.columns(2,gap="small")

        with gg41:
            st.link_button("certificate from DO","https://drive.google.com/file/d/1RLFjRxTGc8LJZjVaYBtbVog3LZgtXKrn/view?usp=drive_link")
        with gg42:
            st.link_button("Official Certificate from IOCL","https://drive.google.com/file/d/1k3vm76_RMflHwXTlYKWk3ieeOz-YM9pq/view?usp=drive_link")














        pass



    pass





