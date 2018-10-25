def cr (ns,arg):
    if ns=='global':
        gl[arg]={}
def ad (ns,arg):
    if ns=='global':
        gl['var'].append(arg)
def ge (ns,arg):
    if ns=='global':
        if arg in gl['var']:
            return 'global'

n=int(input())
gl={}
gl['var']=[]
for i in range (n):
    cmd,ns,arg=input().split()
    if cmd=='add':
        ad(ns,arg)
    if cmd=='create':
        cr(ns,arg)
    if cmd=='get':
        print(ge(ns,arg))
#gl={'var':'a','foo':{'var':['a','b']},'doo':'c'}
#print (gl)