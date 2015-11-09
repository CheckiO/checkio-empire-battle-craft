"use strict";

function Client() {
    this.loop = {};
    this.myInfo = undefined;
}

Client.prototype.start = function () {
    return;
};

// ASK

Client.prototype.ask = function () {
    return;
};

Client.prototype.askMyInfo = function () {
    return {};
};

Client.prototype.askItemInfo = function () {
    return {};
};

Client.prototype.askNearestEnemy = function () {
    return {};
};

Client.prototype.askItems = function () {
    return [];
};

Client.prototype.askEnemyItems = function () {
    return [];
};

Client.prototype.askMyItems = function () {
    return [];
};

Client.prototype.askBuildings = function () {
    return [];
};

Client.prototype.askTowers = function () {
    return [];
};

Client.prototype.askCenter = function () {
    return {};
};

Client.prototype.askUnits = function () {
    return [];
};

Client.prototype.askPlayers = function () {
    return [];
};

Client.prototype.askEnemyPlayers = function () {
    return [];
};

Client.prototype.askMyRangeEnemyItems = function () {
    return [];
};

Client.prototype.askCurTime = function () {
    return [];
};


// DO

Client.prototype.do = function () {
    return;
};

Client.prototype.doAttack = function () {
    return;
};

Client.prototype.doMove = function () {
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