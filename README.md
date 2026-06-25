# 🎬 Movie Recommendation System

An end-to-end **Content-Based Movie Recommendation System** built using **Python**, **Natural Language Processing (NLP)**, and **Streamlit**. The system recommends movies similar to a selected movie by analyzing genres, keywords, cast, crew, and overview information.

---

# 🚀 Project Overview

Movie recommendation systems are widely used by streaming platforms to improve user experience. This project builds a **content-based recommender** that suggests the top 5 similar movies based on textual features extracted from movie metadata.

The recommendation engine is deployed as an interactive **Streamlit web application**, allowing users to select a movie and instantly receive personalized recommendations.

---

# 🎯 Objectives

* Build a content-based recommendation engine.
* Perform feature engineering using movie metadata.
* Apply Natural Language Processing (NLP) techniques.
* Compute movie similarity using cosine similarity.
* Deploy the recommendation system using Streamlit.

---

# 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**, which consists of:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

📥 Download the dataset from Kaggle:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle
* Jupyter Notebook

---

# 🧠 Recommendation Workflow

The recommendation engine follows these steps:

1. Load movie and credits datasets.
2. Merge both datasets.
3. Clean and preprocess data.
4. Combine important textual features:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
5. Apply NLP preprocessing.
6. Convert text into vectors.
7. Calculate Cosine Similarity.
8. Recommend the Top 5 most similar movies.

---

# 🤖 Recommendation Technique

**Algorithm Used**

* Content-Based Filtering

**Similarity Measure**

* Cosine Similarity

---

# 🌐 Streamlit Web Application

The project includes an interactive Streamlit application where users can:

* 🎬 Select any movie
* 🔍 Generate Top 5 Similar Movie Recommendations
* ⚡ Receive instant recommendations

Run the application using:

```bash
streamlit run app.py
```

---

# ✨ Features

* Content-Based Recommendation System
* Natural Language Processing (NLP)
* Cosine Similarity
* Interactive Streamlit UI
* Real-Time Movie Recommendations
* Beginner-Friendly Interface

---

# ⚠️ Important Note

Some generated files are **not included** in this repository because they exceed GitHub's file size limits.

These files include:

* `movies.pkl`
* `similarity.pkl`
* `tmdb_5000_credits.csv` (if unavailable in the repository)

---

# ▶️ How to Regenerate the Files

1. Download the TMDB dataset from Kaggle.

2. Place both dataset files in the project directory:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

3. Open:

```text
movies_recommendation.ipynb
```

4. Run all notebook cells.

The notebook will automatically generate:

* `movies.pkl`
* `similarity.pkl`

5. After generation is complete, launch the Streamlit application:

```bash
streamlit run app.py
```

---

# 🚀 Future Improvements

* Display Movie Posters using TMDB API
* Add Movie Ratings
* Recommend Movies by Genre
* Deploy on Streamlit Community Cloud
* Improve Recommendation Accuracy

---

# 👨‍💻 Author

**Harshit Sharma**

B.Tech CSE Student | Data Science & Machine Learning Enthusiast

⭐ If you found this project useful, consider starring the repository!
