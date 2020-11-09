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
RUN curl -s https://archive.apache.org/dist/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz | tar -xz -C /usr/local

# Install PySpark
RUN \
    pip3 install --upgrade pip && \
    pip3 install pyspark

# Install Hadoop
RUN curl -s https://archive.apache.org/dist/hadoop/common/hadoop-3.0.3/hadoop-3.0.3.tar.gz | tar -xz -C /usr/local

# Install JupyterLab
RUN \
    pip3 install jupyterlab && \
    pip3 install notebook && \
    pip3 install pandas

# Setting up Environments
ENV JAVA_HOME "/usr/lib/jvm/java-8-openjdk-amd64"
ENV JRE_HOME "/usr/lib/jvm/java-8-openjdk-amd64/jre"
ENV PYSPARK_PYTHON python3
ENV SPARK_HOME "/usr/local/spark-2.3.2-bin-hadoop2.7"
ENV PYTHONPATH "$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip"
ENV HIVE_HOME "/usr/local/apache-hive-3.1.2-bin"
ENV HADOOP_HOME "/usr/local/hadoop-3.0.3"
ENV PATH "$JAVA_HOME/bin:$JRE_HOME/bin:$PATH:$SPARK_HOME/bin:$HIVE_HOME/bin:$HADOOP_HOME/bin"
ENV PYTHONIOENCODING "UTF-8"

# Spark UI
EXPOSE 4040

#Jupyter Lab
EXPOSE 8888

# Coyping App
WORKDIR /MyApp
COPY . /MyApp

# Starting App
ENTRYPOINT [ "/bin/bash" ]
# CMD [ "bash" ]