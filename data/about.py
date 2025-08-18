def get_about_data():
    """
    Returns personal data for the About Me section.
    
    Returns:
        dict: Dictionary containing personal information
    """
    about_data = {
        "bio": """
        As an AI/ML Engineer with over 3 years of experience, I specialize in transforming complex business challenges into 
        intelligent, scalable solutions. My journey began at Pune Institute of Computer Technology, where I graduated as the 
        Institute Topper with a 9.87 CGPA, and has evolved into a passion for building AI systems that make a real impact.
        
        Currently serving as AIML Engineer II at Ciklum India, I lead research initiatives and architect end-to-end AI solutions 
        that bridge the gap between cutting-edge research and production deployment. My work spans the entire AI spectrum—from 
        traditional machine learning algorithms to state-of-the-art generative AI applications.
        
        What drives me is the challenge of making AI not just intelligent, but practical and useful. Whether it's developing 
        conversational agents that understand context, building computer vision systems that see the world accurately, or 
        creating data pipelines that process millions of records efficiently, I'm committed to delivering solutions that 
        genuinely solve problems and create value.
        """,
        "interests": [
            {
                "name": "Deep Learning & GenAI",
                "description": "Building intelligent AI agents and working with Large Language Models like GPT and LLaMA."
            },
            {
                "name": "Computer Vision",
                "description": "Developing CV solutions including object detection, segmentation, and 3D point cloud processing."
            },
            {
                "name": "Natural Language Processing",
                "description": "Creating conversational AI applications and fine-tuning NLP models for multimedia parsing."
            },
            {
                "name": "Cloud Architecture",
                "description": "Designing scalable AI solutions on AWS and Azure with end-to-end deployment pipelines."
            },
            {
                "name": "Research & Innovation",
                "description": "Published research on Augmented Reality systems and continuously exploring cutting-edge AI techniques."
            },
            {
                "name": "Voice Technology",
                "description": "Working on voice cloning software and speech processing applications using advanced AI models."
            }
        ]
    }
    
    return about_data

def get_education_data():
    """
    Returns education and certification data.
    
    Returns:
        dict: Dictionary containing education information
    """
    education_data = {
        "education": [
            {
                "degree": "Bachelor of Engineering - Information Technology",
                "institution": "Pune Institute of Computer Technology (PICT), affiliated to SPPU",
                "year": "July 2018 - June 2022",
                "details": "CGPA: 9.87 (Institute Topper). Specialized in AI/ML, Computer Vision, and Data Engineering."
            },
            {
                "degree": "Higher Secondary Certificate (HSC) - Science",
                "institution": "Susheela Bahudhani Junior College (SBJC), HSC Board",
                "year": "2016 - 2018",
                "details": "Percentage: 92.62%. Science stream with focus on Mathematics, Physics, and Chemistry."
            },
            {
                "degree": "Secondary School Certificate (SSC)",
                "institution": "Symbiosis Secondary School, SSC Board",
                "year": "2016",
                "details": "Percentage: 94.8%. Strong foundation in core subjects with excellent academic performance."
            }
        ],
        "certifications": [
            {
                "name": "Generative AI with Large Language Models",
                "issuer": "DeepLearning.AI",
                "year": "2024",
                "details": "Advanced course on generative AI techniques and large language model implementation."
            },
            {
                "name": "Hands-on with PySpark and Spark Tuning",
                "issuer": "Udemy",
                "year": "2024",
                "details": "Comprehensive training on Apache Spark optimization and PySpark development."
            },
            {
                "name": "Build GANs",
                "issuer": "DeepLearning.AI",
                "year": "2023",
                "details": "Specialized course on Generative Adversarial Networks architecture and implementation."
            },
            {
                "name": "Ultimate AWS Certified Cloud Practitioner",
                "issuer": "Udemy",
                "year": "2023",
                "details": "AWS cloud fundamentals and cloud practitioner certification preparation."
            }
        ]
    }
    
    return education_data

def get_experience_data():
    """
    Returns professional experience data.
    
    Returns:
        list: List of dictionaries containing work experience
    """
    experience_data = [
        {
            "title": "AIML Engineer II",
            "company": "Ciklum India (Previously Infogen Labs)",
            "period": "July 2022 - Present",
            "description": """
            Lead cutting-edge AI research initiatives and architect comprehensive machine learning solutions that transform 
            business operations. Spearhead the development of intelligent systems spanning generative AI, computer vision, 
            natural language processing, and traditional ML approaches. Drive innovation through hands-on technical leadership, 
            mentoring emerging talent, and delivering production-ready AI solutions that achieve measurable business impact.
            """,
            "achievements": [
                "Built conversational and voice AI applications using LLMs (GPT, LLaMA2) and Whisper, boosting efficiency by 30%",
                "Built intelligent AI agents and integrated RAG pipelines using Azure platform and OpenAI APIs",
                "Deployed ML/DL models using FastAPI, automating workflows reducing manual effort by 90%",
                "Designed scalable ETL/ELT pipelines with PySpark and AWS Services, cutting data processing time by 80%",
                "Developed and fine-tuned U2-Net, YOLOv5 models for background segmentation, achieving 90% accuracy",
                "Automated onboarding workflows using metadata-driven design, reducing setup time from 6 weeks to 10 days",
                "Developed an Agent to convert natural language into PostgreSQL queries using LLMs with R&D on optimal workflows"
            ]
        }
    ]
    
    return experience_data
