
root_path="$1"
max_depth=$2

dir_count=0
file_count=0
txt_count=0
sh_count=0
other_count=0

for item in $(find "$root_path" -maxdepth "$max_depth" -mindepth 1); do

    if [ -d "$item" ]; then
        (( dir_count++ ))
    
    elif [ -f "$item" ]; then
        (( file_count++ ))

        if [ "${item: -4}" == ".txt" ]; then
            (( txt_count++ ))

        elif [ "${item: -3}" == ".sh" ]; then
            (( sh_count++ ))
        else
            (( other_count++ ))
        fi
    fi
done

echo "Directories: $dir_count"
echo "Files: $file_count"
echo "  + .txt files: $txt_count"
echo "  + .sh files: $sh_count"
echo "  + Other files: $other_count"