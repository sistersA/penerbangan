import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Print semua operasi yang dapat dilakukan
print(s.system.listMethods())
print("----------------------------------------")
#Eksekusi
no = str(input("Nomor Penerbangan  = "))

print("Nomor Penerbangan=",no)

print()

print("asal : ",s.asal(no))
print("Tujuan : ",s.tujuan(no))
print("boarding : ",s.inboard(no))
print("Transit : ",s.insit(no))




# format board
board = "No Penerbangan : {}\nBoarding: {}".format(no,s.inboard(no))
transit = "No Penerbangan : {}\nBoarding: {}".format(no,s.insit(no))
# buka file untuk ditulis
file_board = open("boarding.txt", "w")
file_transit = open("trans.txt", "w")
# tulis board ke file
file_board.write(board)
file_transit.write(transit)
# tutup file
file_board.close()
file_transit.close()

#s.close()