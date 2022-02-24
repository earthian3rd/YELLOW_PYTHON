import csv
from statistics import mode

def save_to_file(jobs):
    file = open('jobs.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'])
    for jobs in jobs:
        writer.writerow(list(jobs.value()))  
    return