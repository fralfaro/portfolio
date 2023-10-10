import streamlit as st
from pathlib import Path
import base64
import requests

# Initial page config
st.set_page_config(
    page_title='Personal Portfolio',
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

# Define img_to_bytes() function
def img_to_bytes(img_url):
    response = requests.get(img_url)
    img_bytes = response.content
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Define the cs_sidebar() function
def cs_sidebar():
    """
    Personal Information
    """
    st.sidebar.markdown(
        '''[<img src='data:image/png;base64,{}' class='img-fluid' width=150 >](https://streamlit.io/)'''.format(
            img_to_bytes("https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/yo2.png")), unsafe_allow_html=True)

    st.sidebar.header('Francisco Alfaro Medina')
    st.sidebar.markdown('**Mathematician & Data Scientist**')

    st.sidebar.markdown('''
<small>
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=14&duration=3000&pause=1000&color=e69138&center=false&vCenter=false&width=477&lines=Developer,+Speaker,+Teacher;Open+Source+Contributor" alt="Typing SVG" /></a>

</small>
    ''', unsafe_allow_html=True)

    # Interests
    st.sidebar.markdown('__Interests__')
    st.sidebar.markdown('''
    <small>
    🎮 Gaming | 🏀 Basketball | 💡 Learning 

☑️ Software Development.  <br>
☑️ Statistical Modelling, Time Series. <br> 
☑️ Machine/Deep Learning.  <br> 
☑️ Cloud computing, Big Data.
    </small>
        ''', unsafe_allow_html=True)

    # Contact Information
    st.sidebar.markdown('__Contact Information__')
    st.sidebar.markdown('''
<small>
<p align="left"> 
<a href="https://www.github.com/fralfaro" target="_blank" rel="noreferrer"><img src="https://icones.pro/wp-content/uploads/2021/06/icone-github-orange.png" width="32" height="32" /></a>
<a href="https://gitlab.com/fralfaro" target="_blank" rel="noreferrer"><img src="https://cdn.worldvectorlogo.com/logos/gitlab.svg" width="32" height="32" /></a>
<a href="https://www.linkedin.com/in/faam" target="_blank" rel="noreferrer"><img src="https://www.pngmart.com/files/21/Linkedin-PNG-Clipart.png" width="32" height="32" /></a> 
<a href="https://www.stackoverflow.com/users/12886284/fralfaro" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/stackoverflow.svg" width="32" height="32" /></a>
<a href="http://www.medium.com/@fralfaro" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Eo_circle_orange_letter-m.svg/1200px-Eo_circle_orange_letter-m.svg.png" width="32" height="32" /></a>
<a href="https://www.kaggle.com/faamds" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Eo_circle_orange_letter-k.svg/1200px-Eo_circle_orange_letter-k.svg.png" width="32" height="32" /></a>
</p>


- **Email**: <small>francisco.alfaro.496@gmail.com</small>
- **Websites**: <small>[Portfolio](https://fralfaro.github.io/portfolio/), [Blog](https://fralfaro.github.io/DS-Blog/)</small>
- **Curriculum Vitae**: <small>[English](https://drive.google.com/file/d/1X-iYm9jzQmjO95-LkrKeDGUXigUbHfxI/view?usp=sharing), [Spanish](https://drive.google.com/file/d/1dgGfEKgSJwr9lObHGAOYQjSN9m0Grk_7/view?usp=sharing)</small>
</small>
            ''', unsafe_allow_html=True)

    return None

# Define the cs_body() function
def cs_body():
    """
    Portfolio Information.
    """

    # Tab menu.
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Activity", "💻 Software", "📖 Teaching", "🌐 Blog"]
    )

    # Activity Section
    with tab1:
        # Create columns for layout
        col1, col2, col3, col4 = st.columns(4)

        # Research
        with col1:
            st.subheader("Research")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/research.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [University Retention, UTFSM, 2023](https://fralfaro.github.io/portfolio/research/research/)
                 * [Reciprocal effects: Happiness and Job Performance, UTFSM, 2019](https://fralfaro.github.io/portfolio/research/research/)
                 * [University Retention - Construction Engineering, PUCV,  2019](https://fralfaro.github.io/portfolio/research/research/)
                 * [Spatial-Statistics for 3D Kriging, PUCV,  2017](https://fralfaro.github.io/portfolio/research/research/)
                 * [Fraud detection in drinking water consumption, UTFSM, 2017](https://fralfaro.github.io/portfolio/research/research/)
                 ''')

        # Talks
        with col2:
            st.subheader("Talks")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/talks.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Solving your first Kaggle competition, PyDay Chile, 2023](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/PyDayChile2023_talk.pdf)
                 * [Data Science Fundamentals, Coding Dojo Webinar, 2023](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/cd_intro_ds_talk.pdf)
                 * [Optimization in the World of Retail, V-Encuentro de Optimización, 2022](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/workshop_optimization_talk.pdf)
                 * [TDD Introduction, Meetup Python Chile, 2022](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/MeetupPythonChile_20220929_talk.pdf)
                 * [Interactive Classes with Google Colab, Mkdocs and Github Actions, Pycon LATAM, 2022](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/PyConLatam2022_talk.pdf)
                 * [Reciprocal effects: Happiness and Job Performance, FNE33 Congress, 2018](https://github.com/fralfaro/portfolio/blob/main/docs/files/talks/FNE33_talk.pdf)
                 ''')

        # Students
        with col3:
            st.subheader("Students")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/students.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Prediction and classification of course of a bank benefit. Juan Briceño, UTFSM, 2022](https://github.com/fralfaro/portfolio/blob/main/docs/files/students/memoria_juan.pdf)
                 ''')

    # Software Section
    with tab2:

        # Create columns for layout
        col1, col2, col3, col4, col5 = st.columns(5)

        # Books
        with col1:
            st.subheader("Books")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/books.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Latex Manual](https://fralfaro.github.io/latex-manual/docs/index.html)
                 * [Kaggle Courses](https://fralfaro.github.io/kaggle-courses/)
                 * [Python Data Science Handbook](https://fralfaro.github.io/python4ds-book/)
                 * [R for Data Science](https://fralfaro.github.io/r4ds-book/)
                 ''')

        # Collaboration
        with col2:
            st.subheader("Collaboration")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/collaboration.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Pandas](https://github.com/pandas-dev/pandas)
                 * [Polars-Book](https://github.com/pola-rs/polars-book)
                 * [Fastmatrix-Book](https://github.com/fralfaro/fastmatrix-book)
                 * [dviz-course](https://github.com/yy/dviz-course)
                 ''')

        # Projects
        with col3:
            st.subheader("Projects")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/projects.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Data Science Cheat Sheets](https://github.com/fralfaro/DS-Cheat-Sheets)
                 * [Streamlit Examples](https://fralfaro.github.io/Streamlit-Examples/)
                 * [Vizzu Examples](https://fralfaro.github.io/Vizzu-Examples/)

                 ''')

        # Python Packages
        with col4:
            st.subheader("Python Packages")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/python.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Fastmatrix](https://gitlab.com/fralfaro/fastmatrix)
                 ''')

    # Teaching Section
    with tab3:
        # Create columns for layout
        col1, col2, col3 = st.columns(3)

        # University Courses
        with col1:
            st.subheader("University Courses")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/university.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [MAT281 - Applications of Mathematics in Engineering (USM)](https://github.com/fralfaro/MAT281_2023)
                 * [MAT021 - Calculus and Algebra I (USM)](https://fralfaro.github.io/portfolio/teaching/universities/)
                 * [MAT022 - Calculus and Algebra II ](https://fralfaro.github.io/portfolio/teaching/universities/)
                 * [DEEP LEARNING_001V - Introduction to Deep Learning (DUOC)](https://fralfaro.github.io/portfolio/teaching/universities/)
                 ''')

        # Personal Courses
        with col2:
            st.subheader("Personal Courses")
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/personal.png")),
                unsafe_allow_html=True)

            st.markdown('''
                 * [Basic Tools - Basic tools for Data Scientists](https://gitlab.com/fralfaro/basic_tools)
                 * [R Introduction - Basic concepts about R](https://github.com/fralfaro/r_intro)
                 * [Python Introduction -  Basic concepts about Python](https://github.com/fralfaro/python_intro)
                 * [Data Manipulation - DA with Pandas & Seaborn](https://github.com/fralfaro/python_data_manipulation)
                 * [Machine Learning - ML with Scikit-learn](https://gitlab.com/fralfaro/python_machine_learning)
                 * [Software Design - Linters, testing, docs, etc.](https://gitlab.com/fralfaro/python_sdk1)
                 ''')

    # Blog Section
    with tab4:
        # Create columns for layout
        col1, col2, col3, col4, col5 = st.columns(5)

        # 2023
        with col1:
            st.subheader('2023')
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/blog.png")),
                unsafe_allow_html=True)
            st.markdown('''
                                     * [Documentación](https://fralfaro.github.io/DS-Blog/blog/posts/2023/art_docs/)
                                     * [Gitlab PDF](https://fralfaro.github.io/DS-Blog/blog/posts/2023/gitlab_pdf/)
                                     ''')

        # 2022
        with col2:
            st.subheader('2022')
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/blog.png")),
                unsafe_allow_html=True)
            st.markdown('''
                                     * [Causal Impact](https://fralfaro.github.io//DS-Blog/blog/posts/2022/2022-10-12-causal_impact/)
                                     * [Collaborative Filtering](https://fralfaro.github.io//DS-Blog/blog/posts/2022/2022-10-12-implicit/)
                                     * [TDD](https://fralfaro.github.io//DS-Blog/blog/posts/2022/2021-07-15-tdd/)
                                     * [Polars](https://fralfaro.github.io//DS-Blog/blog/posts/2022/2022-03-16-polars/)
                                     ''')

        # 2021
        with col3:
            st.subheader('2021')
            st.markdown(
                '''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 >](https://fralfaro.github.io/portfolio/research/research/)'''.format(
                    img_to_bytes(
                        "https://raw.githubusercontent.com/fralfaro/portfolio/main/docs/images/icons/blog.png")),
                unsafe_allow_html=True)
            st.markdown('''
                                     * [Impact on Digital Learning](https://fralfaro.github.io//DS-Blog/blog/posts/2021/basic-analysis-impact-on-digital-learning/)
                                     * [Fastpages](https://fralfaro.github.io//DS-Blog/blog/posts/2021/2021-08-20-fastpages/)
                                     * [Buenas Prácticas](https://fralfaro.github.io//DS-Blog/blog/posts/2021/2021-08-31-buenas_practicas/)
                                     * [Jupyter Book](https://fralfaro.github.io//DS-Blog/blog/posts/2021/2021-08-11-jb/)
                                     * [RISE](https://fralfaro.github.io//DS-Blog/blog/posts/2021/2021-08-05-rise/)
                                     * [Jupyter Noteboook](https://fralfaro.github.io//DS-Blog/blog/posts/2021/2021-07-31-jupyter/)
                                     ''')

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:1.5rem;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)



# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
