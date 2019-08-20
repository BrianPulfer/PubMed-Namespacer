from namespacer import namespacer
from database_scripts import database_downloader, database_unzipper


def main_app():
    """Download and unzips the database. Runs the namespacer to create the '.csv' file"""

    print("STEP 1: \t Downloading database...")
    database_downloader.download_database()
    print("STEP 1: \t Database successfully downloaded\n")

    print("STEP 2: \t Unzipping database...")
    database_unzipper.unzip_database()
    print("STEP 2: \t Database successfully unzipped\n")

    print("STEP 3: \t Generating namespaces...")
    namespacer.main()
    print("STEP 3: \t Namespaces successfully generated\n")


if __name__ == '__main__':
    main_app()
    print("Main application concluded")
