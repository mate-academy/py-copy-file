from app.errors import CommandError, CopyFileExistsError


def file_copy(command, file1, file2) -> bool:
    if command and command == 'cp':
        if file1 != file2:
            try:
                with open(file1, 'r') as f_base:
                    with open(file2, 'w') as f_copy:
                        print(f_base.read(), file=f_copy)
                        return True
            except FileNotFoundError as e:
                print(e)
                return False
        raise CopyFileExistsError(file2)
    raise CommandError(command)


def copy_file(command: str) -> bool:
    com_list = command.split()
    try:
        result = file_copy(com_list[0], com_list[1], com_list[2])
    except IndexError:
        print('Not all parameters are specified')
        return False
    except CommandError as e:
        print(e)
        print("Can't copy file")
        return False
    except CopyFileExistsError as e:
        print(e)
        print("Can't copy file")
        return False
    if not result:
        print("Can't copy file")
        return False
    print('File copy success!')
    return True
