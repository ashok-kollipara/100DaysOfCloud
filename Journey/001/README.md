# Day-1 : Understanding AWS ECS / ECR better with Docker Container Build

## Cloud Research

- Went through the online course module on the AWS ECS for deploying containers on EC2 Instance type launch and Fargate type launch.

- **AWS Documentation** 
    - [AWS ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
    - [AWS Fargate Serverless](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
    
- **Docker Documentation**
    
    - [Dockercon 2022 starter video](https://youtu.be/gAGEar5HQoU)
    - [Read up the documentation](https://docs.docker.com/get-started/)
    
## Hands On Today

- Installed docker engine manually on my practice machine via SSH

- Practice with different images / containers

    - ``$ docker pull``
    - ``$ docker run``
    - ``$ docker build``
    
- Took my **[github project](https://github.com/ashok-kollipara/shrink-my-link)** from last month and made a microservice container out of it with below configuration

    - ``$ docker build --tag shrink .``
    - ``$ docker run --env-file api_keys shrink``
    
- **Dockerfile for container build**

    ```Dockerfile
    FROM python:3.10.7-alpine
    WORKDIR /app
    COPY . .
    RUN pip3 install -r requirements.txt
    ENTRYPOINT ["python","shrink.py"]
    CMD ["python","shrink.py", "-h"]
    ```

## Social Proof

I will just post it on **Discord** channel for today I guess ;)
