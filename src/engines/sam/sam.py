import subprocess

ConfigStructure = {
    "voice": {
        "speed": {"type": "int", "min": 1, "max": 255, "default": 72},
        "pitch": {"type": "int", "min": 0, "max": 255, "default": 64},
        "mouth": {"type": "int", "min": 0, "max": 255, "default": 128},
        "throat": {"type": "int", "min": 0, "max": 255, "default": 128}
    },
    "pronunciation": {
        "phonetic": {"type": "bool", "default": False},
        "sing": {"type": "bool", "default": False}
    },
    "engine": {
        "path_to_executable": {"type": "string", "default": ""}
    }
}

class SapphoneEngine:
    def __init__(self, config):
        self.config = config

    def build_command_args(self):
        # usage: sam [options] Word1 Word2 ....
        # options
        #     -phonetic         enters phonetic mode. (see below)
        #     -pitch number        set pitch value (default=64)
        #     -speed number        set speed value (default=72)
        #     -throat number        set throat value (default=128)
        #     -mouth number        set mouth value (default=128)
        #     -wav filename        output to wav instead of libsdl
        #     -sing            special treatment of pitch
        #     -debug            print additional debug messages
        voice = self.config["voice"]
        args = [self.config["engine"]["path_to_executable"]]
        args += ["-speed", str(voice["speed"]),
                "-pitch", str(voice["pitch"]),
                "-mouth", str(voice["mouth"]),
                "-throat", str(voice["throat"])]
        if self.config["pronunciation"]["phonetic"] is True:
            args.append("-phonetic")
        if self.config["pronunciation"]["sing"] is True:
            args.append("-sing")
        return args


    def speak_to_file(self, script, output):
        command = self.build_command_args()
        command += ["-wav", output]
        command.append(script)

        subprocess.run(command, shell=False, check=True)

