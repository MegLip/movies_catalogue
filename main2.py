from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)
lists = ['popular', 'top_rated', 'upcoming', 'now_playing']


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in lists:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    random.shuffle(movies)
    return render_template(
        "homepage2.html", movies=movies, current_list=selected_list,
        lists=lists)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    def tmdb_post_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url, "tmdb_post_url": tmdb_post_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template(
        "movie_details2.html", movie=details, cast=cast,
        selected_backdrop=selected_backdrop, movie_images=movie_images)


if __name__ == '__main__':
    app.run(debug=True)
