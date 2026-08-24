dict={'name':'tarun',
      
      'age':17,
        'salary':60000
      }
print(dict)
dict['age']=16
print(dict)

dict['school']='dsp'

print(dict)

print("Length:",len(dict))

print("Equivalent String:%s"%str(dict))

dict2=dict.copy()

print(dict2)

print("value:%s"%dict.get('age'))

print("value:%s"%dict.items())

print("value:%s"%dict.keys())

print("value:%s"%dict.values())

print("value:%s"%dict.setdefault('age',None))

print(dict)

tar={'nm':'tarun','age':25}
tar2={'gender':'male'}

tar.update(tar2)

print(tar)