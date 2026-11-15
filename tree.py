def stairs(n):
    if n <= 1: return 1
    return stairs(n-1) + stairs(n-2)

def tree(n):
    if n == 0: return
    print(n, end=" ")
    tree(n-1)
    tree(n-1)

n = int(input("Enter stairs: "))
print("Ways:", stairs(n))

print("Call Tree:")
tree(3)