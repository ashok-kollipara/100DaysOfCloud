# Day-2 : Publish docker image to AWS ECR via AWS CLI

## Introduction

- For this I will be utilizing the docker image build done on [Day-1](../001/README.md) and creating a private registry repository with AWS ECR and push the image to repository from aws cli

## Use Case

- AWS offers docker image repository equivalent to docker hub which is private and can be used for automated deployments of custom images via AWS codepipeline / CodeDeploy which I am planning to do project in following days.

## Cloud Research

- [AWS CLI ECR reference](https://docs.aws.amazon.com/cli/latest/reference/ecr/index.html)
- registry-id is aws account number which I missed in parameters while creating
- by default encryption is chosen as server side with AES256
- aws login used for docker is stored in ~/.docker/config.json which is not good idea

## Hands On
- **Step-1 :** Create new repository from aws iam account via aws cli

    ``sh
    $ aws ecr create-repository --repository-name thatsashok/shrink
    ``
    returns a json with details of similar to the ouput of `` $aws ecr describe-repositories``
    
    **response :**
    ```json
    "repositories": [
        {
            "repositoryArn": "arn:aws:ecr:ap-south-1:149471370307:repository/thatsashok/shrink",
            "registryId": "**********",
            "repositoryName": "thatsashok/shrink",
            "repositoryUri": "*********.dkr.ecr.ap-south-1.amazonaws.com/thatsashok/shrink",
            "createdAt": "2022-09-12T18:53:09+05:30",
            "imageTagMutability": "MUTABLE",
            "imageScanningConfiguration": {
                "scanOnPush": false
            },
            "encryptionConfiguration": {
                "encryptionType": "AES256"
            }
        }
    ]
}
    ```
    
- **Step-2:** Push the docker image to ECR repository via docker using AWS ECR credentials. Deatils availabe in repository page in console as well for easy copy paste. My docker needs root priviliges via sudo 

    ```sh
    $ aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin *********.dkr.ecr.ap-south-1.amazonaws.com
    
    $ sudo docker tag thatsashok/shrink:latest ********.dkr.ecr.ap-south-1.amazonaws.com/thatsashok/shrink:latest
    
    $ sudo docker push **********.dkr.ecr.ap-south-1.amazonaws.com/thatsashok/shrink:latest
    ```
    above commands **return** latest: digest with **sha256 hash** if everything went OK. Same can be checked for prescence of image in AWS Web console.
    
- **Step-3:** Check prescence of image in repo with

    ``sh
    $ aws ecr list-images --repository-name thatsashok/shrink
    ``
    **response :**
    ```json
    {
    "imageIds": [
        {
            "imageDigest": "sha256:<imagehash>",
            "imageTag": "latest"
        }
    ]
}
    ```
    
## Social Proof

Will post on the challenge discord and learntocloud discord channels.
