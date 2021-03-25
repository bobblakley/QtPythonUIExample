import json

# Demo for converting JSON String data to a Python Dictionary.
# JSON Data as a string
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
# Convert JSON string data to a Python Dictionary
print("Example of converting JSON string data to a Python Dictionary")
print("The raw input data type is: ", type(json_string)) # will print "string"
data = json.loads(json_string)
print("The output data type is:", type(data)) # Will print "Dictionary"
print(data)


# Demo of converting JSON data in a Python Dictionary to a string
# JSON Data as a Dictionary
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# Convert JSON Dictionary format of data into a String
print("\nExample of converting JSON data from a Dictionary to a string")
print("Raw Jason Data type is: ", type(x)) # Will print "Dictionary"
data2 = json.dumps(x, indent=4)
print("Converted Data Type of data2 is:", type(data2)) # Will print "string"
# Print out string type of JSON data
print(data2)

