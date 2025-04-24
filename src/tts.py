import os
from typing import Type

from pydantic import BaseModel

import plugins


class SapphoneEngine:
    ConfigModel: Type[BaseModel]

    def __init__(self, config: BaseModel):
        """
        """
        self.config = config

    def speak_to_file(self, script, output):
        """
        """


class SapphoneTTS:
    def __init__(self, engine: str, config: dict):
        self.engine: Type[SapphoneEngine] = engines[engine].SapphoneEngine
        print(config)
        self.instance: SapphoneEngine = self.engine(self.engine.ConfigModel(**config))

    def speak_to_file(self, output_file, script):
        self.instance.speak_to_file(script, output_file)


PluginManager = plugins.PluginManager()
PluginManager.import_plugins_from_directory(os.path.join(os.path.dirname(os.path.realpath(__file__)), "engines"))
engines = PluginManager.plugins
