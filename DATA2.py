# input_helper.py

def get_numbers_from_user():
    """
    ฟังก์ชันรับตัวเลขจากผู้ใช้ทีละตัวและเก็บไว้ในลิสต์
    :return: ลิสต์ของตัวเลข
    """
    num_count = int(input("Please enter the number of values to be sorted: "))
    arr = []
    for i in range(num_count):
        num = int(input(f"Please enter number {i+1}: "))
        arr.append(num)
    return arr

def get_sort_order():
    """
    ฟังก์ชันรับคำสั่งจากผู้ใช้เพื่อเลือกวิธีการเรียงลำดับ
    :return: 'a' สำหรับน้อยไปมาก, 'd' สำหรับมากไปน้อย
    """
    order = input("Please choose the sorting order (Ascending: '1' / Descending: '2'): ").lower()
    return order
