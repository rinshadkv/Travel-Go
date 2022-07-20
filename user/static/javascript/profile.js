$(document).ready(function(){
    $('#update-password').validate({
        rules:{
           
            password:{
               minlength:8,
               maxlength:16

            },
            repassword:{
                equalTo:"#password"

            }
        }
    })

})
