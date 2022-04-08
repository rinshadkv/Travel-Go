$(document).ready(function(){
    $('#signupform').validate({
        rules:{
            email:{
                email:true
                
            },
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
