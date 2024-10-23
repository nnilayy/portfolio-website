# -----------------------------------------------------------------------------
# CERTIFICATIONS-IMAGES
# -----------------------------------------------------------------------------
certfication_1_image = "./certifications/Generative AI with Large Language Models.png"
certfication_2_image = "./certifications/Databases.png"
certfication_3_image = "./certifications/Databases.png"
certfication_4_image = "./certifications/Python Project for Data Science.png"
certfication_5_image = "./certifications/Python for Data Science, AI & Development.png"
certfication_6_image = "./certifications/Data Science Methodology.png"
certfication_7_image = "./certifications/What is Data Science.png"
certfication_8_image = "./certifications/Tools for Data Science.png"
certfication_9_image = "./certifications/Tools for Data Science.png"
certfication_10_image = "./certifications/Tools for Data Science.png"
certfication_11_image = "./certifications/Tools for Data Science.png"
# -----------------------------------------------------------------------------
# CERTIFICATIONS-NAMES
# -----------------------------------------------------------------------------
certification_1_name = "Generative AI with Large Language Models"
certification_2_name = "Databases and SQL for Data Science (With Honors)"
certification_3_name = "AWS Academy Graduate Machine Learning Course"
certification_4_name = "Python Project for Data Science"
certification_5_name = "Python for Data Science, AI & Development"
certification_6_name = "Data Science Methodology"
certification_7_name = "Introduction to Data Science"
certification_8_name = "Tools for Data Science"
certification_9_name = "TensorFlow Developer Certificate in 2023: Zero To Mastery"
certification_10_name = "Complete Tensorflow 2 and Keras Deep Learning Bootcamp"
certification_11_name = "2022 Python for Machine Learning & Data Science Masterclass"
# -----------------------------------------------------------------------------
# CERTIFICATIONS-LINKS
# -----------------------------------------------------------------------------
certification_1_link = (
    "https://www.coursera.org/account/accomplishments/certificate/BN7Z4L9W69LD"
)
certification_2_link = (
    "https://www.coursera.org/account/accomplishments/certificate/PFCQFWD9GW7F"
)
certification_3_link = (
    "https://www.credly.com/badges/51d0c7e9-8928-4ec6-97e8-4f8bf9bf07f1/print"
)
certification_4_link = (
    "https://www.coursera.org/account/accomplishments/certificate/2N7HBCJGFLMA"
)
certification_5_link = (
    "https://www.coursera.org/account/accomplishments/certificate/5GA7CRR744C8"
)
certification_6_link = (
    "https://www.coursera.org/account/accomplishments/certificate/P32JTNTY32L4"
)
certification_7_link = (
    "https://www.coursera.org/account/accomplishments/certificate/7GJXEQGL2L6N"
)
certification_8_link = (
    "https://www.coursera.org/account/accomplishments/certificate/E9XQYBA9X2CR"
)
certification_9_link = (
    "https://www.udemy.com/certificate/UC-45d95e5f-7223-4535-aecd-7ab0997347b4/"
)
certification_10_link = (
    "https://www.udemy.com/certificate/UC-a87228c4-0133-49b0-8292-100ecf89aacc/"
)
certification_11_link = (
    "https://www.udemy.com/certificate/UC-9095f860-b91d-4ee6-a255-adf85863efee/"
)
# -----------------------------------------------------------------------------
# CERTIFICATIONS-PAGE-2-TITLE
# -----------------------------------------------------------------------------
certification_page_2_title = "Course Coverage"
# -----------------------------------------------------------------------------
# BOLD-FUNCTION
# -----------------------------------------------------------------------------
def bold(text):
    return f"<b>{text}</b>"

def italic(text):
    return f"<i>{text}</i>"

# -----------------------------------------------------------------------------
# CERTIFICATION-1-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_1_page_2_content = (
    f"""{bold(italic("1. Transformer Architecture & LLM Fundamentals"))}
    o Transformer architecture: Self-attention mechanisms and multi-head attention
    o Text generation techniques: From n-grams to modern transformer models
    o Scaling laws optimization across compute, dataset size, and inference
    o Pre-training strategies for domain adaptation (BloombergGPT case study)

    {bold(italic("2. Model Training & Optimization"))}
    o Parameter Efficient Fine-Tuning (PEFT) implementation strategies
    o LoRA (Low-Rank Adaptation) for efficient model adaptation
    o Multi-task instruction fine-tuning techniques
    o Soft prompts and prompt engineering methodologies
    """
)

certification_1_page_3_content = (
    f"""{bold(italic("3. Reinforcement Learning Integration"))}
    o RLHF (Reinforcement Learning from Human Feedback) implementation
    o Proximal Policy Optimization (PPO) for model alignment
    o Reward model development and reward hacking prevention
    o KL divergence optimization in model training

    {bold(italic("4. Advanced LLM Applications"))}
    o Chain-of-Thought prompting for enhanced reasoning
    o ReAct framework: Combining reasoning and action
    o Program-Aided Language Models (PAL) implementation
    o AWS SageMaker JumpStart deployment strategies
    """
)

certification_1_page_4_content = (
    f"""{bold(italic("5. Practical Implementation"))}
    o Dialogue summarization using fine-tuned models
    o Multi-GPU compute optimization techniques
    o Model evaluation using industry benchmarks
    o External application integration architectures
    """
)
# -----------------------------------------------------------------------------
# CERTIFICATION-2-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_2_page_2_content = (
    f"""{bold(italic("1. Core SQL Operations"))}
    o Basic Data Manipulation using SELECT, WHERE, INSERT operations
    o Advanced filtering using COUNT, DISTINCT
    o Database Schema Management: CREATE TABLE with constraints, ALTER TABLE modifications
    o Pattern Matching using LIKE, BETWEEN, IN operators

    {bold(italic("2. Advanced Query Techniques"))}
    o Parameterized Stored Procedures for automated reporting
    o ACID-compliant Transaction Management with COMMIT/ROLLBACK
    o Correlated Sub-queries and Multi-table Nested SELECTs
    o Multi-dimensional JOINs (LEFT, RIGHT, FULL OUTER) for data integration
    """
    )

certification_2_page_3_content = (
    f"""{bold(italic("3. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("4. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )

certification_2_page_4_content = (
    f"""{bold(italic("5. Real-World Applications"))}
    o Chicago City Data Analysis: Crime Statistics & Traffic Patterns
    o Multi-table queries for Socioeconomic Data Analysis
    o Cloud-based Database Operations on IBM Db2
    o Real-time Data Processing & Analysis Workflows Using IBM Watson Studio
    """
    )
# -----------------------------------------------------------------------------
# CERTIFICATION-3-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_3_page_2_content = (
    f"""{bold(italic("1. Data Extraction & Web Scraping"))}
    o BeautifulSoup4 implementation for HTML DOM parsing and data extraction
    o Automated web scraping using requests library and bs4
    o yfinance API integration for historical stock data retrieval
    o Real-time stock market data acquisition using REST API endpoints and Pandas

    {bold(italic("2. Financial Data Analysis"))}
    o Stock price trend analysis using pandas time-series functions
    o Historical revenue data processing with NumPy
    o Comparative market analysis using rolling averages and technical indicators
    o Time-series data manipulation with pandas DataFrame operations
    """
)

certification_3_page_3_content = (
    f"""{bold(italic("3. Data Visualization & Dashboard"))}
    o Interactive financial dashboards using plotly and matplotlib
    o Multi-dimensional stock visualization with seaborn heatmaps
    o Time-series trend plotting with customized candlestick charts
    o Dynamic stock metrics visualization

    {bold(italic("4. Real-World Applications"))}
    o GameStop vs Tesla market correlation analysis
    o IBM Watson Studio integration with Jupyter notebooks
    o Automated stock portfolio tracking using yfinance API
    o Financial data processing in IBM Watson Studio
    """
)

# -----------------------------------------------------------------------------
# CERTIFICATION-4-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_4_page_2_content = (
    f"""{bold(italic("1. Data Extraction & Web Scraping"))}
    o BeautifulSoup4 implementation for HTML DOM parsing and data extraction
    o Automated web scraping using requests library and bs4
    o yfinance API integration for historical stock data retrieval
    o Real-time stock market data acquisition using REST API endpoints and Pandas

    {bold(italic("2. Financial Data Analysis"))}
    o Stock price trend analysis using pandas time-series functions
    o Historical revenue data processing with NumPy
    o Comparative market analysis using rolling averages and technical indicators
    o Time-series data manipulation with pandas DataFrame operations
    """
)

certification_4_page_3_content = (
    f"""{bold(italic("3. Data Visualization & Dashboard"))}
    o Interactive financial dashboards using plotly and matplotlib
    o Multi-dimensional stock visualization with seaborn heatmaps
    o Time-series trend plotting with customized candlestick charts
    o Dynamic stock metrics visualization

    {bold(italic("4. Real-World Applications"))}
    o GameStop vs Tesla market correlation analysis
    o IBM Watson Studio integration with Jupyter notebooks
    o Automated stock portfolio tracking using yfinance API
    o Financial data processing in IBM Watson Studio
    """
)
# -----------------------------------------------------------------------------
# CERTIFICATION-5-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_5_page_2_content = (
    f"""{bold(italic("1. Python Core Fundamentals"))}
    o Advanced string manipulations with f-strings and string methods
    o Mathematical operations using complex expressions and operators
    o Object-Oriented Programming with custom class implementations
    o Exception handling with try-except blocks and custom exceptions

    {bold(italic("2. Core Data Structure Operations"))}
    o List comprehensions and advanced tuple operations
    o Dictionary manipulation with nested key-value structures
    o Set operations for data deduplication and unique value handling
    o Multi-dimensional data structure operations
    """
)

certification_5_page_3_content = (
    f"""{bold(italic("3. Data Processing & Analysis"))}
    o DataFrame operations using pandas for tabular data manipulation
    o NumPy array operations for mathematical computations
    o Matrix operations with N-dimensional arrays
    o Advanced data filtering and transformation techniques

    {bold(italic("4. Data Collection & Integration"))}
    o REST API integration using requests library
    o Web scraping implementation with BeautifulSoup4
    o Automated data extraction from HTML tables using pandas
    o Multi-format file processing (CSV, JSON, XML)
    """
)
certification_5_page_4_content = (
    f"""{bold(italic("5. Real-World Applications"))}
    o GDP data extraction and analysis workflows
    o Text analysis using Python string operations
    o HTTP request handling for API endpoints
    o Automated data collection and processing pipelines
    """
)


# -----------------------------------------------------------------------------
# CERTIFICATION-6-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_6_page_2_content = (
    f"""{bold(italic("1. Data Science Methodologies"))}
    o CRISP-DM phases: Business Understanding → Deployment & Feedback
    o Rollins' Foundational Methodology with 10-stage workflow
    o Agile-integrated data science approach with sprint planning
    o ROI-driven problem definition frameworks

    {bold(italic("2. Problem Definition & Analysis"))}
    o Business case formulation using SMART criteria
    o Decision tree classification for predictive modeling scenarios
    o Analytical approach mapping (Descriptive/Predictive/Prescriptive)
    o Data requirement specifications using 5W1H framework
    """
)

certification_6_page_3_content = (
    f"""{bold(italic("3. Data Processing Framework"))}
    o Data quality scoring using completeness, accuracy, consistency metrics
    o Missing data handling: MCAR, MAR, MNAR strategies
    o Outlier detection using IQR and z-score methods
    o ETL pipeline design with data validation rules

    {bold(italic("4. Model Development & Evaluation"))}
    o KPI definition and success metric establishment
    o Model validation using train-test-validation split approach
    o Stakeholder feedback integration using RACI matrix
    o A/B testing protocols for model comparison
    """
)

certification_6_page_4_content = (
    f"""{bold(italic("5. Deployment & Communication"))}
    o Data visualization storytelling using pyramid principle
    o Production deployment strategies with monitoring systems
    o Feedback loop implementation using PDCA cycle
    o Business impact measurement using cost-benefit analysis
    """
)

# -----------------------------------------------------------------------------
# CERTIFICATION-7-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_7_page_2_content = (
    f"""{bold(italic("1. Data Science Fundamentals"))}
    o Core principles of CRISP-DM and SEMMA methodologies
    o Essential skill trinity: Basic Python/R, Descriptive Statistics, Business Domain knowledge
    o Fundamentals of business metrics: CAC, ROI, and KPI frameworks

    {bold(italic("2. Big Data & Cloud Infrastructure"))}
    o Exploring Hadoop ecosystem: HDFS, Hive, and MapReduce basics
    o Survey of cloud platforms: IBM Watson Studio, AWS SageMaker fundamentals
    o Foundational concepts in data mining: clustering and classification approaches
    o Basic architecture of ETL workflows and data lakes
    """
)

certification_7_page_3_content = (
    f"""{bold(italic("3. AI & Machine Learning Integration"))}
    o Primer on neural networks: CNNs and RNNs use cases
    o Discovery of ChatGPT, DALL-E, and modern AI applications
    o Fundamental regression types: Linear, Logistic, Multiple
    o Basics of ML pipeline: from data preparation to model evaluation

    {bold(italic("4. Data Management Systems"))}
    o Key distinctions between PostgreSQL (RDBMS) and MongoDB (NoSQL)
    o Fundamentals of data warehouses vs data lakes architecture
    o Core concepts of data catalogs and governance frameworks
    o Overview of batch vs real-time data processing methods
    """
)

certification_7_page_4_content = (
    f"""{bold(italic("5. Industry Applications"))}
    o Real-world examples: Patient outcome prediction in healthcare
    o Case studies: Netflix recommendation systems basics
    o Exploration of MLB Statcast analytics applications
    o Practical applications: Credit risk scoring fundamentals
    """
)

# -----------------------------------------------------------------------------
# CERTIFICATION-8-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_8_page_2_content = (
    f"""{bold(italic("1. Data Science Toolset Overview"))}
    o Comparative analysis: Open-source (Python, R) vs Commercial tools (SAS, SPSS)
    o Cloud platform fundamentals: IBM Watson Studio, AWS SageMaker, Google Colab
    o Programming environment setup: Anaconda distribution management
    o Version control basics: Git commands and GitHub workflow

    {bold(italic("2. Programming Languages & Environments"))}
    o Python ecosystem: NumPy, Pandas, Scikit-learn core libraries
    o R programming: ggplot2, dplyr, tidyr packages
    o SQL fundamentals for data querying and manipulation
    o Basic syntax comparison: Java, Scala, Julia for data processing
    """
)

certification_8_page_3_content = (
    f"""{bold(italic("3. Jupyter Environment"))}
    o Notebook interface mastery: Code vs Markdown cells
    o Multi-kernel support: Python3, R, and Scala kernels
    o JupyterLab features: File browser, console, terminal integration
    o Basic notebook sharing and collaboration techniques

    {bold(italic("4. Development Tools & Platforms"))}
    o RStudio IDE: Console, Environment, Plots, Files panes
    o Git operations: clone, commit, push, pull request workflows
    o Watson Studio project management and collaboration
    o Data Asset eXchange (DAX) for dataset exploration
    """
)

certification_8_page_4_content = (
    f"""{bold(italic("5. Practical Applications"))}
    o Markdown formatting for technical documentation
    o Basic data visualization using R's plotting functions
    o Repository management with GitHub web interface
    o Watson Studio notebook integration with GitHub
    """
)



# -----------------------------------------------------------------------------
# CERTIFICATION-9-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_9_page_2_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )
certification_9_page_3_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )

# -----------------------------------------------------------------------------
# CERTIFICATION-10-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_10_page_2_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )
certification_10_page_3_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )

# -----------------------------------------------------------------------------
# CERTIFICATION-11-PAGES-CONTENT
# -----------------------------------------------------------------------------
certification_11_page_2_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )
certification_11_page_3_content = (
    f"""{bold(italic("1. Database Systems Integration"))}
    o DDL/DML script development for automated table management
    o Aggregate Functions (AVG, SUM, MAX) with GROUP BY/HAVING
    o Date-Time Functions for temporal data analysis
    o Performance-optimized indexing strategies

    {bold(italic("2. Python-Database Ecosystem"))}
    o Jupyter Notebook integration with SQL Magic commands
    o Database connectivity using DB-API and ibm_db connectors
    o Automated data pipeline development with Python
    o IBM Db2 cloud instance management
    """
    )


# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
certifications_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#7519ff",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#e5d4fc",
    "checkpointGlowColor": "#CC88FF",
    "boxShadow": "0 0 6px rgb(170, 141, 255)",
}
# -----------------------------------------------------------------------------
# TIMELINE PROPERTIES
# -----------------------------------------------------------------------------
certifications_timeline_properties = {
    "lineLength": 2400,  # Customize as needed
    "lineWidth": 600,
    "amplitude": 200,
    "frequency": 400,
    "speed": 1,
}

# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
classes_dict = {
    "outerClassName": "outer-content-certfications",
    "titleClassName": "content-page-title-certfications",
    "contentClassName": "content-page-content-certfications",
    "imgClassName": "content-image-certfications",
    "videoClassName": "content-page-video-certfications",
    "linkClassName": "content-page-link-certfications",
}


# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 11,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_1_name,
                    "image": certfication_1_image,
                    "video": "",
                    "link": certification_1_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_1_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_1_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_1_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_1_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_1_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_1_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 2,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_2_name,
                    "image": certfication_2_image,
                    "video": "",
                    "link": certification_2_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_2_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_2_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_2_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_2_link,
                    "contentClassName": "content-page-n-content-certfications",
                },{
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_2_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_2_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 3,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_3_name,
                    "image": certfication_3_image,
                    "video": "",
                    "link": certification_3_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_3_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_3_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_3_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_3_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 4,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_4_name,
                    "image": certfication_4_image,
                    "video": "",
                    "link": certification_4_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_4_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_4_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_4_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_4_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 5,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_5_name,
                    "image": certfication_5_image,
                    "video": "",
                    "link": certification_5_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_5_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_5_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_5_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_5_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_5_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_5_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 6,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_6_name,
                    "image": certfication_6_image,
                    "video": "",
                    "link": certification_6_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_6_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_6_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_6_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_6_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_6_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_6_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 7,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_7_name,
                    "image": certfication_7_image,
                    "video": "",
                    "link": certification_7_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_7_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_7_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_7_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_7_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_7_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_7_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 8,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_8_name,
                    "image": certfication_8_image,
                    "video": "",
                    "link": certification_8_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_8_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_8_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_8_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_8_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 4,
                    "title": certification_page_2_title,
                    "content": certification_8_page_4_content,
                    "image": "",
                    "video": "",
                    "link": certification_8_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 9,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_9_name,
                    "image": certfication_9_image,
                    "video": "",
                    "link": certification_9_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_9_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_9_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_9_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_9_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 10,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_10_name,
                    "image": certfication_10_image,
                    "video": "",
                    "link": certification_10_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_10_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_10_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_10_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_10_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
        {
            "checkpoint": 11,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "",
                    "content": certification_11_name,
                    "image": certfication_11_image,
                    "video": "",
                    "link": certification_11_link,
                },
                {
                    "pageNumber": 2,
                    "title": certification_page_2_title,
                    "content": certification_11_page_2_content,
                    "image": "",
                    "video": "",
                    "link": certification_11_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
                {
                    "pageNumber": 3,
                    "title": certification_page_2_title,
                    "content": certification_11_page_3_content,
                    "image": "",
                    "video": "",
                    "link": certification_11_link,
                    "contentClassName": "content-page-n-content-certfications",
                },
            ],
        },
    ],
}

# Add the class names to each page using a one-line for loop
for checkpoint in temp_data["checkpoints"]:
    checkpoint["pages"] = [
        {
            **page,
            **{k: v for k, v in classes_dict.items() if k not in page}
        }
        for page in checkpoint["pages"]
    ]

# Assign the result to certifications_data
certifications_data = temp_data
