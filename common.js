// Based on meow.py
// https://github.com/hugovk/meow.py

function getRandomInt(min, max) { // taken from http://stackoverflow.com/questions/1527803
    'use strict';
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function is_word(thing) {
    'use strict';
    var reg = new RegExp("\\w+");
    var found = reg.test(thing);
    return found;
}

function find_words(line, converter_fun) {
    'use strict';
    // Nopify a line
    var thing, worded = [], reg = new RegExp("\\w+|[^\\w]", "g");

    // Break line into words and non-words (e.g. punctuation and space)
    var things = line.match(reg);
    for (thing in things) {
        if (is_word(things[thing])) {
            worded.push(converter_fun(things[thing]));
        } else {
            worded.push(things[thing]);
        }
    }
    return worded.join("");
}

function capify(word, reference) {
    'use strict';
    // Make sure word has the same capitalisation as reference
    var new_word = "";

    // First check whole word before char-by-char
    if (reference === reference.toLowerCase()) {
        return word.toLowerCase();
    }

    if (reference === reference.toUpperCase()) {
        return word.toUpperCase();
    }

    // Char-by-char checks
    var i = 0;
    for (i; i < reference.length; i += 1) {
        if (reference.charAt(i) === reference.charAt(i).toUpperCase()) {
            new_word += word.charAt(i).toUpperCase();
        } else {
            new_word += word.charAt(i);
        }
    }
    return new_word;
}
