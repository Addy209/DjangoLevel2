console.log("connected");
var userdata
var id = 0
$("#search").keyup(function () {
    var value = $('#search').val().trim();
    console.log(value);
    if (value) {
        // Create Ajax Call
        $.ajax({
            url: 'search/',
            data: {
                'search_food': value
            },
            dataType: 'json',
            success: function (data) {
                let response = JSON.parse(data.name)
                let ul = $('#display')
                let li = ""
                for (let i = 0; i < response.length; i++) {
                    li += "<a class='list-group-item'>" + response[i]['dishname'] + "</a>"
                    ul.html(li)
                    sessionStorage.setItem(response[i]['dishname'], JSON.stringify(response[i]))
                }
            }
        });
    } else {
        $('#display').html('')
    }
});
$(document).on('click', 'div#display > a', function () {
    $('#search').val($(this).text())
    $('#display').html('')
})

$(document).on('click', '#addtocart', function () {
    console.log('I am here')
    $('#switchOn').css('display', '')
    let food = $("#search").val()

    let data = sessionStorage.getItem(food)
    let foodDetails = JSON.parse(data)
    let quant = parseInt($('#quant').val())
    let quantPrice = parseFloat(quant * parseFloat(foodDetails['price']))

    $('table > tbody#insertHere').append('<tr><td id="cusine' + id + '">' + foodDetails['dishname'] + '</td><td class="other" id=' + id + '>                                <button class="btn btn-danger btn-sm" id="btn-dec" style="width: 20%"><b>-</b></button>                                <strong style="margin: 0 20px 0 20px">' + quant + '</strong>                                <button class="btn btn-success btn-sm" id="btn-inc" style="width: 20%"><b>+</b></button>                            </td> <td id="price' + (id++) + '">' + quantPrice +
        '</td></tr>')

    calculateTotal()
    $('#sales').prop('disabled', false)
    $('#clearcart').prop('disabled', false)

});

$(document).on('click', '#btn-inc', function () {
    let parent = $(this).parent().attr('id')
    let val = parseInt($('#' + parent + '>strong').text())
    let price = parseFloat($('#price' + parent).text())
    console.log(price)
    let perunitprice = price / val
    if (val === 10) {
        return
    } else {
        val += 1
        let newPrice = val * perunitprice
        $('#' + parent + '>strong').text(val)

        $('#price' + parent).text(newPrice)

        calculateTotal()

    }
})

$(document).on('click', '#btn-dec', function () {
    let parent = $(this).parent().attr('id')
    let val = parseInt($('#' + parent + '>strong').text())
    let price = parseFloat($('#price' + parent).text())
    console.log(price + " " + val)
    let perunitprice = price / val
    console.log(perunitprice)
    if (val === 1) {
        return
    } else {
        val -= 1
        let newPrice = val * perunitprice
        console.log(newPrice)
        $('#' + parent + '>strong').text(val)
        $('#price' + parent).text(newPrice)

        calculateTotal()
    }
})

function calculateTotal() {
    let total = 0
    for (let i = 0; i < id; i++) {
        total += parseFloat($('#price' + i).text())
    }
    $('#total').text(total)
}

$('#clearcart').click(function () {
    id = 0
    $('table > tbody#insertHere').html('')
    $('#total').text('')
    $('#sales').prop('disabled', true)
    $('#clearcart').prop('disabled', true)
})

$('#sales').click(function () {
    console.log('clicked')
    let token = $('input[name="csrfmiddlewaretoken"]').val()
    let order = ''
    for (let i = 0; i < id; i++) {
        if (i + 1 == id) {
            order += $('tr>td#cusine' + i).text()
        } else {
            order += $('tr>td#cusine' + i).text()
            if (i + 2 == id) {
                order += " & "
            } else {
                order += ", "
            }
        }
    }
    let amount = $('#total').text()
    console.log(amount)
    $.ajax({
        headers: {
            "X-CSRFToken": token
        },
        url: 'save/',
        type: 'POST',
        data: {
            'order': order,
            'amount': amount,
        },
        dataType: 'json',
        success: function (data) {
            if (data.resp === 'Ok') {
                alert('Order Placed Successfully!')
                $('#clearcart').trigger('click')

            }

        }

    })
})


$('#reportbtn').click(function () {
    sdate = $('#sdate').val()
    edate = $('#edate').val()
    let token = $('input[name="csrfmiddlewaretoken"]').val()
    console.log(sdate)
    console.log(edate)
    if (sdate && edate) {

        $.ajax({
            headers: {
                "X-CSRFToken": token
            },
            url: 'report/',
            type: 'post',
            data: {
                'sdate': sdate,
                'edate': edate
            },
            dataType: 'json',
            success: function (data) {
                if (data.resp = 'Ok') {
                    let table = $('table>tbody#recordinsert')
                    table.html('')
                    let total = 0
                    record = JSON.parse(data.record)
                    for (let i = 0; i < record.length; i++) {
                        total += record[i]['amount']
                        table.append('<tr><td class="other">' + record[i]['name'] + '</td><td class="order">' + record[i]['order'] + '</td><td class="other">' + record[i]['amount'] + '</td><td class="other">' + record[i]['date'] + '</td></tr>')
                    }
                    $('#earning').text(total)
                }
            }
        })
    } else {
        alert('Please Enter Start Date as Well As End Date')
    }
})

aditya = () => {
    console.log("Hello World")
}
