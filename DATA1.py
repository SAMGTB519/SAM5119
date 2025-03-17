# bubble_sort.py

def bubble_sort(arr, ascending=True):
    """
    ฟังก์ชันสำหรับเรียงลำดับตัวเลขในลิสต์ตามวิธี Bubble Sort
    พร้อมแสดงผลการเรียงลำดับทีละตัว
    :param arr: ลิสต์ของตัวเลขที่ต้องการเรียงลำดับ
    :param ascending: ถ้า True จะเรียงจากน้อยไปมาก ถ้า False จะเรียงจากมากไปน้อย
    """
    n = len(arr)

    # ทำการวนรอบการเปรียบเทียบ
    for i in range(n):
        print(f"Round {i + 1}: {arr}")  # แสดงสถานะของลิสต์ในแต่ละรอบ
        for j in range(0, n - i - 1):
            # เปรียบเทียบและสลับตามเงื่อนไขการเรียงลำดับ
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Swap {arr[j + 1]} with {arr[j]} -> {arr}")  # แสดงผลการสลับ
    print(f"Final result: {arr}")
