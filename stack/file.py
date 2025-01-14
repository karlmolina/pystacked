def save_dict_to_file(dictionary, filename):
    try:
        with open(filename, "w") as file:
            for key, value in dictionary.items():
                file.write(f"{key} {value}\n")
        print(f"Dictionary saved to {filename}.")
    except Exception as e:
        print(f"Error saving dictionary to file: {e}")


def read_file_to_dict(filename):
    try:
        dictionary = {}
        with open(filename, "r") as file:
            for line in file:
                # Split each line into key and value
                key, value = line.strip().split(maxsplit=1)
                dictionary[key] = value
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
