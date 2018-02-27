import csv
import sys

from geoip import geolite2


INPUT_FILE_NAME, OUTPUT_FILE_NAME, IP_COLUMN_NUM = sys.argv[1:]
IP_COLUMN_NUM = int(IP_COLUMN_NUM)

with open(INPUT_FILE_NAME, 'r') as input_file:
    with open(OUTPUT_FILE_NAME, 'w') as output_file:
        input_reader = csv.reader(input_file)
        output_writer = csv.writer(output_file)

        for row in input_reader:
            try:
                ip_match = geolite2.lookup(row[IP_COLUMN_NUM - 1].strip())
            except ValueError:
                ip_match = None

            if ip_match:
                row[IP_COLUMN_NUM - 1] = ip_match.country
            else:
                row[IP_COLUMN_NUM - 1] = 'Unknown'

            output_writer.writerow(row)
