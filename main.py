import os
import re

def search_for_term_in_file(file_path, search_term):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return re.search(search_term, content, re.IGNORECASE) is not None

def search_sql_files(directory, search_term):
    file_list = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".sql"):
                file_path = os.path.join(root, file_name)

                # Check if the search term is in the file name or content
                if search_term.lower() in file_name.lower() or search_for_term_in_file(file_path, search_term):
                    file_list.append(file_path)

    return file_list

if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    directory = input("Enter the directory path to search for SQL files: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
    else:
        result = search_sql_files(directory, search_term)
        if result:
            print("Files containing the search term:")
            for file_path in result:
                print(file_path)
        else:
            print("No files found matching the search term.")
