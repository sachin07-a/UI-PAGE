// OPERATORS

// a.arithmetic-operators-->+,-,/,*,**
// b.comparison-operators--> >=,<=,<,>,==,===,!=
// c.logical operators--> &&,||,!
// d.assignment-operators--> =,+=,-=,*=
// e.unary-operators-->
// f.ternary-operators--> ?


// A.ARITHMETIC-OPERATORS
console.log(10 + 20);
console.log(10 + "jaat");
// --> "+" is used for adding and concatenation 

console.log(20 - 20); //-->result:0
console.log(20 - "20");//--> result:0
console.log(20 - "hey"); //--> NaN(not a number)
console.log("30" - "10"); //-->result:20
//--> string of "20" is converted in number bcz js converts it into number
// -->only +-operation doess concatenation and "-" doesnt

console.log(10 * 20); //  -->result:200
console.log("10" * "20"); //  -->result:200
console.log("10" * "hi"); //  -->result:NaN

console.log(10 / 20); //-->result:0.5
console.log("10" / 20); //-->result:0.5
console.log("10" / "20"); //-->result:0.5

console.log(10 % 3); //-->result:1
console.log(20 % 3); //-->result:2

// B.COMPARISON-OPERATORS

console.log(4<3); //-->result: false
console.log(5==2); //-->result: false
console.log(6!=4); //-->result:true
console.log(4>"hey"); //-->result:false
console.log(" ">" "); //-->one value is truthy so output will be true

// falsy: null undefined false 0 -0 0n "" Nan document.all
// true: rest all is truthy values
    // when comparing, if any value is not comparable then it will find only one truthy values
    //and returns the true result

console.log(8=="8"); // true:"==" only compares values
console.log(8==="8"); // false:strick checking

// !-opposite's everything
console.log(!true); //-->false
console.log(9!=8); //-->true
console.log(8!=="8"); //-->true(datatype is not same)

// C.LOGICAL-OPERATORS

  // --control flow 
  // if(){}--if block always works in true condition 
  // else{only works if statement is false
  //  }

// &&--it always accepts all true values
// ||--it will check only one true condition

if (true){              //-->hey (if)
    console.log("hey");    
} else{
    console.log("bye..");
}

if (0){                 //-->bye (else)
    console.log("hey");    
} else{
    console.log("bye..");
}

if (1 && 2){            //-->hey (if)
    console.log("hey");    
} else{
    console.log("bye..");
}

if (0 && 2){            //-->bye(else)
    console.log("hey");    
} else{
    console.log("bye..");
}

let age=18;
let id =true;

if (age>=18 && id){
    console.log("access granted")
} else{
    console.log("access denied");
}

let Age=18;
let ids=false;

if (Age>=18 || ids){
    console.log("access granted")
} else{
    console.log("access denied");
}

if(!true) {
    console.log("ok fine")
} else{
    console.log("not fine")
}

// D.ASSIGNMENT-OPERATOR


// let sum=0
// sum = sum + 5 // or sum+=5;  //-->5
// console.log(sum);

// E.UNARY-OPERATOR

let sum=0
console.log(sum) // (0)
console.log(sum++)  //-->post increment (0)
console.log(++sum)  //-->pre increment (2)

// F.TERNARY-OPERATOR

true ?
    console.log("hello")
:
    console.log("bye");

false ?
console.log("hello")
:
console.log("bye");

0 ?
    console.log("hello") : console.log("bye");

