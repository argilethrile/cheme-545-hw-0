def extract_parameter(unit_name, parameter_name, index):
    try:
        unitname_dict = unit_operations_data[unit_name] # Get the value attached to unit_name, which is a dictionary
    except KeyError:
        print(f"The unit name {unit_name} doesn't exist in unit_operations_data.") # If this throws the KeyError exception, let the user know that their key doesn't exist
        print("The available unit names are:") # Give them a list of available unit_names
        pretty_string="" # Print available unit names in a nice format
        for k in unit_operations_data.keys():
            if len(pretty_string) == 0:
                pretty_string += k
            else:
                pretty_string += f",{k}"
        print(pretty_string)
        return "Invalid input"

    try:
        index_val = unitname_dict[parameter_name][index] # Get the value in the correct unit_name dictionary that corresponds to parameter, which is a list
                                                         # Then get the requested index in that list
    except KeyError:
        print(f"The parameter {parameter_name} doesn't exist for the unit {unit_name}.") # Alert the user if the requested parameter doesn't exist for this unit_name
        print("The available parameters are:")
        pretty_string="" # Print available unit names in a nice format
        for k in unitname_dict.keys():
            if len(pretty_string) == 0:
                pretty_string += k
            else:
                pretty_string += f",{k}"
        print(pretty_string)
        return "Invalid input"
    except IndexError:
        print(f"The index {index} is out of range for the parameter list {parameter_name} for the unit {unit_name}.") # Alert the user if the requested index doesn't exist for this parameter
        print(f"The index for {parameter_name} must be between 0 and {len(unitname_dict[parameter_name]) - 1}") # Give them the possible index values for this parameter
        return "Invalid input"
    
    return f"{unit_name}_{parameter_name}_{index_val}"