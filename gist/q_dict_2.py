car_info_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# 1.จงเขียนคำสั่งเพื่อแสดงค่า brand และ model ใน car_info_dict

print(car_info_dict["brand"])
print(car_info_dict["model"])

# print(car_info_dict.get("brand"))
# print(car_info_dict.get("model"))

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน car_info_dict โดยเพิ่ม key เป็น color และ value เป็น ["red", "white", "blue"]

car_info_dict["color"] = ["red", "white", "blue"]
# car_info_dict.update({"color": ["red", "white", "blue"]})

# 3.จงเขียนคำสั่งเพื่อลบค่าใน car_info_dict โดยลบ key "year"

car_info_dict.pop("weight")
# del car_info_dict["weight"]

# 4.จงเขียนคำสั่งเพื่อวนเพื่อแสดงค่า key และ value ใน car_info_dict

for key, value in car_info_dict.items():
    print(f"key: {key} value: {car_info_dict[key]}")

# for key in car_info_dict:
#     print(f"key: {key} value: {car_info_dict[key]}")