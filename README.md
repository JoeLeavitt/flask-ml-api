docker build -t mnist_model .

docker run  -p 5000:5000 mnist_model

run this command in the mnist-api dir:

curl -F 'file=@test_images/0.jpg' localhost:5000/classify

result should be {"digit": 0}
