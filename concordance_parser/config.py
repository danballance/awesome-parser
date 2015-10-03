# encoding=utf8
import json


class Config(object):
    def __init__(self, arguments):
        self.params = json.load(open(arguments["--config"]))
        self.corpus = arguments["--corpus"]
        self.word = arguments["--word"]
        self.params["general"]["citations"] = arguments["--citations"]
        if '--filename' in arguments:
            self.params["general"]["filename"] = arguments["--filename"]
