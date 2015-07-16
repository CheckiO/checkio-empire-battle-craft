Here is where we will code our units. All units in the current craft have the same code which runs when a battle start. Units can ask for information about a battle or subscribe to various events.

**You main goal is destroy the enemy center**.

## Get Started

First we need to start a battle client for our unit.
This object is the main interface to manage by unit.
For that use the `commander` module with the `Client` class.

```javascript
var Client = require("battle/commander.js").Client;
var client = new Client();
```
