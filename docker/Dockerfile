ARG FUNCTION_DIR="/var/task"

FROM pytorch/pytorch:latest AS build-image
# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
        apt-get install -y \
        g++ \
        make \
        cmake \
        unzip \
        libcurl4-openssl-dev

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code
COPY . ${FUNCTION_DIR}

# Install the runtime interface client
RUN pip install --target ${FUNCTION_DIR} awslambdaric



FROM pytorch/pytorch:latest

ARG FUNCTION_DIR
COPY aws-lambda-rie /usr/local/bin/
COPY entry_script.sh /

WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

RUN pip install cython
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update -y && apt install -y build-essential

RUN mkdir build
WORKDIR ${FUNCTION_DIR}/build


RUN cmake ..
RUN make all
RUN make large_resource

RUN apt-get install -y language-pack-ko
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN make package_python
WORKDIR ${FUNCTION_DIR}/build/package_python
RUN pip install .
WORKDIR ${FUNCTION_DIR}

ENTRYPOINT ["/bin/sh", "/entry_script.sh"]
CMD ["lambda_handler.lambda_handler"]
