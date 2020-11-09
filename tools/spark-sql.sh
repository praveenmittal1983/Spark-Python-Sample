#!/bin/sh
#Simple Wrapper for spark-sql

PROJECTDIR=/MyApp
SQL=/usr/local/bin/spark-sql

#Setting up Logging Level
if [ ! -f $SPARK_HOME/conf/log4j.properties ]; then
    cp $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties
fi
sed -i 's/INFO/WARN/' $SPARK_HOME/conf/log4j.properties

#Starting spark-sql
cd $PROJECTDIR && ${SQL} -i $PROJECTDIR/sql/createTemporaryViews.sql;