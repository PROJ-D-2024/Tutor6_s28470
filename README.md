# Tutor6_s28470

## Create and Publish a Dockerized API with a Predictive Model

This project provides an API for predictive modeling using FastAPI and a pre-trained machine learning model. Follow the instructions below to set up and run the project.

### Prerequisites

- Python 3.9 or higher (if running locally)
- Docker (if using Docker)

### Run Locally

#### Clone the Repository


#### Install Dependencies

Use pip to install the required Python packages:

```bash
pip install -r requirements.txt
```

#### Run the Application

Start the API server using uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Access the API

The API will be available at:

- Base URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Run with Docker

#### Pull the Prebuilt Image from Docker Hub

Download the Docker image using the following command:

```bash
docker pull uladzimirkaraliou/iris-api
```

#### Run the Docker Container

Start the container:

```bash
docker run -d -p 8000:8000 uladzimirkaraliou/iris-api
```

### Access the API

The API will be accessible at:

- Base URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
