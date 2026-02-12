'''
This is used to repeatedly run DenseNet_One_vs_Rest2.py for the many variations of GAF, data sets, words, and subjects
'''

import os
import subprocess

subjects = ['MM05', 'MM08']

for subject in subjects:
    for gaf in ['GASF', 'GADF']:                       #['GASF', 'GADF']
        for method in ['RAW','FILTERED']:     # type of image method, ['DTCWT', 'FILTERED', 'RAW', 'ICA']
            for word in ['gnaw', 'knew', 'pat', 'pot']:                         #['gnaw', 'knew', 'pat', 'pot']
                #os.system("python DenseNet_One_vs_Rest2.py {} {} {} {}".format(gaf, word, method, subject))
                cmd = ["python", "DenseNet_One_vs_Rest2.py", gaf, word, method, subject]
                p = subprocess.Popen(cmd)
                print("PID do filho:", p.pid)
                p.wait()

