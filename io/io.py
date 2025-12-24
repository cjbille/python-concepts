import csv, json
from json import JSONDecodeError

read_file = open('input_file.txt', 'r') # r means read
for line in read_file.readlines():
    print(line.strip())

write_file = open('output_file.txt', 'w') # w means write
for i in range(10):
    write_file.write(f"line {i}\n")
write_file.close()

append_file = open('output_file.txt', 'a') # a means append
for i in range(10, 20):
    append_file.write(f"line {i}\n")
append_file.close()

with open('us_counties.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader) # skip csv header
    for row in reader:
        print(row)

with open('us_counties.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t') # prints out csv data as a dictionary
    next(reader) # skip csv header
    for row in reader:
        print(row)

# JSON stuff
jsonString = '''
{
    "name": "John Doe",
    "age": 28,
    "email": "john.doe@example.com",
    "isActive": true,
    "hobbies": ["reading", "cycling", "traveling"],
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere",
        "zip": "12345"
    }
}
'''

try:
    json_dict = json.loads(jsonString)
    print(json_dict)
except JSONDecodeError as e:
    print(f"Error decoding json: {e}")

# Dump JSON
some_dictionary = {
    "name": "John Doe",
    "age": 28,
}

json_string_from_dict = json.dumps(some_dictionary)
print(json_string_from_dict)
