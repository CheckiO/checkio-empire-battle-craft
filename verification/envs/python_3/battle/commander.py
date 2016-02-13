class PARTY():
    REQUEST_NAME = 'parties'
    MY = "my"
    ENEMY = "enemy"
    ALL = (MY, ENEMY)


class ROLE():
    REQUEST_NAME = "roles"
    CENTER = "center"
    TOWER = "tower"
    UNIT = "unit"
    BUILDING = 'building'
    OBSTACLE = "obstacle"
    ALL = (CENTER, TOWER, UNIT, BUILDING, OBSTACLE)

SAMPLE_ITEM_INFO = {
    'id': 41,
    'player_id': 1,
    'role': "unit",
    'type': 'rocketBot',
    'hit_points': 100,
    'size': 0,
    'speed': 5,
    'coordinates': [35, 17],
    'rate_of_fire': 7,
    'damage_per_shot': 50,
    'area_damage_per_shot': 0,
    'area_damage_radius': 0,
    'firing_range': 5,
    'status': {'action': 'idle'},
}


class Client(object):

    @classmethod
    def set_client(cls, client):
        cls.CLIENT = client

    def ask(self, fields):
        return {}
    select = ask

    def ask_my_info(self):
        return SAMPLE_ITEM_INFO

    def ask_item_info(self, item_id):
        return SAMPLE_ITEM_INFO

    def ask_items(self, parties=PARTY.ALL, roles=ROLE.ALL):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_enemy_items(self):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_my_items(self):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_buildings(self):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_towers(self):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_center(self):
        return SAMPLE_ITEM_INFO

    def ask_units(self):
        return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO]

    def ask_nearest_enemy(self):
        return SAMPLE_ITEM_INFO

    def ask_my_range_enemy_items(self):
        return []

    def ask_cur_time(self):
        return 1

    def do_attack(self, item_id):
        pass

    def do_move(self, coordinates):
        pass

    def do_moves(self, steps):
        pass

    def do_message_to_id(self, message, item_id):
        return

    def do_message_to_craft(self, message):
        return

    def do_message_to_team(self, message):
        return

    def unsubscribe_all(self):
        pass

    def when_in_area(self, center, radius, callback):
        pass

    def when_item_in_area(self, center, radius, callback):
        pass

    def when_idle(self, callback):
        pass

    def when_enemy_in_range(self, callback):
        pass

    def when_enemy_out_range(self, item_id, callback):
        pass

    def when_item_destroyed(self, item_id, callback):
        pass

    def when_time(self, secs, callback):
        pass

    def when_message(self, callback, infinity=True):
        pass
