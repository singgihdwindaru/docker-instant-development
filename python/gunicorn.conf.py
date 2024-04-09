import multiprocessing

# https://docs.gunicorn.org/en/stable/configure.html#configuration
workers = multiprocessing.cpu_count()
bind = ':8080'
timeout= 60 * 5
errorlog = "-"
accesslog = "-"