from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from CI/CD Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello from My NEW WebApp with Kubernetes and Monitoring!"

from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Create a counter metric
REQUEST_COUNTER = Counter("http_requests_total", "Total HTTP Requests", ["endpoint"])

@app.route("/")
def hello():
    REQUEST_COUNTER.labels(endpoint="/").inc()
    return "Hello from MyWebApp running on Kubernetes!"

# Expose /metrics endpoint for Prometheus
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
