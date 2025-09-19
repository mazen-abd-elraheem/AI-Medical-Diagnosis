# AI-Powered Medical Diagnosis System 🏥🤖

An intelligent web-based medical diagnosis assistant that analyzes symptoms and provides potential diagnoses using multiple AI approaches including Machine Learning, Prolog reasoning, and database matching.

## 🌟 Project Description

This Flask-based web application serves as a comprehensive medical diagnosis tool that helps users identify potential health conditions based on their symptoms. The system employs a multi-modal approach combining:

- **Natural Language Processing** for symptom extraction from user input
- **Machine Learning models** for pattern recognition and probabilistic diagnosis
- **Prolog-based reasoning engine** for rule-based medical logic
- **Database matching** for symptom-disease correlation
- **Intelligent symptom validation** to ensure accuracy

The application is designed to be user-friendly, allowing patients to describe their symptoms in natural language and receive comprehensive diagnosis suggestions with explanations, confidence scores, and recommended treatments.

> **⚠️ Important Disclaimer**: This system is for educational and informational purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## ✨ Features

### Core Functionality
- **Natural Language Symptom Input** - Users can describe symptoms in plain English
- **Multi-AI Diagnosis Engine** - Combines ML, Prolog, and database approaches
- **Intelligent Symptom Extraction** - Automatically identifies medical symptoms from text
- **Symptom Validation** - Ensures only recognized medical symptoms are processed
- **Comprehensive Results** - Provides multiple diagnosis possibilities with explanations
- **Confidence Scoring** - Shows reliability scores for each diagnosis
- **Treatment Suggestions** - Offers basic treatment recommendations

### Technical Features
- **Responsive Web Interface** - Works on desktop and mobile devices
- **Real-time Processing** - Instant symptom analysis and diagnosis
- **Error Handling** - Robust error management for reliability
- **Logging System** - Comprehensive logging for debugging and monitoring
- **Database Integration** - SQLite database for symptom and disease data
- **Model Flexibility** - Easily replaceable ML models and reasoning engines

### User Experience
- **One-Click Access** - Immediate functionality from the home page
- **Clean Interface** - Intuitive and user-friendly design
- **Detailed Explanations** - Clear reasoning behind each diagnosis
- **Multiple Result Sources** - Shows which AI methods contributed to each result

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/medical-diagnosis-system.git
   cd medical-diagnosis-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database** (if needed)
   ```bash
   python database_creation/database_creation.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   ```
   Navigate to: http://localhost:5000
   ```

## 🔧 Usage

### Basic Usage
1. **Enter Symptoms**: Type your symptoms in natural language in the text area
   ```
   Example: "I have a headache, fever, and feel nauseous"
   ```

2. **Click Analyze**: Submit your symptoms for analysis

3. **Review Results**: Get comprehensive diagnosis suggestions including:
   - Disease names and categories
   - Confidence scores
   - Detailed explanations
   - Treatment recommendations
   - Source methods (ML, Prolog, Database)

### Advanced Usage
- **Multiple Symptoms**: List multiple symptoms separated by commas or in sentences
- **Detailed Descriptions**: Provide detailed symptom descriptions for better accuracy
- **Follow-up Analysis**: Refine your symptom description based on initial results

## 🏗️ System Architecture

### Components Overview
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │────│  Flask Backend   │────│   AI Engines    │
│   (HTML/CSS/JS) │    │   (Python)       │    │  (ML/Prolog)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                       ┌──────────────────┐
                       │  SQLite Database │
                       │ (Symptoms/Diseases)│
                       └──────────────────┘
```

### Key Modules
- **app.py** - Main Flask application and routing
- **ml_model/** - Machine learning model and text analysis
- **Prolog/** - Prolog reasoning engine for rule-based diagnosis
- **templates/** - HTML templates for web interface
- **database.db** - SQLite database with medical data

### AI Diagnosis Pipeline
1. **Input Processing** - Extract and validate symptoms from user input
2. **Multi-Modal Analysis** - Run parallel diagnosis using:
   - Machine Learning probability models
   - Prolog rule-based reasoning
   - Database symptom matching
3. **Result Combination** - Merge and rank results from all sources
4. **Output Generation** - Present comprehensive diagnosis with explanations

## 📊 Database Schema

### Tables Structure
```sql
-- Symptoms table
symptoms (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL
)

-- Diseases table  
diseases (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    treatment TEXT
)

-- Many-to-many relationship
disease_symptoms (
    disease_id INTEGER,
    symptom_id INTEGER,
    FOREIGN KEY (disease_id) REFERENCES diseases(id),
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id)
)
```

## 🤖 AI Models

### Machine Learning Component
- **Model Type**: Scikit-learn based classification model
- **Input**: Binary symptom presence vectors
- **Output**: Disease probability distributions
- **File**: `ml_model/symptom_checker.pkl`

### Prolog Reasoning Engine
- **Purpose**: Rule-based medical logic and inference
- **File**: `Prolog/prolog_engine.py`
- **Functionality**: Logical reasoning for symptom-disease relationships

### Text Analysis
- **Purpose**: Extract medical symptoms from natural language
- **File**: `ml_model/text_analyzer.py`
- **Method**: NLP-based symptom identification and validation

## 🚀 Deployment

### Local Development
```bash
# Development server
python app.py

# Production-like testing
gunicorn app:app
```

### Cloud Deployment Options

#### Heroku
```bash
heroku create your-app-name
git push heroku main
```

#### Railway
1. Connect GitHub repository to Railway
2. Automatic deployment on git push

#### Render
1. Connect GitHub repository to Render
2. Configure build settings
3. Deploy automatically

#### Docker
```bash
docker build -t medical-diagnosis .
docker run -p 5000:5000 medical-diagnosis
```

### Environment Variables
```bash
PORT=5000                    # Server port
HOST=0.0.0.0                # Server host
FLASK_ENV=production         # Environment mode
FLASK_DEBUG=False           # Debug mode
```

## 📁 Project Structure

```
MEDICAL-EXPERT-SYSTEM/
├── app.py                      # Main Flask application
├── database.db                 # SQLite database
├── requirements.txt            # Python dependencies (create this)
├── Procfile                    # Heroku deployment config (create this)
├── .gitignore                  # Git ignore rules (create this)
├── README.md                   # This documentation
│
├── database_creation/          # Database setup and management
│   ├── add.py                 # Add new data to database
│   ├── clean_the_data.py      # Data cleaning utilities
│   ├── database_creation.py   # Database initialization
│   ├── databaseclean.py       # Database cleaning scripts
│   ├── disease_symptoms.csv   # Disease-symptom mappings
│   ├── diseases_create.py     # Disease data creation
│   ├── diseases.csv           # Disease database
│   ├── export_data.py         # Data export utilities
│   ├── exported_diseases.csv  # Exported disease data
│   └── symptoms.csv           # Symptoms database
│
├── ml_model/                  # Machine Learning components
│   ├── __pycache__/           # Python cache files
│   ├── dataset.csv            # Training dataset
│   ├── dataset.csv.py         # Dataset processing
│   ├── model_training.py      # ML model training script
│   ├── symptom_checker.pkl    # Trained ML model
│   └── text_analyzer.py       # Symptom extraction from text
│
├── Prolog/                    # Prolog reasoning engine
│   ├── __pycache__/           # Python cache files
│   ├── medical_kb.pl          # Prolog knowledge base
│   └── prolog_engine.py       # Rule-based diagnosis logic
│
├── static/                    # Static web files
│   └── style.css              # CSS styling
│
└── templates/                 # HTML templates
    ├── analyze.html           # Symptom input form
    ├── base.html              # Base template
    ├── index.html             # Home page template
    └── results.html           # Diagnosis results page
```

## 🔍 API Endpoints

### Main Routes
- `GET /` - Home page with symptom input form
- `POST /` - Process symptom analysis
- `GET /analyze` - Alternative symptom input route
- `POST /analyze` - Process symptoms (alternative route)
- `GET /health` - Health check endpoint for deployments

### Response Format
```json
{
  "results": [
    {
      "disease": "Common Cold",
      "category": "Respiratory",
      "score": 85,
      "explanation": "Diagnosis suggested due to symptoms: runny nose, cough, fatigue",
      "treatment": "Rest, fluids, over-the-counter medications",
      "sources": ["ml", "database", "prolog"]
    }
  ]
}
```

## 🧪 Testing

### Run Tests
```bash
# Install test dependencies
pip install pytest pytest-flask

# Run all tests
pytest

# Run with coverage
pytest --cov=app
```

### Test Coverage
- Unit tests for core functions
- Integration tests for database operations
- End-to-end tests for web interface
- Model validation tests

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for changes
- Ensure all tests pass before submitting



## ⚠️ Medical Disclaimer

**IMPORTANT MEDICAL DISCLAIMER:**

This application is designed for educational and informational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. 

- Always seek the advice of qualified healthcare professionals
- Never disregard professional medical advice based on this application
- In case of medical emergencies, contact emergency services immediately
- This system should not be used for critical health decisions

The developers assume no responsibility for any medical decisions made based on the output of this system.


## 🙏 Acknowledgments

- Medical databases and research that informed the symptom-disease relationships
- Open source libraries that made this project possible
- Healthcare professionals who provided guidance on medical logic
- The machine learning and AI communities for algorithms and techniques

## 📞 Support

If you encounter any issues or have questions:

1. **Check the Issues** - Look for existing solutions in GitHub Issues
2. **Create an Issue** - Submit a detailed bug report or feature request
3. **Documentation** - Refer to this README and inline code documentation
4. **Contact** - Reach out via GitHub or email for urgent matters

## 🔄 Version History

- **v1.0.0** - Initial release with basic diagnosis functionality
- **v1.1.0** - Added Prolog reasoning engine
- **v1.2.0** - Improved ML model and symptom extraction
- **v1.3.0** - Enhanced web interface and deployment ready

---

**Made with ❤️ for better healthcare accessibility**
