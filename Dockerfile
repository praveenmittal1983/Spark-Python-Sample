# FROM python:3.7-alpine
FROM ubuntu:latest

# Setup Timezone
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Get Curl
RUN \
    apt-get update -y && \
    apt-get install -y curl

# Install Python
RUN \
    apt-get update -y && \
    apt-get install -y python3 python3-pip python-dev

# Install JDK
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk

# Install Spark
RUN curl -s https://archive.apache.org/dist/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz | tar -xz -C /usr/local

# Install PySpark
RUN \
    pip3 install --upgrade pip && \
    pip3 install pyspark

# Setting up Environments
ENV PYSPARK_PYTHON python3
ENV SPARK_HOME "/usr/local/spark-2.3.2-bin-hadoop2.7"
ENV PYTHONPATH "$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip"
ENV PATH "$JAVA_HOME/bin:$JRE_HOME/bin:$PATH:$SPARK_HOME/bin"

# Coyping App
WORKDIR /MyApp
COPY . /MyApp

# Starting App
ENTRYPOINT [ "/bin/bash" ]
# CMD [ "bash" ]