# csv-geocoder

Given a CSV file with IP addresses in a column, this script geocodes the IPs to
country and outputs a new file with the IP column replaced with a country
column.

This doesn't attempt to detect column headers. If you have column headers you'll
want to rename the IP column manually when you're finished; it'll be changed to
"Unknown" in the output.

## Example usage

The easiest thing to do is to run this in Docker as below, or if you want to
run it directly install the requirements from `requirements.txt`. Either way the
arguments are the same:

```
geocode.py INPUT_FILE OUTPUT_FILE COLUMN_NUMBER
```

Running with Docker:

```
$ cat in.csv
Header 1, Header 2
Local, 127.0.0.1
Google, 8.8.8.8
Oxford, 163.1.0.1

$ docker run -v $PWD:/data --rm zooniverse/csv-geocoder /data/in.csv /data/out.csv 2

$ cat out.csv
Header 1,Unknown
Local,Unknown
Google,US
Oxford,GB
```
