res = 'within Range' if 20 < 30 and 20 > 10 else 'outside Range'
print(res)

res = 'within Range' if 20 < 30 > 10 else 'outside Range'
print(res)

res = 'within Range' if 30>20> 10 else 'outside Range'
print(res)

res = 'within Range' if 10<20<30 else 'outside Range'
print(res)

res = 'within Range' if 30>20 and 20 > 10 else 'outside Range'
print(res)

res = 'within Range' if 10<20 and 20 < 30 else 'outside Range'
print(res)