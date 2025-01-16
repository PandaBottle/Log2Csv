import tkinter as tk
from tkinter import filedialog as fd
import json 
import re

i = 0
result = {}

####################### PART 1: IMPORT ACCESS.LOG'S FILEPATH

root = tk.Tk()  #Main window of the GUI
root.withdraw() #Hides window so that it does not appear when file dialog is displayed

file_path = fd.askopenfilename() #Function from filedialog module that returns filepath as a string

####################### PART 2: READ THE CONTENTS

with open(file_path) as f:
    lines = f.readlines()

regex = '(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>.*?)\] \"(?P<httpstatus>(GET|POST) .+ HTTP\/1\.1)\" (?P<returnstatus>\d{3}) (?P<responsesize>\d+) \"(?P<referer>.*?)\" (?P<browserinfo>.*)'


for line in lines:
    r = re.match(regex, line)
    
    if r is not None:
        result[i] = {
            'IP address': r.group('ipaddress'),
            'Time Stamp': r.group('dateandtime'),
            'HTTP status': r.group('httpstatus'),
            'Return status': r.group('returnstatus'),
            'Referer': r.group('referer'),  # Capture the referer
            'Browser Info': r.group('browserinfo')
        }
        i += 1

with open('data.json', 'w') as fp:
    json.dump(result, fp) 