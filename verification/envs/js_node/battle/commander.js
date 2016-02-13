"use strict";

function Client() {}

var SAMPLE_ITEM_INFO = {
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
};

// ASK

Client.prototype.askMyInfo = function () {
    return SAMPLE_ITEM_INFO;
};

Client.prototype.askItemInfo = function () {
    return SAMPLE_ITEM_INFO;
};

Client.prototype.askNearestEnemy = function () {
    return SAMPLE_ITEM_INFO;
};

Client.prototype.askItems = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askEnemyItems = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askMyItems = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askBuildings = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askTowers = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askCenter = function () {
    return SAMPLE_ITEM_INFO;
};

Client.prototype.askUnits = function () {
    return [SAMPLE_ITEM_INFO, SAMPLE_ITEM_INFO];
};

Client.prototype.askMyRangeEnemyItems = function () {
    return [];
};

Client.prototype.askCurTime = function () {
    return 1;
};


// DO

Client.prototype.doAttack = function () {
    return;
};

Client.prototype.doMove = function () {
    return;
};

Client.prototype.doMoves = function () {
    return;
};

Client.prototype.doMessageToId = function (message, id) {
    return;
};

Client.prototype.doMessageToCraft = function (message, id) {
    return;
};

Client.prototype.doMessageToTeam = function (message, id) {
    return;
};

// SUBSCRIBE

Client.prototype.when = function () {
    return new Promise(function(){});
};

Client.prototype.unSubscribeAll = function () {
    return this.when();
};

Client.prototype.whenInArea = function () {
    return this.when();
};

Client.prototype.whenItemInArea = function () {
    return this.when();
};

Client.prototype.whenStoped = function () {
    return this.when();
};

Client.prototype.whenIdle = function () {
    return this.when();
};

Client.prototype.whenEnemyInRange = function () {
    return this.when();
};

Client.prototype.whenEnemyOutRange = function () {
    return this.when();
};

Client.prototype.whenItemDestroyed = function () {
    return this.when();
};

Client.prototype.whenTime = function () {
    return this.when();
};

Client.prototype.whenMessage = function () {
    return this.when();
};

exports.Client = Client;