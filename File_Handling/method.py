#m1
file = open('file.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

#m2
with open('fil2.txt','w')as file:
    file.write('chai aur python')