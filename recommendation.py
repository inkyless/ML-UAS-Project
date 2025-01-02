import rapidfuzz
from rapidfuzz import process  
import pandas as pd

def recommend_movies(data, movie_title=None, genres=None, min_runtime=None, max_runtime=None,
                    language=None, period_release=None):
    #Condition if user input movie title (use dbscan cluster)
    if movie_title:
         # Find the closest match to the input movie title
        combined_title = data["title"].tolist() + data["original_title"].tolist()
        closest_match, score, _ = process.extractOne(movie_title, combined_title)
        
        if score < 65:  # Threshold for match confidence
            return f"No close match found for '{movie_title}'. Please try again with a more specific title."
        
        #Use closest match
        movie_title = closest_match
        cluster_label = data.loc[data['title'] == movie_title, 'cluster'].values[0]
        if cluster_label == -1:
            return "This movie belongs to outlier, please try again."
        recommendations = data[data["cluster"] == cluster_label]

        # Exclude the movie with the same title as the provided movie_title
        recommendations = recommendations[recommendations['title'] != movie_title]
        
    else: #If no title provided, start with full data
        recommendations = data

    #Additional options of filters 
    if genres:
        genre_filter = recommendations[genres].sum(axis=1) > 0
        recommendations = recommendations[genre_filter]
    if min_runtime:
        recommendations = recommendations[recommendations['runtime'] >= min_runtime]
    if max_runtime:
        recommendations = recommendations[recommendations['runtime'] <= max_runtime]
    if language:
        recommendations = recommendations[recommendations['original_language'] == language]
    if period_release:
        recommendations = recommendations[recommendations['period_release'] == period_release]

    data_columns = ["title","imdb_id","release_date","runtime","original_language","overview",
                    "score", "genres","poster_path"]

    #Use cluster when no movie title inputted
    if movie_title is None and "cluster" in data.columns:
        clusters = recommendations["cluster"].unique()
        result = []
        for cluster in clusters:
            cluster_data = recommendations[recommendations["cluster"] ==cluster]
            cluster_data = cluster_data.sort_values(['score', 'popularity'], ascending=False)
            cluster_data["cluster"] = cluster
            result.append(cluster_data)
        result_df = pd.concat(result,ignore_index=True)
        if len(result_df) < 10:
            return result_df[data_columns]
        return result_df[data_columns]
    
    #Print result with sorted volues
    recommendations = recommendations.sort_values(['score', 'popularity'], ascending=False)

    #Return top 10 recommendations
    if recommendations.empty:
        return "No movies found matching the criteria"
    elif len(recommendations) < 10:
        return recommendations[data_columns]
    #Final result
    return recommendations[data_columns].head(25)
