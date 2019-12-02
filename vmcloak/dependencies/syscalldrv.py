# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.1"
    exes = [{
        "version": "1.1",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-80282ba481f7458fb825ef60e53b929b/syscalldrv-x64-1_1.zip",
        "sha1": "73fade332e9d22f0aa32ff471dbe14c330ef4244",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_1.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")