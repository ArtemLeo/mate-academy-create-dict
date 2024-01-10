def create_dict(*args) -> dict:
    result_dict = {}
    for key, value in enumerate(args):
        invalid_types = (list, dict, set)
        if isinstance(value, invalid_types):
            print(f"Cannot add {value} to the dict!")
        else:
            result_dict[value] = key
    return result_dict
