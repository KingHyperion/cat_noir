class Suspect:
    def __init__(self, suspect_id: str, name: str, alibi: str, dialogue: str):
        self._suspect_id = suspect_id
        self._name = name
        self._alibi = alibi
        self._dialogue = dialogue

    def get_name(self):
        return self._name
    def get_dialogue(self):
        return self._dialogue
    def get_alibi(self):
        return self._alibi