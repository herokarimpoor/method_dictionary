# Define a function that returns a dictionary
def create_dictionary(name, family, age, city):
    # Create a dictionary with the provided information
    person = {
        'name': name,
        'family': family,
        'age': age,
        'city': city
    }
    return person
# ------------------------------------------------------------
def merge_dicts(*args):

    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict
# ---------------------------------------------------------
def delete_key(dict, key_to_delete):

    if key_to_delete in dict:
        del dict[key_to_delete]
        print(f"Key '{key_to_delete}' has been deleted.")
    else:
        print(f"Key '{key_to_delete}' does not exist in the dictionary.")
# ------------------------------------------------------------

def pop_random_item(dictionary):
    if not dictionary:
        print("Dictionary is empty.")
        return None
    key, value = dictionary.popitem()
    print(f"Removed item: '{key}': {value}")
    return key, value
# -----------------------------------------------------------------
# Clear the dictionary using the function
def clear_dictionary(dictionary):
    dictionary.clear()
    print("Dictionary has been cleared.")
# -------------------------------------------------------------

# Method 1: Using copy() method
def copy_dictionary_method1(original_dict):
    copied_dict = original_dict.copy()
    return copied_dict

# Method 2: Using dict() constructor
def copy_dictionary_method2(original_dict):
    copied_dict = dict(original_dict)
    return copied_dict
# ---------------------------------------------------------

def create_dictionary(keys, initial_value=None):
    # Using the fromkeys() method to create a dictionary
    new_dict = dict.fromkeys(keys, initial_value)
    return new_dict
# -------------------------------------------------------------

def get_value(dictionary, key, default_value=None):
    # Using the get() method to retrieve the value
    value = dictionary.get(key, default_value)
    return value
# -----------------------------------------------------------------

def get_dict_items(dictionary):
    return list(dictionary.items())
# -------------------------------------------------------------------

def get_dict_keys(dictionary):
    return list(dictionary.keys())
# ------------------------------------------------------------------


def pop_key(dictionary, key, default_value=None):
    try:
        value = dictionary.pop(key)
        print(f"Removed '{key}': {value}")
        return value
    except KeyError:
        print(f"Key '{key}' not found in the dictionary.")
        return default_value
# -----------------------------------------------------------------------

def add_or_get_key(dictionary, key, default_value=None):
    value = dictionary.setdefault(key, default_value)
    return value
# -------------------------------------------------------------------------


def compare_dicts(dict1, dict2):
    # Check if both dictionaries have the same keys
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Check if the values for each key are the same
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False

    # If all checks pass, the dictionaries are equal
    return True
# --------------------------------------------------------------------------

def get_dict_length(my_dict):
    length = len(my_dict)
    return length
# --------------------------------------------------------------------------

def find_value_in_dictionary(my_dict, key_to_find):
    # Check if the key exists in the dictionary
    if key_to_find in my_dict:
        return my_dict[key_to_find]
    else:
        return None  # Return None if the key is not found
# ------------------------------------------------------------------------



