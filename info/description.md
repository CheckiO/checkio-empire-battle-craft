Here we will code our units. All units in the current craft has the same code and
 it will be run at begging of a battle. Unit can ask information about a battle or
 subscribe to various events.

**You main goal is destroy the enemy center**.

## Get Started

First we need to initialise a battle client for our unit.
This object is the main interface to manage by unit.
For that use `commander` module with `Client` class.

```python
from battle import commander
unit_client = commander.Client()
```

Next we need a code to launch. For example, we want our unit attack the nearest enemy.
To find the nearest enemy use `ask_nearest_enemy` command from the client.
This command will return a dictionary with item data. We need only `id` now.
Attack the enemy with `attack_item` command.
Next if we would to repeat it after the enemy is destroyed, use subscribe method with
callback function `subscribe_the_item_is_dead`. As an argument this function receive
id of the item which we are watching. And as callback we can use the same function that
search an enemy. Your function which is using for callback should can receive `data` argument,
that contains various data from an event.
And call your function.


```python
def attack_nearest(data=None, *args, **kwargs)
    nearest_enemy = unit_client.ask_nearest_enemy()
    unit_client.attack_item(nearest_enemy["id"])
    unit_client.subscribe_the_item_is_dead(nearest_enemy["id"], attack_nearest)

attack_nearest()
```

Now your unit is ready to fight.

## Items

Units, towers, buildings and other objects on a map are called "items".
When you ask info about some items, as result you receive a dictionary with item data or
a list of these dictionaries. The item info for various items can contain various field.
Thus is better to use `dict.get` method. An item can have next keys:

- "id": (int) Unique identifier of the item. All items has this field.
- "player_id": (int) Ownership of the item.
- "role": (str) This field is describe a role if the item. It can be
  `unit`, `tower`, `building`, `center`, `obstacle`. Below you can read more about roles.
- "hit_points": (int/float) Define durability of the item. If "hit_points" is zero or below, then
  the item is destroyed.
- "coordinates": (list of two int/float): Item location coordinates. Units are singular point objects.
  For sized objects as buildings this field is coordinates of the center (middle) point.
- "size": (int/float) Units don't have a size. All static objects (buildings, towers etc) are
  square and edge length is equal to "size".
- "action": (str) What the item is doing. Can be `idle`, `move`, `shoot`, `charge`.
- "speed": (int/float) Unit attribute only. Tiles in second speed.
- "damage_per_shot": (int/float) Unit and Tower attribute.
  How many hit points will be reduced to enemy per on shot.
- "rate_of_fire": (int/float) Unit and Tower attribute. How many shots per second an item can do.
- "firing_range": (int/float) Unit and Tower attribute. Maximum distance of shooting.


### Roles

You can use predefined constants instead string variables.

```python
from battle import ROLE
```

- `unit` - Mobile fighting item. Appear from crafts. `ROLE.UNIT`
- `tower` - Stationary fighting item. `ROLE.TOWER`
- `center` - Command Center. The main building. If it's destroyed, then a battle is over. `ROLE.CENTER`
- `building` - All other stationary buildings. `ROLE.BUILDING`
- `obstacle` - Neutral stationary objects like rocks. `ROLE.OBSTACLE`

## Ask info

- `ask_my_info()` Return information about the current managed item.

- `ask_item_info(item_id)` Return information about the item with `id == item_id` or None.

- `ask_enemy_items()` Return a list with information of enemy items.

- `ask_my_items()` Return a list with information of your items.

- `ask_buildings()` Return a list with information of all buildings.
    The Command Center is included.

- `ask_towers()` Return a list with information of all towers.

- `ask_center()` Return information about the Command Center.

- `ask_units()` Return a list with information of all units.

- `ask_nearest_enemy()` Return information about the nearest enemy item.

- `ask_enemy_items_in_my_firing_range()`  
    Return a list with information of all enemies in the current item firing range.

## Commands.

- `attack_item(item_i)` Attack the item with `id == item_id`.
    If the target is too far, then unit will move to target.

- `move_to_point(coordinates)` Unit only command.
    Move to the point with the given coordinates. _coordinates_: list/tuple of two int/float.


## Subscribes.

You can subscribe your unit to an event and when this event is occured, _callback_ function
will be called. The callback function will receive input data related to subscription.
All subscriptions are disposable and removed when triggered.

- `subscribe_im_in_area(center, radius, callback)` Triggered when the current unit in
  the circle. _center_ is coordinates of the center point and _radius_ is length of circle radius.

- `subscribe_any_item_in_area(center, radius, callback)` The same as `subscribe_im_in_area` but
  triggered for any item.

- `subscribe_im_idle(callback)` Triggered when the current unit is idle (finished moving or
  destroy enemy or don't have commands).

- `subscribe_enemy_in_my_firing_range(callback)` Triggered when an enemy item in the current item
  firing range.

- `subscribe_the_item_out_my_firing_range(item_id, callback)` Triggered when the item with _item_id_
  out of th current item firing range (leave or already out).

- `subscribe_the_item_is_dead(item_id, callback)` Triggered when the item with _item_id_ is destroyed.
