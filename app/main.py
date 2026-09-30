def copy_file(command: str) -> None:
    arr = command.split(" ")

    if len(arr) != 3:
        return

    data_file_name = arr[1]
    report_file_name = arr[2]
    if arr[0] != "cp":
        return

    if data_file_name == report_file_name:
        return
    try:

        with open(data_file_name, "r") as input_file:
            with open(report_file_name, "w") as output_file:
                output_file.write(input_file.read())
    except FileNotFoundError:
        return
