#!/bin/bash

cd /python-OP_RETURN/

# this enables an alternative method for setting a default
# change address, through environmental variable
if [[ -v CHANGE_ADDR ]] ; then
    echo "CHANGE_ADDR = '$CHANGE_ADDR'" >>user_defined.py
fi

# this enables configuration through mounted dir
# (overrides settings above)
cp /conf/user_defined.py . >/dev/null 2>&1

# start http server on port 8000
su gunicorn -c "gunicorn -b 0.0.0.0:8000 api_server:app"

