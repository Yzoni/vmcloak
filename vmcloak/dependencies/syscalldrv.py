# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-322b479daa63760455c69dfc64bb15c9/syscalldrv-x64-1_0.zip",
        "sha1": "bebef2470d3a4a7dc05a574dfb05fde375ba6949",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")