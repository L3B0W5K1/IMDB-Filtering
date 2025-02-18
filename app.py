from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset when the app starts
df = pd.read_csv('imdb_dataset.tsv', delimiter='\t')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def filter_movies():
    # Get the minimum rating and vote count from the form
    try:
        min_rating = float(request.form.get('min_rating', 0))
    except ValueError:
        min_rating = 0
    try:
        min_votes = int(request.form.get('min_votes', 0))
    except ValueError:
        min_votes = 0

    # Filter the DataFrame based on the criteria
    filtered = df[(df['averageRating'] >= min_rating) & (df['numVotes'] >= min_votes)]
    
    # Get a list of movie titles (tconst values) from the filtered data
    movie_list = filtered['tconst'].tolist()
    
    return render_template('results.html', movies=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
