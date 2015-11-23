Let's work on some new code for our units. All units in the current craft run the same code which starts when a battle begins. Units can ask for information about a battle or subscribe to various events.

**Your main goal is to destroy the enemy center**.

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
This command will return a dictionary with the item data. We only need the `id` now.
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

## Battle Field

The battle field has a size of 40 by 40 tiles, but the half of that is occupied by rocks. The zero coordinates are placed in the top corner. This image should help you to understand how axises are situated:
 
![Map Axises](map.png)

## Items

Units, towers, buildings and other objects on the map are called "items". When you ask for info about specific items, you will receive a dictionary with the item data, or a list of these dictionaries. The item info can contain various fields, so it is better to use the `dict.get` method. An item can have the following keys:

- "id": (int) Unique identifier for the item. All items have this field.
- "player_id": (int) the ownership of the item.
- "role": (str) Describes the role of the item. It can be a `unit`, `tower`, `building`, `center`, or `obstacle`. You can read more below on the different roles.
- "hit_points": (int/float) Defines the durability of the item. If "hit_points" is zero or lower, the item is destroyed.
- "coordinates": (list of two int/float): The item's location coordinates. Units are single point objects.
  For large objects such as buildings, this field contains the coordinates of the center (middle) point.
- "size": (int/float) Units don't have a size. All static objects (buildings, towers etc) are square and the edge length is equal to their "size".
- "action": (str) What the item is doing. It can be `idle`, `move`, `shoot`, or `charge`.
- "speed": (int/float) This is a unit attribute only. It describes how fast the unit may move.
- "damage_per_shot": (int/float) This is a unit/tower attribute which describes how many hit points an attack will take.
- "rate_of_fire": (int/float) This is a unit/tower attribute which describes how many attacks per second the item can take.
- "firing_range": (int/float) This is a unit/tower attribute which describes the maximum distance it can attack.

### Roles

You can use predefined constants instead of string variables.

```python
from battle import ROLE
```

- `unit` - Mobile fighting items, these come from crafts. `ROLE.UNIT`
- `tower` - Stationary fighting items. `ROLE.TOWER`
- `center` - Command Centers, the main building in the game. If they're destroyed, then a battle is over. `ROLE.CENTER`
- `building` - All other stationary buildings. `ROLE.BUILDING`
- `obstacle` - Neutral stationary objects like rocks or plants. `ROLE.OBSTACLE`

## Ask info

- `ask_my_info()` Returns information about the current item.

- `ask_item_info(item_id)` Returns information about the item with `id == item_id` or None.

- `ask_enemy_items()` Returns a list with information on the enemy items.

- `ask_my_items()` Returns a list with information on your items.

- `ask_buildings()` Returns a list with information for all buildings including the Command Center.

- `ask_towers()` Returns a list with information for all towers.

- `ask_center()` Returns information about the Command Center.

- `ask_units()` Returns a list with information for all units.

- `ask_nearest_enemy()` Returns a list with information on all enemies in the current item's firing range.

- `ask_my_range_enemy_items()`  
    Returns a list with information on all enemies in the current items firing range.

- `ask_cur_time()`
    Returns current in-game time. (secs)

## Commands.

- `do_attack(item_id)` Attack the item with `id == item_id`.
    If the target is too far, then the unit will move to the target.

- `do_move(coordinates)` A unit only command.
    Move to the point with the given coordinates. _coordinates_: list/tuple of two int/float.

### LEVEL 4

for units with level 4 or more.

- `do_message_to_id(message, item_id)` send a message to a unit with `item_id`.

- `do_message_to_craft(message)` send a message to all units from your craft.

- `do_message_to_team(message)` send a message to all units from your team.


## Subscribes.

You can subscribe your units to an event and when this event occurs the _callback_ function
will be called. The callback function will receive input data related to the subscription.
All subscriptions are disposable and removed when triggered.

- `when_in_area(center, radius, callback)` Is triggered when the current unit is in the circle. _center_ describes the coordinates of the center point and _radius_ describes the length of the circle's radius.

- `when_item_in_area(center, radius, callback)` The same as `whenInArea` but gets triggered for any item.

- `when_idle(callback)` Is triggered when the current unit is idle (finishes moving,
  destroys an enemy or doesn't have commands).

- `when_enemy_in_range(callback)` Is triggered when an enemy item is in the current item's
   firing range.

- `when_enemy_out_range(item_id, callback)` Is triggered when the item with _item_id_ is
  out of the current item's firing range.

- `when_item_destroyed(item_id, callback)` Is triggered when the item with _item_id_ is destroyed.

### LEVEL 2

for units with level 2 or more.

- `when_time(secs, callback)` Is triggered at a specific game time. Very useful for the synchronization of units.

### LEVEL 4

for units with level 4 or more.

- `when_message(callback, infinity=True)` Is triggered when a unit gets a message from another unit. The `infinity` argument indicates that you don't need to subscribe on the event again after getting the message and should be used if you want use `when_message` again. The `callback` function gets one argument as a dict with the `message` and `from_id` keys.
