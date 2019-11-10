# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-d9bd6f905c255a93c063a44149ede708/syscalldrv-x64-1_0.zip",
        "sha1": "604ec3745fbc5b07771db93e88751904558ab27e",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")