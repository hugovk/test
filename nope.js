// Replace all words with Nos, preserving punctuation.
// Requires functions in common.js so include that first

// Based on meow.py
// https://github.com/hugovk/meow.py

function nope(word) {
    'use strict';
    // Nopify a word
    var noped = "";
    var length = word.length;

    if (length === 1) {
        return capify("n", word);
    }

    if (length === 2) {
        return capify("no", word);
    }

    if (length === 3) {
        return capify("nuh", word);
    }

    if (length === 4) {
        return capify("nope", word);
    }

    // Words longer than four will have:
    //  * first letter N
    //  * last letter O
    //  * middle with a random number of Ns, then some Os

    // Number of NOs:
    var enohsCount = length - 2; // accounting for the "m" and the "w"
    // Number of Ns:
    var nsCount = getRandomInt(1, enohsCount);
    // Number of Os:
    var ohsCount = enohsCount - nsCount;

    var ens = new Array( nsCount + 1).join("n"); // got this trick here:
    var ohs = new Array( ohsCount + 1).join("o"); // http://stackoverflow.com/questions/1877475

    noped = "n" + ens + ohs + "o";
    return capify(noped, word);
}

function nopify(inputText) {
    'use strict';
    var outputText = "", line, lines = inputText.split('\n');

    for (line in lines) {
        outputText += find_words(lines[line], nope) + '\n';
    }
    return outputText;
}
