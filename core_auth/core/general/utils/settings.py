import os

from .misc import yaml_coerce

# Pull environment variables from parents
# Use namespacing to select specific variables and not all of them


def get_settings_from_environment(prefix):
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
