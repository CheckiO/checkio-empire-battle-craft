
class Client(object):
    def __init__(self):
        pass

    @classmethod
    def set_client(cls, client):
        pass

    def select(self, fields):
        pass

    def ask_initials(self):
        pass

    def ask_nearest_enemy(self):
        return {
            'id': 17
        }

    def subscribe(self, event, callback, data=None):
        pass

    def subscribe_item_in_range(self, callback, coordinates, range_value):
        pass

    def subscribe_item_in_my_range(self, callback):
        pass

    def subscribe_death_item(self, item_id, callback):
        pass

    def attack_item(self, item_id):
        pass
