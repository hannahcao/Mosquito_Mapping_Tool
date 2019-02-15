# Mosquito Mapping Tool

## Step 1: Search for and retrieve article info
The first phase of this tool involves submitting a search term to the
PubMed API and retrieving information about the first 100 relevant articles.
In order to run this script, navigate into the directory and type:
`python3 get100ids.py`
You will be prompted to enter your search term. (Ex: `microbiome anopheles` )Make sure words are space-separated.
The script will then print out the information of the first 100 found relevant articles.

## Step 2: Search for and retrieve file from the FTP server
For the second phase you will need to unzip oa_file_list.
The second phase of this tool will search the PubMed FTP server list of all
articles stored to the PubMed server. Please note that at this time articles
listed on PubMed and hosted externally will not be retrieved in this process.
The tool will search the file `oa_file_list.txt` for the retrieved ID of an
article. If the ID is found on the list, the tool will then go to the path
listed within `oa_file_list.txt` and will download the directed folder. This
will give us a folder which contains the PDF of the article.
