def get_float_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Please enter a valid number.")


def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("Please enter a valid integer.")
