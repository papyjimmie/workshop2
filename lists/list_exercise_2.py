# จงแสดง "rat"
animal = ["cat", "bat", "rat", "dog"]
print(animal[2])

# จงแก้ไขข้อมูลจาก "cat" เป็น "hen"
animal = ["cat", "bat", "rat", "dog"]
animal[0] = "hen"
print(animal)

# จงเพิ่ม "hen" ไปยัง animal list
animal = ["cat", "bat", "rat", "dog"]
animal.append("hen")
print(animal)

# จงเพิ่ม "hen" ไประหว่าง "rat" กับ "ิิdog"
animal = ["cat", "bat", "rat", "dog"]
animal.insert(3, "hen")
print(animal)

# จงลบ "rat" จาก list
animal = ["cat", "bat", "rat", "dog"]
animal.remove("rat")
# del animal[2]
# animal.pop(2)
print(animal)

# จงแสดงตัวสุดท้ายของ animal
animal = ["cat", "bat", "rat", "dog"]
print(animal[-1])

# จงแสดงจำนวนของ animal
animal = ["cat", "bat", "rat", "dog"]
print(len(animal))