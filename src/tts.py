import plugins

class SapphoneTTS:
    def __init__(self, engine, config):
        self.engine = engines[engine].SapphoneEngine(config)

    def speak_to_file(self, output_file, script):
        self.engine.speak_to_file(script, output_file)



PluginManager = plugins.PluginManager()
PluginManager.import_plugins_from_directory("engines")
engines = PluginManager.plugins