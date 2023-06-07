

# 判断是否为素数
def primeNum(num):
    if num == 1 or num == 0:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

# 判断两个数是否互质
def coprime(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b == 1

# 根据给定的指数和模数执行幂运算并返回结果
def candp(b, p, k):
    if p == 1:
        return b % k
    if p == 2:
        return (b * b) % k
    if p % 2 == 0:
        sum = candp(b, p // 2, k)
        return (sum * sum) % k
    if p % 2 == 1:
        sun = candp(b, p // 2, k)
        return (sun * sun * b) % k

# 生成密钥
def key():
    p = int(input("请输入素数 p: "))
    q = int(input("请输入素数 q: "))
    if not primeNum(p) or not primeNum(q):
        print("输入的 p 或 q 不是素数")
        return

    n = p * q

    # t 为 n 的欧拉函数
    t = (p - 1) * (q - 1)

    e = int(input("请输入密钥 e: "))
    d = 1
    # 求 e 的乘法逆
    while (e * d) % t != 1:
        d += 1

    print(f"n = p * q = {n}")
    print(f"t = (p - 1) * (q - 1) = {t}")
    print(f"公钥 (e, n) 为: ({e}, {n})")
    print(f"私钥 (d, n) 为: ({d}, {n})")

# 加密
def encryption():
    e = int(input("请输入公钥 e: "))
    n = int(input("请输入公钥 n: "))
    x = int(input(f"请输入明文 (明文需小于 {n}): "))
    if x >= n:
        print("输入数据过大！")
        return

    y = candp(x, e, n)
    print(f"密文为: {y}")

# 解密
def decode():
    d = int(input("请输入私钥 d: "))
    n = int(input("请输入私钥 n: "))
    y = int(input("请输入密文: "))

    x = candp(y, d, n)
    print(f"明文为: {x}")

def menu():
    print("------------------------------------------")
    print("*****          1.生成密钥            *****")
    print("*****          2.加密                *****")
    print("*****          3.解密                *****")
    print("------------------------------------------")

def RSA():
    while True:
        menu()
        i = int(input("请输入选项: "))
        if i == 1:
            key()
        elif i == 2:
            encryption()
        elif i == 3:
            decode()
        elif i == 4:
            break
        else:
            print("输入错误，请重新输入")

def menu1():
    print("******************************************")
    print("******************************************")
    print("******     欢迎来到RSA加密测试系统   *******")
    print("******************************************")
    print("******************************************")

def main():
    menu1()
    RSA()

main()
