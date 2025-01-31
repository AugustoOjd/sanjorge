from celery import Celery

app = Celery('app',
                broker='redis://redis:6379/0',
                backend='redis://redis:6379/0',
                include=['app.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()