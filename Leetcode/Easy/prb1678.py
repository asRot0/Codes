import re

class Solution:
    def interpret(self, command: str) -> str:
        # command = re.sub('\(al\)', 'al', command)
        # command = re.sub('\(\)', 'o', command)
        return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))