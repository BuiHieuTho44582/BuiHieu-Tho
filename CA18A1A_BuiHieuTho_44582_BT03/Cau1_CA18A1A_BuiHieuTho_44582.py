"""
Đề thi 03
Date: 02/11/2021
Bui Hieu Tho
"""

def  Cau1 ():
    def  snt ( n ):
        "" "Kiểm tra tiền tố" ""
        f  =  Đúng
        cho  j  trong  phạm vi ( 2 , n ):
            nếu  n  %  j  ==  0 :
                f  =  Sai
                nghỉ
        trả lại  f
    def  in_snt ( a = 5 , b = 100 ):
        print ( "Prefix list:" )
        "" "Kiểm tra tiền tố trong khoảng từ a đến b" ""
        cho  tôi  trong  phạm vi ( a , b  +  1 ):
            nếu  snt ( i ):
                print ( i , end = "" )
    # Nguyên tố thực thi
    in_snt ( 5 , 100 )

if  __name__  ==  '__main__' :
    Cau1 ()
