#! /bin/sh
export CLASSPATH=".:/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH"
echo $CLASSPATH
java org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener LabeledExpr.g4 
