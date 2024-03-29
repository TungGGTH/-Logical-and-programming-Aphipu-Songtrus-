#intro
print(" ~~~ ยินดีต้อนรับเข้าสู่โปรแกรมเปลี่ยนศักราชต่าง ๆ ครับ :D ~~~ ")
print("จัดทำโดย นาย อภิภู ส่งตรัส ชั้น ม.4/1 เลขที่ 5")

#input รับข้อมูลต่าง ๆ
import sys
try :
    era = int(input("\nกรุณาป้อนตัวเลขศักราชที่ต้องการคำนวณด้วยครับ (ไม่ต้องพิมพ์หน่วยศักราชนำตัวเลข) : "))
except ValueError :
    print ("*** เกิดข้อผิดพลาด โปรเเกรมไม่สามารถคำนวนต่อได้ (กรุณาพิมพ์เเค่เฉพาะตัวเลขนะครับผม) ***")
    sys.exit()
    
#process กระบวนการทำงานต่าง ๆ
print ("\nไม่ทราบว่าคุณต้องการคำนวณศักราชแบบไหนหรอครับ ?" , "(ให้พิมพ์เฉพาะตัวเลข)")
print ("* ตัวอย่างเช่น ผมต้องการใช้ตัวเลือกที่ 1 คือ จาก พ.ศ. --> ค.ศ. ให้เราพิมพ์เเค่ เลข 1 เท่านั้นครับผม *")

print ("\n1. จาก พ.ศ. --> ค.ศ.")
print ("2. จาก ค.ศ. --> พ.ศ.")
print ("3. จาก พ.ศ.  --> ม.ศ.")
print ("4. จาก ม.ศ. --> พ.ศ.")
print ("5. จาก พ.ศ. --> จ.ศ.")
print ("6. จาก จ.ศ. --> พ.ศ.")
print ("7. จาก พ.ศ. --> ร.ศ.")
print ("8. จาก ร.ศ. --> พ.ศ.")
print ("9. จาก พ.ศ. --> ฮ.ศ.")
print ("10. จาก ฮ.ค. --> พ.ศ.")

try :
    choice = int(input("\nกรุณาป้อนตัวเลือกที่ต้องการคำนวณ ครับ : "))
    if choice == 1:
        EraFinal = era - 543
        unit = (" 1. จาก พ.ศ. --> ค.ศ.")

    elif choice == 2:
        EraFinal = era + 543
        unit = ("2. จาก ค.ศ. --> พ.ศ.")

    elif choice == 3:
        EraFinal = era - 621
        unit = ("3. จาก พ.ศ.  --> ม.ศ.")
    
    elif choice == 4:
        EraFinal = era + 621
        unit = ("4. จาก ม.ศ. --> พ.ศ.")

    elif choice == 5:
        EraFinal = era - 1181
        unit = ("5. จาก พ.ศ. --> จ.ศ.")
    
    elif choice == 6:
        EraFinal = era + 1181
        unit = ("6. จาก จ.ศ. --> พ.ศ.")

    elif choice == 7:
        EraFinal = era - 2324
        unit = ("7. จาก พ.ศ. --> ร.ศ.")
    
    elif choice == 8:
        EraFinal = era + 2324
        unit = ("8. จาก ร.ศ. --> พ.ศ.")

    elif choice == 9:
        EraFinal = era - 1122
        unit = ("9. จาก พ.ศ. --> ฮ.ศ.")
    
    elif choice == 10:
        EraFinal = era + 1122
        unit = ("10. จาก ฮ.ค. --> พ.ศ.")
        
except ValueError :
    print ("*** เกิดข้อผิดพลาด โปรเเกรมไม่สามารถคำนวนต่อได้ (กรุณาพิมพ์เเค่เฉพาะตัวเลขนะครับผม) ***")
    sys.exit()

#output เเสดงผลลัพธ์ที่ได้
print("\nจากตัวเลขศักราชที่คุณพิมพ์ :",era,"จะได้ว่า",unit,"คำตอบที่ได้คือ",EraFinal,"ครับผม :D")
print("\n~~~ ขอขอบคุณสำหรับการใช้งานโปรเเกรมครับ :D ~~~")

#loading screen (เเบบวงกลม)
import turtle, random
turtle.hideturtle()

turtle.pensize(25)
turtle.colormode(255)
x = 0
while (x < 3) :
    x = x + 1
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.color((r, g, b))
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(50)
