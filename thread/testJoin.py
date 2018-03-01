import threading

def test():
    for i in range(1000000000):
        count = i
    print('%s %s done' % (threading.current_thread().name, count))


t1 = threading.Thread(target=test, name='test() thread')


#设置为守护进程
t1.setDaemon(True)
t1.start()
#t1.join()
print('main done')

