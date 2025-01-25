from typing import Dict
from stack.stackitem import StackItem


def save_dict_to_file(dictionary, filename):
    try:
        with open(filename, "w") as file:
            for key, value in dictionary.items():
                file.write(f"{value}\n")
        print(f"Dictionary saved to {filename}.")
    except Exception as e:
        print(f"Error saving dictionary to file: {e}")


def read_file_to_dict(filename):
    try:
        dictionary: Dict[str, StackItem] = {}
        with open(filename, "r") as file:
            for line in file:
                # Split each line into key and value
                elements = line.strip().split()
                stack_item = StackItem(elements[0], elements[2])
                dictionary[elements[0]] = stack_item
                stack_item.parent = dictionary.get(elements[1])

        return dictionary
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}


def read_file_to_tuples(filename):
    try:
        tuples_list = []
        with open(filename, "r") as file:
            for line in file:
                # Split the line into tuple elements and convert to a tuple
                elements = line.strip().split()
                tuples_list.append(tuple(elements))
        return tuples_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def save_tuples_to_file(tuples_list, filename):
    try:
        with open(filename, "w") as file:
            for tpl in tuples_list:
                # Join tuple elements with space and write to the file
                file.write(" ".join(map(str, tpl)) + "\n")
        print(f"List of tuples saved to {filename}.")
    except Exception as e:
        print(f"Error saving tuples to file: {e}")


def print_tuples(tuples_list):
    for tpl in tuples_list:
        # Join tuple elements with space and write to the file
        print(" ".join(map(str, tpl)))


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(value)
