import json

from jira import JIRA
from jira import JIRAError
from os.path import expanduser
from constant import LOGGER
from userdata import UserData
import logging
import subprocess

open_statuses = []
homedir = expanduser("~")

class JiraAction():
    open_statuses = []
    homedir = expanduser("~")
    jira = None
    userdata = UserData()

    def setup(self):
        if self.jira == None:
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

    def save_or_return_dtid(self,issuekey):
        sdtid = self.userdata.default_transition_id()

        if sdtid is not None:
            return sdtid

        print("Could not find any default transition id for this issue; please select one to use as the default 'in progress' transition:\n")

        trs = self.jira.transitions(issuekey)
        for idx, t in enumerate(trs):
            tch = t["to"]
            d = "no description" if not tch["description"] else tch["description"]
            print("\t%d) %s (%s)" % (idx+1, tch["name"], d))

        selected = 0
        while True:
            try:
                sel = int(input("\nPlease specify the number of the transition you want to use as default: "))
                if (sel >= 1) and (sel <= len(trs)):
                    selected = sel
                    break
                print("Please enter a number between %d and %d" % (1,len(trs)))
            except:
                print("Please enter a number between %d and %d" % (1, len(trs)))

        tid = trs[selected-1]
        self.userdata.save_default_tid(tid["id"])
        return tid["id"]

    def assign_issue_to_self(self, issuekey):
        logging.debug("assigning %s to self" % (issuekey))
        dtid = self.userdata.default_transition_id()
        if dtid == None:
            logging.debug("could not find any default tid")
        else:
            logging.debug("using '%s' as tid" % (dtid))

        try:
            myself = self.jira.myself()
            issue = self.jira.issue(issuekey)
            tid = self.save_or_return_dtid(issuekey)
            issue.update(assignee={'name': myself["name"]})
            subprocess.call(["git","checkout","-b",issuekey])
        except JIRAError as e:
            logging.error("could not assign issue '%s' to self: '%s'" % (issuekey, e.text))
