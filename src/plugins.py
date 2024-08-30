import importlib
import importlib.util
import os

# I copied this structure from an older project completely unrelated to sapphone
# and this could really be written better


def plugins_in_directory(directory):
    dirlist = []
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,filename)): # and os.path.exists(os.path.join(directory,filename, "plugin.json")):
            dirlist.append(os.path.join(directory,filename))
    for i in dirlist:
        # Remove pycache folder from returned list bc i dont test things properly
        # Pycharm for the love of god stop spellchecking my comments
        if "__pycache__" in i:
            dirlist.remove(i)
    return dirlist


class PluginManager:
    def __init__(self):
        self.plugins = {}
    def import_plugin(self, directory):
        module_id = os.path.basename(os.path.normpath(directory))
        spec = importlib.util.spec_from_file_location(module_id, os.path.join(directory, f"{module_id}.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.plugins[module_id] = module
    def import_plugins_from_directory(self, directory):
        for plugin in plugins_in_directory(directory):
            self.import_plugin(plugin)