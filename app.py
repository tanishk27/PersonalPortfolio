import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import io

# Import data modules
from data.skills import get_skills_data
from data.projects import get_projects_data
from data.about import get_about_data, get_education_data, get_experience_data
from utils.helpers import local_css

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define navigation
def navigation():
    # Add comprehensive dark mode CSS
    st.markdown("""
    <style>
    /* Main app styling */
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    
    /* Navigation bar - force dark styling */
    [data-testid="stSidebar"] {
        background-color: #2d2d2d !important;
    }
    
    [data-testid="stSidebar"] > div {
        background-color: #2d2d2d !important;
    }
    
    /* Navigation elements - comprehensive sidebar styling */
    .sidebar .sidebar-content, .css-1d391kg, .css-17eq0hr {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }
    
    /* Sidebar background override */
    .css-1y4p8pa {
        background-color: #2d2d2d !important;
    }
    
    /* Radio button styling in sidebar */
    .stRadio > div {
        background-color: #2d2d2d !important;
    }
    
    /* All sidebar text */
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Force sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #2d2d2d !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #2d2d2d !important;
    }
    
    /* Text elements */
    .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Form inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #64b5f6 !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #64b5f6 !important;
        color: white !important;
        border: none !important;
    }
    
    /* Containers */
    .stContainer, .stColumns {
        background-color: transparent !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }
    
    /* Success/error messages */
    .stSuccess {
        background-color: #2d5a3d !important;
        color: #ffffff !important;
    }
    
    /* Headers in main content */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Make sidebar toggle/hamburger menu more visible */
    button[kind="header"] {
        background-color: #64b5f6 !important;
        color: white !important;
        border-radius: 5px !important;
        border: 2px solid #ffffff !important;
        padding: 8px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* Alternative selector for hamburger menu */
    [data-testid="collapsedControl"] {
        background-color: #64b5f6 !important;
        color: white !important;
        border-radius: 5px !important;
        border: 2px solid #ffffff !important;
        padding: 8px !important;
        font-size: 18px !important;
        box-shadow: 0 2px 8px rgba(100, 181, 246, 0.5) !important;
    }
    
    /* Sidebar header button */
    .css-1rs6os {
        background-color: #64b5f6 !important;
        color: white !important;
        border: 2px solid #ffffff !important;
    }
    
    /* Make the arrow/hamburger icon more prominent */
    [data-testid="stSidebar"] button[kind="header"] svg,
    [data-testid="collapsedControl"] svg {
        color: white !important;
        stroke: white !important;
        fill: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Simple profile section with small photo and name
    col1, col2 = st.sidebar.columns([1, 3])
    with col1:
        st.image("assets/profile_photo.jpg", width=60)
    with col2:
        st.markdown("""
        <div style="margin-top:8px;">
            <h4 style="color:#64b5f6; margin:0;">Tanishk Rane</h4>
        </div>
        """, unsafe_allow_html=True)
    
    # Add a separator
    st.sidebar.markdown("<hr style='margin:10px 0; border-color:#404040;'>", unsafe_allow_html=True)
    
    # Navigation header
    st.sidebar.markdown("""
    <div style="text-align:center; padding:5px; margin-bottom:15px;">
        <h3 style="color:#64b5f6;">Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom CSS for navigation (dark mode)
    st.markdown("""
    <style>
    div.row-widget.stRadio > div {
        flex-direction: column;
        gap: 10px;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: #3d3d3d;
        color: #ffffff;
        padding: 10px 15px;
        border-radius: 5px;
        border-left: 5px solid #64b5f6;
        cursor: pointer;
        transition: all 0.3s;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
        background-color: #4d4d4d;
    }
    </style>
    """, unsafe_allow_html=True)
    
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Skills", "About Me", "Projects", "Contact"]
    )
    
    # Add some space
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    return page

# Home page
def home():
    # Add a cover section with a background (dark mode)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2d2d2d, #404040); padding:20px; border-radius:10px; margin-bottom:20px; border: 1px solid #64b5f6;">
        <h1 style="color:#64b5f6; text-align:center; font-size:3em;">Welcome to My Portfolio</h1>
        <h3 style="color:#ffffff; text-align:center; font-weight:300;">AIML Engineer II | Deep Learning Specialist | AI Architect</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile picture placeholder using SVG with a border (dark mode)
        st.markdown("""
        <div style="padding:5px; border:2px solid #64b5f6; border-radius:10px; margin-bottom:10px; background-color:#2d2d2d;">
        """, unsafe_allow_html=True)
        st.image("assets/profile_photo.jpg", width=250)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color:#2d2d2d; padding:20px; border-radius:10px; border-left:5px solid #64b5f6; border: 1px solid #404040;">
        <p style="font-size:1.1em; line-height:1.5; color:#ffffff;">
        Hello! I'm Tanishk Rane, an AI/ML Engineer passionate about building intelligent systems that solve real-world problems. 
        With over 3 years of hands-on experience in artificial intelligence and machine learning, I specialize in transforming 
        complex data into actionable insights and scalable AI solutions.
        </p>
        <p style="font-size:1.1em; line-height:1.5; color:#ffffff;">
        My expertise spans the full spectrum of AI technologies—from traditional machine learning to cutting-edge generative AI. 
        I'm passionate about creating innovative solutions that not only demonstrate technical excellence but also deliver 
        meaningful value to businesses and users alike.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick links with styled buttons
        st.markdown("<h3>Quick Links</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Skills 🧠", key="quick_skills", use_container_width=True):
                st.session_state.page = "Skills"
                st.session_state.quick_navigation = True
                st.rerun()
        with col2:
            if st.button("Projects 🚀", key="quick_projects", use_container_width=True):
                st.session_state.page = "Projects"
                st.session_state.quick_navigation = True
                st.rerun()
        with col3:
            if st.button("Contact 📧", key="quick_contact", use_container_width=True):
                st.session_state.page = "Contact"
                st.session_state.quick_navigation = True
                st.rerun()

# Skills page
def skills():
    st.title("Technical Expertise & Skills")
    st.markdown("""
    <div style="background-color:#2d2d2d; padding:15px; border-radius:10px; margin-bottom:25px; border: 1px solid #404040;">
    <p style="font-size:1.1em; line-height:1.5; color:#ffffff;">
    My technical expertise spans the full spectrum of modern AI and software development, from cutting-edge generative AI 
    to traditional machine learning, cloud architecture, and data engineering. Each skill has been honed through real-world 
    applications and continuous learning.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get skills data categorized
    tech_skills, frameworks, tools, soft_skills = get_skills_data()
    
    # Technical Skills
    st.header("Technical Skills")
    
    # Create grid layout for technical skills
    st.subheader("Programming Languages")
    cols = st.columns(3)
    for i, skill in enumerate(tech_skills):
        with cols[i % 3]:
            st.markdown(f"**{skill}**")
    
    # Create two columns for frameworks and tools
    col1, col2 = st.columns(2)
    
    # Frameworks & Libraries
    with col1:
        st.subheader("Frameworks & Libraries")
        for skill in frameworks:
            st.markdown(f"- **{skill}**")
    
    # Tools & Platforms
    with col2:
        st.subheader("Tools & Platforms")
        for skill in tools:
            st.markdown(f"- **{skill}**")
    
    # Soft Skills
    st.header("Soft Skills")
    soft_cols = st.columns(3)
    for i, skill in enumerate(soft_skills):
        with soft_cols[i % 3]:
            st.markdown(f"**{skill}**")
    
    # Detailed expertise sections
    st.header("Areas of Expertise")
    
    with st.expander("🤖 Generative AI & Large Language Models"):
        st.markdown("""
        **Advanced GenAI Development**: I architect and deploy sophisticated generative AI solutions using state-of-the-art 
        models like GPT-4o, LLaMA2, and DeepSeek. My expertise includes:
        
        - **Agentic AI Systems**: Building intelligent agents that can reason, plan, and execute complex tasks autonomously
        - **RAG Pipelines**: Developing retrieval-augmented generation systems that achieve 90%+ relevance scores
        - **Prompt Engineering**: Crafting optimized prompts that improve model accuracy by 15-30%
        - **Model Fine-tuning**: Custom training on domain-specific data using techniques like LoRA and full fine-tuning
        - **LLM Integration**: Seamlessly integrating language models into production applications via APIs and custom endpoints
        
        Recent achievements include building a storyboard generation agent with 90% relevance score and developing 
        natural language to SQL conversion systems with high accuracy.
        """)
    
    with st.expander("🧠 Traditional Machine Learning & Deep Learning"):
        st.markdown("""
        **Classical ML & Advanced Neural Networks**: With deep expertise in both traditional and modern ML approaches:
        
        - **Computer Vision**: Developed CNNs and advanced architectures like U2-Net, YOLOv5 achieving 90%+ accuracy
        - **3D Point Cloud Processing**: Built systems for human body analysis, classification, and segmentation
        - **Time Series Forecasting**: Implemented predictive models for various business applications
        - **Anomaly Detection**: Created robust systems for identifying outliers and unusual patterns
        - **Model Optimization**: Expertise in pruning, quantization, and converting models (ONNX, TFLite) for deployment
        - **Ensemble Methods**: Combining multiple models to enhance performance and reduce artifacts by 25%
        
        Successfully deployed models achieving 82% accuracy in student risk prediction and 90%+ accuracy across 
        multimedia processing tasks.
        """)
    
    with st.expander("☁️ Cloud Architecture & MLOps"):
        st.markdown("""
        **Enterprise-Scale AI Deployment**: Specialized in building robust, scalable AI infrastructure:
        
        - **AWS Ecosystem**: Expert in EC2, Lambda, S3, Glue, Step Functions, DynamoDB, Athena, RDS, Bedrock
        - **Azure AI Platform**: Advanced usage of AI Search, AI Foundry, Functions, CosmosDB for AI solutions
        - **MLOps Pipelines**: Automated workflows reducing manual effort by 90% and deployment time by 80%
        - **Data Engineering**: Built ETL/ELT pipelines processing millions of records with PySpark and cloud services
        - **Serverless Deployment**: Optimized models for AWS Lambda execution with 35% latency reduction
        - **Workflow Automation**: Metadata-driven designs reducing setup time from weeks to days
        
        My cloud solutions handle enterprise-scale data processing while maintaining 99.9% reliability and optimal performance.
        """)
    
    with st.expander("🗣️ Natural Language Processing & Speech Technology"):
        st.markdown("""
        **Advanced NLP & Voice AI**: Comprehensive expertise in language understanding and speech processing:
        
        - **Conversational AI**: Built chatbots and voice assistants with context awareness and multi-language support
        - **Voice Cloning**: Developed TTS/STT systems achieving 90%+ naturalness and speaker similarity scores
        - **Named Entity Recognition**: Implemented NER systems for various domain applications
        - **Speech Processing**: Advanced work with Whisper and custom audio processing techniques
        - **Multimedia Parsing**: Fine-tuned NLP models achieving 95%+ accuracy on audio, video, and document data
        - **Text Analytics**: Built systems for sentiment analysis, document classification, and information extraction
        
        My NLP solutions boost efficiency by 30% through intelligent automation and advanced natural language understanding.
        """)
        
    with st.expander("🔬 Research & Innovation"):
        st.markdown("""
        **Cutting-Edge Research & Development**: Committed to advancing the field through research and innovation:
        
        - **Published Research**: Co-authored IEEE conference paper on AR-based fashion and beauty systems
        - **Proof of Concepts**: Lead development of innovative AI solutions from concept to prototype
        - **Technology Evaluation**: Conduct R&D to identify optimal models and architectures for specific use cases
        - **Knowledge Transfer**: Mentor junior engineers and conduct technical training sessions
        - **Industry Trends**: Stay current with latest AI developments and integrate emerging technologies
        - **Cross-functional Leadership**: Collaborate across teams to drive AI adoption and best practices
        
        My research-driven approach ensures solutions leverage the most effective and current AI methodologies.
        """)

# About Me page
def about_me():
    st.title("About Me")
    
    # Get about data
    about_data = get_about_data()
    education_data = get_education_data()
    experience_data = get_experience_data()
    
    # Personal Introduction
    st.header("Who I Am")
    st.write(about_data["bio"])
    
    # Experience Timeline
    st.header("Professional Experience")
    for job in experience_data:
        with st.expander(f"{job['title']} at {job['company']} ({job['period']})"):
            st.write(f"**Role:** {job['title']}")
            st.write(f"**Company:** {job['company']}")
            st.write(f"**Period:** {job['period']}")
            st.write(f"**Description:** {job['description']}")
            st.write("**Key Achievements:**")
            for achievement in job['achievements']:
                st.write(f"- {achievement}")
    
    # Education
    st.header("Education & Certifications")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Education")
        for edu in education_data["education"]:
            st.write(f"**{edu['degree']}**")
            st.write(f"{edu['institution']}, {edu['year']}")
            st.write(f"_{edu['details']}_")
            st.write("---")
    
    with col2:
        st.subheader("Certifications")
        for cert in education_data["certifications"]:
            st.write(f"**{cert['name']}**")
            st.write(f"Issued by: {cert['issuer']}, {cert['year']}")
            st.write(f"_{cert['details']}_")
            st.write("---")
    
    # Personal Interests
    st.header("Personal Interests & Hobbies")
    interests = about_data["interests"]
    
    # Display interests in a grid
    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.subheader(interest["name"])
            st.write(interest["description"])

# Projects page
def projects():
    # Title with styled header (dark mode)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2d2d2d, #404040); padding:15px; border-radius:10px; margin-bottom:20px; border: 1px solid #64b5f6;">
        <h1 style="color:#64b5f6; text-align:center;">My Projects</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color:#2d2d2d; padding:15px; border-radius:10px; margin-bottom:25px; border: 1px solid #404040;">
    <p style="font-size:1.1em; line-height:1.5; color:#ffffff;">
    Below are some of the key projects I've worked on. Each project demonstrates 
    different skills and approaches to solving problems.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get projects data
    projects_data = get_projects_data()
    
    # Display projects with enhanced styling
    for i, project in enumerate(projects_data):
        with st.container():
            # Project title with background (dark mode)
            st.markdown(f"""
            <div style="background-color:#2d2d2d; padding:15px; border-radius:10px; border-left:5px solid #64b5f6; margin-bottom:15px; border: 1px solid #404040;">
                <h2 style="color:#64b5f6;">{project["title"]}</h2>
                <p style="color:#ffffff;"><strong>Technologies:</strong> {project["technologies"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Project description (dark mode)
            st.markdown(f"<div style='margin-bottom:20px; color:#ffffff;'>{project['description']}</div>", unsafe_allow_html=True)
            
            # Key features with columns and cards
            st.subheader("Key Features")
            cols = st.columns(len(project["features"]))
            for j, feature in enumerate(project["features"]):
                with cols[j]:
                    st.markdown(f"""
                    <div style="background-color:#3d3d3d; padding:10px; border-radius:10px; height:150px; border:1px solid #404040;">
                        <h4 style="color:#64b5f6; text-align:center;">{feature['name']}</h4>
                        <p style="text-align:center; color:#ffffff;">{feature['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Project links with button styling
            st.subheader("Links")
            col1, col2 = st.columns(2)
            with col1:
                if project["github_link"]:
                    st.markdown(f"""
                    <a href="{project['github_link']}" target="_blank" style="text-decoration:none;">
                        <div style="background-color:#64b5f6; color:white; padding:10px; border-radius:5px; text-align:center;">
                            GitHub Repository
                        </div>
                    </a>
                    """, unsafe_allow_html=True)
            with col2:
                if project["live_link"]:
                    st.markdown(f"""
                    <a href="{project['live_link']}" target="_blank" style="text-decoration:none;">
                        <div style="background-color:#64b5f6; color:white; padding:10px; border-radius:5px; text-align:center;">
                            Live Project
                        </div>
                    </a>
                    """, unsafe_allow_html=True)
            
            st.markdown("<hr style='margin:30px 0;'>", unsafe_allow_html=True)

# Contact page
def contact():
    # Sleek minimalist header
    st.markdown("""
    <div style="text-align:center; margin-bottom:50px;">
        <h1 style="color:#64b5f6; font-size:2.5em; margin:0; font-weight:300;">Contact</h1>
        <p style="color:#ffffff; font-size:1.1em; margin:10px 0 0 0;">Let's discuss your next AI project</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Minimalist contact info
    st.markdown("""
    <div style="max-width:600px; margin:0 auto 60px auto;">
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:30px; text-align:center;">
            <div>
                <div style="color:#64b5f6; font-size:24px; margin-bottom:10px;">✉️</div>
                <p style="color:#ffffff; margin:0; font-size:0.9em;">tanishk.rane@gmail.com</p>
            </div>
            <div>
                <div style="color:#64b5f6; font-size:24px; margin-bottom:10px;">📱</div>
                <p style="color:#ffffff; margin:0; font-size:0.9em;">+91 7030597486</p>
            </div>
            <div>
                <div style="color:#64b5f6; font-size:24px; margin-bottom:10px;">📍</div>
                <p style="color:#ffffff; margin:0; font-size:0.9em;">Pune, India</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Social media links
    st.markdown("""
    <div style="text-align:center; margin:40px 0;">
        <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">
            <a href="https://www.linkedin.com/in/tanishkrane" target="_blank" style="text-decoration:none;">
                <div style="background-color:#0077B5; color:white; padding:12px 24px; border-radius:25px; display:inline-block; transition:all 0.3s;">
                    <span style="font-size:16px;">💼</span> LinkedIn
                </div>
            </a>
            <a href="https://github.com/tanishk27" target="_blank" style="text-decoration:none;">
                <div style="background-color:#333; color:white; padding:12px 24px; border-radius:25px; display:inline-block; transition:all 0.3s;">
                    <span style="font-size:16px;">🐙</span> GitHub
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple contact form
    st.markdown("""
    <div style="max-width:500px; margin:0 auto;">
        <h3 style="color:#ffffff; text-align:center; margin-bottom:30px; font-weight:300;">Send a Message</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered form container
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("contact_form", clear_on_submit=False):
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="your.email@example.com")
            message = st.text_area("Message", placeholder="Tell me about your project...", height=100)
            
            submit_button = st.form_submit_button("Send", use_container_width=True)
            
            if submit_button:
                if name and email and message:
                    st.success("Message sent successfully!")
                else:
                    st.error("Please fill in all fields.")

# Main app
def main():
    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    
    # Sidebar navigation - only update if different from current state
    sidebar_page = navigation()
    
    # Only update session state if sidebar selection is different
    # This prevents sidebar from overriding button clicks
    if sidebar_page != st.session_state.page and 'quick_navigation' not in st.session_state:
        st.session_state.page = sidebar_page
    
    # Clear quick navigation flag if it exists
    if 'quick_navigation' in st.session_state:
        del st.session_state.quick_navigation
    
    # Display the selected page
    if st.session_state.page == "Home":
        home()
    elif st.session_state.page == "Skills":
        skills()
    elif st.session_state.page == "About Me":
        about_me()
    elif st.session_state.page == "Projects":
        projects()
    elif st.session_state.page == "Contact":
        contact()
    
    # Footer (dark mode)
    st.sidebar.markdown("<hr style='border-color:#404040;'>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    <div style="background-color:#2d2d2d; padding:10px; border-radius:10px; margin-top:20px; text-align:center; border: 1px solid #404040;">
        <p style="color:#64b5f6; font-weight:bold;">© 2025 Tanishk Rane</p>
        <p style="font-size:0.8em; color:#ffffff;">Built with ❤️ using Streamlit</p>
        <p style="font-size:0.8em; color:#ffffff;">AIML Engineer II at Ciklum India</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
