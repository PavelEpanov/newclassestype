class C:
	pass

X = C()
print(type(X), type(C)) # Тип - экземпляр класса, из которого он создавался

# >>> <class '__main__.C'> <class 'type'>

print(isinstance(X, object)) # Классы всегда унаследованы от object
print(isinstance(C, object))
# True
# True

print(type("spam"), type(str))
# <class 'str'> <class 'type'>

print(isinstance("spam", object)) # То же смое и для встроенных типов(классов)
# True
print(isinstance(str, object))
#True

"""
В действительности сам type унаследован от object, a object от type, хотя они
представляют собой разные объекты — циклическое отношение, которое завершает
объектную модель и происходит из того факта, что типы являются классами, генери­
рующими классы:

"""

print(type(type))
#<class 'type'>
print(type(object)) #
#<class 'type'>
print(isinstance(type, object)) # Все классы являются производными от object, даже type
# True
print(isinstance(object, type)) # Типы создают классы, и type - это класс
# True

print(C.__bases__)
#(<class 'object'>,)
print(dir(C)) # Классы получают все стандартные методы
"""
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
"""
print(C().__repr__)
# <method-wrapper '__repr__' of C object at 0x7ffb95bdbd60>
