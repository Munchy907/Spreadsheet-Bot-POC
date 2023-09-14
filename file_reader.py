def read_data_from_file(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data.append(line.strip().split(', '))
        return data
    except Exception as e:
        print(f'Error reading from {file_name}: {str(e)}')
        return None
