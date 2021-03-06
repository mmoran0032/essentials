#!/bin/bash

# conda-auto-env activates the conda environment specified by the
# environment.yml file in the directory. If the environment doesn't
# exist, conda-auto-env creates and activates it.
#
# To install, add this line to your .bashrc or .bash-profile:
#
#     source /path/to/conda_auto_env.sh
#
# Run the command from anywhere with:
#
#     autoenv
#

function autoenv() {
    if [ -e "environment.yml" ]; then
        # echo "environment.yml file found"
        ENV=$(head -n 1 environment.yml | cut -f2 -d ' ')
        # Check if you are already in the environment
        if [[ $PATH != *$ENV* ]]; then
            # Check if the environment exists
            conda activate $ENV
            if [ $? -eq 0 ]; then
                :
            else
                # Create the environment and activate
                echo "Conda env '$ENV' doesn't exist."
                conda env create -q
                conda activate $ENV
            fi
        fi
    else
        echo "No environment.yml file present"
    fi
}

# multiple prompt commands doesn't work, so just run it manually
# export PROMPT_COMMAND=autoenv
