FROM python:3.11-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies first
COPY requirements.txt /usr/src/app
RUN apk add --no-cache build-base \
    && apk add --no-cache mpc1-dev \
    && apk add --no-cache gcc curl \
    && apk add --no-cache postgresql \
    && python3 -m pip install --upgrade pip --no-cache-dir \
    && python3 -m pip install -r requirements.txt --no-cache-dir

# copy the app code
COPY . /usr/src/app/

ENV PYTHONPATH=/usr/src/app

LABEL type="starlab"

# RUN chmod +x /usr/src/app/app/scripts/create_test_data.py
# RUN python3 /usr/src/app/app/scripts/create_test_data.py

CMD ["python", "app/main.py"]
# docker exec --env-file env/.env 41d72aa4bf99 alembic init -t async app/migrations
# docker exec --env-file env/.env 41d72aa4bf99 alembic revision --autogenerate -m "init migration"
# docker exec --env-file env/.env 41d72aa4bf99 alembic upgrade head
# docker exec -it 333beee0b8a5 psql -U postgres