
function pay() {
  ammount = 999;
  $.ajax({
    url: '/packageselect',
    type: 'POST',
    data: {
      totalprice: ammount * 100,
    },
    success: function (response) {
      console.log("payment_id = " + response.id);
      var options = {
        "key": "rzp_test_jSJtKTJ5JPeABv", // Enter the Key ID generated from the Dashboard
        "amount": response.ammount, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
        "currency": "INR",
        "name": "For rent",
        "order_id": response.id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
        "handler": function (response) {
          console.log(response.razorpay_payment_id);
          console.log(response.razorpay_order_id);
          console.log(response.razorpay_signature)
          updatePayment()
        },
        "theme": {
          "color": "#3399cc"
        }
      };
      var rzp1 = new Razorpay(options);
      rzp1.on('payment.failed', function (response) {
        alert(response.error.code);
        alert(response.error.description);
        alert(response.error.source);
        alert(response.error.step);
        alert(response.error.reason);
        // alert(response.error.metadata.order_id);
        alert(response.error.metadata.payment_id);
      });
      rzp1.open();
    }
  })
}
function updatePayment() {
  $.ajax({
    url: '/pack',
    type: 'GET',
    success: function (response) {
      alert(" Payment successfull")
      window.location.href = '/selectbasic'

    }


  })
}
$(document).ready(function () {
  $("#check_in").change(function () {

    $.ajax({
      url: "/check_avilable/",
      type: "GET",
      data: {
        check_in: $("#check_in").val(),
        room_id: $("#room_id").val()
      },
      success: function (response) {

        if (response.isAvailable == true) {
          alert("room is already booked")
          $("#submit_btn").attr({ "disabled": true })
          $("#check_in").css({ "border-color": "red" })


        }
        else {
          $("#check_in").css({ "border-color": "green" })
          $("#details_div").attr({ "hidden": false })
          $("#submit_btn").attr({ "disabled": false })

        }


      }

    })

  })
  // $("#check_out").change(function () {

  //   var check_in = $("#check_in").val()
  //   var check_out = $("#check_out").val()
  //   var diff = (check_out - check_in)
  //   var day = (diff)
  //   console.log(diff)

  // })
  $(function () {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if (month < 10)
      month = '0' + month.toString();
    if (day < 10)
      day = '0' + day.toString();

    var maxDate = year + '-' + month + '-' + day;

    // or instead:
    // var maxDate = dtToday.toISOString().substr(0, 10);


    $('#check_in').attr('min', maxDate);
  });
  $(function () {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if (month < 10)
      month = '0' + month.toString();
    if (day < 10)
      day = '0' + day.toString();

    var maxDate = year + '-' + month + '-' + day;

    // or instead:
    // var maxDate = dtToday.toISOString().substr(0, 10);


    $('#check_out').attr('min', maxDate);
  });
  $("#check_out").change(function () {
    var check_in = $('#check_in').val()
    var check_out = $('#check_out').val()
    if (check_in == check_out) {
      alert("guest must be stay atleast one night")
      $("#check_out").css({ "border-color": "red" })




    }




  })



  $("#continue_btn").click(function () {
   

    $("#date").attr({ "hidden": true })
    $("#book-summery").attr({ "hidden": false })
    $("#s_check_in").html($("#check_in").val(),)
    $("#s_check_out").html($("#check_out").val(),)
    var email=$("#email").val()
    var username= $("#username").val()
    var start = $("#check_in").val()
    var end = $("#check_out").val()

    var startDate = Date.parse(start);
    var endDate = Date.parse(end);


    var diff = new Date(endDate - startDate);

    var days = diff / 1000 / 60 / 60 / 24
    $("#totel_nights").html(days)
    var nights = days
    var price = $("#price").html()
    $("#totel_price").html(price * nights)
    $("#final_amount").html(price * nights)
    $("#s_email").html(email),
    $("#s_username").html(username),
    $("#s_user_id").html(user_id),
    $("#s_room_id").html(room_id),
    








    $.ajax({
      type: "POST",
      url: "/book_now/",
      data: {

        check_in: $("#check_in").val(),
        check_out: $("#check_out").val(),
        email: $("#email").val(),
        username: $("#username").val(),
        user_id: $("#user_id").val(),
        room_id: $("#room_id").val(),
        
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),






      },
      success: function (pay_hotel) {
        // if (response.msg == true) {
        //  pay_hotel(check_in,check_out,email,username,user_id,room_id,csrfmiddlewaretoken)
        
          
        // }


      }
    })

  })
 

function pay_hotel(check_in,_csrfmiddlewaretoken){
  $("#pay_at_hotel").click(function(){

 
   
      // var payment_mode = "pay at hotel"
      // var payment_status = "pending"
      console.log(check_in)


    $.ajax({
      url: "/payment_at_hotel/",
      type: "POST",
      data: {
        check_in: check_in,
        // check_out: $("#s_check_out").val(),
        // email: $("#s_email").val(),
        // username: $("#s_username").html(),
        // price: $("#totel-price").val(),
        // user_id:$("#s_user_id").val(),
        // room_id:$("#s_room_id").val(),
        // payment_mode: payment_mode,
        // payment_status: payment_status,
        csrfmiddlewaretoken: _csrfmiddlewaretoken
      },
      success: function (response) {
        if (response.message == true) {
          alert("hiii")
        }
      }




    })
  
})}

  function pay_online(){
    var payment_mode = "pay online"
      var payment_status = "completed"


    $.ajax({
      url: "/payment_online/",
      type: "POST",
      data: {
        price: $("#final_amount").val(),
        payment_mode: payment_mode,
        payment_status: payment_status,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (response) {
        if (response.message == true) {
          alert("hiii")
        }
      }




    })
  }

  
 




  

// $("#pay-now").click(function(){
//   amount= $("#final_amount").val(),
//   $.ajax({
//     url:"/online_payment/",
//     type:"POST",
//     data:{
//       final_amount:amount*100
//     }





//   })

 })



