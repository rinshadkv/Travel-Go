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

            }
        }
    })

})
