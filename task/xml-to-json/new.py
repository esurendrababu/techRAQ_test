import json
import xmltodict


file=("AUTO550DUAL_AU-AU.xml")
# print(file)
with open(file, 'r') as f:
    # data = json.dump(f.write(),)    
    my_dict = xmltodict.parse(f.read())
    print(my_dict)



#convert to json and push data to a file
file_convert=(my_dict, 'get.json')
with open('AUTO550DUAL_AU-AU.json', 'w') as f:
    json_str = json.dumps(file_convert, indent=4)
    f.write(json_str)


# json_file=("AUTO550DUAL_AU-AU.json")
# with open('AUTO550DUAL_AU-AU.json', 'w') as f:
#     print(my_dict)
#     test= json.dump(f.write, my_dict, indent=4)