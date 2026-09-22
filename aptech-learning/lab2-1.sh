path="$1"

if [ -d "$path" ]; then
    echo "this is a directory"

elif [ -f "$path" ]; then
    echo -n "this is a file; "
    if [ -s "$path" ]; then
        echo "not empty"
    else
        echo "empty"
    fi

else
    echo "not exists"
fi