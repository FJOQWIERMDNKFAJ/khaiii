#!/bin/sh
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
      exec /usr/local/bin/aws-lambda-rie /opt/conda/bin/python3.8 -m awslambdaric $@
  else
      exec /opt/conda/bin/python3.8 -m awslambdaric $@
fi  

