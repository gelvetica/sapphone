from typing import Type
from gtts import gTTS
from pydantic import BaseModel, Field


class VoiceModel(BaseModel):
    lang: str = Field(default="en", title="Language", description="The language (IETF language tag) to read the text in. ")
    tld: str = Field(default='com', title='Top-level domain', description='Top-level domain for the Google Translate host, i.e https://translate.google.<tld>. Different Google domains can produce different localized ‘accents’ for a given language.')
    slow: bool = Field(default=False, title="Slow", description="Reads text more slowly.")

class ConfigModel(BaseModel):
    voice: VoiceModel = Field(default_factory=VoiceModel, title="Voice")

class SapphoneEngine:
    ConfigModel = ConfigModel

    def __init__(self, config: ConfigModel):
        self.config = config.model_dump()

    def speak_to_file(self, script, output):
        gTTS(script, **self.config["voice"]).save(output)