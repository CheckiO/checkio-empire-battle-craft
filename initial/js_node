"use strict";
var Client = require("battle/commander.js").Client;
var client = new Client();

function attackNearest() {
    var data = client.askNearestEnemy();
    client.doAttack(data.id);
    client.whenItemDestroyed(data.id).then(attackNearest);
}

attackNearest();