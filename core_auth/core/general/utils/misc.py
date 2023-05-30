import yaml


def yaml_coerce(value):
    # Convert value to proper Python object
    # Converts string dict "{'apples: 1, 'bananas': 2}" to Python dict
    # usefull because somethins we need to stringify settings

    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
