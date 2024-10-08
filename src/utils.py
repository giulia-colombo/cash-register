def sanitize_user_input(input):
    '''Takes user input and returns it as a lowercase string, without trailing spaces and a single space in between every word'''
    sanitized_input = input.lower().strip()
    sanitized_input = " ".join(sanitized_input.split())
    return sanitized_input