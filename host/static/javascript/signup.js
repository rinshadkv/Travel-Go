$(document).ready(function(){
    $('#signup').validate({
        rules:{
            name:{
                minlength:4,
                maxlength:16
            },
            phone:{
               minlength:4
            },
            country:{

            },
            email:{
                email:true
            },
            username:{
                minlength:4,
                maxlength:20
            },
            password:{
                minlength:8,
                maxlength:16
            },
            c_password:{
                equalTo:'#password'

            },
            image:{
                
            }

        }
    })

})
