my_dict = {"name": "gloria", "age": 38, "tribe": "kenyan"}
print(my_dict)

backup = my_dict.copy()
print(backup)

keys = ["name", "age", "city"]
values = "unknown"
default = dict.fromkeys(keys, values)
print(default)

getting = backup.get("name")
print(getting)

key1 = backup.keys()
print(key1)

value1 = backup.values()
print(value1)

all_items = backup.items()
print(all_items)

popping = backup.pop("name")
print(popping)
print(backup)

popitem = my_dict.popitem()
print(popitem)
print(my_dict)

new_dict = {"name": "joy", "country": "kenya"}
# setdefault = backup.setdefault("ethnicity", "kamba")
# print(setdefault)
setdefault = new_dict.setdefault("name", "purity")
print(setdefault)
print(new_dict)

updating = my_dict.update(new_dict)
# print(updating)
print(new_dict)

new_keys = ["school", "gender", "class"]
new_values = ["kenyahigh","female", "form 4"]
complete_dict = dict(zip(new_keys, new_values))
print(complete_dict)

# my_dict.clear()
# print(my_dict)