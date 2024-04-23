def validate_data_type(value, datatype):
    if not isinstance(value, datatype):
        raise ValueError(f'You entered incorrect datatype. Datatype for {value} should be {datatype}')
    return value
