FROM amd64/python:3 as base

RUN mkdir /work/
WORKDIR /work/

COPY ./app/requirements.txt /work/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app/ /work/
ENV FLASK_APP=app.py

###########START NEW IMAGE: DEVELOPMENT ###################
FROM base as dev
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
