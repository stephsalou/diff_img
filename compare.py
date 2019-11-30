# from diffimg import diff
from diffimg import diff


d = diff('img/test_b copie.jpg','img/test_0.jpg')
# ,d.fromhex(5)
print('type of d := ',type(d),'action of d := \n\r',dir(d),'\n\r valiue of d := ',d,'as integer :=',d.as_integer_ratio(),'conjugate : = ',d.conjugate(),'from hex := ','hex := ',d.hex(),'imag := ',d.imag,'interger := ',d.is_integer(),'real := ',d.real)
