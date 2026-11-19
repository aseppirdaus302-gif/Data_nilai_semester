print("Grade Student")
print("==============")

nama = str(input("Enter name : "))
print("Enter test scores ")
nilai1 = float(input("Nilai semester 1: "))
nilai2 = float(input("Nilai semester 2: "))
nilai3 = float(input("Nilai semester 3: "))
nilai4 = float(input("Nilai semester 4: "))
nilai5 = float(input("Nilai semester 5: "))
jumlah = float(5)
print ("processing grades ......")
print ("Student Grade Report")
print ("=====================")
print ("Name :" + " " + nama)
print ("Test Scores :" + " " + str(nilai1) + ", " + str(nilai2) + ", " + str(nilai3) + ", " + str(nilai4) + ", " + str(nilai5))
average = (float(nilai1) + float(nilai2) + float(nilai3) + float(nilai4) + float(nilai5)) / float(jumlah)
print("Average scores :" + " " + str(average))
if average >= 90:
  print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 70:
    print("Letter Grade: C")
elif average >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: E")

if average > 70:
  print("Status: Lulus")
else:
  print("Status: Mohon maaf anda tidak lulus")

