#!/bin/bash

cd /home/crustypi/application/crustypi/

changed=0
git remote update && git status -uno | grep -q 'Your branch is behind' && changed=1
if [ $changed = 1 ]; then
    # Changes on github
    git pull
    echo "Restarting crustypi..."
    pm2 restart crustypi
    pm2 restart crustypi-poster
    echo "Crustypi restarted!"
else
    echo "Up-to-date"
fi