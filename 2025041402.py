import sys
# f =open('C:/Users/user/Desktop/myfile.txt')
i = 0
try:
    f =open('myfile1.txt')
    s =f.readline()
    i =int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise
else:   # try - else 사용
    print(arg,'has',len(f.readlines()),'lines')
    f.close()

print(i)

for arg in sys.argv[1:]:
    try:
        f =open(arg,'r') #rwx
        print(f)
    except OSError:
        print('cannot open',arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()

try:
    raise Exception('spam','eggs') # anonymous class -> create object
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,                         
                         # but may be overridden in exception subclasses
    x,y =inst.args       # unpack args
    print('x =',x)
    print('y =',y)
    