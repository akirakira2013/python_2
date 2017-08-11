Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
list1 = [1, 2, 3]
>>> list1[0]
1
>>> list1[1]
2
>>> list1[2]
3
>>> list[3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list[3]
TypeError: 'type' object is not subscriptable
>>> list1[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list1[3]
IndexError: list index out of range
>>> crafter = ["NAME", "otoko", 15]
>>> print("namae:" + crafter[0])
namae:NAME
>>> print("seibetu:" + crafter[1])
seibetu:otoko
>>> print("nenrei:" + crafter[2])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("nenrei:" + crafter[2])
TypeError: must be str, not int
>>> print("nenrei:" + str(crafter[2]))
nenrei:15
>>> 
