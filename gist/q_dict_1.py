profile_info_dict = {
    "first_name": "pipusana",
    "last_name": "petgumpoom",
    "age": 26,
    "weight": 74.2,
    "can_walk": True,
}


# 1.จงเขียนคำสั่งเพื่อแสดงค่า firstname และ lastname ใน profile_info_dict

print(profile_info_dict["first_name"])
print(profile_info_dict["last_name"])

# print(profile_info_dict.get("first_name"))
# print(profile_info_dict.get("last_name"))

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน profile_info_dict โดยเพิ่ม key เป็น email และ value เป็นอีเมลของตัวเอง

profile_info_dict["email"] = "pipusana.p@gmail.com"
# profile_info_dict.update({"email": "pipusana.p@gmail.com"})

# 3.จงเขียนคำสั่งเพื่อลบค่าใน profile_info_dict โดยลบ key "weight"

profile_info_dict.pop("weight")
# del profile_info_dict["weight"]

# 4.จงเขียนคำสั่งเพื่อวนเพื่อแสดงค่า key และ value พร้อมกันใน profile_info_dict
for key, value in profile_info_dict.items():
    print(f"key: {key} value: {profile_info_dict[key]}")

# for key in profile_info_dict:
#     print(f"key: {key} value: {profile_info_dict[key]}")
