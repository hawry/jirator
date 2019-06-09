from os.path import expanduser
from constant import CONFIG_DIR
import json

class UserData():
    homedir = expanduser("~")
    configinfo = {}

    def __init__(self):
        self._load()

    def _load(self):
        with open(self.homedir + CONFIG_DIR) as fh:
            self.configinfo = json.load(fh)

    def server(self):
        return self.configinfo["server"]

    def username(self):
        return self.configinfo["username"]

    def password(self):
        return self.configinfo["password"]

    def statuses(self):
        return self.configinfo["status"]

    def default_transition_id(self):
        if "dtid" not in self._runtime():
            return None
        return self._runtime()["dtid"]

    def save_default_tid(self, tid):
        if "runtime" not in self.configinfo:
            self.configinfo["runtime"] = {}
        self.configinfo["runtime"]["dtid"] = tid
        with open(self.homedir + CONFIG_DIR,"r+") as fh:
            json.dump(self.configinfo, fh, indent=4)

    def _runtime(self):
        if "runtime" not in self.configinfo:
            return {}
        return self.configinfo["runtime"]
