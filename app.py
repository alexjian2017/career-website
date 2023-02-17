from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Taipei, Taiwan',
    'salary':'1,000,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Taipei, Taiwan',
    'salary':'1,500,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Taipei, Taiwan',
    'salary':'800,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'New York, USA',
    'salary':'2,000,000'
  },
]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS,company_name='Alex')

@app.route('/api/jobs')
def api_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
