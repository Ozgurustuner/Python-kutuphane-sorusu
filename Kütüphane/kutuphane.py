from kutuphane_islemleri import *

print('  Hoşgeldiniz  '.center(100,'-'))
print('1-Kitap Listesi Görüntüle')
print('2-Kitap Ödünç Al')
print('3-Kitap Ödünç Ver')
print('4-Kitap Bağışla')
print('5-Çıkış')


while True :
    
    while True :
        #kullanıcıdan geçerli input alınır
        try :
            secim = int(input('Yapmak istediğiniz işlem numarasını giriniz:'))
            if secim in [1,2,3,4,5] :
                break 
            else :
                print('1-5 arasında değer giriniz.')
        
        except :
            print('Lütfen geçerli değer giriniz.')
            
            
    if secim == 1 :
        kitap_sayisi = 1
        for kitap in kitaplar() :
            print(f' {kitap_sayisi}. Kitap Bilgileri '.center(100,'*'))
            for key,value in kitap.items() :
                print(f'{key} : {value}')
            kitap_sayisi += 1
                    
    elif secim == 2 :
        kitap_ismi = input('Ödünç vermek istediğiniz kitap ismini yazınız:')
        odunc_alma(kitap_ismi)
    
    elif secim == 3 :
        kitap_ismi = input('Ödünç vermek istediğiniz kitap ismini yazınız:')
        odunc_verme(kitap_ismi)
    
    elif secim == 4 :
        while True :
            try:
                deger_sayisi = int(input('Kaç değer girilecek:'))
                break 
            except :
                print('Lütfen sayı giriniz')
        
        dict = {}
        for i in range(deger_sayisi) :
            key = input('Key değeri giriniz:')
            value_tipi = input('str or int:')
            value = input('Value değeri giriniz:')
            if value_tipi == 'int' :
                dict[key] = int(value )
            else :
                dict[key] = value 
        
        kitap_bagisla(dict)
    
    elif secim == 5 :
        print('Uygulamadan çıktınız.')
        break 
               