FROM jupyter/base-notebook:x86_64-python-3.11.6
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
