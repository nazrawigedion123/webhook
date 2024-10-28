## Use the official Python image as the base
#FROM python:3.12
#
## Set the working directory in the container
#WORKDIR /app
#
## Copy the requirements file into the container
#COPY requirements.txt /app/
#
## Install the Python dependencies
#RUN pip install -r requirements.txt
#
## Copy the project files into the container
#COPY . /app/
#
## Expose the port that Django will run on
#EXPOSE 8000
#
## Run the Django development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/