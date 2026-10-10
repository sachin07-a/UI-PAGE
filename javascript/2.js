// variables -var, let, const with scope understanding
// var,let,constant
// var can be redeclared and updated
// let can be updated but not redeclared


let a="rahul";
let b=90;

console.log(a);
console.log(b);

const c=100;
// c=200; // This will throw an error because 'c' is a constant and cannot be reassigned.

console.log(c);

a=90; // This is valid because 'a' was declared with 'let' and can be updated.
console.log(a);