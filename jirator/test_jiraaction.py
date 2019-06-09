from jiraaction import JiraAction
import json
import pytest
from mock import Mock, patch

class TestJiraAction(object):
    def setup_userdata(self,sut):
        userdata = Mock()
        userdata.server.return_value = "http://localhost:3000"
        userdata.username.return_value = "user"
        userdata.password.return_value = "pass"
        userdata.statuses.return_value = ["IN PROGRESS","TODO"]
        userdata.default_transition_id.return_value = "12"
        sut.userdata = userdata

    @patch("jirator.jiraaction.JIRA")
    def test_setup(self,jira):
        sut = JiraAction()
        self.setup_userdata(sut)
        sut.setup()

        jira.assert_called_once_with(options={'server': 'http://localhost:3000'},basic_auth=('user','pass'))
        assert "\"IN PROGRESS\"" in sut.open_statuses
        assert "\"TODO\"" in sut.open_statuses

    @patch("jirator.jiraaction.JIRA")
    def test_fetch_open_issues(self, jira):
        print("-----")
        sut = JiraAction()
        self.setup_userdata(sut)
        sut.setup()

        actual = sut.fetch_open_issues()
        os = []
        for s in ["IN PROGRESS","TODO"]:
            app = '\"' + s + '\"'
            os.append(app)
        statuses = ",".join(os)
        strass = 'assignee=currentUser() and status in ('+statuses+')'
        args,kwargs = jira().search_issues.call_args
        assert strass in args[0] # weird hack since the assert got funky when calling with quotations in the raw string

    @patch("jirator.jiraaction.JIRA")
    def test_save_or_return_dtid_tid_returned(self,jira):
        sut = JiraAction()
        self.setup_userdata(sut)
        sut.setup()

        assert sut.save_or_return_dtid("issue-1") == "12"

    testdata = [
        ("1","20"),
        ("2","21")
    ]

    @pytest.mark.parametrize("answer,expected", testdata)
    @patch("jirator.jiraaction.JIRA")
    def test_dtid_user_input(self,jira,answer,expected):
        sut = JiraAction()
        self.setup_userdata(sut)
        sut.setup()

        lst = []
        lst.append({"id": "20","to": {"name": "in progress","description":"in progress desc"}})
        lst.append({"id": "21","to": {"name": "done","description":"done desc"}})
        jira().transitions.return_value = lst
        with patch("__builtin__.input", return_value=answer) as mi:
            assert sut._dtid_user_input("any-1") == expected

    @patch("__builtin__.print")
    @patch("jirator.jiraaction.JIRA")
    def test_dtid_user_input_invalid_answer(self, jira, pri):
        sut = JiraAction()
        self.setup_userdata(sut)
        sut.setup()

        lst = []
        lst.append({"id": "20","to": {"name": "in progress","description":"in progress desc"}})
        lst.append({"id": "21","to": {"name": "done","description":"done desc"}})
        jira().transitions.return_value = lst

        with patch("__builtin__.input") as mi:
            mi.side_effect = ["invalid","3","2"]
            assert sut._dtid_user_input("any-1") == "21"
