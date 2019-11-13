# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Winlogbeat(Dependency):
    name = "winlogbeat"
    description = "Preconfigured Winlogbeat: Windows event log streamer"
    default = "7.4.2"
    exes = [{
        "version": "7.4.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-39dbd0212ced0518a6e32ca545dd46ce/winlogbeat-7.4.2-windows-x86_64.zip",
        "sha1": "fa6dde0461b343cd9ac3311df180897e7659a77e",
    }]

    def run(self):
        self.upload_dependency("C:\\winlogbeat-7.4.2-windows-x86_64.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\winlogbeat-7.4.2-windows-x86_64.zip")
