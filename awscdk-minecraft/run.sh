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
    export AWS_PROFILE=minecraft
    export AWS_REGION=us-west-2
}

# ------- #

function deploy {
    set-local-aws-env-vars
    uv run -- cdk deploy \
        --app 'python app.py' \
        --profile $AWS_PROFILE \
        --region $AWS_REGION 
}

function destroy {
    set-local-aws-env-vars
    uv run -- cdk destroy \
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
