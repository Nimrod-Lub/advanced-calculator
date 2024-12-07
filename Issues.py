from abc import ABC


class Issue(ABC):
    issue: str

    def __init__(self, issue_explanation: str):
        self.issue = issue_explanation

    def get_issue(self) -> str:
        return self.issue


class MathIssue(Issue):

    def __init__(self, issue_explanation: str):
        super().__init__(
            "The following expression is mathematically impossible: " + issue_explanation)


class ValueIssue(MathIssue):
    def __init__(self, issue_explanation: str):
        super().__init__(issue_explanation)