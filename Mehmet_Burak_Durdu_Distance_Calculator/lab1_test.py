import dbm
import pickle
def lab1_question1(input_file_name, output_file_name):
  """Girdi olarak verilen dosyaya satir numalari ekleyerek yeni bir
  dosya olarak kaydeder. Girdi dosyasinin oldugunu ve okuma modunca acilabildigini varsayar.
  
  Args:
  input_file_name: Girdi dosyasinin ismi
  output_file_name: Cikti dosyasinin ismi
  
  Returns:
  None
  
  Raises:
    Girdi dosyasi yoksa FileNotFoundError hatasi verecektir
  """
  counter = 1
  with open(input_file_name, "r") as file: # open file
    with open(output_file_name, "w") as file2:
      for line in file:
        num="{0:04}".format(counter) # Neden format ve neden 0.04 kullanildi!
        file2.write(num +" " +line)
        counter += 1

  if counter > 1:
    print("{} dosyasi basariyla olusturulmustur".format(output_file_name))



def lab1_question1_v2(input_file_name, output_file_name):
  """Girdi olarak verilen dosyaya satir numalari ekleyerek yeni bir
  dosya olarak kaydeder.
  
  Args:
  input_file_name: Girdi dosyasinin ismi
  output_file_name: Cikti dosyasinin ismi
  
  Returns:
  None
  
  Raises:
  None
  """
 

  try:
    file = open(input_file_name, 'r')
  except (FileNotFoundError) as e:
    # Eger FileNotFoundError alirsan o zaman kullaniciya uyari bas ve cik
    print("{} ile verilen dosya ismi bulunamadi {}".format(input_file_name, e))
    return 
    
  counter = 1
  with open(output_file_name, "w") as file2:
    for line in file:
      num="{0:04}".format(counter) # Neden format ve neden 0.04 kullanildi!
      file2.write(num +" " +line)
      counter += 1
    file.close() # Kapamayi unutmayin

  if counter > 1:
    print("{} dosyasi basariyla olusturulmustur".format(output_file_name))


def lab1_soru2(girdi_dosya_ismi, db_dosya_ismi):
  """Girdi olarak verilen girdi_dosya_ismi dosyasini okur ve db dosya ismi ile bir database olusturur.
    Icerisini doldurduktan sonra ayni dosyayi geri acip icerdekileri ekrana bastirilir.
  Args:
  girdi_dosya_ismi: Girdi dosyasinin ismi
  db_file_name: Girilen database dosya ismi
  Returns:
  None
  Raises:
  None
  """
  # Yazma
  db = dbm.open(db_dosya_ismi, 'c')

  try:
    file = open(girdi_dosya_ismi, 'r')
  except (FileNotFoundError) as e:
    # Eger FileNotFoundError alirsan o zaman kullaniciya uyari bas ve cik
    print("{} ile verilen dosya ismi bulunamadi {}".format(girdi_dosya_ismi, e))
    return 

  counter = 1
  for line in file:
      num="{0:04}".format(counter) # Neden format ve neden 0.04 kullanildi!
      db[pickle.dumps(num)] = line
      counter += 1

  file.close() # Artik girdi dosyasini kapayabiliriz


  for key in db.keys():
    val = db[key]
    # deger ve anahtar icin pickle load dene, olmuyorsa ayni degeri al
    try:
      skey = pickle.loads(key)
    except (TypeError, pickle.UnpicklingError):
      skey = key
    
    try:
      sval = pickle.loads(val)
    except (TypeError, pickle.UnpicklingError):
        sval = val
    print("DB dosyasindan okunan key: {}, value: {}".format(skey, sval))



