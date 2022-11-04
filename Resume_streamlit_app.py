# Imports
import streamlit as st
from PIL import Image

# Set custom page title and favicon + use entire width of browser area
image = Image.open('Professional rounded headshot.png')

st.set_page_config(page_title="Resume App", page_icon = image, layout="wide", initial_sidebar_state="expanded")

# Add background using local image file

#import base64
#def add_bg_from_local(image_file):
#    with open(image_file, "rb") as image_file:
#        encoded_string = base64.b64encode(image_file.read())
#    st.markdown(
#    f"""
#    <style>
#    .stApp {{
#        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#        background-size: cover
#    }}
#    </style>
#    """,
#    unsafe_allow_html=True
#    )
    
#add_bg_from_local('landscape-4347888_1280.jpg')    

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
#####################
# Header 
st.write('''
# Niels Decorte
##### *Resume* 
''')

#col1, col2, col3 = st.columns(3)
#col2.image(image, width=300)

col1, col2, col3 = st.columns([1,8,1])

with col1:
    st.write("")

with col2:
    st.image(image, width=250)

with col3:
    st.write("")

st.markdown('## Profile Summary', unsafe_allow_html=True)
st.info('''
On both a professional and personal level I perceive myself as a rational and thoughtful
person with attention to detail and a considerable amount of perseverance. Modest, but
straightforward and (sometimes) brutally honest. Always challenging myself, having the
urge to become better is part of who I am naturally. 'Plateauing' is not for me! Hence
it should not come as a big surprise that I'm also a competitive triathlete, aiming to
participate in the 2023 Ironman 70.3 WC for age groupers in Finland. I love the consistency
and freedom (being in nature) that triathlon has to offer in life. Professionally, a
straightforward vision, combined with some structure and efficiency are important
elements for me as a planner-type. Nonetheless, I do appreciate a dynamic/flexible
environment where there's room for initiative and personal development is encouraged.
Finally, I'm used to working autonomously, but I prefer to have team members around
me with whom you can exchange thoughts every now and then. That's how I learn new
things quickly.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #BDC4A7;">
  <!--<a class="navbar-brand" href="https://www.linkedin.com/in/niels-decorte" target="_blank">Niels Decorte</a>-->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
      <div class="mx-auto">
        <ul class="navbar-nav" me-auto order-0 >
          <li class="nav-item active">
            <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#education">Education</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#work-experience">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#projects">Projects</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#skills">Skills</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#social-media">Social Media</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#references">References</a>
          </li>
        </ul>
      </div>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Advanced MSc in Data Science for Business** (Marketing Analysis), *Ghent University*, Ghent','2019 - 2020')
st.markdown('''
- Curriculum: `Analytical Customer Relationship Management, Big Data, Database Marketing, Pricing & Revenue management, Social Media & Web Analytics, Deep Learning, Advanced Predictive Analytics`.
- Research thesis (In-company project) entitled `The analysis of web traffic and integration of analytical tools towards a user-centered website`. A close collaboration with [Westtoer](https://www.westtoer.be/); about clickstream analysis, dashboarding with Dash Plotly, recommender systems and customer segmentation using on clustering techniques.
''')

txt('**MSc in Business Economics** (Main Subject: Corporate Finance), *Ghent University*, Ghent','2017 - 2018')
st.markdown('''
- Curriculum: `Advanced Corporate Finance, Corporate Finance in Practice, Cases in Corporate Finance, Research Methods in Corporate Finance, Strategic Management, Financial Statement Analysis...`.
- Research thesis entitled `The relationship between board composition and success of high-tech ventures: the impact of venture capital representatives and independent directors`.
''')

txt('**BSc in Business Economics**, *Ghent University*, Ghent',
'2014 - 2017')

txt('**Secondary Education** (Mathematics-Sciences), *KA Erasmus De Pinte*, De Pinte',
'2008 - 2014')


#####################
st.markdown('''
## Work Experience
''')

txt('**CRM Specialist**, *Accent Jobs*, Roeselare',
'2021-Present')
st.markdown('''
An interesting mix between Business Analyst, Data Analyst and Marketing Automation
Specialist. My responsibilities include too a large extent devising and implementing
both ad hoc and automatic campaigns (e.g. onboarding journey) on a structural but
also substantive level. The problem solving part is something I greatly appreciate.
Furthermore, dashboarding (Power BI) and data analysis in general are quite prevalent
as well. Some project management here and there is required in order to keep things on
track.
''')

txt('**Department Manager**, *Decathlon*, Kortrijk',
'2018 - 2019')
st.markdown('''
A wide variety of duties among which: Designing commercial strategies based on
the needs of local customers, closing partnerships, designing work schedules, people management, aligning product offerings with local demand, organizing events in order to create new and boost existing communities. In addition, due to a sub-optimal
collaboration between two major departments, an optimization strategy was designed
in which staff and by extension also resources had to be shared. Moreover, a minimal occupation of each department had to be guaranteed at all times.
''')

txt('**Organizer Puyenbroeck Cyclocross**, *Bikearound*, Puyenbroeck',
'2017 - 2017')
st.markdown('''
A one-time off-road cycling event for all ages in favor of Sportaround, a non-profit organization. An event planning experience from start to finish. Responsibilities: financials and sponsors.
''')

txt('**Administrative Assistant** (Student Job), *Le Roy Vision Center*, Nazareth',
'2013 - 2013')

#####################
st.markdown('''
## Projects
''')
txt('**In-Company Project**, *Westtoer*, Remote',
'March 2020 - July 2020')
st.markdown('''
An actual marketing-focused data science project in close collaboration with Westtoer, in which a more profound understanding was gained about the surfing behavior of
website visitors. In order to facilitate the build of a more customer-oriented website, a variety of helpful tools were developed: an extensive dashboard with Dash Plotly, a content-based recommender system, and a customer segmentation based on multiple
clustering techniques or algorithms.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SQL`, `Pyspark`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `Numpy`, `Microsoft Office Suite`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`, `Power BI`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`Streamlit`, `Azure ML`')
txt3('Marketing Automation', '`Selligent`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/niels-decorte')
#txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/nielsdecorte/')

#####################
st.markdown('''
## References
''')
st.markdown('''
References available upon request.
''')



# Add a sidebar to the web page

# Sidebar Configuration
with st.sidebar:
 
    st.title('Details')
    st.markdown("**Address**")
    st.markdown("Jolleveld 4, 9890 Asper, Belgium")
    st.markdown("**Phone number**")
    st.markdown("0497 937171")
    st.markdown("**Email**")
    st.markdown("niels.decorte@gmail.com")
    st.markdown("**Date of birth**")
    st.markdown("1996-12-05")
    st.markdown("**Nationality**")
    st.markdown("Belgian")
    st.markdown("**Driving license**")
    st.markdown("B")
    
    st.write('')
    
    st.title('Languages')
    st.markdown("Dutch")
    st.progress(100)
    st.markdown("English")
    st.progress(90)
    st.markdown("French")
    st.progress(30)
    
    st.write('')

    st.title('Hobbies')
    st.markdown("Triathlon, loves good weather and food, self-teaching the topic of exercise physiology")
    
# Design Configuration
    st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)


# Pdf button
#from fpdf import FPDF
#import base64

#report_text = st.text_input("Add text")


#export_button = st.button("Export Resume")

#def create_download_link(val, filename):
#    b64 = base64.b64encode(val)  # val looks like b'...'
#    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

#if export_button:
#    pdf = FPDF()
#    pdf.add_page()
#    pdf.set_font('Arial', 'B', 16)
#    pdf.cell(40, 10, report_text)
    
#    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

#    st.markdown(html, unsafe_allow_html=True)
