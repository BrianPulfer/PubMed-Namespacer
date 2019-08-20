import urllib.request

import definitions
import os


NR_FILES = 972


def download_database():
    """Downloads the database in the database folder defined in the 'definitions.py' file.
    The database is downloaded as .xml.gz files. Already present files will not be downloaded."""

    download_link = definitions.DATABASE_DOWNLOAD_LINK
    destination = definitions.DATABASE_PATH

    file_names = list()

    for i in range(1, NR_FILES+1):
        if i < 10:
            file_names.append('pubmed19n000'+str(i)+'.xml.gz')
        elif i < 100:
            file_names.append('pubmed19n00' + str(i) + '.xml.gz')
        else:
            file_names.append('pubmed19n0' + str(i) + '.xml.gz')

    for file_name in file_names:
        new_file_path = destination + '/' + file_name

        if not os.path.isfile(new_file_path):
            file_url = download_link + '/' + file_name
            file_content = urllib.request.urlopen(file_url).read()

            file = open(new_file_path, 'wb')
            file.write(file_content)
            file.close()


if __name__ == '__main__':
    download_database()
