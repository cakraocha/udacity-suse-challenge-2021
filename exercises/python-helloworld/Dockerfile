FROM python:3.8
LABEL maintaner="Ocha Cakramurti"

# COPY . /app

# Path for GitHub action
COPY ./exercises/python-helloworld /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]