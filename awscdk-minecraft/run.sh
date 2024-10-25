#!/bin/bash

set -e

#####################
# --- Constants --- #
#####################

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


##########################
# --- Task Functions --- #
##########################

function set-local-aws-env-vars {
    export AWS_PROFILE=minecraftjay
    export AWS_REGION=us-west-2
}

# ------- #

function deploy {
    set-local-aws-env-vars
    uv run -- cdk deploy MinecraftServerS3Stack-2 \
        --app 'python app.py' \
        --profile $AWS_PROFILE \
        --region $AWS_REGION
}

function destroy {
    set-local-aws-env-vars
    uv run -- cdk destroy MinecraftServerS3Stack-2\
        --app 'python app.py' \
        --profile $AWS_PROFILE \
        --region $AWS_REGION 
}

# print all functions in this file
function help {
    echo "$0 <task> <args>"
    echo "Tasks:"
    compgen -A function | cat -n
}

TIMEFORMAT="Task completed in %3lR"
time ${@:-help}
