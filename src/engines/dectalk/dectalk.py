import subprocess

ConfigStructure = {
    "advanced": {
        "prefix": {"type": "string", "default": ""},
        "suffix": {"type": "string", "default": ""}
    },
    "engine": {
        "path_to_executable": {"type": "string", "default": ""}
    }
}


class SapphoneEngine:
    def __init__(self, config):
        self.config = config

    def build_command_args(self):
        args = []
        args += [self.config["engine"]["path_to_executable"]]
        if self.config["advanced"]["prefix"] != "":
            args += ["-pre", self.config["advanced"]["prefix"]]
        if self.config["advanced"]["suffix"] != "":
            args += ["-post", self.config["advanced"]["suffix"]]
        return args

    def speak_to_file(self, script, output):
        command = self.build_command_args()
        command += ["-fo", output]
        command += ["-a", script]

        subprocess.run(command, shell=False, check=True)
