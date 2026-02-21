import multiprocessing

# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file

# The socket to bind
bind = "0.0.0.0:8000"

# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1

# The worker class to use
# Uvicorn's Gunicorn worker class
worker_class = "uvicorn.workers.UvicornWorker"

# The maximum number of simultaneous clients
worker_connections = 1000

# The maximum number of requests a worker will process before restarting
max_requests = 1000

# The maximum jitter to add to the max_requests setting
max_requests_jitter = 50

# The timeout for handling requests
timeout = 120

# The access log file to write to
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# The error log file to write to
errorlog = "-"
accesslog = "-"

# The level of logging
loglevel = "info"
