
    console.log("connected")
    function validate(){
    phone=$('#id_phoneNo').val()
    if(phone!=''){
        let pattern=/[7-9][0-9]{9}/
        if(pattern.test(phone)) {
            console.log("matched")
            return
        }
    else{
        alert("Phone no is not valid")
            event.preventDefault()
        }

    }
}