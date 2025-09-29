# use the official python runtime image
FROM python:3.13

# create the app directory 
RUN mkdir /app

# set the working directory inside the container
WORKDIR /app

# set envirnoment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# upgrade pip
RUN pip install --upgrade pip

# copy the django project and install dependencies
COPY requirements.txt /app/

# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the django project to the container
COPY . /app/

# expose the django port
EXPOSE 8000

# run djangos development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
