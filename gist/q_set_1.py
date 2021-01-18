cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

# 1.จงเขียนคำสั่งเพื่อแสดงค่าของใน cafe_ao_udom_set ทั้งหมด
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

for cafe_ao_udom in cafe_ao_udom_set:
    print(cafe_ao_udom)

print(cafe_ao_udom_set)

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน cafe_ao_udom_set โดยเพิ่ม "Baannom" ลงไป
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

cafe_ao_udom_set.add("Baannom")
print("[2] cafe_ao_udom_set", cafe_ao_udom_set)

# 3.จงเขียนคำสั่งเพื่ออัพเดตค่าใน cafe_ao_udom_set โดยให้อัพเดต set ของ {"SaiNom's", "COFFEE DOE"} ในตัวแปร cafe_ao_udom_set
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

update_cafe_ao_udom_set = {"SaiNom's", "COFFEE DOE"}
cafe_ao_udom_set.update(update_cafe_ao_udom_set)
# cafe_ao_udom_set + update_cafe_ao_udom_set
print("[3] cafe_ao_udom_set", cafe_ao_udom_set)

# 4.จงเขียนคำสั่งเพื่อลบค่า "เพียวนม" ออกจากตัวแปร  cafe_ao_udom_set
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

cafe_ao_udom_set.remove("เพียวนม")
# cafe_ao_udom_set.discard("เพียวนม")
print("[4] cafe_ao_udom_set", cafe_ao_udom_set)


# 5.จงเขียนคำสั่งเพื่อสุ่มลบหนึ่งค่าในตัวแปร cafe_ao_udom_set
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

cafe_ao_udom_set.pop()
print("[5] cafe_ao_udom_set", cafe_ao_udom_set)


# 6.จงเขียนคำสั่งเพื่อเคลียค่าของ cafe_ao_udom_set ทั้งหมด
cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

cafe_ao_udom_set.clear()
print("[6] cafe_ao_udom_set", cafe_ao_udom_set)