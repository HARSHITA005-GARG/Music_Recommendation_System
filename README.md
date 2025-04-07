# Music Recommendation System 🎵

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A content-based recommendation system that suggests music tracks based on user preferences using Spotify's API.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features ✨
1. **Personalized Recommendations**  
   Analyzes user's listening history to suggest similar tracks
2. **Spotify Integration**  
   Direct access to Spotify's extensive music database
3. **Audio Feature Analysis**  
   Utilizes 12+ musical characteristics including danceability, energy, and tempo
4. **Interactive Interface**  
   Simple CLI for easy interaction with recommendation engine

## Technology Stack 💻
- **Core Language**: Python 3.8+
- **APIs**: [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- **Machine Learning**: Scikit-learn for cosine similarity calculations
- **Data Handling**: Pandas, NumPy
- **Dependency Management**: Pipenv

## Installation ⚙️

### Prerequisites
- Spotify Developer Account (for API credentials)
- Python 3.8+

### Steps
1. Clone repository:
   ```bash
   git clone https://github.com/HARSHITA005-GARG/Music_Recommendation_System.git
   cd Music_Recommendation_System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration 🔧
1. Create `.env` file:
   ```bash
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   ```

2. Get Spotify API credentials:
   - Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create new application and copy credentials

## Usage 🚀
1. Run the recommendation system:
   ```python
   python main.py
   ```

2. Example workflow:
   ```python
   # Get user authorization
   auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               redirect_uri=REDIRECT_URI)
   
   # Generate recommendations
   recommendations = generate_recommendations(user_id="spotify_user_id")
   ```

## Recommendation Algorithm 🧠
The system uses cosine similarity to match audio features:

\[ \text{Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} \]

**Audio Features Analyzed**:
1. Acousticness
2. Danceability
3. Energy
4. Instrumentalness
5. Key
6. Liveness
7. Loudness
8. Mode
9. Speechiness
10. Tempo
11. Time Signature
12. Valence

## Project Structure 📁
```
├── data/               # Sample datasets
├── utils/              # Helper functions
│   ├── spotify_api.py  # API wrappers
│   └── recommender.py  # Core algorithm
├── main.py             # Entry point
├── requirements.txt    # Dependencies
└── .env.example        # Environment template
```

## License 📄
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬
For questions or issues, please [open an issue](https://github.com/HARSHITA005-GARG/Music_Recommendation_System/issues).
