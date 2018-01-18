soDuong = int(input("Moi ban nhap so duong zic zac:"))
soDiem = int(input("Moi ban nhap so diem tren moi duong:"))

done = False
while not done:
    for i in range(0,soDiem):
        for j in range(0, soDuong*(soDiem-1)+1):
            for k in range(1, soDuong+1):
                if k % 2 != 0:
                    if (j+i) == (soDiem -1)*k or (j-i) == (soDiem -1)*k:
                        print("*", end = "")
                        done = True
                        k = soDuong +1
                        break
            else:
                print(" ", end="")
                done = False
        print(" ")
        done = True

