def write_data_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for row in data:
                file.write(', '.join(row) + '\n')
        return True
    except Exception as e:
        print(f'Error writing to {file_name}: {str(e)}')
        return False
