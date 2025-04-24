# win32com might not be necessary here
# pyttsx uses comtypes but it still depends on win32com ???
import sys
from typing import Any

import comtypes.client
import win32com.client
from pydantic import BaseModel, Field, BeforeValidator
from typing_extensions import Annotated

try:
    from comtypes.gen import SpeechLib
except ImportError:
    # Generate the SpeechLib lib and any associated files
    engine = comtypes.client.CreateObject("SAPI.SpVoice")
    stream = comtypes.client.CreateObject("SAPI.SpFileStream")
    from comtypes.gen import SpeechLib


# This is improper

def voices_helper(value: Any) -> Any:
    tts = win32com.client.Dispatch("SAPI.SpVoice")
    voices = []
    for i in tts.GetVoices():
        voices.append(i.GetAttribute("Name"))
    if value in voices:
        return value
    else:
        print("Invalid voice selection, please set voice to one of the following:")
        for i in voices:
            print(i)
        input("\nPress Enter to close...")
        sys.exit(0)


class VoiceModel(BaseModel):
    voice: Annotated[str, Field(default="default value that causes it to fail", validate_default=True,
                                title="Voice"), BeforeValidator(voices_helper)]
    rate: float = Field(default=0, ge=-10, le=10, title="Rate")


class ConfigModel(BaseModel):
    voice: VoiceModel = Field(default_factory=VoiceModel, title="Voice")


# list of voice token attributes for testing
sapi_attributes = ["Name", "Gender", "Age", "Language", "Vendor"]


class SapphoneEngine:
    ConfigModel = ConfigModel

    def __init__(self, config):
        self.config = config
        self.tts = win32com.client.Dispatch("SAPI.SpVoice")
        for i in self.tts.GetVoices():
            if i.GetAttribute("Name") == self.config.voice.voice:
                self.tts.Voice = i
        self.tts.Rate = self.config.voice.rate

    def speak_to_file(self, script, output):
        output_stream = win32com.client.Dispatch("SAPI.SPFileStream")
        output_stream.Open(output, SpeechLib.SSFMCreateForWrite)
        tts_stream = self.tts.AudioOutputStream
        self.tts.AudioOutputStream = output_stream
        self.tts.Speak(script)
        self.tts.AudioOutputStream = tts_stream
        output_stream.close()
