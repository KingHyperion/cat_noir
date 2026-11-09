class Suspect:
    def __init__(self, suspect_id: str, name: str, alibi: str, dialogue: str):
        self._suspect_id = suspect_id
        self._name = name
        self._alibi = alibi
        self._dialogue = dialogue

    def get_id(self): return self._suspect_id
    def get_name(self): return self._name
    def get_alibi(self): return self._alibi
    def get_dialogue(self): return self._dialogue

class Location:
    def __init__(self, location_id: str, name: str, description: str, suspect_ids: list = None):
        self._location_id = location_id
        self._name = name
        self._description = description
        self._suspect_ids = suspect_ids if suspect_ids else []

    def get_name(self): return self._name
    def get_description(self): return self._description
    def get_suspect_ids(self): return self._suspect_ids

class CaseData:
    def __init__(self, title: str, initial_suspect_ids: list, locations: dict, suspects: dict):
        self._title = title
        self._initial_suspect_ids = initial_suspect_ids
        self._locations = locations
        self._suspects = suspects

    def get_title(self): return self._title
    def get_initial_suspect_ids(self): return self._initial_suspect_ids
    def get_locations(self): return self._locations
    def get_suspects(self): return self._suspects