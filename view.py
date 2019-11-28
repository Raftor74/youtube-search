from app import app
from modules.parsers.YouTubeSearch import YouTubeVideoSearch
from flask import render_template
from flask import request


@app.route('/', methods=['GET', 'POST'])
def index():
    query = ''
    max_results = 20
    max_result_list = [
        {'name': 10, 'value': 10},
        {'name': 20, 'value': 20},
        {'name': 50, 'value': 50},
    ]
    video_list = list()

    if request.method == 'POST':
        query = str(request.form['query'])
        max_results = int(request.form['max_results'])
        # Если запрос не пустой
        if len(query):
            search = YouTubeVideoSearch()
            video_list = search.search(query, max_results)

    context = {
        'video_list': video_list,
        'query': query,
        'max_results': max_results,
        'max_result_list': max_result_list,
    }
    return render_template('index.html', context=context)


@app.route('/about/')
def about():
    return render_template('about.html')