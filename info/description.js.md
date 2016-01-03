Let's work on some new code for our units. All units in the current craft run the same code which starts when a battle begins. The script you are currently writing will command one craft. So if a craft has 7 units inside, that means 7 copies of this script will be launched.

The commanding principles are based on the 3 main groups of functions.

**Asks** are started with _ask_. Ask functions provide information about the unit you control or environment around it. For example, check out the following code...

```javascript
var Client = require("battle/commander.js").Client;
var client = new Client();
myInfo = client.askMyInfo();
console.log("My ID: " + myInfo.id);
```

... this shows a current unit's ID in the battle console.

**Actions** are started with _do_. The Action function sends a command to a unit. The unit can only hold information about the last command, so every following command will overwrite previous one. For example, check out the following code...

```javascript
var Client = require("battle/commander.js").Client;
var client = new Client();
client.doMove([30, 30]);
client.doMove([20, 30]);
```

... that code commands units to go to the point (20, 30), but the unit will never get to the point (30, 30).

**Subscriptions** are started with _when_. The subscribe function always has a callback argument. Callback is the function that gets called when a specific event occurs. For example, check out the following code...

```javascript
var Client = require("battle/commander.js").Client;
var client = new Client();

function attackNearEnemy(data){
    client.doAttack(data.id);
}

client.whenEnemyInRange(attackNearEnemy);
```

... that commands the unit to attack any enemy that comes into its firing range.

**Logs**. Feel free to use the _console.log_ function and see every script's output in the right-hand panel for battle replays.

**Your main goal is to destroy the enemy center**.


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

- `askMyInfo()` Returns information about the current item.

- `askItemInfo(item_id)` Returns information about the item with `id == item_id` or None.

- `askEnemyItems()` Returns a list with information on the enemy items.

- `askMyItems()` Returns a list with information on your items.

- `askBuildings()` Returns a list with information for all buildings including the Command Center.

- `askTowers()` Returns a list with information for all towers.

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

- `doMessageToId(message, item_id)` send a message to a unit with `item_id`.

- `doMessageToCraft(message)` send a message to all units from your craft.

- `doMessageToTeam(message)` send a message to all units from your team.


## Subscribes.

You can subscribe your units to an event and when this event occurs the _callback_ function
will be called. The callback function will receive input data related to the subscription.
All subscriptions are disposable and removed when triggered.

_every function in this category returns a promise object so you can pass your callback function into its then method. For example:_

```javascript
client.whenItemDestroyed(data.id).then(attackNearest);
```

_Here https://www.promisejs.org/ you can find more about promices functionality_

- `whenInArea(center, radius)` Is triggered when the current unit is in the circle. _center_ describes the coordinates of the center point and _radius_ describes the length of the circle's radius.

- `whenItemInArea(center, radius)` The same as `whenInArea` but gets triggered for any item.

- `whenIdle()` Is triggered when the current unit is idle (finishes moving,
  destroys an enemy or doesn't have commands).

- `whenEnemyInRange()` Is triggered when an enemy item is in the current item's
   firing range.

- `whenEnemyOutRange(item_id)` Is triggered when the item with _item_id_ is
  out of the current item's firing range.

- `whenItemDestroyed(item_id)` Is triggered when the item with _item_id_ is destroyed.

### LEVEL 2

for units with level 2 or more.

- `whenTime(secs)` Is triggered at a specific game time. Very useful for the synchronization of units.

### LEVEL 4

for units with level 4 or more.

- `whenMessage()` Is triggered when a unit gets a message from another unit. Be aware that promise only resolve the first message in the stack. If you want to get another, you should call whenMessage again.
