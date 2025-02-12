# Trong Python, list là một cấu trúc dữ liệu linh hoạt và mạnh mẽ
# List cho phép lưu trữ nhiều phần tử trong một biến duy nhất.

my_list = [1, 2, 3, 4, 5]

empty_list = [] # 1 list rỗng

# truy cập phần tử trong list
#print(my_list[-1]) # 5

# thay đổi giá trị phần tử
my_list[-1] = 99
# print(my_list) # [1 2 3 4 99] 

# cắt list [start:stop:step]
# print(my_list[0::2]); # [1 3 99]

# thêm phần tử vào list
# append(): thêm phần tử vào cuối list
# insert(): thêm phần tử vào vị trí cụ thể
# extend(): thêm nhiều phần tử từ 1 list khác
l = [1, 2, 3]
l.append(4) # [1 2 3 4]
l.insert(1, 99) # [1 99 2 3 4]
l.extend([5, 6, 7]) # [1 99 2 3 4 5 6 7]

# Xóa phần tử khỏi list
# remove(): xóa phần tử đầu tiên được chỉ định
# pop(): xóa phần tử tại vị trí cụ thể (mặc định là vị trí cuối) & trả về phần tử bị xóa
# del: xóa phần tử bằng chỉ số
# clear(): xóa toàn bộ phần tử trong list

l2 = [1, 2, 3, 4, 5]
l2.remove(3) # [1 2 4 5]
l2.pop() # [1 2 4]
del l2[0] # [2 4]
l2.clear() # [] - list rỗng

# các phương thức hữu ích khác
# len(): Trả về số lượng phần tử trong list.
# index(): Trả về chỉ số của phần tử đầu tiên có giá trị được chỉ định.
# count(): Đếm số lần xuất hiện của một giá trị trong list.
# sort(): Sắp xếp list (có thể sắp xếp ngược với reverse=True).
# reverse(): Đảo ngược thứ tự các phần tử trong list.
# copy(): Tạo một bản sao của list. (khác ô nhớ)

# List comprehension
# List comprehension là cách ngắn gọn để tạo list từ một biểu thức.

squares = [x * 3 for x in range(10)]
# print(squares) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# Kiểm tra phần tử có trong list
# Sử dụng từ khóa in để kiểm tra xem một phần tử có tồn tại trong list hay không.
l3 = [1, 2, 3]
# print(3 in l3) # True

# Nối list (merge list)
l4 = [1, 2]
l5 = [5, 6]
# print(l4 + l5) #[1 2 5 6]

# nested list
my_list_nested = [1, 2, [99, 100]]
# print(my_list_nested[2][1]) # 100

# Chuyển đổi list sang các cấu trúc khác
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)
my_set = set(my_list)  # {1, 2, 3}
# print(my_tuple, my_set) # (1, 2, 3) {1, 2, 3}

# List và bộ nhớ
# List là kiểu dữ liệu tham chiếu, nên khi gán một list cho một biến khác, cả hai biến sẽ tham chiếu đến cùng một đối tượng.
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
# print(list1)  # [99, 2, 3]

# Xử lý list với hàm map() và filter()
# map(): Áp dụng một hàm lên từng phần tử của list.
# filter(): Lọc các phần tử thỏa mãn điều kiện.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# List vs Tuple
# List có thể thay đổi (mutable), trong khi tuple là bất biến (immutable).
# List sử dụng [], tuple sử dụng ().
