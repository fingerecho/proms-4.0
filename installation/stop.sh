echo "kill -9 `ps aux | grep fuseki | grep -v grep | awk '{print $2}'`" > stop.sh
