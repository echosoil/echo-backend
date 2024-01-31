# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /usr/src/app
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY ./api /code/api

# FROM ckan/ckan:latest

# Add CKAN plugin settings
# RUN sed -i '/ckan.plugins/ s/$/ dcat dcat_rdf_harvester dcat_json_harvester dcat_json_interface structured_data keycloak/' /srv/app/ckan.ini
# RUN echo "ckan.plugins = dcat dcat_rdf_harvester dcat_json_harvester dcat_json_interface structured_data" >> /etc/ckan/default/production.ini

# Run uvicorn when the container launches
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]