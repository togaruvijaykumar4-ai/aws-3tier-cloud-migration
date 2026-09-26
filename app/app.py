import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = '''<!doctype html><html><head><title>AWS Cloud Migration Demo</title><style>body{font-family:Arial;max-width:800px;margin:60px auto;padding:20px}code{background:#eee;padding:3px 6px}</style></head><body><h1>AWS Cloud Migration Demo</h1><p>Flask application designed for EC2 with optional RDS integration.</p><p>Environment: <code>{{ env }}</code></p><p>Health: <a href="/health">/health</a> | API: <a href="/api/info">/api/info</a></p></body></html>'''

@app.get('/')
def home():
    return render_template_string(HTML, env=os.getenv('APP_ENV', 'local'))

@app.get('/health')
def health():
    return jsonify(status='healthy', service='ec2-web-tier')

@app.get('/api/info')
def info():
    return jsonify(application='aws-3tier-cloud-migration', database=os.getenv('DB_HOST','not-configured'), storage='Amazon S3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT','5000')))
