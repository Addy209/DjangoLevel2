function calculate(){
    console.log("Hello World")
    let jMass=document.getElementById("1").value
    let jWeight=document.getElementById("2").value
    let mMass=document.getElementById("3").value
    let mWeight=document.getElementById("4").value
    if(!jMass||!jWeight){
        alert('Fill John\'s Details First')
        document.getElementById("e1").innerHTML='Fill John\'s Details First'
        event.preventDefault()
        return 0
    }
    if(!mMass||!mWeight){
        alert('Fill Mark\'s Details First')
        document.getElementById("e2").innerHTML='Fill Mark\'s Details First'
        event.preventDefault()
        return 0
    }

    let jBMI=jMass/(jWeight*jWeight)
    let mBMI=mMass/(mWeight*mWeight)
    document.getElementById("fillj").innerHTML="<p><b>John\'s Weight:</b> "+jMass+" Kg</p><p><b>John\'s Height:</b> "+jWeight+" cm</p><p><b>John\'s BMI:</b> "+jBMI+"</p>"
    document.getElementById("fillm").innerHTML="<p><b>Mark\'s Weight:</b> "+mMass+" Kg</p><p><b>Mark\'s Height:</b> "+mWeight+" cm</p><p><b>Mark\'s BMI:</b> "+mBMI+"</p>"
    event.preventDefault()
}

function clearfield(){
    console.log("CF")
    let jMass=document.getElementById("1").value
    let jWeight=document.getElementById("2").value
    let mMass=document.getElementById("3").value
    let mWeight=document.getElementById("4").value
    if(mMass&&mWeight){
        document.getElementById("e2").innerHTML=''
        return 0
    } 
    if(jMass&&jWeight){
        
        document.getElementById("e1").innerHTML=''
        return 0
    }
    
}
calculate()
clearfield()