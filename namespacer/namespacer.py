import os
from bs4 import BeautifulSoup

import definitions

OUTPUT_FILE_NAME = 'namespaces.csv'


def fill_namespaces_dict(namespaces, db_path):
    """Fills a given dictionary. Keys will be the namespaces, Values will be the cardinality"""
    file_counter, nr_files = 1, 0

    for file_name in os.listdir(db_path):
        if file_name.endswith('.xml'):
            nr_files = nr_files + 1

    for file_name in os.listdir(db_path):
        if file_name.endswith('.xml'):
            print('Processing file '+str(file_counter)+'/'+str(nr_files))
            file_counter = file_counter + 1

            current_file = open(db_path + "/" + file_name, 'r')
            file_content = current_file.read()
            current_file.close()

            soup = BeautifulSoup(file_content, 'xml')

            authors = soup.find_all('Author')

            for author in authors:
                if author.LastName and author.ForeName:
                    lastname = author.LastName.string
                    initial = author.ForeName.string[0]

                    namespace = (lastname, initial)

                    if namespace not in namespaces.keys():
                        namespaces[namespace] = 1
                    else:
                        namespaces[namespace] = namespaces[namespace] + 1
    return namespaces


def write_namespaces_to_file(namespaces, file_path):
    """Writes the given dictionary (namespaces) to the given file (csv)"""
    file = open(file_path, 'w')

    header_line = 'NAMESPACE;CARDINALITY\n'
    file.write(header_line)

    for k in namespaces.keys():
        line = str(k) + ';' + str(namespaces[k]) + '\n'
        file.write(line)

    file.close()


def main():
    """Counts the namespaces and the relative cardinalities. Writes the results to file"""

    # Namespaces dictionary
    nss = dict()

    # Reading all files authors to fill namespaces dictionary
    nss = fill_namespaces_dict(nss, definitions.DATABASE_PATH)

    # Writing namespace dictionary to file
    write_namespaces_to_file(nss, OUTPUT_FILE_NAME)


if __name__ == '__main__':
    main()
    
    # Telling the user that the program has finished
    print("Program finished")
