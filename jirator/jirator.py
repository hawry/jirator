from jira import JIRA
from consolemenu import *
from consolemenu.items import *
from os.path import expanduser
import json

open_statuses = []
homedir = expanduser("~")

def setup():
    print("running setup")

    with open(homedir + "/.jirator/config") as fh:
        data = json.load(fh)

    options = {
        "server": data["server"]
    }

    jira = JIRA(options=options, basic_auth=(data["username"],data["password"]))
    for s in data["status"]:
        app = '\"' + s + '\"'
        open_statuses.append(app)
    return jira

def showmenu(commands):
    menu = ConsoleMenu("Jirator","Select issue to work on")
    for c in commands:
        menu.append_item(c)
    menu.show()

def fetch_issues(jira):
    statuses = ",".join(open_statuses)

    my_issues = jira.search_issues('assignee=currentUser() and status in (' + statuses +')')
    cmds = []
    for issue in my_issues:
        cmd_item = CommandItem('{}: {}'.format(issue.key, issue.fields.summary), "git", ["checkout","-b",issue.key], should_exit=True)
        cmds.append(cmd_item)
    return cmds

def main():
    jira = setup()
    showmenu(fetch_issues(jira))
