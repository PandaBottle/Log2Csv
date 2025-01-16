# Log2Csv - Convert nginx logs into a csv document
This Repo is for my own personal learning. I wanted to convert Nginx logs to a more readible format and although there might be alternatives to format the logs into json, I am currently not allowed to modify the nginx service.
Therefore, this repo will guide you through how to make Nginx logs in a more readible format.

# Prerequisite
This program relies on pandas.py to be installed. Therefore, please ensure that you have imported the python package pandas.
```
pip install pandas
```

# Usage
Have your nginx access.log saved in a repository, then run the log2json.py. It will create data.json as output.
Then, run json2csv.py in the same repository where data.json resides.
The csv file is created!
