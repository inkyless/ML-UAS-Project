from flask import Flask, request, jsonify, render_template
import pandas as pd
from recommendation import recommend_movies

app = Flask(__name__)

data = pd.read_csv("clean_movies_data.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend",methods=["GET","POST"])
def recommend():
    if request.method == "POST":
        #Get data from user input
        movie_title = request.args.get('movie_title',None)
        genres = request.args.get('genres')
        min_runtime = (request.args.get('min_runtime', type=int))
        max_runtime = (request.args.get('max_runtime', type=int))
        language = request.args.get('language')

        #Proceed the data to function recommendation
        recommendations = recommend_movies(
            data=data,
            movie_title=movie_title,
            genres=genres,
            min_runtime=min_runtime,
            max_runtime=max_runtime,
            language=language
        )

         # Check if recommendations is a DataFrame
        if isinstance(recommendations, str):  # If the result is a message, return it as an error
            return render_template("results.html", recommendations=None, error_message=recommendations)
        return render_template("results.html", recommendations=recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)