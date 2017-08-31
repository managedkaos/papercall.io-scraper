cmd=$(ps -e | grep java | grep DynamoDBLocal.jar)
pid=$(echo $cmd | awk '{print $1}')

case "$1" in
    star*)
        nohup java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb > /dev/null &
        echo "Starting ..."
        ;;
    sto*)
        if [[ $pid ]];
        then
            echo "Stopping ${pid}..."
            kill $pid
        else
            echo "No process found.  Nothing to stop."
        fi
        ;;
    stat*)
        echo $cmd        
        ;;
    *)
        echo "$0 start|stop|status"
        ;;
esac


