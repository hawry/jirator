from jiraaction import JiraAction
from consolemenu import *
from consolemenu.items import *
import logging

class WorkAction():
    jira = None
    def __init__(self):
        self.jira = JiraAction()
        self.jira.setup()

    def __call__(self):
        my_issues = self.jira.fetch_open_issues()
        self._showmenu(self._convert_to_command(my_issues))

    def _convert_to_command(self, issues):
        cmds = []
        for issue in issues:
            cmd_item = CommandItem('{}: {}'.format(issue.key, issue.fields.summary), "git",["checkout","-b",issue.key], should_exit=True)
            cmds.append(cmd_item)
        return cmds

    def _showmenu(self, commands):
        menu = ConsoleMenu("Jirator","Select issue to work on")
        for c in commands:
            menu.append_item(c)
        menu.show()
