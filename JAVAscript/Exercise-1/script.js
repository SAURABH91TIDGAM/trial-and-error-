let js = 'amazing';
if (js === 'amazing') alert('javascript is FUN!');


// 40 + 35 + 21 - 5;
// console.log(40 + 35 + 21 - 5);

let firstName = 'Matilda';
// let jonas_matilda = "JM";
// let $function = 27;

const birthyear = 1991
var job = "Programmer"
let year = 2023

// console.log(firstName);
// console.log(jonas_matilda);
// console.log($function);
// let javaScriptIsFun = true
// if (javaScriptIsFun)
// {
//     console.log(javaScriptIsFun);
//     console.log(typeof javaScriptIsFun);
//     console.log(typeof firstName);
//     console.log(typeof jonas_matilda);
//     console.log(typeof $function);
//     job = "Teacher"
//     console.log(job);
// }

// const jonas = "I'm " + firstName + " a " + (year - birthyear) + 'year old ' + job + '!';
// console.log(jonas);

// const jonasNew = `I'm  ${ firstName}, a ${year - birthyear} year old ${job}!`;
// console.log(jonasNew);

// console.log(`just a regular string`);

// console.log(Number(birthyear), birthyear);
// console.log(Number(birthyear) + 18);
// console.log(Number('jonas'));
// console.log(Number(typeof NaN));

// console.log(String(23), 23);

// console.log('I am ' + 32  + ' years old');
// console.log('23' - '10' - 3); // the result will be 10
// console.log('23' / '2'); // the result will be 11.5

// let n = '1' + 1; //11  this will not result in 2 it will concatinate the two and make it 11.
// n = n - 1;
// console.log(n);

// console.log(2 + 3 + 4 + '5');
// console.log('10'-'4'-'3'-2+'5');

// console.log(Boolean(0));
// console.log(Boolean(undefined));
// console.log(Boolean('jonas'));
// console.log(Boolean({}));
// console.log(Boolean(''));

// const money = 0;
// if (money)
// {
//     console.log("Do not spend it all!");
// }
// else
// {
//     console.log("You should get a job!");
// }

// let height;
// if (height)
// {
//     console.log("Yay! height is defined!");
// }
// else
// {
//     console.log("Height is UNDEFINED!");
// }


// const age = '18';
// if (age === 18)
// {
//     console.log("You just became an adult:D (strict)");
// }

// if (age == 18)
// {
//     console.log("You just became an adult:D (loose)");
// }

// const favourite = prompt("Whats your favourite ?")
// console.log(favourite);
// console.log(typeof favourite);

// if (favourite === 23) {
//     console.log("cool 23 is an amazing number")
// }
// else if (favourite === 7) {
//     console.log("cool 7 is an cool number")
// }
// else if (favourite === 9) {
//     console.log("cool 9 is an amazing number")
// }
// else {
//     console.log("Number is not 13 or 7 or 9")
// }


const day = 'friday';

switch (day)
{
    case 'monday': //day of the week === Monday
        console.log("Plan tghe course structure");
        console.log("Go to codeing meetup");
        break;
    case 'tuesday': //day of the week === Monday
        console.log("Prepare theory videos");
        break;
    case 'wednesday': //day of the week === Monday
        console.log("wednesday");
        console.log("Go to codeing meetup");
        break;
    case 'thursday':
    case 'friday':
        console.log("write code examples");
        break;
    case 'saturday':
    case 'sunday':    
        console.log("Enjoy the weekend :D");
        break;
    default:
        console.log("Not a valid day");
}

if (day === 'monday')
{
    console.log("plan course structure");
    console.log("Go to coding meet up");
} else if (day === 'tuesday')
{
    console.log("prepare theory structure")
} else if (day === 'wednesday' || day === 'thursday')
{
    console.log("prepare theory structure");
} else if (day === 'friday')
{
    console.log("Record videos");
} else if (day === 'saturday' || day === 'sunday')
{
    console.log("Enjoy the Weekend :D");
}
else {
    console.log('Not a valid  day');
}

const age = 13;
age >= 18 ? console.log('i like to drink wine 🍷'): console.log('i like to drink water 💧');

const drink = age>= 18 ? 'wine 🍷' : 'water 💧' ;
console.log(drink);

let drink2;
if(age >= 18){
    drink2 = 'wine 🍷';
}else{
    drink2= 'water💧'
}



