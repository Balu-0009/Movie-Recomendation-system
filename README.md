# Movie Recommendation System

A content-based movie recommendation system built with Python, scikit-learn, and Streamlit. This project analyzes movie metadata (genres, keywords, cast, crew) to recommend similar movies based on TF-IDF vectorization and cosine similarity.

## Project Overview

This system processes movie data from TMDB (The Movie Database) and generates personalized movie recommendations. It uses:
- **TF-IDF Vectorization** to convert movie metadata into numerical features
- **Cosine Similarity** to compute similarity between movies
- **Streamlit** for an interactive web interface
- **Pandas & NumPy** for data processing

## Features

- ✅ Content-based movie recommendations
- ✅ Interactive web UI with Streamlit
- ✅ Movie poster display from TMDB API
- ✅ Top 10 similar movie suggestions
- ✅ Efficient data preprocessing and caching

## Project Structure

```
Movie Recomendation system/
├── movierecomendations.ipynb    # Jupyter notebook (data prep & model building)
├── app.py                        # Streamlit web application
├── movies.csv                    # Credits dataset
├── tmdb_5000_movies.csv         # TMDB movies dataset
├── movie_data.pkl               # Serialized model (movies + similarity matrix)
└── README.md                    # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip or conda package manager
- Virtual environment (recommended)

### Step 1: Clone or Download the Project
```bash
cd "d:\project\Movie Recomendation system"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -U pip setuptools wheel
pip install numpy pandas scikit-learn streamlit requests
```

### Step 4: Get TMDB API Key
1. Visit [TMDB API](https://www.themoviedb.org/settings/api)
2. Sign up and generate an API key
3. Replace `YOUR_API_KEY` in `app.py` line 30:
```python
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
```

## Usage

### Running the Jupyter Notebook
Use this to rebuild the model and regenerate `movie_data.pkl`:

```bash
jupyter notebook movierecomendations.ipynb
```

Then run all cells in order. The notebook will:
1. Load CSV datasets
2. Merge movies and credits data
3. Extract and process genres, keywords, cast, and crew
4. Create TF-IDF vectors and compute cosine similarity
5. Save the model to `movie_data.pkl`

### Running the Streamlit Web App
```bash
streamlit run app.py
```

This will open a web browser at `http://localhost:8501` where you can:
1. Select a movie from the dropdown
2. Click "Show Recommendations"
3. View the top 10 similar movies with posters

## Dataset Information

### movies.csv
- Source: TMDB Credits dataset
- Contains: movie_id, title, cast, crew

### tmdb_5000_movies.csv
- Source: TMDB 5000 Movies dataset
- Contains: budget, genres, keywords, overview, revenue, runtime, etc.

**Total movies in merged dataset:** ~4,800

## How It Works

### 1. Data Preprocessing
- Merge movies and credits on `title`
- Extract genre, keyword, actor, and director names from JSON-formatted columns
- Combine all metadata into a single `tags` column

### 2. Vectorization
- Convert text tags to TF-IDF vectors (Term Frequency-Inverse Document Frequency)
- Stop words (common words) are removed

### 3. Similarity Calculation
- Compute cosine similarity matrix between all movie pairs
- Cosine similarity ranges from 0 (completely different) to 1 (identical)

### 4. Recommendation Logic
- For a selected movie, retrieve its similarity scores with all other movies
- Sort by similarity in descending order
- Return top 10 most similar movies

## Key Code Sections

### TF-IDF Vectorization
```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies['tags'])
```

### Cosine Similarity
```python
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
```

### Recommendation Function
```python
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 (excluding the movie itself)
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]
```

## Troubleshooting

### Issue: `FileNotFoundError` for CSV files
**Solution:** Ensure `movies.csv` and `tmdb_5000_movies.csv` are in the project folder.

### Issue: `KeyError: '__reduce_cython__'`
**Solution:** Reinstall scikit-learn:
```bash
pip uninstall scikit-learn -y
pip install --no-cache-dir scikit-learn
```
Then restart the kernel.

### Issue: `InvalidIndexError` when getting recommendations
**Solution:** The movie title doesn't exist. Check available titles:
```python
print(movies['title'].unique())
```

### Issue: Posters not displaying
**Solution:** Verify your TMDB API key is correct and the API is responsive.

## Performance Notes

- Model generation: ~30-60 seconds (one-time)
- Recommendation lookup: <100ms
- Memory usage: ~50-100 MB

## Future Enhancements

- [ ] Add collaborative filtering (user ratings)
- [ ] Implement user ratings and feedback
- [ ] Add movie search and filtering
- [ ] Deploy to cloud (Heroku, AWS, etc.)
- [ ] Multi-language support
- [ ] Mobile-friendly interface

## API Reference

### TMDB Movie Endpoint
```
GET https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}
```

Returns JSON with movie details including poster path, release date, ratings, etc.

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | >=1.3.0 | Data manipulation |
| numpy | >=1.20.0 | Numerical operations |
| scikit-learn | >=1.0.0 | TF-IDF & cosine similarity |
| streamlit | >=1.0.0 | Web UI framework |
| requests | >=2.25.0 | API calls |

## License

This project is open-source and available for educational purposes.

## Credits

- **Data Source:** [TMDB (The Movie Database)](https://www.themoviedb.org/)
- **Framework:** [Streamlit](https://streamlit.io/)
- **ML Library:** [scikit-learn](https://scikit-learn.org/)

## Contact & Support

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages in the terminal
3. Verify file paths and API keys

---

**Last Updated:** November 14, 2025