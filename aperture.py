#from aperture import gui
from multiprocessing import Process
#import os

def ruby(script):
    print "test"
    #os.execv("ruby.exe", script)

def call(fn, arg):
    fn(arg)

def main():
    p = Process(target=ruby, args=('app.rb'))
    p.start()
    p.join()
    #gui.show_gui()

if __name__ == '__main__':
    main()
