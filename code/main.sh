#!/usr/bin/env bash


stamp=`date +%Y%m%d%H%M%S`
LOG="../log/run"


while getopts "r:" opt; do
    case "${opt}" in
        r)
            run_mode=$OPTARG;;
    esac
done


function init_env()
{
    set -o pipefail
    set -o errexit
    exec &> ${LOG}.${stamp}.out 2>${LOG}.${stamp}.err
}
init_env







main() {
    if [[ ${run_mode} == "1" ]]; then
        echo "1"
        echo "2"
    elif [[ ${run_mode} == "2" ]]; then
        echo "2"
    else
        echo "3"
    fi
    echo "ending..."
}

main $@
