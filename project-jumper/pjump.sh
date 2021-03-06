#!/bin/bash

# Input your base directory.
# 

# TODO: Check peco command

BASE_DIR=~/Project/
CACHE_DIR=`dirname $0`/.cache
CACHE_FILE=`dirname $0`/.cache/projects.txt
MOVING_FILE=`dirname $0`/.cache/projects.log

# Echo help
add_project() {
    exit 0
}

delete_project() {
    exit 0
}

echo_help() {
    echo "Usage: command [-p ProjectNo] [-l]" 2>&1
    exit 1
}

echo_projects() {
    LINE_NO=1
    cat $CACHE_FILE | while read LINE; do
        PROJECT_NAME=`echo $LINE| awk -F / '{print $NF }'`
        echo $LINE_NO: $PROJECT_NAME
        LINE_NO=`expr $LINE_NO + 1`
    done
}

go_project() {
    PROJECT_NO=$1
    expr $PROJECT_NO + 1 > /dev/null 2>&1
    if [ \( $? -ge 2 \) -o $PROJECT_NO -eq 0 ]; then
        echo "You must indicate project no as integer."
        echo_help
        exit 1
    fi
    LINE_NO=1
    GO_DIR=
    while read TMP_PROJECT_DIR; do
        if [ $LINE_NO -eq $PROJECT_NO ]; then
            GO_DIR=$TMP_PROJECT_DIR
        fi
        LINE_NO=`expr $LINE_NO + 1`
    done < $CACHE_FILE
    if [ -z $GO_DIR ]; then
        echo "Your project no is out of all."
        echo_help
        exit 1
    else
        echo $BASE_DIR$GO_DIR >> $MOVING_FILE
    fi
}

# Parse Options.
# You need to ":" when argments is needed.
OPT=
while getopts "p:hlad" OPT
do
    case $OPT in
        a) add_project
            ;;
        d) delete_project
            ;;
        l) echo_projects
            ;;
        p) go_project $OPTARG
            ;;
        h) echo_help
            ;;
        \?) echo_help
            ;;
    esac
done
