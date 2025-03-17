from DATA1 import bubble_sort
from DATA2 import get_numbers_from_user, get_sort_order

def main():
    while True:  # ใช้ while True เพื่อให้วนซ้ำรับข้อมูลได้เรื่อย ๆ
        # รับตัวเลขจากผู้ใช้
        arr = get_numbers_from_user()

        # รับวิธีการเรียงลำดับจากผู้ใช้
        order = get_sort_order()

        # เรียงลำดับตามคำสั่ง
        if order == '1':
            print("Sorting from least to greatest:")
            bubble_sort(arr, ascending=True) # เรียกใช้ฟังก์ชัน bubble_sort() และเรียงลำดับจากน้อยไปมาก
        elif order == '2':
            print("Sorting in descending order:")
            bubble_sort(arr, ascending=False) # เรียกใช้ฟังก์ชัน bubble_sort() และเรียงลำดับจากมากไปน้อย
        else:
            print("Invalid command!!")
            continue  # ถ้าคำสั่งไม่ถูกต้อง ให้กลับไปรับค่าใหม่

        # แสดงผลลัพธ์
        print("Sorted result:", arr)

        # ถามว่าต้องการเรียงข้อมูลใหม่หรือไม่
        again = input("\nWant to reorder?? (print 'S' to leave, N to continue): ").strip().lower()
        if again == "s":
            print("The program has ended.")
            break  # ออกจากลูป while

if __name__ == "__main__":
    main()
