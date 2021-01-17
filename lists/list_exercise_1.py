# จงแสดง "banana"
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# จงแก้ไขข้อมูลจาก "apple" เป็น "kiwi"
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# จงเพิ่ม "kiwi" ไปยัง fruits list
fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")
# fruits.insert(0, "lemon")

# จงเพิ่ม "lemon" ไประหว่าง "apple" กับ "ิิbananna"
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# จงลบ "cherry" จาก list
fruits = ["apple", "banana", "cherry"]
fruits.remove("cherry")

# จงแสดงตัวสุดท้ายของ fruits
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# จงแสดงจำนวนของ fruits
fruits = ["apple", "banana", "cherry"]
print(len(fruits))