class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class ListBag:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # trả về số lượng phần tử
    def __len__(self):
        return self.size
    
    #thêm 1 phần tử vào bag
    def add(self, item):
        newNode = Node(item)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
    # duyệt phần tử
    def duyet(self):
        if self.size < 1:
            print("Phần tử rỗng ông êy !")
        else:
            curNode = self.head
            while curNode is not None:
                print(curNode.data, end= ' ')
                curNode = curNode.next
    #tìm kiếm xem 1 phần tử có trong list hay không
    def check(self, target):
        curNode = self.head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None
    # xóa bỏ item, trả về giá trị của item xóa 
    def remove(self, item):
        prevNode = None
        curNode = self.head
        while curNode is not None and curNode.data != item:
            prevNode = curNode
            curNode = curNode.next
        assert curNode is not None, "Lỗi rồi em yêu ơi !"
        if curNode is self.head:
            self.head = curNode.next
        else:
            prevNode.next = curNode.next
        self.size -= 1
        return curNode.data
    
# checkkk lewlew
a = ListBag()
n = int(input("Nhập số lượng phần tử cần thêmm : "))
for i in range(n):
    x = int(input(f"Nhập số cần thêm thứ {i} : "))
    a.add(x)
a.duyet()
print()
print(f"Số lượng phần tử trong list là : {a.__len__()}")
search = int(input("Kiểm tra phần tử : "))
if a.check(search):
    print(f"Phần tử {search} của em có trong list đó bé.")
else:
    print(f"Dĩ nhiên con chóa {search} không có trong list gòi bé iuuuu !")
remove = int(input("Nhập số cần xóa đi con chóa: "))
print(f"Đã xóa số {a.remove(remove)} cho con chóa thành công gòi, đíu tin nhìn bên dưới xem: ")
print(f"Số lượng phần tử trong list còn lại là : {a.__len__()}")
a.duyet()