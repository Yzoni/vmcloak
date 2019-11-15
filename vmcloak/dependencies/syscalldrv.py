# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-8ce913ee5e39589cce1d61245b69d5d9/syscalldrv-x64-1_0.zip",
        "sha1": "9a3999c740f12c9a8b37daa6d5bd87fc56da4058",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")

        # Enable test-signing
        self.a.execute("bcdedit /set testsigning on")