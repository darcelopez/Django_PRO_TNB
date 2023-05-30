
from core.general.utils.collections import deep_update
from core.general.utils.settings import get_settings_from_environment


"""
This takes env variables with a matching prefix, strips out the prefix, and adds it to globals

For example:
export CORESETTINGS_IN_DOCKER=true (environment variable)
"""

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  #type: ignore
