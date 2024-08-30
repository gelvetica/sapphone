import re
import yaml
import time
import tts

def load_config(file):
    with open(file) as f:
        return yaml.safe_load(f)


def save_config(file, config):
    pass


def follow(file, rate):
    file.seek(0, 2)

    while True:
        line = file.readline()

        if line:
            yield line
        else:
            time.sleep(rate)


def replace(match):
    return REPL_INDEX[match.lastindex - 1]


config = load_config("../config.yml")


REPL_DICT = config["basic_substitutions"]
REPL_PATTERN = re.compile("|".join(["\\b(" + v + ")\\b" for v in REPL_DICT.keys()]), flags=re.I)
REPL_INDEX = [k for k in REPL_DICT.values()]


def __main__():
    engine = tts.SapphoneTTS(config["tts"]["engine"], config["tts"]["engines"][config["tts"]["engine"]])

    logfile = open(config["target_file"], "r", encoding='utf-8')
    loglines = follow(logfile, config["refresh_rate"])

    for line in loglines:
        search = re.search(config["target_pattern"], line)
        if search:
            message = search.group(1)
            print(f"Received message: {message}")
            message = re.sub(REPL_PATTERN, replace, message)
            for pattern, substitution in config["regex_substitutions"].items():
                message = re.sub(pattern, substitution, message)

            print(f"Speaking message: {message}")
            engine.speak(message)


if __name__ == "__main__":
    __main__()
