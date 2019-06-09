import argparse
from jiraaction import JiraAction
from consolemenu import *
from consolemenu.items import *

class WorkAction(argparse.Action):
    def __init__(self,option_strings,dest,nargs=None, **kwargs):
        print("running WorkAction init")
        super(WorkAction,self).__init__(option_strings,dest,**kwargs)

    def __call__(self,parser,namespace,values,option_string=None):
        setattr(namespace, self.dest,values)
        jira = JiraAction()
        jira.setup()

        my_issues = jira.fetch_open_issues()
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
