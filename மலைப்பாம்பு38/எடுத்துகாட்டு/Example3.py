# program comment
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
BitAnd= a&b
BitOr=a|b
BitXor=a^b
BitInverse= ~a
LeftShift= a>>1
RightShift=a<<1

print ('Logical operations of', a, 'and', b)
print ('Bitwise And',BitAnd)
print ('Bitwise Or',BitOr)
print ('Bitwise Xor',BitXor)
print ('Bit inverse of a',BitInverse)
print ('Left Bit shift of a (ax2)',LeftShift)
print ('Right Bit shift of a(a/2)',RightShift)

