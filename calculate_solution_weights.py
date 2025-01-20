import re

def calculate_solution_weights(molecular_weights, solutions_needed):
    out_list = [] # Initialize the output list
    float_re = re.compile(r"(\d+.\d+)M") # Be a bit more efficient by pre-compiling the concentration parser regex
    int_re = re.compile(r"(\d+)M")
    for i in range(0,len(solutions_needed)): # Get the necessary data for each compound in solutions_needed
        compound_concentration = solutions_needed[i].split('-') # Get a list with the compound and concentration strings separated into a list
        compound = compound_concentration[0] # The compound name is the first element
        try: # for floats
            concentration = float(float_re.match(compound_concentration[1]).group(1)) # Parse the 2nd element with regex to get the concentration as a float
        except AttributeError: # for ints
            concentration = int(int_re.match(compound_concentration[1]).group(1))
        try:
            molweight = molecular_weights[compound] # Get the molecular weight from the dictionary, if it exists
            weight = molweight * concentration # Use it to calculate the weight
            out_list.append(f"{solutions_needed[i]}-{weight}g") # Add this to the output list
        except KeyError:
            out_list.append("unknown") # Add unknown back to the output list if the weight is unknown

    return out_list # return the modified list