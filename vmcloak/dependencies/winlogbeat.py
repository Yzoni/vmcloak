# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Winlogbeat(Dependency):
    name = "winlogbeat"
    description = "Preconfigured Winlogbeat: Windows event log streamer"
    default = "7.4.2"
    exes = [{
        "version": "7.4.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-afb4c1b0c153b96c5b8e6e081bb620a0/winlogbeat.zip",
        "sha1": "69a09fdf6916d6b900c304e68936dd6030752825",
    }]

    def run(self):
        self.upload_dependency("C:\\winlogbeat-7.4.2-windows-x86_64.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\winlogbeat-7.4.2-windows-x86_64.zip")
