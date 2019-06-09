import json

from jira import JIRA
from os.path import expanduser

open_statuses = []
homedir = expanduser("~")

class JiraAction():
    open_statuses = []
    homedir = expanduser("~")
    jira = None

    def __init__(self):
        print("Init jira action")

    def setup(self):
        if self.jira == None:
            print("running setup")
            with open(homedir + "/.jirator/config") as fh:
                data = json.load(fh)
            options = {
                "server": data["server"]
            }
            self.jira = JIRA(options=options,basic_auth=(data["username"],data["password"]))
            for s in data["status"]:
                app = '\"' + s + '\"'
                self.open_statuses.append(app)

    def fetch_open_issues(self):
        statuses = ",".join(self.open_statuses)
        my_issues = self.jira.search_issues('assignee=currentUser() and status in (' + statuses + ')')
        return my_issues
