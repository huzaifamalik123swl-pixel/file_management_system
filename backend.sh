#!/bin/bash

operation=$1

case $operation in

create_file)
    touch "$2"
    echo " File Created: $2"
    ;;
create_dir)
    mkdir "$2"
    echo "Directory Created: $2"
    ;;
delete_file)
    rm -f "$2"
    echo "File Deleted: $2"
    ;;
delete_dir)
    rm -rf "$2"
    echo "Directory Deleted: $2"
    ;;
copy)
    cp "$2" "$3"
    echo "Copied $2 to $3"
    ;;
move)
    mv "$2" "$3"
    echo "Moved $2 to $3"
    ;;
rename)
    mv "$2" "$3"
    echo "Rename $2 to $3"
    ;;
list)
    ls -lh "$2"
    ;;
search)
    find "$2" -name "$3"
    ;;
disk_usage)
    df -h
    ;;
*)
    echo "Invalid Operation"
    ;;
esac
