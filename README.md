# ✈️ Trip UI Gemini

An AI-powered travel planning application that creates personalized travel itineraries using advanced AI agents. The application combines the power of CrewAI, Google's Generative AI, and Streamlit to provide an intuitive and intelligent travel planning experience.

## 🌟 Features

- **Smart Travel Planning**: Get personalized travel itineraries based on your preferences
- **AI-Powered Agents**: Utilizes multiple AI agents for different aspects of travel planning:
  - City Selection Agent
  - Local Expert Agent
  - Travel Concierge Agent
- **Interactive UI**: Beautiful and user-friendly interface built with Streamlit
- **Customizable Preferences**: 
  - Multiple city selection
  - Date range planning
  - Interest-based recommendations
  - Flexible travel preferences

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher (but less than 3.12)
- Poetry for dependency management

### Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd Trip-UI-Gemini
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up your environment variables:
Create a `.env` file in the root directory and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key
```

### Running the Application

1. Start the Streamlit application:
```bash
poetry run streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## 🛠️ Technology Stack

- **Python 3.10+**: Core programming language
- **CrewAI**: For orchestrating AI agents
- **Streamlit**: For the web interface
- **Google Generative AI**: For advanced AI capabilities
- **Poetry**: For dependency management
- **LangChain**: For AI/ML operations
- **Pydantic**: For data validation

## 📝 Usage

1. Enter your travel origin
2. Specify the cities you'd like to visit
3. Select your travel dates
4. Choose your interests from the provided options
5. Add any additional interests
6. Click "Generate Travel Plan" to get your personalized itinerary

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- CrewAI for the agent framework
- Google for the Generative AI capabilities
- Streamlit for the web interface framework
