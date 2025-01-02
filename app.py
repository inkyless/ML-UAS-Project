from flask import Flask, request, jsonify, render_template
import pandas as pd
from recommendation import recommend_movies
from waitress import serve

app = Flask(__name__)

data = pd.read_csv("clean_movies_data.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend",methods=["GET","POST"])
def recommend():
    if request.method == "POST":
        #Get data from user input
        movie_title = request.form.get('movie_title',None)
        genres = request.form.getlist('genre')
        min_runtime = (request.form.get('min_runtime', type=int))
        max_runtime = (request.form.get('max_runtime', type=int))
        language = request.form.get('language')
        period = (request.form.get('period', type=int))

        #Proceed the data to function recommendation
        recommendations = recommend_movies(
            data=data,
            movie_title=movie_title,
            genres=genres,
            min_runtime=min_runtime,
            max_runtime=max_runtime,
            language=language,
            period_release=period
        )

         # Check if recommendations is a DataFrame
        if isinstance(recommendations, str):  # If the result is a message, return it as an error
            return render_template("results.html", recommendations=None, error_message=recommendations)
        return render_template("results.html", recommendations=recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()
    serve(app,host='127.0.0.1',url_scheme='https')