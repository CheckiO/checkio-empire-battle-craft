Here we will code our units. All units in the current craft have the same code which runs when a battle starts. Units can ask for information about a battle or subscribe to various events.

**You main goal is destroy the enemy center**.

## Get Started

First we need to start a battle client for our unit.
This object is the main interface to manage a unit.
Use the `commander` module with the `Client` class.

```python
from battle import commander
unit_client = commander.Client()
```

Next we need the code to launch. This will kick off when we want our unit to attack the nearest enemy.
To find the nearest enemy, we'll use the `ask_nearest_enemy` command from the client.
This command will return a dictionary with item data. We only need the `id` now.
Attack the enemy with the `attack_item` command.
Next if we want to repeat the action after the enemy is destroyed, use the subscribe method with the
callback function `when_item_destroyed`. As an argument, this function receives the
id of the item which we are watching. As a callback, we can use the same function to
search for an enemy. Your function can receive a `data` argument which contains the data from a given event.
Now call your function.


```python
def attack_nearest(data=None, *args, **kwargs):
    nearest_enemy = unit_client.ask_nearest_enemy()
    unit_client.do_attack(nearest_enemy["id"])
    unit_client.when_item_destroyed(nearest_enemy["id"], attack_nearest)

attack_nearest()
```

After all that, your unit is ready to fight.

## Items

Units, towers, buildings and other objects on a map are called "items".
When you ask for info about items, you will receive a dictionary with the item data, or
a list of these dictionaries. The item info for can contain various fields, so it is better to use the `dict.get` method. An item can have the following keys:

- "id": (int) Unique identifier of the item. All items has this field.
- "player_id": (int) Ownership of the item.
- "role": (str) Describes the role of the item. It can be a `unit`, `tower`, `building`, `center`, or `obstacle`. You can read more below on the different roles.
- "hit_points": (int/float) Defines the durability of the item. If "hit_points" is zero or lower, then
  the item is destroyed.
- "coordinates": (list of two int/float): Item location coordinates. Units are single point objects.
  For large objects such as buildings, this field contains the coordinates of the center (middle) point.
- "size": (int/float) Units don't have a size. All static objects (buildings, towers etc) are
  square and the edge length is equal to their "size".
- "action": (str) What the item is doing. It can be `idle`, `move`, `shoot`, or `charge`.
- "speed": (int/float) This is a unit attribute only. It describes how fast the unit may move.
- "damage_per_shot": (int/float) This is a unit/tower attribute which describes how many hit points a shot will take.
- "rate_of_fire": (int/float) This is a unit/tower attributewhich describes how many shots per second the item can do.
- "firing_range": (int/float) This is a unit/tower attributewhich describes the maximum distance it can shoot.


### Roles

You can use predefined constants instead of string variables.

```python
from battle import ROLE
```

- `unit` - Mobile fighting items. Appears from crafts. `ROLE.UNIT`
- `tower` - Stationary fighting items. `ROLE.TOWER`
- `center` - Command Centers. The main building. If it's destroyed, then the battle is over. `ROLE.CENTER`
- `building` - All other stationary buildings. `ROLE.BUILDING`
- `obstacle` - Neutral stationary objects such as rocks. `ROLE.OBSTACLE`

## Ask info

- `ask_my_info()` Returns information about the current item.

- `ask_item_info(item_id)` Returns information about the item with `id == item_id` or None.

- `ask_enemy_items()` Returns a list with information on the enemy items.

- `ask_my_items()` Returns a list with information on your items.

- `ask_buildings()` Returns a list with information for all buildings including the Command Center.

- `ask_towers()` Return a list with information of all towers.

- `ask_center()` Returns information about the Command Center.

- `ask_units()` Returns a list with information for all units.

- `ask_nearest_enemy()` Returns information about the nearest enemy item.

- `ask_my_range_enemy_items()`  
    Returns a list with information on all enemies in the current items firing range.

## Commands.

- `do_attack(item_id)` Attack the item with `id == item_id`.
    If the target is too far, then unit will move to the target.

- `do_move(coordinates)` A unit only command.
    Move to the point with the given coordinates. _coordinates_: list/tuple of two int/float.


## Subscribes.

You can subscribe your units to an event and when this event occurs the _callback_ function
will be called. The callback function will receive input data related to the subscription.
All subscriptions are disposable and removed when triggered.

- `when_in_area(center, radius, callback)` Triggered when the current unit is in
  the circle. _center_ are the coordinates of the center point and _radius_ is length of circle radius.

- `when_item_in_area(center, radius, callback)` The same as `when_in_area` but
  triggered for any item.

- `when_idle(callback)` Triggered when the current unit is idle (finishes moving or
  destroys an enemy or doesn't have commands).

- `when_enemy_in_range(callback)` Triggered when an enemy item is in the current item
  firing range.

- `when_enemy_out_range(item_id, callback)` Triggered when the item with _item_id_ is
  out of the current item firing range.

- `when_item_destroyed(item_id, callback)` Triggered when the item with _item_id_ is destroyed.
