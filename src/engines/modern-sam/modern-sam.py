import re
import subprocess

from pydantic import BaseModel, Field


class VoiceConfig(BaseModel):
    speed: int = Field(ge=1, le=255, default=72, title="Speed")
    pitch: int = Field(ge=0, le=255, default=64, title="Pitch")
    mouth: int = Field(ge=0, le=255, default=128, title="Mouth")
    throat: int = Field(ge=0, le=255, default=128, title="Throat")


class PronunciationConfig(BaseModel):
    phonetic: bool = Field(default=False, title="Phonetic Mode",
                           description="bypass SAM's english parser and specify sounds through SAM's phonetic alphabet, see README.")
    sing: bool = Field(default=False, title="Sing Mode", description="SAM will speak at one pitch. good for singing.")
    moderncmu: bool = Field(default=True, title="Modern CMU",
                            description="uses CMUDict and to-words for better pronunciation and stress patterns.")


class EngineConfig(BaseModel):
    path_to_executable: str = Field(title="Path to executable", description="the path to the sam-cli executable")


class ConfigModel(BaseModel):
    voice: VoiceConfig = Field(title="Voice", default_factory=VoiceConfig)
    pronunciation: PronunciationConfig = Field(title="Pronunciation", default_factory=PronunciationConfig)
    engine: EngineConfig = Field(title="Engine", default_factory=EngineConfig)


class SapphoneEngine:
    ConfigModel = ConfigModel

    def __init__(self, config: ConfigModel):
        self.config: ConfigModel = config

    def build_command_args(self):
        voice = self.config.voice
        args = [self.config.engine.path_to_executable]
        args += ["--speed", str(voice.speed),
                 "--pitch", str(voice.pitch),
                 "--mouth", str(voice.pitch),
                 "--throat", str(voice.throat)]
        if self.config.pronunciation.phonetic is True:
            args.append("--phonetic")
        if self.config.pronunciation.sing is True:
            args.append("--singmode")
        if self.config.pronunciation.moderncmu is True:
            args.append("--moderncmu")
        return args

    def speak_to_file(self, script, output):
        # ensure script string does not add arguments to the command
        script = re.sub(r"^-+", "", script)
        command = self.build_command_args()
        command += ["--wav", output]
        command.append(script)

        subprocess.run(command, shell=False, check=True)
