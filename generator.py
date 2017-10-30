import time

def consumer(name):
    print('%s 准备吃包子啦'%name)
    while True:
        baozi = yield
        print('包子%s来啦，被%s吃辣'%(baozi,name))

c= consumer('zd')
c.__next__()
b1 = '韭菜馅'
c.send(b1)
# c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('laozi lai la')
    for i in range(10):
        time.sleep(1)
        print('做了一个包子分成凉拌')
        c.send(i)
        c2.send(i)

producer('cc')
