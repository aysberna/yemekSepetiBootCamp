import csv, json

class FileTool:
    def __init__(self, path, fields):
        self.path = path
        self.fields = fields
        # Dosyamızı oluşturalım.
        with open(self.path, 'w', newline='') as outcsv:
            self.headers = self.fields.split(',')
            writer = csv.writer(outcsv)
            writer.writerow(self.headers)

    def menu(self):
        '''
        İşlem menüsü    
        '''
        def search(self):
            '''
            Girilen metni dosyada arar, bulunduğu satırı yazdırır.
            '''
            text = input("Aramak istediğiniz metni yazın:")
            with open(self.path) as fp:
                for num, line in enumerate(fp, 1):
                    if text in line:
                        print ('Metnin bulunduğu satır:', num)
                    else:
                        print ('Metin bulunamadı.')
        
        def add(self):
            '''
            Girilen metni dosyanın sonuna ekler.
            '''
            text = input("Eklemek istediğiniz metni yazın:") # Örn: Berna,Aksoy,29
            fp = open(self.path, 'a')
            fp.write(text)

        def delete(self):
            '''
            Girilen metnin olduğu satırı siler.
            '''
            text = input("Silmek istediğiniz satır metnini yazın:") # Örn: Berna,Aksoy,29
            with open(self.path, "r") as fp:
                lines = fp.readlines()
            with open(self.path, "w") as fp:
                for line in lines:
                    if line.strip("\n") != text:
                        fp.write(line)

        def update(self):
            '''
            Girilen satırı girilen metin ile günceller.
            '''
            text = input("Güncellemek istediğiniz metni yazın:")
            newtext = input("Metni yazın:")
            replacement = ""
            with open(self.path, "r") as fp:        
                for line in fp:
                    line = line.strip()
                    changes = line.replace(text, newtext)
                    replacement = replacement + changes + "\n"
            fp.close()
            # Yeni halini yazalım
            with open(self.path, "w") as f:
                f.write('\n')
                f.write(replacement)
        def csvToJson(csvfile):
            '''
            Csv dosyanının içeriğini oluşturduğu json dosyasına yazar.
            '''
            data = {} # fields girilmediği durumda kullanılacak
            with open(csvfile) as f:
                # fields varsa
                if len(self.headers) > 1:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                else:
                    reader = csv.reader(f)
                    i = 1
                    for line in reader:
                        data[i] = line
                        i += 1
            if len(self.headers) > 1:
                with open('output.json', 'w') as o:
                    json.dump(rows, o)
            else:
                with open('output_without_headers.json', 'w') as f:
                    f.write(json.dumps(data))

        def mergeFiles(csvfile):
            '''
            Girilen dosyayı ilk oluşturulan dosya ile birleştirir.
            '''
            with open(csvfile, 'r') as f1:
                original = f1.read()

            with open(self.path, 'a') as f2:
                f2.write('\n')
                f2.write(original)
           
        def getHeaders(jsonfile):
            '''
            Header bilgisini yazdırır.
            '''
            jsonfile = open(jsonfile, 'r')
            print('Başlıklar: ', jsonfile.readlines(1))

        print("1'den 8'e kadar seçim yapınız.\nMenü: ")
        print("1. Arama\n2. Ekleme\n3. Silme\n4. Güncelleme\n5. Dosyaları birleştirme\n6. Csv'den Json'a çevirme\n7. Başlıkları alma\n8. Ana menü")
        choice = '0'
        while True:
            choice = input ("Seçiminiz: ")
            if choice == "1":
                search(self)
            elif choice == "2":
                add(self)
            elif choice == "3":
                delete(self)
            elif choice == "4":
                update(self)
            elif choice == "5":
                path = input("Yeni dosya adını girin: ")
                mergeFiles(path)
            elif choice == "6":
                path = input("Dosya adını girin: ")
                csvToJson(path)
            elif choice == "7":
                path = input("Dosya adını girin: ")
                getHeaders(path)
            elif choice == "8":
                self.menu()
            else:
                print("Hatalı seçim!")


fileName = input('Dosya adı girin:') # Örn: data.csv
fields  = input('Başlıkları girin:') # Örn: Ad,Soyad,Yas

FileTool(fileName, fields).menu()
