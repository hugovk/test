// Replace all words with meows, preserving punctuation.
// Requires functions in common.js so include that first

// Based on meow.py
// https://github.com/hugovk/meow.py

function meow(word) {
    'use strict';
    // Meowify a word
    var meowed = "";
    var length = word.length;

    if (length === 1) {
        return capify("m", word);
    }

    if (length === 2) {
        return capify("me", word);
    }

    if (length === 3) {
        return capify("mew", word);
    }

    if (length === 4) {
        return capify("meow", word);
    }

    // Words longer than four will have:
    //  * first letter M
    //  * last letter W
    //  * middle with a random number of Es, then some Os

    // Number of EOs:
    var eeohsCount = length - 2; // accounting for the "m" and the "w"
    // Number of Es:
    var eesCount = getRandomInt(1, eeohsCount);
    // Number of Os:
    var ohsCount = eeohsCount - eesCount;

    var ees = new Array( eesCount + 1).join("e"); // got this trick here:
    var ohs = new Array( ohsCount + 1).join("o"); // http://stackoverflow.com/questions/1877475

    meowed = "m" + ees + ohs + "w";
    return capify(meowed, word);
}

function meowify(inputText) {
    'use strict';
    var outputText = "", line, lines = inputText.split('\n');

    for (line in lines) {
        outputText += find_words(lines[line], meow) + '\n';
    }
    return outputText;
}
