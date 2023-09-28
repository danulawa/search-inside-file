import os
import re
import argparse

def search_for_term_in_file(file_path: str, search_term: str) -> bool:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return re.search(search_term, content, re.IGNORECASE) is not None

def search_sql_files(directory : str, search_term : str):
    file_name : str
    file_list = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            if not file_name.endswith(".sql"):
                continue

            file_path = os.path.join(root, file_name)
            # Check if the search term is in the file name or content
            if search_term.lower() in file_name.lower() or search_for_term_in_file(file_path, search_term):
                file_list.append(file_path)

    return file_list

def main():
    parser = argparse.ArgumentParser(description="Search for a term in SQL files.")
    parser.add_argument("--term", help="Search term", default=None)
    parser.add_argument("--dir", help="Directory path to search for SQL files", default=None)
    args = parser.parse_args()

    search_term = args.term if args.term else input("Enter the search term: ")
    directory = args.dir if args.dir else input("Enter the directory path to search for SQL files: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    result = search_sql_files(directory, search_term)
    if result:
        print("Files containing the search term:")
        for file_path in result:
            print(file_path)
    else:
        print("No files found matching the search term.")

if __name__ == "__main__":
    main()