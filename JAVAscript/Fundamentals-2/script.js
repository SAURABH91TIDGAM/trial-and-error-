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
// const calcAge3 = birthYeah => 2037 - birthYeah;

// const age3 = calcAge3(1991);


// console.log(age3)

// const yearsUntilRetirement = (birthYeah, firstName) => {
//     const age = 2037 - birthYeah;
//     const retirement = 65 - age;
// //     return retirement;
//     return `${firstName} retires in ${retirement} years`;
//  }


// console.log(yearsUntilRetirement(1991, 'Saurabh'));




// console.log(yearsUntilRetirement(1991, 'pranjal'));


function cutFruitPieces(fruit)
{
    return fruit * 4;
}


function fruitProcessor(apples, oranges) {

    const applePieces = cutFruitPieces(apples);
    const orangePieces = cutFruitPieces(oranges);

    console.log(apples, oranges);
    const juice = `Juice with ${applePieces} piece of apple, and ${orangePieces} piece of oranges.`;
    return juice;
}

console.log(fruitProcessor(3, 5));

//Review Arrow function expression

const calcAge3 = birthYeah => 2037 - birthYeah;
const age3 = calcAge3(1991);
console.log(age3)

const yearsUntilRetirement = (birthYeah, firstName) => {
    const age = 2037 - birthYeah;
    const retirement = 65 - age;

    if (retirement > 0)
    {
        console.log(`${firstName} retires in ${retirement} years`);
        return retirement;
        
    } else
    {
        console.log(`${firstName} retires in ${retirement} years`);
        return -1;
        }

//  return retirement;
//     return `${firstName} retires in ${retirement} years`;

}

console.log(yearsUntilRetirement(1991, 'Saurabh'));



console.log(yearsUntilRetirement(1950, 'pranjal'));


/* Write your code below. Good luck! 🙂 */


const calcAverage = (s1,s2,s3) =>  (s1+s2+s3)/3;

let scoreDolphins = calcAverage(44,23,71);
let scoreKoalas = calcAverage(65,54,49);

console.log(scoreKoalas, scoreDolphins);

const checkWinner = function(avgKoalas, avgDolphins){
    if (avgDolphins >= 2 * avgKoalas){
        console.log(`Dolphins win 🏆 ( ${avgDolphins} vs. ${avgkoalas})`)
    }
    else if(avgKoalas >= 2 * avgDolphins)
    {
        console.log(`Koalas win 🏆 ( ${avgKoalas} vs. ${avgDolphins})`)
    }
    else
    {
        console.log('No team wins') 
    }
}

checkWinner(scoreKoalas, scoreDolphins);