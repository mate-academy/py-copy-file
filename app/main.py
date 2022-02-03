def copy_file(command):
    command = command.split(' ')
    if command[1] != command[2]:
        with open(f'{command[1]}', 'r') as f:
            with open(f'{command[2]}', 'w') as fc:
                fc.write(f.read())


if __name__ == '__main__':
    copy_file('cp file.txt new_file.txt')
