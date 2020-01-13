# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Syscalldrv(Dependency):
    name = "syscalldrv"
    description = "Systemwide logger for system calls"
    default = "1.3"
    exes = [{
        "version": "1.3",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-af78a095c5fdc4a8c6549737b7c8c65b/syscalldrv-x64-1_3.zip",
        "sha1": "656155daf2f780effbc6c5de3ef1ccf9bde817aa",
    }]

    def run(self):
        self.upload_dependency("C:\\syscalldrv-x64-1_3.zip")