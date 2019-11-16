# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Winlogbeat(Dependency):
    name = "winlogbeat"
    description = "Preconfigured Winlogbeat: Windows event log streamer"
    default = "7.4.2"
    exes = [{
        "version": "7.4.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-52e20ae9ab546f876052c3e3271ef59f/winlogbeat.zip",
        "sha1": "8a93aae79c794d94f37f5a86eb5ea65c0c80389d",
    }]

    def run(self):
        self.upload_dependency("C:\\winlogbeat-7.4.2-windows-x86_64.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\winlogbeat-7.4.2-windows-x86_64.zip")
