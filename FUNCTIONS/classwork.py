# LEGB
# Local
# Enclosed
# Global
# Builtin

json_file_path = '../JSONFILES/{}'


def get_data_from_file(file_name: str):
    with open(json_file_path.format(file_name), 'r') as file:
        result = file.read()
    return result


text = get_data_from_file('test.json')
text_1 = get_data_from_file('test_1.json')
print(text_1)
