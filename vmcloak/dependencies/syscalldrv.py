# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-8401285eba7292b56ba09a8ebb5b4239/syscalldrv-x64-1_0.zip",
        "sha1": "88812d039044ff880095a29ad1210c4edad4bf1f",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")
        self.a.extract("C:\\", "C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")