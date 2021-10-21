def temperature_in_range(temperature, min_temp=60, max_temp=90):
    """Check if temperature is in acceptable range.

    :param temperature: (int, float): temperature to check
    :param min_temp: (int, float): minimum acceptable temperature
    :param max_temp: (int, float): maximum acceptable temperature
    :return bool:
    """
    return min_temp <= temperature <= max_temp


def humidity_in_range(humidity, min_humidity=25, max_humidity=40):
    """Check if humidity is in acceptable range.

    :param humidity: (int, float): humidity to check
    :param min_humidity: (int, float): minimum acceptable humidity
    :param max_humidity: (int, float): maximum acceptable humidity
    :return bool:
    """
    return min_humidity <= humidity <= max_humidity


def seconds_in_range(seconds, min_seconds=10, max_seconds=20):
    """Check if seconds are in acceptable range.

    :param seconds: (int, float): seconds to check
    :param min_seconds: (int, float): minimum acceptable seconds
    :param max_seconds: (int, float): maximum acceptable seconds
    :return bool:
    """
    return min_seconds <= seconds <= max_seconds


def data_similar(cloud_data, local_data):
    """Check if two data collections are the same.

    :param cloud_data: (list, tuple): collection representing cloud data.
    :param local_data: (list, tuple): collection representing local data.
    :return bool:
    :raises TypeError: if cloud_data or local_data not a list or tuple
    :raises ValueError: if cloud_data and local_data are unequal in length
    """
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
