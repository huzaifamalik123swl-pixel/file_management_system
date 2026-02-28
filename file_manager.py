import subprocess
import logging
import sys

# logging setup
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_backend(args):
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        msg = f"Command not found: {args[0]}"
        print(msg)
        logging.error(msg)
        return 1

    if result.stdout:
        print(result.stdout.strip())
        logging.info(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
        logging.error(result.stderr.strip())

    return result.returncode

while True:
    print("""
1. create file
2. create directory
3. delete file
4. delete directory
5. move file
6. copy file
7. rename file/directory
8. list folder content
9. disk usage
10. search file/directory
0. exit
""")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        file_name = input("File name: ")
        run_backend(["./backend.sh", "create_file", file_name])
    elif choice == "2":
        dir_name = input("Directory name: ")
        run_backend(["./backend.sh", "create_dir", dir_name])
    elif choice == "3":
        file_name = input("File name: ")
        run_backend(["./backend.sh", "delete_file", file_name])
    elif choice == "4":
        dir_name = input("Directory name: ")
        run_backend(["./backend.sh", "delete_dir", dir_name])
    elif choice == "5":
        src = input("Source file: ")
        dest = input("Destination: ")
        run_backend(["./backend.sh", "move", src, dest])
    elif choice == "6":
        src = input("Source file: ")
        dest = input("Destination: ")
        run_backend(["./backend.sh", "copy", src, dest])
    elif choice == "7":
        old = input("Old name: ")
        new = input("New name: ")
        run_backend(["./backend.sh", "rename", old, new])
    elif choice == "8":
        folder = input("Folder Path: ")
        run_backend(["./backend.sh", "list", folder])
    elif choice == "9":
        run_backend(["./backend.sh", "disk_usage"])
    elif choice == "10":
        path = input("search in path: ")
        name = input("File/Directory name: ")
        run_backend(["./backend.sh", "search", path, name])
    elif choice == "0":
        break
    else:
        print("Invalid Choice")