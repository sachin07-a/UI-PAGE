console.log("hi")

// CONDITIONALS

// if else -->only checks conditions (true/false,+,-,<,>,rest all operators)
// if else else-if
// -->for checking truthy and falsy values: console.log(!!value)

// if (true){
//     console.log("succeess")
// } else{
//     console.log("reject")
// }

let marks=90;

if(marks>=90){
    console.log("A grade");
} else if(marks>=75){
    console.log("B grade");
} else{
    console.log("c grade");
}

// SWITCH

//-->switch only checks the actual value

let markss=90;

switch(markss){
    case 90 :
        console.log("A");
        break;
    case 85:
        console.log("B");
        break;
    case 80:
        console.log("C");
        break;
    case 60:
        console.log("D");
        break;  
    default:
        console.log("you are failed");
}

console.log("after switch case");

//-->LOOPS

// a. entry-control
// b. exit-control

//1.for loop
   //SYNTAX-- for(start; end; change){}

   for(let i=0; i<50; i++){
    console.log("hlo")
   }

   for(let i=1; i<50; i++){
    console.log(i)
    console.log("hi")
   }

//2.while loop
 //SYNTAX--

 let i=1;
 while (i<50){
    console.log("hello");
    i++;
 }

//   let k=200;
//  while (k<30){
//     console.log("hello");
//     i++;      
//  }



//3.do while loop

