$(document).ready(function () {
    let coviddata = null
    let odata = "<option value='-1'>---Select State---</option>"
    let urlState = ""
    let searchquery = false
    $.ajax({
        url: 'https://api.covid19india.org/v2/state_district_wise.json',
        dataType: 'JSON',
        success: function (data, status) {
            coviddata = data;
            coviddata.sort(compare)
            urlState = window.location.search
            if (urlState) {
                urlState = urlState.substr(1).split('=')[1].replace(/%20/g, " ").trim()
                searchquery = true
                console.log(urlState)
            }
            if (searchquery) {
                for (let i = 0; i < coviddata.length; i++) {
                    if (urlState === coviddata[i].state.trim()) {
                        odata += "<option value='" + i + "' selected>" + coviddata[i].state + "</option>"
                        continue
                    }
                    odata += "<option value=' " + i + "'>" + coviddata[i].state + "</option>"
                }
            } else {
                for (let i = 0; i < coviddata.length; i++) {
                    odata += "<option value='" + i + "'>" + coviddata[i].state + "</option>"
                }
                console.clear()
            }
            $("#states").append(odata)

            if (searchquery) {
                const index = parseInt($("#states").val())
                console.log(index)
                tdata = ""
                for (let i = 0; i < coviddata[index]['districtData'].length; i++) {
                    percent=Number(((coviddata[index]['districtData'][i].recovered/coviddata[index]['districtData'][i].confirmed)*100).toFixed(2))
                    percent=Number.isNaN(percent)?0:percent
                    
                    tdata += "<tr><td>" + coviddata[index]['districtData'][i].district + "</td><td>" + coviddata[index]['districtData'][i].confirmed + "<sub>+" + coviddata[index]['districtData'][i].delta.confirmed + "</sub></td><td>"+percent+" %</td></tr>"
                }
                $("#statedetailinsert").html("")
                $("#statedetailinsert").append(tdata)
                $("#showme").css('display', 'block')
                console.clear()
            }

        }

    })


    $("#getstatedata").on('click', function () {

        $("#overallerror").text("")
        const index = parseInt($("#states").val())
        console.log()
        if (index == "-1") {
            $("#overallerror").text("Please Select a State First!!")
            return
        }
        console.log()
        tdata = ""
        for (let i = 0; i < coviddata[index]['districtData'].length; i++) {
            percent=Number(((coviddata[index]['districtData'][i].recovered/coviddata[index]['districtData'][i].confirmed)*100).toFixed(2))
            percent=Number.isNaN(percent)?0:percent
                    
            tdata += "<tr><td>" + coviddata[index]['districtData'][i].district + "</td><td>" + coviddata[index]['districtData'][i].confirmed + "<sub>+" + coviddata[index]['districtData'][i].delta.confirmed + "</sub></td><td>"+percent+" %</td></tr>"
        }
        $("#statedetailinsert").html("")
        $("#statedetailinsert").append(tdata)
        $("#showme").css('display', 'block')
        setTimeout(()=>{
            console.clear()
        },2000)

    })




    function compare(a, b) {
        const stateA = a.state.toUpperCase();
        const stateB = b.state.toUpperCase();

        let comparison = 0;
        if (stateA > stateB) {
            comparison = 1;
        } else if (stateA < stateB) {
            comparison = -1;
        }
        return comparison;
    }

})

setTimeout(()=>{
    console.clear()
},5000)