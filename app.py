from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]


@app.route('/')
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Wiswol')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


@app.route('/jobForm/', methods=["POST", "GET"])
def jobForm():
    if request.method == "POST":
        print(request.form)
        return jsonify(request.form)
    else:
        return render_template('jobOpeningForm.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
