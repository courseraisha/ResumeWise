import streamlit as st
import time

# Set page config
st.set_page_config(layout="wide", page_title="ResumeWise")

# Custom CSS for styling and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

body {
    font-family: 'Montserrat', sans-serif;
    background-color: #f5f7fa;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0rem;
}

.header {
    text-align: left;
    margin-bottom: 0rem;
    position: relative;
    overflow: hidden;
}

.header::before {
    content: '';
    position: absolute;
    top: -200%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, rgba(0,180,216,0.1) 0%, rgba(0,131,176,0.1) 100%);
    animation: rotate 20s linear infinite;
    z-index: -1;
}

@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.title {
    font-size: 4rem;
    font-weight: 700;
    color: #2c3e50;
    margin: 0;
    padding: 0;
    opacity: 0;
    transform: translateY(-20px);
    animation: fadeInDown 1s ease-out forwards;
}

.tagline {
    font-size: 1.5rem;
    color: #34495e;
    margin-top: 1rem;
    opacity: 0;
    transform: translateY(20px);
    animation: fadeInUp 1s ease-out 0.5s forwards;
}

@keyframes fadeInDown {
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
    to { opacity: 1; transform: translateY(0); }
}

.feature, .step {
    background-color: white;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1.rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feature::before, .step::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, rgba(0,180,216,0.05) 0%, rgba(0,131,176,0.05) 100%);
    transform: rotate(45deg);
    z-index: 0;
}

.feature:hover, .step:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.feature h3, .step-title {
    color: #2c3e50;
    margin-bottom: 0.5rem;
    position: relative;
    z-index: 1;
}

.feature p {
    color: #34495e;
    position: relative;
    z-index: 1;
}

.how-it-works {
    margin-top: 3rem;
    overflow: hidden;
}

.step {
    text-align: center;
    opacity: 0;
    transform: translateY(50px);
    animation: slideIn 0.5s ease-out forwards;
}

@keyframes slideIn {
    to { opacity: 1; transform: translateY(0); }
}

.step-icon {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    color: #00b4d8;
}

.step-title {
    font-weight: 600;
    font-size: 1rem;
}

.stButton > button {
    display: block;
    width: 250px;
    margin: 2rem auto;
    padding: 1rem;
    background: linear-gradient(45deg, #00b4d8, #0077be);
    color: white;
    text-align: center;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.2rem;
    border: none;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    box-shadow: 0 6px 12px rgba(0, 123, 255, 0.2);
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(120deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: 0.5s;
}

.stButton > button:hover {
    transform: scale(1.05) translateY(-3px);
    box-shadow: 0 8px 15px rgba(0, 123, 255, 0.3);
}

.stButton > button:hover::before {
    left: 100%;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(0, 180, 216, 0.7);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(0, 180, 216, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(0, 180, 216, 0);
    }
}

.stButton > button {
    animation: pulse 2s infinite;
}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Updated header with left-aligned, animated title and tagline
st.markdown("""
<div class="header">
    <h1 class="title">ResumeWise</h1>
    <p class="tagline">Your AI-powered resume optimization tool</p>
</div>
""", unsafe_allow_html=True)

# Features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">
        <h3>ATS Score Analysis</h3>
        <p>Get an ATS compatibility score by comparing your resume with job descriptions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <h3>Grammar Correction</h3>
        <p>Enhance your resume's language with our advanced grammar correction tool.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <h3>Keyword Analysis</h3>
        <p>Identify missing keywords and skills based on the job description.</p>
    </div>
    """, unsafe_allow_html=True)

# How it works (horizontal with 4 columns and animation)
st.markdown('<h2 style="text-align: center; margin-top: 3rem;">How It Works</h2>', unsafe_allow_html=True)

# Use columns for each step
col1, col2, col3, col4 = st.columns(4)

steps = [
    {"icon": "📄", "title": "Upload Resume"},
    {"icon": "📝", "title": "Add Job Description"},
    {"icon": "🤖", "title": "AI Analysis"},
    {"icon": "📊", "title": "Get Insights"}
]

for i, col in enumerate([col1, col2, col3, col4]):
    col.markdown(f"""
    <div class="step" style="animation-delay: {i * 0.2}s;">
        <div class="step-icon">{steps[i]['icon']}</div>
        <div class="step-title">{steps[i]['title']}</div>
    </div>
    """, unsafe_allow_html=True)

# Call to action
if st.button("Get Started Now"):
    st.write("Let's optimize your resume!")

st.markdown('</div>', unsafe_allow_html=True)