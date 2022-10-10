# Day-22 : AWS CDK - Concepts, Documentation and installation

## Introduction

- Today tried to understand the AWS Cloud Development Kit - CDK, its concepts and how it is enabling to use programming language to provision infrastructure as code

- Saw a notification that new exam for Cloud Developer Associate next year will include more focus on CDK

- Eventually wanted to try out Terraform as its cloud agnostic and AWS CDK helps in Terraform as well

## Cloud Research

- CDK is abstraction of Cloudformation with bells and whistles of programming language like loops, exception handling
    - Cloudformation is declarative, just specify **configuration** and loong with eye paining text
    - output of CDK is cloudformation via ``cdk synth``

- Abstractions involve reducing AWS services to simple constructs which can be provisioned and can update configurations in least amount of code
    - Also programming features like inheritance can reduce time in recreating resources and also help in grouping a bunch of services into a single service

- Needs Node Package Manger - ``npm`` , to install ``aws-cdk``
- Python required ``aws-cdk-lib`` via ``pip``

## Next Steps

- Continue working with Step functions workflow and try to deploy via CDK

## Social Proof

- Will post on **Discord** channels - 100daysofCloud & LearntoCloud
