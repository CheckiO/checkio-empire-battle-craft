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


_tower_example = {
    'id': 10,
    'player_id': 0,
    'role': "tower",
    'hit_points': 1100,
    'size': 2,
    'speed': 0,
    'coordinates': [25, 16],
    'rate_of_fire': 7,
    'damage_per_shot': 50,
    'area_damage_per_shot': 0,
    'area_damage_radius': 0,
    'firing_range': 5,
    'action': "charge",

}
_unit_example1 = {
    'id': 42,
    'player_id': 1,
    'role': "unit",
    'hit_points': 100,
    'size': 0,
    'speed': 5,
    'coordinates': [35, 16],
    'rate_of_fire': 7,
    'damage_per_shot': 50,
    'area_damage_per_shot': 0,
    'area_damage_radius': 0,
    'firing_range': 5,
    'action': "move",

}
_unit_example2 = {
    'id': 41,
    'player_id': 1,
    'role': "unit",
    'hit_points': 100,
    'size': 0,
    'speed': 5,
    'coordinates': [35, 17],
    'rate_of_fire': 7,
    'damage_per_shot': 50,
    'area_damage_per_shot': 0,
    'area_damage_radius': 0,
    'firing_range': 5,
    'action': "move",

}
_center_example = {
    'id': 1,
    'player_id': 0,
    'role': ROLE.CENTER,
    'hit_points': 2100,
    'size': 4,
    'coordinates': [20, 16],
    'action': "idle",

}

_building_example = {
    'id': 3,
    'player_id': 0,
    'role': ROLE.BUILDING,
    'hit_points': 2000,
    'size': 3,
    'coordinates': [30, 16],
    'action': "idle",

}
_obstacle_example = {
    'id': 99,
    'role': ROLE.OBSTACLE,
    'hit_points': 2100,
    'size': 3,
    'coordinates': [10, 10],
    'action': "idle",

}

_example_dict = {
    42: _unit_example1,
    41: _unit_example2,
    10: _tower_example,
    1: _center_example,
    3: _building_example,
    99: _obstacle_example
}


class Client(object):
    CLIENT = None

    def __init__(self):
        self._initial_info = self.ask_my_info()

    @property
    def item_id(self):
        return 42

    @property
    def player_id(self):
        return 1

    @classmethod
    def set_client(cls, client):
        cls.CLIENT = client

    def ask(self, fields):
        return {}
    select = ask

    def ask_my_info(self):
        return _unit_example1

    def ask_item_info(self, item_id):
        return _example_dict.get(item_id)

    def ask_items(self, parties=PARTY.ALL, roles=ROLE.ALL):
        return _example_dict.values()

    def ask_enemy_items(self):
        return [_center_example, _tower_example, _building_example]

    def ask_my_items(self):
        return [_unit_example1, _unit_example2]

    def ask_buildings(self):
        return [_building_example]

    def ask_towers(self):
        return [_tower_example]

    def ask_center(self):
        return _center_example

    def ask_units(self):
        return [_unit_example1, _unit_example2]

    def ask_players(self, parties=PARTY.ALL):
        return [{"id": 0}, {"id": 1}]

    def ask_enemy_players(self):
        return [{"id": 0}]

    def ask_nearest_enemy(self):
        return _center_example

    def ask_my_range_enemy_items(self):
        return [_center_example]
    ask_enemy_items_in_my_firing_range = ask_my_range_enemy_items

    def do_attack(self, item_id):
        isinstance(item_id, int) and item_id >= 0
    attack_item = do_attack

    def do_move(self, coordinates):
        return isinstance(coordinates, (tuple, list)) and len(coordinates) == 2
    move_to_point = do_move

    def when(self, event, callback, data=None):
        pass
    subscribe = when

    def unsubscribe_all(self):
        pass

    def when_in_area(self, center, radius, callback):
        return (isinstance(center, (tuple, list)) and len(center) == 2 and
                isinstance(radius, (int, float)) and radius >= 0)
    subscribe_im_in_area = when_in_area

    def when_item_in_area(self, center, radius, callback):
        return (isinstance(center, (tuple, list)) and len(center) == 2 and
                isinstance(radius, (int, float)) and radius >= 0)
    subscribe_any_item_in_area = when_item_in_area

    def when_stop(self, callback):
        return True
    subscribe_im_stop = when_stop

    def when_idle(self, callback):
        return True
    subscribe_im_idle = when_idle

    def when_enemy_in_range(self, callback):
        return True
    subscribe_enemy_in_my_firing_range = when_enemy_in_range

    def when_enemy_out_range(self, item_id, callback):
        return isinstance(item_id, int) and item_id >= 0
    subscribe_the_item_out_my_firing_range = when_enemy_out_range

    def when_item_destroyed(self, item_id, callback):
        return isinstance(item_id, int) and item_id >= 0
    subscribe_the_item_is_dead = when_item_destroyed

