# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.2"
    exes = [{
        "version": "1.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-9491c2772dfc285cbc3a83609f5d2a3a/syscalldrv-x64-1_2.zip",
        "sha1": "5d984667a21cd0d480c36f7d994472c6d5eaf590",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_2.zip")