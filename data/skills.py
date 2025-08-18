def get_skills_data():
    """
    Returns structured data for different skill categories.
    
    Returns:
        tuple: (tech_skills, frameworks, tools, soft_skills) lists
    """
    # Technical Skills - Programming Languages  
    tech_skills = ["Python", "SQL", "C++", "HTML", "CSS"]
    
    # Frameworks & Libraries
    frameworks = ["PyTorch", "TensorFlow", "FastAPI", "Flask", "Gradio", "Streamlit", "Langchain", "FastMCP", "OpenCV", "Mediapipe", "Matplotlib", "Seaborn", "Pandas", "NumPy", "PySpark", "Scikit-learn", "HuggingFace Transformers"]
    
    # Tools & Platforms (including AI/ML Techniques)
    tools = ["AWS (EC2, Lambda, S3, Glue)", "Azure (AI Search, AI Foundry)", "MySQL", "MongoDB", "PostgreSQL", "Git", "Docker", "Ngrok", "OpenAI", "Agentic AI", "CNNs", "LLMs", "RAG", "NER", "Anomaly Detection", "Prompt Engineering", "Deep Learning", "GenAI", "Computer Vision"]
    
    # Soft Skills
    soft_skills = ["Research & Development", "Team Leadership", "Mentoring Juniors", "Problem Solving", "Technical Writing", "Project Management", "Cross-functional Collaboration", "Innovation"]
    
    return tech_skills, frameworks, tools, soft_skills
