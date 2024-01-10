
# Functions with output
def format_name(f_name, l_name):
    """Take a first and last name and format it to 
    return the title case vesrion of the name."""
    if f_name == "" or l_name == "":
        return "You did't provide valid input."
    full_name = f_name + " " + l_name
    return full_name.title()


name = format_name(
    input("What is your first name? "), input("What is your last name? ")
)
print(name)
