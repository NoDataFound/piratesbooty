#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import glob
import pandas as pd
import sys
import warnings

booty = '''\033[1;30m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░░░░░░░░░░░     ░░░░░░░░░░     ░░░░░░░░   ░░░░░░░░░░░░
▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒    ▒  ▒   ▒▒▒   
▓   ▓   ▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓   ▓   ▓
▓   ▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓    ▓▓
▓   ▓▓▓   ▓▓▓   ▓▓▓▓▓   ▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓   ▓ ▓▓▓▓▓   ▓▓
█   █   ███████     ██████████     █████████   █████   ███
███████████████████████████████████████████████████   ████
\033[0;34mReassembler for \033[1;34mhttps://github.com/Shell-Company/QRExfil
'''
print(booty)
# https://raw.githubusercontent.com/Shell-Company/QRExfil/main/output.gif
filename = input("\n\033[1;97mInput filename or path for downloaded car:\033[0;34m ")
df = pd.DataFrame(columns=['frame_number', 'frame'])
vidcap = cv2.VideoCapture(filename)
total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(total_frames):
    success, image = vidcap.read()
    cv2.imwrite("loot/output/QRExfil-%d.jpg" % i, image)
    sys.stdout.write("\033[1;97mFiles Created:\033[0;34m %d   \r" % (i) )
    sys.stdout.flush()

warnings.simplefilter('ignore')
files = glob.glob('loot/output/*.jpg')
df = pd.DataFrame(columns=['filename', 'qr_code'])
for file in files:
    img = cv2.imread(file)
    decoded_data = cv2.QRCodeDetector().detectAndDecode(img)
    df = df.append({'filename': file, 'qr_code': decoded_data[0]}, ignore_index=True)
    with open('loot/output/qr_codes.txt', 'a') as f:
        f.write(decoded_data[0] + '\n')
print(df)
df.to_csv('loot/output/qr_codes.csv', index=False)
sys.stdout.write("\033[1;97mCSV Created here: \033[0;34m loot/output/qr_codes.csv" )
sys.stdout.flush()
