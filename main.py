from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extraer información importante de dataframe
movies_columns = movies_data[['original_title', 'poster_link', 'release_date', 'runtime', 'weighted_rating']]

# variables para almacenar información
liked_movies = []
not_liked_movies = []
did_not_watch = []

# método para obtener información de la base de datos
def get_info():
  first_movie = {
    "original_title": movies_columns.iloc[0,0],
    "poster_link": movies_columns.iloc[0,1],
    "release_date": movies_columns.iloc[0,2],
    "duracion": movies_columns.iloc[0,3],
    "rating": movies_columns.iloc[0,4] 
  }
  return first_movie


# /movies api
@app.route("/movies")
def get_movies():
  movies_dates = get_info()
  return jsonify({
    "data": movies_dates,
    "status": "success"
  })

# /like api+


# /dislike api


# /did_not_watch api


if __name__ == "__main__":
  app.run()
