jaehwan = list(input())
doctor = list(input())

jaehwan_count = 0
doctor_count = 0

for char in jaehwan:
    if (char == 'h'):
        break
    jaehwan_count += 1

for char in doctor:
    if (char == 'h'):
        break
    doctor_count += 1

if (jaehwan_count >= doctor_count):
    print('go')
else:
    print('no')