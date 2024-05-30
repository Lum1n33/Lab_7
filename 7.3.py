def find_routes(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return find_routes(n-1, m) + find_routes(n, m-1)

n = int(input("Ввод кол-во по вертикали:"))
m = int(input("Ввод кол-во по горизонтали:"))
print("Маршрутов:", find_routes(n, m))