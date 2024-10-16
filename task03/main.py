#importing sys for getting the path from the args
#impoting pathlib to work with dirs and files 
#importing colorama for colored output

import sys
import pathlib
#importing init so the colors are dispayed in PowerShell
from colorama import init, Fore 
init(autoreset=True)


def main():
    #checking the args for possible wrong usage 
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>") 
        sys.exit(1)
    else:
        #getting the path
        raw_dir_path = sys.argv[1]
        dir_path = pathlib.Path(raw_dir_path)

        #making sure that the path exists and is pointing at the dir
        if not dir_path.exists():
            print("Path doesn't exist!")
            sys.exit(1)
        if not dir_path.is_dir():
            print("This is not a dir!")
            sys.exit(1)
        print_dirs(dir_path)


def print_dirs(dir_path: pathlib.Path, level=0):
        #indentation for the tree-view of the output
        indent = ' '*level
        try:
            for item in dir_path.iterdir(): #checking every sub-unit
                if item.is_dir():
                    #using colorama to color the dirs as cyan
                    print(f"{indent}{Fore.CYAN}{item}")
                    print_dirs(item, level+1)
                elif item.is_file():
                    #using colorama to color the files as green
                    print(f"{indent}{Fore.GREEN}{item}")
        except PermissionError:
            #handling PermissionError and paiting those in red
            print(f"{indent}{Fore.RED}[Access Denied: {dir_path}]")
    


if __name__ == "__main__":
    main()