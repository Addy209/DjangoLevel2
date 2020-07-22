
console.log("connected")
let btn=document.querySelector('#b')
btn.setAttribute("class","btn btn-primary btn-lg")
btn.setAttribute("onMouseOver","clear()")
let squares=document.querySelectorAll("td")
console.log(2)

function clear(){
    console.log(1)
    for(let i=0;i<squares.length;i++){
        squares[i].textContent=""
    }
    document.querySelector('h1').remove()
}
console.log(3)
btn.addEventListener("click",clear)

function change(){
    if(this.textContent===''){
        this.textContent='X'
    }
    else if(this.textContent==='X'){
        this.textContent='0'
    }
    else{
        this.textContent=''
    }
}

for(let i=0; i<squares.length;i++){
    squares[i].addEventListener('click',change)
}