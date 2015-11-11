Let's work on some new code for our units. All units in the current craft run the same code which starts when a battle begins. Units can ask for information about a battle or subscribe to various events.

**Your main goal is destroy the enemy center**.

## Get Started

First we need to start a battle client for our unit.
This object is the main interface to manage a unit.
Use the `commander` module with the `Client` class.

```javascript
var Client = require("battle/commander.js").Client;
var client = new Client();
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


```javascript
function attackNearest() {
    var data = client.askNearestEnemy();
    client.doAttack(data.id);
    client.whenItemDestroyed(data.id).then(attackNearest);
}

attackNearest();
```

After all that, your unit is ready to fight.

## Battle Field

The battle field has a size of 40 by 40 tiles, but the half of that is occupied by rocks. Zero coordinates are placed in the top corner. This image should help you to understand how axises are located:
 
![Map Axises](map.png)

## Items

Units, towers, buildings and other objects on a map are called "items". When you ask for info about items, you will receive a dictionary with the item data, or a list of these dictionaries. The item info can contain various fields, so it is better to use the `dict.get` method. An item can have the following keys:

- "id": (int) Unique identifier of the item. All items have this field.
- "player_id": (int) Ownership of the item.
- "role": (str) Describes the role of the item. It can be a `unit`, `tower`, `building`, `center`, or `obstacle`. You can read more below on the different roles.
- "hit_points": (int/float) Defines the durability of the item. If "hit_points" is zero or lower, than
  the item is destroyed.
- "coordinates": (list of two int/float): Item location coordinates. Units are single point objects.
  For large objects such as buildings, this field contains the coordinates of the center (middle) point.
- "size": (int/float) Units don't have a size. All static objects (buildings, towers etc) are square and the edge length is equal to their "size".
- "action": (str) What the item is doing. It can be `idle`, `move`, `shoot`, or `charge`.
- "speed": (int/float) This is a unit attribute only. It describes how fast the unit may move.
- "damage_per_shot": (int/float) This is a unit/tower attribute which describes how many hit points a shot will take.
- "rate_of_fire": (int/float) This is a unit/tower attribute which describes how many shots per second the item can take.
- "firing_range": (int/float) This is a unit/tower attribute which describes the maximum distance it can shoot.

### Roles

You can use predefined constants instead of string variables.

```python
from battle import ROLE
```

- `unit` - Mobile fighting items. Appears from crafts. `ROLE.UNIT`
- `tower` - Stationary fighting items. `ROLE.TOWER`
- `center` - Command Centers. The main building. If it's destroyed, then a battle is over. `ROLE.CENTER`
- `building` - All other stationary buildings. `ROLE.BUILDING`
- `obstacle` - Neutral stationary objects such as rocks. `ROLE.OBSTACLE`

## Ask info

- `askMyInfo()` Returns information about the current item.

- `askItemInfo(item_id)` Returns information about the item with `id == item_id` or None.

- `askEnemyItems()` Returns a list with information on the enemy items.

- `askMyItems()` Returns a list with information on your items.

- `askBuildings()` Returns a list with information for all buildings including the Command Center.

- `askTowers()` Return a list with information of all towers.

- `askCenter()` Returns information about the Command Center.

- `askUnits()` Returns a list with information for all units.

- `askNearestEnemy()` Returns a list with information on all enemies in the current item's firing range.

- `askMyRangeEnemyItems()`  
    Returns a list with information on all enemies in the current items firing range.

- `askCurTime()`
    Returns current in-game time. (secs)

## Commands.

- `doAttack(item_id)` Attack the item with `id == item_id`.
    If the target is too far, then the unit will move to the target.

- `doMove(coordinates)` A unit only command.
    Move to the point with the given coordinates. _coordinates_: list/tuple of two int/float.

### LEVEL 4

for units with level 4 or more.

- `doMessageToId(message, item_id)` send a message to unit with `item_id`

- `doMessageToCraft(message)` send a message to all units from your craft

- `doMessageToTeam(message)` send a message to all units from your team


## Subscribes.

You can subscribe your units to an event and when this event occurs the _callback_ function
will be called. The callback function will receive input data related to the subscription.
All subscriptions are disposable and removed when triggered.

_every function in this category returns a promice object so you can pass your callback function into its then method. For example:_

```javascript
client.whenItemDestroyed(data.id).then(attackNearest);
```

_Here https://www.promisejs.org/ you can find more about promices functionality_

- `whenInArea(center, radius)` Triggered when the current unit is in the circle. _center_ describes the coordinates of the center point and _radius_ describes the length of the circle's radius.

- `whenItemInArea(center, radius)` The same as `whenInArea` but
  triggered for any item.

- `whenIdle()` Triggered when the current unit is idle (finishes moving or
  destroys an enemy or doesn't have commands).

- `whenEnemyInRange()` Triggered when an enemy item is in the current item's
   firing range.

- `whenEnemyOutRange(item_id)` Triggered when the item with _item_id_ is
  out of the current item's firing range.

- `whenItemDestroyed(item_id)` Triggered when the item with _item_id_ is destroyed.

### LEVEL 2

for units with level 2 or more.

- `whenTime(secs)` Triggered in a specific game time. Very useful for synchronization units

### LEVEL 4

for units with level 4 or more.

- `whenMessage()` Triggered when unit gets message from another unit. Be aware that promice will be resolve for only the first message  in stack. If you want to get one more you should call whenMessage again.
