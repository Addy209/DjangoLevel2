let jg1=90,jg2=120,jg3=103
let mg1=120,mg2=90,mg3=103
let mag1=103,mag2=120,mag3=90

let javg=(jg1+jg2+jg3)/3
let mavg=(mg1+mg2+mg3)/3

//javg>mavg?console.log("Jhon is the winner. Avg Score is "+javg):javg==mavg?console.log("It's a tie. Score "+javg):console.log("Mike is the Winner. Score "+mavg)



let maavg=(mag1+mag2+mag3)/3

if(maavg>mavg&&maavg>javg){
    console.log("Mary is the Winner")
}
else if(mavg>maavg&&mavg>javg){
console.log("Mike is the Winner")
}
else if(javg>maavg&&javg>mavg){
console.log("John is the Winner")
}
else{
    console.log("There is  a tie")
}