import os
import gzip

import definitions


def unzip_database():
    """Iterates the whole database and extracts every .xml.gz file to .xml files.
    Already extracted files won't be uncompressed again."""

    for file_name in os.listdir(definitions.DATABASE_PATH):
        if file_name.endswith('.xml.gz'):
            new_file_name = definitions.DATABASE_PATH + '/' + file_name[:-3]

            if not os.path.isfile(new_file_name):
                gz_file = gzip.GzipFile(definitions.DATABASE_PATH + '/' + file_name, 'rb')
                file_content = gz_file.read()
                gz_file.close()

                xml_file = open(new_file_name, 'wb')
                xml_file.write(file_content)
                xml_file.close()


if __name__ == '__main__':
    unzip_database()
