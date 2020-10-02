import importlib
import json

class EmployeeData:
    def __init__(self, id, name, age, date):
        self.id = id
        self.name = name
        self.age = age
        self.date = date

"""
https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041

    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    
    USAGE:
    jsonStr  = '{"name":"Bob", "age":23, "__module__":"__main__", "__class__":"EmployeeData"}'
    empData = json.loads(jsonStr, object_hook=dict_to_obj)  # or load(<json file>,....)
    print(empData.name)     
    
    __module__ should equal the package, ex /foo/employee/__init__.py  # if this has emp class then use 'employee'       
"""
def dict_to_obj(our_dict):
    
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")

        # XXX We use the built in __import__ function since the module name is not yet known at runtime XXX
        module = importlib.import_module(module_name)
        # module = __import__(module_name) # dosen't work with ?nested? modules

        # Get the class from the module
        class_ = getattr(module, class_name)

        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj


"""
  A function takes in a custom object and returns a dictionary representation of the object.
  This dict representation includes meta data such as the object's module and class names.
"""
def convert_to_dict(obj):

  #  Populate the dictionary with object meta data 
  obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
  }
  
  #  Populate the dictionary with object properties
  obj_dict.update(obj.__dict__)
  
  return obj_dict
  
  
if __name__ == '__main__':
    #dataDict = {"name":"Bob", "age":23, "__module__":"__main__", "__class__":"EmployeeData"}
    jsonStr  = '{"name":"Bob", "age":23, "__module__":"__main__", "__class__":"EmployeeData"}'
    #print(dataDict)
    empData = json.loads(jsonStr, object_hook=dict_to_obj)
    print(empData.name)
    
    dataDict = convert_to_dict(empData)
    print(dataDict)
