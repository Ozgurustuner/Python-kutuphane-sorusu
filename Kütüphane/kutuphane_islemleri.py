from kitap_bilgileri import *


odunc_alinanlar = []

'''
def odunc_alma(kitap_ismi) :
    for kitap in kitap_listesi :
        if kitap['Kitap Adi'] == kitap_ismi : 
            kitap_listesi.remove(kitap)
            print('Kitap Ödünç Alınmıştır.')
            print('  Kitap Bilgileri  '.center(100,'*'))
            for key,value in kitap.items() :
                print(f'{key} : {value}')
            continue
            

    print('Kitap Kütüphanede Bulunmuyor.')
'''


def odunc_alma(kitap_ismi) :
    kitap_var_mi = False
    for kitap in kitap_listesi :
        if kitap['Kitap Adi'] == kitap_ismi : 
            kitap_var_mi = True 
            kitap_listesi.remove(kitap)
            odunc_alinanlar.append(kitap)
            print('Kitap Ödünç Alınmıştır.')
            print('  Kitap Bilgileri  '.center(100,'*'))
            for key,value in kitap.items() :
                print(f'{key} : {value}')
            break
            
    if kitap_var_mi == False : #if not kitap_var_mi (ikisi de kullanılabilir)
        print('Kitap Kütüphanede Bulunmuyor.')


def odunc_verme(kitap_ismi:str)  : 
    '''
    Ödünç alınan kitabı geri vermeyi sağlar . 
    
    params
    :kitap ismi -> str 
    
    returns -> string
    '''
    if len(odunc_alinanlar) == 0 :
        print('Kitap ödünç alınmamıştır.')
    
    for kitap in odunc_alinanlar :
        if kitap_ismi != kitap['Kitap Adi'] :
            print('Kitap ödünç alınmamıştır.')
        
        else :
            #kitap_listesi.insert(0,kitap)
            kitap_listesi.append(kitap)
            odunc_alinanlar.remove(kitap)
            print('Kitap geri ödünç verilmiştir.')
    
    
# liste = []
# for x in kitap_listesi :
#     liste.append(x['Kitap Adi'])

def kitap_bagisla(dict) :
    if list(dict.keys()) == list(kitap_listesi[0].keys()) :
        if dict['Kitap Adi'] in [x['Kitap Adi'] for x in kitap_listesi ] :
            print('Kitap zaten kütüphanede mevcut.')
        else :
            kitap_listesi.append(dict) 
            print('Kitap bağışı alınmıştır.')
    else :
        print('Key değerlerini kontrol ediniz.')
    


# print(kitaplar())
# print('-'.center(99,'-'))
# odunc_alma('1984')
# print(kitaplar())
# print('-'.center(99,'-'))
# odunc_verme('1984')
# print('-'.center(99,'-'))
# print(kitaplar())
# print(kitaplar())
# print('-'.center(99,'-'))
# kitap_bagisla({'Kitap Adi' : 'Simyaci1','Yazari' : 'Paulo Coelho','Basim Yili' : 2005,'Türü' : 'Hikaye'})
# print(kitaplar())

