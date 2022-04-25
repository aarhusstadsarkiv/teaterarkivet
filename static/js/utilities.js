// Place as first js-file after the jquery-library

// Avoid `console` errors in browsers that lack a console.
// https://github.com/h5bp/html5-boilerplate/blob/master/src/js/plugins.js
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

// helper-function
// https://websanova.com/blog/jquery/jquery-remove-class-by-regular-expression
(function($) {
    $.fn.hasClassRegEx = function(regex)
    {
        var classes = $(this).attr('class');
        if(!classes || !regex) return false;
        classes = classes.split(' ');
        for(var i=0, len=classes.length; i < len; i++) {
            if(classes[i].match(regex)) return true;
        }
        return false;
    }; 
})(jQuery);

// helper-function
// https://websanova.com/blog/jquery/jquery-remove-class-by-regular-expression
(function($) {
    $.fn.getClassRegEx = function(regex)
    {
        var classes = $(this).attr('class');
        if(!classes || !regex) return false;
        classes = classes.split(' ');
        for(var i=0, len=classes.length; i < len; i++) {
            if(classes[i].match(regex)) return classes[i];
        }
        return false;
    }; 
})(jQuery);

/**
 * http://creativenotice.com/2013/07/regular-expression-in-array-indexof/
 * Regular Expresion IndexOf for Arrays
 * This little addition to the Array prototype will iterate over array
 * and return the index of the first element which matches the provided
 * regular expresion.
 * Note: This will not match on objects.
 * @param  {RegEx}   rx The regular expression to test with. E.g. /-ba/gim
 * @return {Numeric} -1 means not found
 */
if (typeof Array.prototype.reIndexOf === 'undefined') {
    Array.prototype.reIndexOf = function (rx) {
        for (var i in this) {
            if (this[i].toString().match(rx)) {
                return i;
            }
        }
        return -1;
    };
}

// Polyfill. Url: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray
// Good way to test if a variable is an array. Used by forms.js
if (!Array.isArray) {
    Array.isArray = function(arg) {
        return Object.prototype.toString.call(arg) === '[object Array]';
    };
}