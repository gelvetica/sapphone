import plugins
import tempfile
import pyaudio
import wave
import os


class SapphoneTTS:
    def __init__(self, engine, config):
        self.engine = engines[engine].SapphoneEngine(config)
        self.audio = pyaudio.PyAudio()

    def speak(self, script):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = os.path.join(tmpdir, "output.wav")
            self.engine.speak_to_file(script, output_file)
            with wave.open(output_file, 'rb') as output:
                stream = self.audio.open(format=self.audio.get_format_from_width(output.getsampwidth()),
                                         channels=output.getnchannels(),
                                         rate=output.getframerate(),
                                         output=True)

                while len(data := output.readframes(1024)):
                    stream.write(data)

                stream.close()

PluginManager = plugins.PluginManager()
PluginManager.import_plugins_from_directory("engines")
engines = PluginManager.plugins