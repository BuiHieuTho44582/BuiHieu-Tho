"""
Đề thi 02
Date: 01/11/2021
Bui Hieu Tho

"""
def Cau1():
    
    Chuoinhiphan = input("Nhap so nhi phan vao day: ")
    Sothapphan = 0
    Somu = len(Chuoinhiphan) - 1
    for i in Chuoinhiphan:
     Sothapphan = Sothapphan + int(i) * 2 ** Somu
     Somu = Somu - 1
    print("So thap phan la: ", Sothapphan)

if __name__ == '__main__':
    Cau1()