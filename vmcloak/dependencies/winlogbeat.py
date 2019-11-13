# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Winlogbeat(Dependency):
    name = "winlogbeat"
    description = "Preconfigured Winlogbeat: Windows event log streamer"
    default = "7.4.2"
    exes = [{
        "version": "7.4.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-ae5b79ac05213d316505262ddb5b219f/winlogbeat-7.4.2-windows-x86_64.zip",
        "sha1": "e76fd50560ed8862d6d06b634ec450e133b5ef2a",
    }]

    def run(self):
        self.upload_dependency("C:\\winlogbeat-7.4.2-windows-x86_64.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\winlogbeat-7.4.2-windows-x86_64.zip")
