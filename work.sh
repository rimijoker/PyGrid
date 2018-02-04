python3 ipfs_grid_worker_daemon.py &

while true
do
    echo "Check if pull needed"
    PULL_MSG="$(git pull)"
    if [[ $PULL_MSG != *"up-to-date"* ]]; then
        echo "Pulled, rebuilding and restarting worker"
        sudo pkill python3
        sudo python3 setup.py install
        python3 ipfs_grid_worker_daemon.py &  
    elif [[ $PULL_MSG = *"Aborting"* ]]; then
        echo "Not able to pull, you probably neeed to commit"
        exit 1
    fi
    sleep 5
done
