# PubMed 2019 annual baseline downloader and namespacer

## Project
This project has the main purpose of downloading, unzipping and analysing the PubMed annual baseline for year 2019 
(december 2018).

The goal of the project is to create a file containing all PubMed namespaces and counting their cardinality.

## Namespace
A namespace is the composition of an author's last name with its forename initial (e.g. John Doe -> (Doe, J)).
Creating a file containing every namespace and the relative cardinality has as major goal becoming a feature for an 
Author Name Disambiguation (AND) classifier.

Information about a namespace's ambiguity (cardinality) can help a classifier out in classifying correctly a couple of
scientific articles has 'belonging to the same author' or 'not belonging to the same author'.

## Author Name Disambiguation (AND)
The Author Name Disambiguation project can be found at the following link: 
https://github.com/BrianPulfer/AuthorNameDisambiguation

## Conditions
To see PubMed data download conditions, check out the following link:
https://www.nlm.nih.gov/databases/download/terms_and_conditions.html

## System requirements
MacOS or Linux operating system. Python3 or greater. Internet connection and 200GB of free space on disk 
(if downloading database).

## Set-up
Create a new virtual environment (for pycharm users: Preferences...-> Project -> Project Interpreter -> show all -> new).
Install all requirements specified in the 'requirements.txt' file.