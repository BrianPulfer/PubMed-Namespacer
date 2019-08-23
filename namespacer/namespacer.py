import os

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

            for line in current_file:
                if "<Author" in line and "AuthorList" not in line:
                    lastname_line = current_file.readline()
                    forename_line = current_file.readline()

                    if "LastName" in lastname_line and "ForeName" in forename_line:
                        if len(lastname_line.split("<LastName>")) == 2 and len(forename_line.split("<ForeName>")) == 2:
                            lastname = lastname_line.split("<LastName>")[1].split("</LastName>")[0]
                            forename = forename_line.split("<ForeName>")[1].split("</ForeName>")[0]

                            namespace = (lastname, forename[0])

                            try:
                                namespaces[namespace] = namespaces[namespace] + 1
                            except KeyError:
                                namespaces[namespace] = 1
            current_file.close()
            del current_file

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
