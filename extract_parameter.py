def extract_parameter(unit_name, parameter_name, index):
    try:
        unitname_dict = unit_operations_data[unit_name] # Get the value attached to unit_name, which is a dictionary
    except KeyError:
        return "Invalid input"

    try:
        index_val = unitname_dict[parameter_name][index] # Get the value in the correct unit_name dictionary that corresponds to parameter, which is a list
                                                         # Then get the requested index in that list
    except KeyError:
        return "Invalid input"
    except IndexError:
        return "Invalid input"
    
    print(f"{unit_name}_{parameter_name}_{index_val}")