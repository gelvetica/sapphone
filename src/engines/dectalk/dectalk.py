import subprocess
import sys
from pydantic import BaseModel, Field


class AdvancedConfig(BaseModel):
    prefix: str = Field(default="", title="Prefix", description="Text to be passed to DECtalk Software before the normal input. The prefix text is \"forced\" out before the input text is read.")
    suffix: str = Field(default="", title="Suffix", description="Text to be passed to DECtalk Software after the normal input. ")

class EngineConfig(BaseModel):
    path_to_executable: str = Field(title="Path to executable", description="The path to your DECtalk say executable.")

class ConfigModel(BaseModel):
    advanced: AdvancedConfig = Field(title="Advanced", default_factory=AdvancedConfig)
    engine: EngineConfig = Field(title="Engine", default_factory=EngineConfig)

class SapphoneEngine:
    ConfigModel = ConfigModel
    def __init__(self, config: ConfigModel):
        self.config: ConfigModel = config

    def dectalk_windows(self, script, output):
        args = []
        args += [self.config.engine.path_to_executable]
        if self.config.advanced.prefix != "":
            args += ["-pre", self.config.advanced.prefix]
        if self.config.advanced.suffix != "":
            args += ["-post", self.config.advanced.suffix]
        args += ["-w", output]
        #args.append(script)
        subprocess.run(args, shell=False, check=True, input=script, text=True)

    def dectalk_linux(self, script, output):
        args = []
        args += [self.config.engine.path_to_executable]
        if self.config.advanced.prefix != "":
            args += ["-pre", self.config.advanced.prefix]
        if self.config.advanced.suffix != "":
            args += ["-post", self.config.advanced.suffix]
        args += ["-fo", output]
        args += ["-a", script]
        subprocess.run(args, shell=False, check=True)

    def dectalk_macos(self, script, output):
        args = [self.config.engine.path_to_executable]
        if self.config.advanced.prefix:
            args += ["-pre", self.config.advanced.prefix]
        if self.config.advanced.suffix:
            args += ["-post", self.config.advanced.suffix]
        args += ["-fo", output]
        args += ["-a", script]
        subprocess.run(args, shell=False, check=True)

    def speak_to_file(self, script, output):
        if sys.platform in ["win32", "cygwin"]:
            self.dectalk_windows(script, output)
        elif sys.platform == "linux":
            self.dectalk_linux(script, output)
        elif sys.platform == "darwin":
            self.dectalk_macos(script, output)
        else:
            raise OSError("I'm so sorry. Please install a real OS. Or keep using FreeBSD because you're cool idk")

