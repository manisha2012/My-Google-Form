var myEvents = (function () {

    var attachEvent = function (eventArr) {
        for(var i in eventArr) {
            var handler = eventArr[i].handler;
            var target = eventArr[i].target;
            var type = eventArr[i].type;
            target.bind(type, handler);
        }

    };

    return {
        attachEvent : attachEvent
    };

})();