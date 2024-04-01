print("===metodo format===")

variavel= "codemaster"


print("{:.<20} ".format(variavel))
print("{:.>20} ".format(variavel))
print("{:.^20} ".format(variavel))


print("===================")

print("{:<20}********************".format(variavel))
print("******************** {:>20} ".format(variavel))
print("********* {:^20} ***********".format(variavel))


print("===================")

saldo_1 = 3.1
saldo_2= 3.14
saldo_3= 3.142
saldo_4= 3.141592

print(" {:.1f} | {:.2f} | {:.3f} ".format(saldo_1,saldo_2,saldo_3,saldo_4))






