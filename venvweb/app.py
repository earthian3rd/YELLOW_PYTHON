from flask import Flask, redirect, render_template, request, redirect, send_file
from scrapping import get_jobs
from exporter import save_to_file

app = Flask('Superscrapper')
db = []
@app.route('/')
def home():
    return render_template(search.html)

@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get.jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template('report.html', searchingBy=word, resultsNumber=len(jobs), jobs=jobs)

@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv')
    except:
        return redirect('/')

# @app.route('/<username>')
# def contact(username):
#     return f'welcome to contact page for {username}.'

#app.run(host='192.168.0.103')
app.run(host='0.0.0.0')
