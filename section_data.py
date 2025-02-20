import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


class DataStructureDemo:
    BOUNDARY_HIGH = 100
    BOUNDARY_LOW = 0

    def __init__(self, items: Optional[List[str]] = None, data: Optional[Dict[str, Any]] = None):
        self.items = items if items else []
        self.items_backup = []
        self.data = data if data else {}

    def add_item(self, item):
        """creates a backup and appends the given item"""
        self.items_backup = self.items.copy() #Explain: Here i used `.copy()` to prevent reference issues.
        self.items.append(item)

    def set_item(self, key, value):
        self.data[key] = value  #Explain: Store value as its original type.

    def transform_items(self, start_index: int = 0):
        result = []
        num_items = len(self.items)

        for idx, item in enumerate(self.items[start_index:], start=start_index):
            print(f"Transforming item {idx}/{num_items} ...")
            result.append(item.upper())
        return result
        
        

    def get_evaluation(self, value):
        if value > self.BOUNDARY_HIGH:
            return "Large"
        elif value <= self.BOUNDARY_LOW: #Explain: Added equal sign, due to requirement from test_data.
            return "Negative"
        else:
            return "Normal"

    def write_data(self, filepath: Union[str, Path]):
        with open(filepath, 'w', encoding="utf-8") as fd:
            #json.dump({"data": self.data}, fd)
            json.dump(self.data, fd)

            '''Explain: Fixed write_data() so it doesn't wrap self.data inside another dictionary. 
            Because previously the function had wraps self.data inside another dictionary ({"data": self.data}).
            No need to change read_data() it works fine.'''

    def read_data(self, filepath: Union[str, Path]):
        with open(filepath, 'r', encoding="utf-8") as fd:
            loaded_data = json.load(fd)
        self.data = loaded_data.copy()

def format_string(name, age):
        old_style = "Name: %s, Age: %d" % (name, age) 
        #Explain: here it already %d, which comes integer from method, i.e Integer
        #new_style = f"Name: {name}, Age: {age:.2f}" it take upto floating point and which we don't require. We require 'Int' in age for compare.
        new_style = f"Name: {name}, Age: {int(age)}"
        return old_style, new_style
       
