def get_projects_data():
    """
    Returns a list of projects with their details.
    
    Returns:
        list: List of dictionaries containing project information
    """
    projects = [
        {
            "title": "Aptara - Storyboard Agent",
            "description": """
            Orchestrated the end-to-end construction of a RAG-based AI Agent utilizing Azure AI Search and Azure
            Foundry, achieving a 90% relevance score in storyboard content generation and reducing research time.
            Fine-tuned GPT-4o model using Azure AI Foundry with JSONL format, increasing output accuracy by 15%.
            """,
            "technologies": "Python, Azure AI Search, Azure Foundry, GPT-4o, RAG, JSONL",
            "features": [
                {
                    "name": "RAG-based AI Agent",
                    "description": "Intelligent agent with 90% relevance score for content generation"
                },
                {
                    "name": "Azure Integration",
                    "description": "Automated workflows reducing manual configuration by 75%"
                },
                {
                    "name": "Model Fine-tuning",
                    "description": "GPT-4o optimization with 15% accuracy improvement"
                }
            ],
            "github_link": None,
            "live_link": None
        },
        {
            "title": "AI-Based Interior Design Application",
            "description": """
            Contributed to an AI-powered interior design app for Android and iOS, featuring style transfer, 
            paint simulation, object replacement, and design rendering using diffusion models and VLMs.
            Boosted visual realism by 30% through prompt engineering and workflow optimization.
            """,
            "technologies": "Python, Diffusion Models, VLMs, Stability AI, OpenAI, Cloud Deployment",
            "features": [
                {
                    "name": "Style Transfer",
                    "description": "AI-powered interior design style transformation"
                },
                {
                    "name": "Object Replacement",
                    "description": "Smart object replacement with realistic rendering"
                },
                {
                    "name": "Performance Optimization",
                    "description": "25% latency reduction with optimized model pipelines"
                }
            ],
            "github_link": None,
            "live_link": None
        },
        {
            "title": "School Data Solutions",
            "description": """
            Led customer onboarding and integration of K–12 school data into a metadata-driven ETL pipeline,
            processing student performance data. Achieved 82% accuracy in student risk prediction using ML models.
            Reduced customer onboarding time from 6 weeks to 10 days through automation.
            """,
            "technologies": "Python, ETL Pipelines, Machine Learning, Jira Automations, Data Validation",
            "features": [
                {
                    "name": "Metadata-driven ETL",
                    "description": "Automated data processing pipeline for K-12 schools"
                },
                {
                    "name": "Risk Prediction",
                    "description": "ML model achieving 82% accuracy in student risk assessment"
                },
                {
                    "name": "Process Automation",
                    "description": "Reduced onboarding time by 83% through automation"
                }
            ],
            "github_link": None,
            "live_link": None
        },
        {
            "title": "FitMatch.ai",
            "description": """
            Designed and implemented deep learning solutions using CNNs and 3D point cloud processing for human
            body part classification, segmentation and regeneration, with accuracy of 90%+. Optimized models
            for serverless deployment on AWS Lambda for iOS AppClip integration.
            """,
            "technologies": "Python, CNNs, 3D Point Cloud, AWS Lambda, ONNX, TFLite, Computer Vision",
            "features": [
                {
                    "name": "3D Body Analysis",
                    "description": "90%+ accuracy in body part classification and segmentation"
                },
                {
                    "name": "Serverless Deployment",
                    "description": "Optimized models for AWS Lambda execution"
                },
                {
                    "name": "Mobile Integration",
                    "description": "iOS AppClip integration with efficient model formats"
                }
            ],
            "github_link": None,
            "live_link": None
        },
        {
            "title": "VoiceCity - AI Voice Cloning",
            "description": """
            Collaborated in developing state-of-the-art AI-based Voice Cloning software for Text-to-Speech (TTS)
            and Speech-to-Text (STT). Fine-tuned deep learning models including GAN and transformer architectures
            for high-fidelity voice replication, achieving 90%+ naturalness and speaker similarity scores.
            """,
            "technologies": "Python, GANs, Transformers, TTS, STT, Deep Learning, Audio Processing",
            "features": [
                {
                    "name": "High-Fidelity Voice Cloning",
                    "description": "90%+ naturalness and speaker similarity scores"
                },
                {
                    "name": "Model Ensemble",
                    "description": "Enhanced audio quality reducing synthesis artifacts by 25%"
                },
                {
                    "name": "Multi-Modal Support",
                    "description": "Both TTS and STT capabilities with advanced architectures"
                }
            ],
            "github_link": None,
            "live_link": None
        },
        {
            "title": "Pixlit - AI Multimedia Processing",
            "description": """
            Developed an AI-powered solution for processing images, videos, audio, and PDFs with deep learning models
            achieving over 90% accuracy. Built and optimized computer vision algorithms, improving output quality
            and consistency by 30%. Deployed scalable model APIs on AWS and on-premise servers.
            """,
            "technologies": "Python, Deep Learning, Computer Vision, AWS, FastAPI, NLP, Multimedia Processing",
            "features": [
                {
                    "name": "Multi-Media AI Processing",
                    "description": "90%+ accuracy across images, videos, audio, and PDFs"
                },
                {
                    "name": "Optimized CV Algorithms",
                    "description": "30% improvement in output quality and consistency"
                },
                {
                    "name": "Scalable Deployment",
                    "description": "35% reduction in inference latency with cloud deployment"
                }
            ],
            "github_link": None,
            "live_link": None
        }
    ]
    
    return projects