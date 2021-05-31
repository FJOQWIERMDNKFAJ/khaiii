#!/bin/bash

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 788797908348.dkr.ecr.ap-northeast-2.amazonaws.com
docker build --no-cache -f docker/Dockerfile -t analytics-khaiii .
docker tag analytics-khaiii:latest 788797908348.dkr.ecr.ap-northeast-2.amazonaws.com/analytics-khaiii:latest
docker push 788797908348.dkr.ecr.ap-northeast-2.amazonaws.com/analytics-khaiii:latest
