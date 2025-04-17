# The incredible README for sapphone tts
## Installation
If you're on Windows, you can grab a copy from the
[Releases page](https://github.com/gelvetica/sapphone/releases/).
If you're on Linux or MacOS, you can go cry in the corner because currently I don't really have a good way to package releases for these two.

Or you could clone the repo, install the requirements.txt, install mpv media player, and run `pyinstaller sapphone.spec` from the root of the repo, and have it packaged up in `.dist/sapphone`!

## Usage
1. Run sapphone.
2. Read the on-screen instructions.

## Extra Files
The `dectalk` and `modern-sam` engines require files that cannot be included due to the licensing of these two softwares.

### DECTalk
[DECTalk](https://en.wikipedia.org/wiki/DECtalk)
was originally developed by Digital Equipment Corporation, with later additions from [all of these wonderful people](https://github.com/dectalk/dectalk/graphs/contributors).
- [Windows](https://github.com/dectalk/dectalk/releases/download/2023-10-30/vs6.zip)
- [Linux](https://github.com/dectalk/dectalk/releases/download/2023-10-30/ubuntu-latest.tar.gz)
- [MacOS](https://github.com/dectalk/dectalk/releases/download/2023-10-30/macos-latest.tar.gz)

Extract the archive, and in the engine config, point `path_to_executable` to the absolute path of the `say` executable.

### modern-sam
[Software Automatic Mouth](https://en.wikipedia.org/wiki/Software_Automatic_Mouth)
was originally developed by Don't Ask Software. It was ported to C by [s-macke](https://github.com/s-macke), then Javascript by [discordier](https://github.com/discordier),
with additional improvements by [machineonamission](https://github.com/machineonamission), who has also provided the following CLI packages.
- [Windows](https://github.com/machineonamission/sam-cli/releases/download/1.0.0/sam-win.exe)
- [Linux](https://github.com/machineonamission/sam-cli/releases/download/1.0.0/sam-linux)
- [MacOS](https://github.com/machineonamission/sam-cli/releases/download/1.0.0/sam-macos)

In the engine config, point `path_to_executable` to the absolute path of the file you have downloaded.
