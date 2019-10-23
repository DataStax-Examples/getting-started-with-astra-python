import sys


def get_cql_schema_string_from_file(string_key):
    cql_string = ''
    start_of_block = False
    with open('schema.cql', 'r') as f:
        for line in f:
            if ' ' + string_key + ' ' in line:
                cql_string += line.strip('\n').strip(' ')
                start_of_block = True
            if start_of_block is True and string_key not in line:
                cql_string += ' ' + line.strip('\n').strip(' ')
            if start_of_block is True and '\n' == line:
                break
    return cql_string
