cmd=$(ps -e | grep java | grep DynamoDBLocal.jar)
pid=$(echo $cmd | awk '{print $1}')

case "$1" in
    star*)
        nohup java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb > /dev/null &
        ;;
    sto*)
        kill $pid
        ;;
    stat*)
        echo $cmd        
        ;;
    *)
        echo "$0 start|stop|status"
        ;;
esac


