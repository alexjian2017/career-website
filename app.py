from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, job_detail_from_db, application_to_db

app = Flask(__name__)

company_name = 'Alex'
@app.route("/")
def home():
  jobs = load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name=company_name)

@app.route('/api/jobs')
def api_job():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def job_detail(id):
  job = job_detail_from_db(id)
  if not job:
    return '', 404
  return render_template('job_detail.html',job=job,company_name=company_name)

@app.route('/job/<id>/apply',methods=['post'])
def apply_for_job(id):
  data = request.form
  if application_to_db(id, data):
    return render_template('application_submit.html',data=data,company_name=company_name)
  else:
    return '',404
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
