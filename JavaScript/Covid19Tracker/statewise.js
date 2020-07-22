$(document).ready(function () {
    let coviddata = null
    if (!coviddata) {
        //window.location.href = "./index.html"
    }

    console.log("connected")
    const today = new Date()
    if (today.getDate() == 1 || today.getDate() == 21 || today.getDate() == 31)
        $("#headingfill").html("Statewise Data as of " + today.getDate() + "<sup>st</sup> " + monthNames[today.getMonth()])
    else if (today.getDate() == 2 || today.getDate() == 22)
        $("#headingfill").html("Statewise Data as of " + today.getDate() + "<sup>nd</sup> " + monthNames[today.getMonth()])
    else if (today.getDate() == 3 || today.getDate() == 23)
        $("#headingfill").html("Statewise Data as of " + today.getDate() + "<sup>rd</sup> " + monthNames[today.getMonth()])
    else
        $("#headingfill").html("Statewise Data as of " + today.getDate() + "<sup>th</sup> " + monthNames[today.getMonth()])

    let tdata = ""

    $.ajax({
        url: 'https://api.covid19india.org/data.json',
        dataType: 'JSON',
        success: function (data, status) {
            coviddata = data;
            for (let i = 1; i < coviddata["statewise"].length; i++) {
                percent=Number(((coviddata["statewise"][i].recovered/coviddata["statewise"][i].confirmed)*100).toFixed(2))
                percent=Number.isNaN(percent)?0:percent
                console.log(percent)
                tdata += "<tr> <td><a href='./statedetails.html?state=" + coviddata["statewise"][i].state + "'>" + coviddata["statewise"][i].state + "</a></td>                    <td>" + coviddata["statewise"][i].confirmed + "<sub>+" + coviddata["statewise"][i].deltaconfirmed + "</sub></td>                    <td>" + coviddata["statewise"][i].active + "</td>                    <td>" + coviddata["statewise"][i].recovered + "<sub>+" + coviddata["statewise"][i].deltarecovered + "</sub></td>                    <td>" + coviddata["statewise"][i].deaths + "<sub>+" + coviddata["statewise"][i].deltadeaths + "</sub></td><td>"+percent+" %</td></tr>"
            }
            $("#stateinsert").append(tdata)
            console.clear()

        }

    })


})

setTimeout(()=>{
    console.clear()
},5000)