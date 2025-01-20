# cheme-545-hw-0

## Problem 1
Ensure you have a dictionary called unit_operations_data whose values are dictionaries that hold parameters as keys and lists of parameter values as values. An example dictionary:

```
unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}
```
extract_parameter returns a string with the unit name you specify, the parameter you specify, and the value of that parameter for that unit at the index you specify. For example, `extract_parameter("distillation_column", "temperature", 1)` should return "distillation_column_temperature_160".

I used the try-except approach in a stepwise manner. First, the function tries to get the dictionary corresponding to the specified unit_name. If this throws a KeyException, the user is alerted and told what possible unit_names exist.

If no exception is thrown, the function tries to pull the list from the unit_name dictionary corresponding to the parameter provided, then get the value of the list at the index provided. If a KeyError is thrown, the user is alerted that their parameter name was invalid and a list of valid parameter names for that unit_name is printed. If an IndexError is thrown, the user is alerted that the provided list index is out of range, and the possible range of indices for this parameter's values in printed.

## Problem 2
`calculate_solution_weight` takes as input a dictionary with compound names (strings) as keys and their molecular weights (floats) as values, and a list with entries in the format "compoundname-concentration" where the concentration is in the form "(int or float)M" (e.g., "0.1M" or "1M").

The function will return a list with entries in the form "compoundname-concentration-weight" where weight = molecular weight * concentration. If a particular compoundname is not found in the molecular_weights dictionary, the entry for that compound is listed as "unknown". 

I iterated through the list first. For each entry, I split the string on "-", then got the strings for compoundname and concentration. I used regex to get just the int or float from the concentration string. I then used the try-except method. If the dictionary has a key that matched compoundname, weight is calculated according to the formula above and the new entry string is constructed and added to the output list. If a KeyError is thrown, "unknown" is added to the output list.