# flask-ml-api
Deploys a pre-trained MNIST model to a Flask API using Docker

### Build Docker Image From Dockerfile
```
docker build -t mnist_model .
```

### Create Running Container That Deploys MNIST Model
```
docker run -p 5000:5000 mnist_model
```

### Hit The API From The ./mnist-api Directory
```
curl -F 'file=@test_images/0.jpg' localhost:5000/classify
```

```result should be {"digit": 0}```
