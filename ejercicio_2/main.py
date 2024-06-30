from app.tasks import write_response
from celery import chain, group


# result = chain(write_text.s(10) | write_numbers.s(10) | write_response.s(count=10))().get(timeout=5)


group(write_response.s(i) for i in range(30))().get(timeout=5)
