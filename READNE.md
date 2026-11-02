### 练习 1：BUU SQL COURSE 1
- **状态**：未解出（仅完成漏洞验证）
- **学到的知识**：
  - 这是一个基于 Vue.js 的前端站点，真实接口隐藏在 `content_detail.php`。
  - 通过 `id=1 AND 1=1` 与 `id=1 AND 1=2` 的对比，确认了 GET 参数存在数字型 SQL 注入。
  - 题解提示 Flag 隐藏在一个叫 virink 的用户密码哈希中。
- **下一步**：学习 SQLMap 工具的使用，或者手写 UNION 注入语句。