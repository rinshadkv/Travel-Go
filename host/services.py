import random



def change_path(folder,filename):
    fname= filename+'.'+str(random.randint(111111,999999))
    return 'host-profile/{0}'.format(fname)

def hotel_path(folder,filename):
    fname= filename+'.'+str(random.randint(111111,999999))
    return 'hotel_image/{0}'.format(fname) 