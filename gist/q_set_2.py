pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

# 1.จงเขียนคำสั่งเพื่อแสดงค่าของใน pub_ao_udom_set ทั้งหมด\
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

for pub_ao_udom in pub_ao_udom_set:
    print(pub_ao_udom)

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน pub_ao_udom_set โดยเพิ่ม "Oldise" ลงไป
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

pub_ao_udom_set.add("Oldise")
print("[2] pub_ao_udom_set", pub_ao_udom_set)

# 3.จงเขียนคำสั่งเพื่ออัพเดตค่าใน pub_ao_udom_set โดยให้อัพเดต set ของ {"ผิงไฟ", "ตั้งหลัก"} ในตัวแปร pub_ao_udom_set
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

update_pub_ao_udom_set = {"ผิงไฟ", "ตั้งหลัก"}
pub_ao_udom_set.update(update_pub_ao_udom_set)
print("[3] pub_ao_udom_set", pub_ao_udom_set)

# 4.จงเขียนคำสั่งเพื่อลบค่า "SevenDays" ออกจากตัวแปร  pub_ao_udom_set
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

pub_ao_udom_set.remove("SevenDays")
# pub_ao_udom_set.discard("SevenDays")
print("[4] pub_ao_udom_set", pub_ao_udom_set)

# 5.จงเขียนคำสั่งเพื่อสุ่มลบหนึ่งค่าในตัวแปร pub_ao_udom_set
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

pub_ao_udom_set.pop()
print("[5] pub_ao_udom_set", pub_ao_udom_set)

# 6.จงเขียนคำสั่งเพื่อเคลียค่าของ pub_ao_udom_set ทั้งหมด
pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

pub_ao_udom_set.clear()
print("[6] cafe_ao_udom_set", pub_ao_udom_set)