FROM pytorch/pytorch:latest
MAINTAINER nako.sung@navercorp.com

#RUN git clone https://github.com/kakao/khaiii.git
WORKDIR /workspace/khaiii
COPY . .

RUN pip install cython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt update -y && apt install -y build-essential

RUN mkdir build
WORKDIR /workspace/khaiii/build


RUN cmake ..
RUN make all
RUN make large_resource

RUN apt-get install -y language-pack-ko
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN make package_python
WORKDIR /workspace/khaiii/build/package_python
RUN pip install .
WORKDIR /workspace/khaiii

CMD ["/bin/bash"]
