# Copyright (C) 2019 Y. de Boer.


from vmcloak.abstract import Dependency

class Winlogbeat(Dependency):
    name = "winlogbeat"
    description = "Preconfigured Winlogbeat: Windows event log streamer"
    default = "7.4.2"
    exes = [{
        "version": "7.4.2",
        "arch": "amd64",
        "url": "https://user.fm/files/v2-1ca162f69887ec37d09eeac624d9d042/winlogbeat-7.4.2-windows-x86_64.zip",
        "sha1": "1d0c035b9b7f60146114b27d1e2dfec94ce14317",
    }]

    def run(self):
        self.upload_dependency("C:\\winlogbeat-7.4.2-windows-x86_64.zip")

        # Somehow cannot find the file...
        #self.a.extract("C:\\", "C:\\winlogbeat-7.4.2-windows-x86_64.zip")
