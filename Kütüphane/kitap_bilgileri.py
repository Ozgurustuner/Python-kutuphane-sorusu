
#“Kitap Adı”,”Yazarı”,”Basım Yılı”,”Türü”
kitap_listesi = { '001' :
    {'Kitap Adi' : '1984',
    'Yazari' : 'Geaorge Orwell',
    'Basim Yili' : 2010,
    'Türü' : 'Roman'},
          '002' :{
    'Kitap Adi' : 'Dönüsüm',
    'Yazari' : 'Franz Kafka',
    'Basim Yili' : 2011,
    'Türü' : 'Hikaye' },
         '003' : {
    'Kitap Adi' : 'Acimak',
    'Yazari' : 'Resat Nuri',
    'Basim Yili' : 2000,
    'Türü' : 'Hikaye'},
          '004'  : {
    'Kitap Adi' : 'Tutunamayanlar',
    'Yazari' : 'Oguz Atay',
    'Basim Yili' : 2015,
    'Türü' : 'Hikaye'},
           '005' : {
    'Kitap Adi' : 'Simyaci',
    'Yazari' : 'Paulo Coelho',
    'Basim Yili' : 2005,
    'Türü' : 'Hikaye'}
        }

#print(list(kitap_listesi.values())) 

# yeni_liste=[]
# for key,value in kitap_listesi.items() :
#     yeni_liste.append(value)

kitap_listesi = [
    {'Kitap Adi' : '1984','Yazari' : 'Geaorge Orwell','Basim Yili' : 2010,'Türü' : 'Roman'} ,
    {'Kitap Adi' : 'Dönüsüm','Yazari' : 'Franz Kafka','Basim Yili' : 2011,'Türü' : 'Hikaye' },
    {'Kitap Adi' : 'Acimak','Yazari' : 'Resat Nuri','Basim Yili' : 2000,'Türü' : 'Hikaye'} ,
    {'Kitap Adi' : 'Tutunamayanlar','Yazari' : 'Oguz Atay','Basim Yili' : 2015,'Türü' : 'Hikaye'},
    {'Kitap Adi' : 'Simyaci','Yazari' : 'Paulo Coelho','Basim Yili' : 2005,'Türü' : 'Hikaye'}
]




def kitaplar() :
    return kitap_listesi 



    
