import json, prometheus_client, requests
from flask import Response, Flask
from flask_basicauth import BasicAuth
from gevent import pywsgi
from node import get_cpu_info,get_disk_info,get_mem_info,REGISTRY


app = Flask(__name__)

app.config["BASIC_AUTH_USERNAME"] = 'admin'
app.config["BASIC_AUTH_PASSWORD"] = 'admin'
basic_auth = BasicAuth(app)

@app.route('/')
# 添加认证，哪个路由需要认证就添加到哪里
@basic_auth.required
def index():
    return """
    <h1>Customized Exporter</h1>
    <br> <a href='node'>Node Metrics</a>
    <br> <a href='process'>Process Metrics</a>
    <br> <a href='db'>DB Metrics</a>
    <br> <a href='other'>Other Metrics</a>
    """

@app.route('/node')
@basic_auth.required
def get_node_metrics():
    # get_cpu_info()
    get_mem_info()
    get_disk_info() #数据采集
    return Response(prometheus_client.generate_latest(REGISTRY),mimetype="text/plain")

@app.route('/process')
@basic_auth.required
def get_process_metrics():
    pass

@app.route('/db')
@basic_auth.required
def get_db_metrics():
    pass

@app.route('/other')
@basic_auth.required
def get_other_metrics():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9088,threaded=True)
    # server = pywsgi.WSGIServer(('0.0.0.0', 9088), app)
    # server.serve_forever()