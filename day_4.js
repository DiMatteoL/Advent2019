// https://adventofcode.com/2019/day/4
const passwordLimits = { min: 307237, max: 769058 };

const passwordRange = Array.from(new Array(passwordLimits.max - passwordLimits.min + 1), (x,i) => String(i + passwordLimits.min));

const assertNoDecrease = numString => {
    const numArray = Array.from(numString, Number);
    return JSON.stringify(numArray) === JSON.stringify(numArray.sort())
};

const assertRepeat = numString => /^.*(.)\1.*$/.test(numString);

const assertRepeatThriceOrMore = numString => /^.*(.)\1\1.*$/.test(numString);

const thriceRepeatedNumber = numString => numString.match(/^.*(.)\1\1.*$/);

const assertRepeatTwice = numString => {
    if (assertRepeatThriceOrMore(numString)) {
        const newNumString = numString.replace(new RegExp(thriceRepeatedNumber(numString)[1], 'g'), '');
        return assertRepeatTwice(newNumString);
    } else if (assertRepeat(numString)) {
        return true;
    }
    return false;
};

const removeDecreases = range => range.filter(password => assertNoDecrease(password));

const removeUnrepeated = range => range.filter(password => assertRepeat(password));

const removeToManyRepeats = range => range.filter(password => assertRepeatTwice(password));

const answers = range => {
    const possiblePasswords = removeUnrepeated(removeDecreases(range));
    return {
        1: possiblePasswords.length,
        2: removeToManyRepeats(possiblePasswords).length,
    }
};

console.log(answers(passwordRange));