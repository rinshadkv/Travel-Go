from django.shortcuts import redirect


# def user_login(fun):
#     def wrap(request,*args,**kwargs):
#         if request.session.has_key('user_id'):
#             return fun(request,*args,**kwargs)
#         else:
#             return redirect("login")    
#     return wrap        