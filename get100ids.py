from bs4 import BeautifulSoup
from subprocess import CalledProcessError
import requests
import time
import json
import sys
import subprocess
import urllib.request

search_term = input("Enter a search term: ")
search_term.replace(" ", "+")
# Make a get request to PubMed
response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=" + search_term + "&retmax=100&tool=mosquito_map_tool&email=card@nmsu.edu")

soup = BeautifulSoup(response.content, 'html.parser')
# Print the information of the first 100 articles
for id in soup.find_all('id'):
    uid = id.get_text()

    paper = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=" + id.get_text() + "&retmode=json&tool=mosquito_map_tool&email=card@nmsu.edu")
    json_data = paper.json()
    # Print the information of the given article
    print("Title: " + json_data['result'][uid]['title'])
    print("Authors: ")
    for author in json_data['result'][uid]['authors']:
        print(author['name'])
    print("Publisher: " + json_data['result'][uid]['fulljournalname'])
    print("Publish Date: " + json_data['result'][uid]['pubdate'])

    print(uid)
    # Find the location of the pdf from the file list
    # Updated oa_file_list.txt can be found at: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_file_list.txt
    try:
        output = subprocess.run("grep " + uid + " oa_file_list.txt", capture_output=True, check=True, shell=True)
        path = output.stdout.decode('Latin-1').split("\t",1)[0]
        print(path)
        path_1 = path.split("/", 4)[0]
        path_2 = path.split("/", 4)[1]
        path_3 = path.split("/", 4)[2]
        path_4 = path.split("/", 4)[3]
        print('Beginning file download')
        url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/" + path_1 + path_2 + path_3
        # This currently is not working - research ways of downloading from FTP server
        response = urllib.request.urlretrieve(url)
    except CalledProcessError as ex:
        # The file was not found in the oa_file_list.txt
        print('Error: ', ex)

    # print(output)
    # API yells at you if you don't wait a bit between requests
    # time.sleep(1)
