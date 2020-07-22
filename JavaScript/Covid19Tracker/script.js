var coviddata = null;
const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
$(document).ready(function () {
    const today = new Date().toISOString().split("T")[0];
    const formattedToday = FormatDate(today)
    localStorage.setItem('formattedToday', formattedToday)
    console.log(formattedToday)
    end.min = "2020-01-30"
    end.max = today
    start.min = "2020-01-30"
    start.max = today
    let visible=false
    let row=[]
    let drawChart

    $.ajax({
        url: 'https://api.covid19india.org/data.json',
        dataType: 'JSON',
        success: function (data, status) {
            coviddata = data;
            localStorage.setItem('coviddata', JSON.stringify(coviddata))
            $("#cases").append(
                "<h1>Total Cases: " + coviddata["statewise"][0].confirmed + "<sub>+" + coviddata["statewise"][0].deltaconfirmed + "</sub></h1><h1>Active: " + coviddata["statewise"][0].active + "</h1><h1>Recovered: " + coviddata["statewise"][0].recovered + "<sub>+" + coviddata["statewise"][0].deltarecovered + "</sub></h1>            <h1>Deaths: " + coviddata["statewise"][0].deaths + "<sub>+" + coviddata["statewise"][0].deltadeaths + "</sub></h1>"

            )
            row=[]
            for(i=0; i<coviddata["cases_time_series"].length;i++){
                row.push([new Date(coviddata["cases_time_series"][i].date+"2020"),Number(coviddata["cases_time_series"][i].totalconfirmed),Number(coviddata["cases_time_series"][i].totaldeceased),Number(coviddata["cases_time_series"][i].totalrecovered)])
            }
            datewisegraph(row)

        }

    })
    
    

    $('#get').on('click', function () {
        const start = $('#start').val()
        const end = $('#end').val()
        console.log(start, end)
        oError = $("#overallerror")
        if (!start || !end) {
            oError.text("Both Date Fields are Mandatory!!")
            return
        }
        oError.text("")
        if (start < "2020-01-30" || start > today) {
            oError.text("From Date not correct!!")
            return

        }

        if (end < "2020-01-30" || end > today) {
            oError.text("To Date not correct!!")
            return
        }

        if (start > end) {
            oError.text("From Date can not be greater than To Date!!")
            return
        }
        if(start==end){
            oError.text("To Date and From Date can't be same")
            return  
        }
        const formattedStartDate = FormatDate(start)
        let formattedEndDate = FormatDate(end)
        const len = coviddata["cases_time_series"].length - 1
        if (formattedEndDate.trim() === formattedToday.trim()) {
            if (!(coviddata["cases_time_series"][len].date.trim() === formattedToday.trim())) {
                let yesterday = new Date()
                yesterday.setDate(new Date().getDate() - 1)

                formattedEndDate = FormatDate(yesterday.toISOString().split("T")[0])
            }
        }



        const startIndex = getIndex(formattedStartDate)
        const endIndex = getIndex(formattedEndDate)




        console.log(startIndex)
        console.log(endIndex)

        let tdata = null
        $("#insert").html("")
        $('#line_top_x').html("")
        row=[]
        for (let i = startIndex; i <= endIndex; i++) {
            tdata += "<tr><td>" + coviddata["cases_time_series"][i].date.trim() + "</td><td>" + coviddata["cases_time_series"][i].totalconfirmed + "<sub>+" + coviddata["cases_time_series"][i].dailyconfirmed + "</sub></td><td>" + coviddata["cases_time_series"][i].totalrecovered + "<sub>+" + coviddata["cases_time_series"][i].dailyrecovered + "</sub></td><td>" + coviddata["cases_time_series"][i].totaldeceased + "<sub>+" + coviddata["cases_time_series"][i].dailydeceased + "</sub></td></tr>"
            row.push([new Date(coviddata["cases_time_series"][i].date+"2020"),Number(coviddata["cases_time_series"][i].totalconfirmed),Number(coviddata["cases_time_series"][i].totaldeceased),Number(coviddata["cases_time_series"][i].totalrecovered)])
        }
        $("#insert").append(tdata)
        $("#showme").css("display", "block")
        datewisegraph(row)
        visible=true

    })

    const datewisegraph=(row)=>{
        google.charts.load('current', {'packages':['line']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      data = new google.visualization.DataTable();
      data.addColumn('date', 'Date');
      data.addColumn('number', 'Cases');
      data.addColumn('number', 'Death');
      data.addColumn('number', 'Recovered');

        console.log(row)
      data.addRows(row);

      var options = {
        chart: {
          title: `Covid-19 Cases in India from ${row[0][0].toDateString()} to ${row[row.length-1][0].toDateString()}  `
        },
        height:"500px",
        axes: {
          x: {
            0: {side: 'bottom'}
          }
        }
      };

      var chart = new google.charts.Line(document.getElementById('line_top_x'));

      chart.draw(data, google.charts.Line.convertOptions(options));
      console.clear()
    }
    }

    function FormatDate(date) {
        const month = monthNames[parseInt(date.substr(5, 2)) - 1]
        const day = date.substr(8, 2)
        return day + " " + month

    }

    function getIndex(date) {
        for (let i = 0; i < coviddata["cases_time_series"].length; i++) {
            if (coviddata["cases_time_series"][i].date.trim() === date.trim()) {
                return i
            }

        }
        return "-1"
    }

    
    $(window).resize(()=>{
        datewisegraph(row)
        
    })

})


$(window).on("beforeunload", function (e) {

});

setTimeout(()=>{
    console.clear()
},5000)