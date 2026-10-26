class Suspect:
    def __init__(self, name, dialogue):
        self._name = name
        self._dialogue = dialogue
    
    def get_name(self):
        return self._name
    def get_dialogue(self):
        return self._dialogue