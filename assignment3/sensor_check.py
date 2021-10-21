def temperature_in_range(temperature, min_temp=60, max_temp=90):
    return min_temp <= temperature <= max_temp

def humidity_in_range(humidity, min_humidity=25, max_humidity=40):
    """Is humidity within the range  < 25 to 40> Yes : Pass , No : Fail"""
    return min_humidity <= humidity <= max_humidity

def seconds_in_range(seconds, min_seconds=10, max_seconds=20):
    """Does the output readings reset within the range of 10 to 20 secs , Yes :  Pass, No : fail"""
    return min_seconds <= seconds <= max_seconds

def data_similar(cloud_data, local_data):
    """Does the data displayed on thingspeak cloud as well showed on the RSPi local terminal similar < yes : Pass and NO Fail >"""
    if not isinstance(cloud_data, (list, tuple)):
        raise TypeError(f'Invalid type for cloud_data: {type(cloud_data)}')
    if not isinstance(local_data, (list, tuple)):
        raise TypeError(f'Invalid type for local_data: {type(local_data)}')
    if len(cloud_data) != len(local_data):
        raise ValueError('cloud_data and local_data must have the same number of elements')
    for c_datum, l_datum in zip(cloud_data, local_data):
        if c_datum != l_datum:
            return False
    return True