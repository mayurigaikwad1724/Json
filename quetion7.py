# a_dictionary = {}

# a_file = "JSON/Text.txt"
# with open(a_file) as f:
#     for line in f:
#         command,description=line.strip().split(None,1)
#         a_dictionary[command]=description.strip()

# # for line in a_file:

# #     key, value = line.split()




# #     a_dictionary[key] = value
# out_file=open("sample.json","w")
# json.dump(a_dictionary,out_file,indent=4,sort_keys=False)
# out_file.close()


import json

filename = 'commands.txt'

commands = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(' ', 1)
        commands[command] = description.strip()

print(json.dumps(commands, indent=2, sort_keys=True))
json.dump(a_dictionary,out_file,indent=4,sort_keys=False)
# out_file.close()