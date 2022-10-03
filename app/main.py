def copy_file(cp: str):
    arr1 = cp.split(' ')
    if arr1[1] != arr1[2]:
        with open(arr1[1], "r") as file_in, open(arr1[2], "w") as file_out:
            file_out.write(file_in.read())
