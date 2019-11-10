# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-fd6362d29b5845efafd48d9358956d15/syscalldrv-x64-1_0.zip",
        "sha1": "3283a92032b8e234808d11ae7c5b4bbe4a207f93",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")