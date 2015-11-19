#!/usr/bin/python
import os
import sys
import csv

def get_file_name(filePath):
    return os.path.basename(filePath).split('.')[0]

def csv_field(filepath):
    with open(filepath) as text:
        return list(csv.reader(text))[0]
    return ""

def input_field(path, entryType):
    result = """
input {
    file {
        path => "%s"
        type => "%s"
        start_position => "beginning"
        }
}
    """ % (path, entryType)
    return result

#fields should be a list
def filter_field(fields):
    result = """
filter {
    csv {
        columns => %s
        separator => ","
        }
}
    """ % (fields,)
    return result

def output_field(indexName, host="localhost"):
    result = """
output {
    elasticsearch {
        action => "index"
        host => "%s"
        index => "%s"
        workers => 1
}
    """ % (host, indexName)
    return result

def type():
    return NULL
###
usage: ./logstash_conf.py <csv path> <conf path>
###
def main():
    input_csv = sys.argv[1]
    target_file = sys.argv[2]
    target_file_name = get_file_name(target_file)
    csv_field_list = csv_field(input_csv)
    with open(target_file, 'w') as f:
        f.write(input_field(input_csv, target_file_name))
        f.write(filter_field(csv_field_list))
        f.write(output_field(target_file_name))
        f.close()
        print "done"

if __name__ =="__main__":
    main()
