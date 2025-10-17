# lớp Cell------------------------
import math

class Cell:
    def __init__(self, position, parent=None, status='free', g=0, h=0, f=0):
        self.position = position   # tọa độ (x, y) - là 1 object Position
        self.parent = parent       # parent (object) trong đường đi
        self.status = status       # {'free', 'start', 'dirty', 'clean'}

        # các chi phí
        self.g = g   # chi phí từ ô bắt đầu đến ô hiện tại
        self.h = h   # chi phí ước lượng từ ô hiện tại đến đích
        self.f = f   # tổng chi phí f = g + h

        # chi phí làm sạch ( = 1, tăng thêm sau mỗi hành động)
        self.cleaning_cost = 1

    # hàm tính chi phí di chuyển (Move)= 1
    def move_cost(self):
        return 1

    # hàm update tổng cphí f
    def update_f(self):
        self.f = self.g + self.h

    # hàm ktra 2 ô có cùng vị trí ko
    def __eq__(self, other):
        return (self.position.x == other.position.x and self.position.y == other.position.y)

    # hàm biểu diễn object khi in ra mh
    def __repr__(self):
        return (f"Cell({self.position.x}, {self.position.y}, "
                f"status={self.status}, g={self.g}, h={self.h}, f={self.f}, "
                f"clean_cost={self.cleaning_cost})")

    # hàm tính estimated cost (kh.cách Euclid)
    def calculate_h(self, goal):
        self.h = math.sqrt((self.position.x - goal.position.x)**2 + (self.position.y - goal.position.y)**2)
        self.update_f()
    
    # hàm tăng cphí ô dirty (gọi mỗi khi robot move 1 bước)
    def increase_cleaning_cost(self):
        if self.status == 'dirty':
            self.cleaning_cost += 1

    # khi robot thực hiện hút bụi tại ô này, cộng cphí làm sạch vào g
    def apply_cleaning_cost(self):
        if self.status == 'dirty':
            self.g += self.cleaning_cost
            self.update_f()
            self.status = 'clean'
