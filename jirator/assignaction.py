import json
import argparse
from jiraaction import JiraAction

class AssignAction():
    def __call__(self, issue):
        self._assign_issue(issue)

    def _assign_issue(self,issue):
        jira = JiraAction()
        jira.setup()
        jira.assign_issue_to_self(issue)
