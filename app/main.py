def copy_file(input_str: str) -> None:
    validator = input_str.split()
    if len(validator) == 3 and validator[0] == "cp":
        key_name, old_name, new_name = validator
        if old_name != new_name:
            with (open(old_name, "r") as input_file,
                  open(new_name, "w") as output_file):
                output_file.write(input_file.read())
