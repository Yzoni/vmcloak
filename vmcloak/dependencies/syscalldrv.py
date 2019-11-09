# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.0"
    exes = [{
        "version": "1.0",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-4c7e0648f2f13bf4883253b8bd87c041/syscalldrv-x64-1_0.zip",
        "sha1": "fb2347a982da59627ed89c246ee9ebe9e43a56d6",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_0.zip")

        # Enable powershell script execution
        self.a.execute("Set-ExecutionPolicy RemoteSigned -force")
        self.a.execute("bcdedit /set nointegritychecks off")
        self.a.execute("bcdedit /set testsigning on")