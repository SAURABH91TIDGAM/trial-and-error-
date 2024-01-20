'use strict';

let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true;
if (hasDriversLicense) console.log('I can drive :D');

// const interface = 'Audio';
// const private = 534;

function loggers() {
    console.log('My name is saurabh');
}

loggers();

function fruitProcessor(apples, oranges) {
    console.log(apples, oranges);
    const juice = `Juice with ${apples} apples, and ${oranges} oranges.`;
    return juice;

}

const mixedJuice = fruitProcessor(5, 3)
console.log(mixedJuice);
const Juice = fruitProcessor(3, 4)
console.log(Juice);

// Function declaration
function calcAge1(birthYeah)
{
    return 2024 - birthYeah;
}

const age1 = calcAge1(1991);
console.log(age1)


// Function expression
const calcage2 = function (birthYeah)
{
    return 2024 - birthYeah;
}

const age2 = calcAge1(1991);
console.log(age1, age2)

//Arrow function expression

const calcAge3 = birthYeah => 2037 - birthYeah;
const age3 = calcAge3(1991);
console.log(age3)

const yearsUntilRetirement = (birthYeah, firstName) => {
    const age = 2037 - birthYeah;
    const retirement = 65 - age;
//     return retirement;
    return `${firstName} retires in ${retirement} years`;
 }

console.log(yearsUntilRetirement(1991, 'Saurabh'));
console.log(yearsUntilRetirement(1991, 'pranjal'));