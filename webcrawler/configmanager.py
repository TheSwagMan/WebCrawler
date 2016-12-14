#! /usr/bin/python3

class ConfigManager():
    is_file_open=False
    confilename = ""
    configuration= {}
    def __init__(self,conffile):
        self.confilename=conffile
        self.confile=open(self.confilename,"r")
        self.is_file_open=True
        self.parse_file()

    def parse_file(self):
        if self.is_file_open:
            for line in self.confile.readlines():
                self.parse_line(line)
        else:
            raise Exception("File error !")

    def parse_line(self,line):
        self.configuration+={"ok": "ok"}
        print(self.configuration)