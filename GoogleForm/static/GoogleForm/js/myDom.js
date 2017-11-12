var myDom = (function () {

    var getElById = function (id) {
        return $('#' + id);
    };

    var getElByClass = function (cls) {
        return $('.' + cls).first();     //returns first element
    };

    var getElsByClass = function (cls) {
        return $('.' + cls);             //returns array of matched elements
    };

    return {
      getElById : getElById,
      getElByClass : getElByClass,
      getElsByClass : getElsByClass,
    };

})();
