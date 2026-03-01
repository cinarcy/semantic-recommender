# Semantic Recommender 🤖📚

![Semantic Recommender](https://img.shields.io/badge/Release-v1.0.0-blue.svg) [![GitHub Releases](https://img.shields.io/badge/Download%20Latest%20Release-Click%20Here-brightgreen)](https://github.com/cinarcy/semantic-recommender/releases)

Welcome to the **Semantic Recommender** repository! This project showcases an AI-powered article recommender that utilizes sentence embeddings and FAISS for effective semantic search. With a robust FastAPI backend and an interactive Streamlit frontend, this tool provides a seamless experience for content recommendation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In today's digital age, finding relevant content can be overwhelming. The **Semantic Recommender** aims to simplify this process by leveraging advanced natural language processing (NLP) techniques. By using sentence embeddings, it can understand the context of articles and recommend similar content effectively.

## Features

- **AI-Powered Recommendations**: The recommender uses machine learning algorithms to suggest articles based on user preferences.
- **FastAPI Backend**: The backend is built with FastAPI, ensuring fast response times and efficient handling of requests.
- **Streamlit Frontend**: The user interface is designed with Streamlit, making it easy to navigate and interact with the recommender.
- **Semantic Search**: Utilizing FAISS, the system performs vector searches to find semantically similar articles.
- **Open Source**: This project is open-source, encouraging collaboration and improvement from the community.

## Installation

To set up the **Semantic Recommender** on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cinarcy/semantic-recommender.git
   cd semantic-recommender
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required packages.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   Visit the [Releases](https://github.com/cinarcy/semantic-recommender/releases) section to download the latest version of the application. Ensure you execute the necessary files as per the instructions provided.

## Usage

Once you have installed the necessary components, you can start the application. Here’s how:

1. **Start the FastAPI Backend**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Launch the Streamlit Frontend**:
   In a new terminal, run:
   ```bash
   streamlit run app/frontend.py
   ```

3. **Access the Application**:
   Open your web browser and go to `http://localhost:8000` for the FastAPI interface and `http://localhost:8501` for the Streamlit frontend.

## How It Works

The **Semantic Recommender** operates through a series of steps:

1. **Data Collection**: The system gathers articles from various sources. You can add your own dataset for personalized recommendations.
   
2. **Embedding Generation**: Using Hugging Face's sentence transformers, the articles are converted into vector embeddings. This allows the model to capture the semantic meaning of the text.

3. **Indexing with FAISS**: The embeddings are indexed using FAISS (Facebook AI Similarity Search). This indexing enables quick retrieval of similar articles based on user queries.

4. **Recommendation Engine**: When a user inputs a query, the system finds the closest embeddings in the index and returns the most relevant articles.

5. **User Interaction**: The Streamlit frontend provides a user-friendly interface for inputting queries and displaying recommendations.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Streamlit**: A library for creating beautiful web apps for machine learning and data science projects.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **Hugging Face**: Provides state-of-the-art pre-trained models for NLP tasks.
- **Python**: The programming language used for development.

## Contributing

We welcome contributions to enhance the **Semantic Recommender**. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or feedback, please reach out to the project maintainer:

- **Name**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

Thank you for checking out the **Semantic Recommender**! We hope you find it useful for your content recommendation needs. For the latest updates, please visit the [Releases](https://github.com/cinarcy/semantic-recommender/releases) section.