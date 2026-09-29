// ============================================
// 综合题3-1：照课程做一遍"用户列表渲染"案例
// ============================================
// 目标：浏览器打开 http://localhost:8080/user.html 能看到用户表格，
//       表格里的数据来自后端接口 http://localhost:8080/list 返回的 JSON。
//
// 完成以下操作（每一步都跑一遍再进下一步）：
// 1. 创建 SpringBoot 工程，勾选 Web 开发相关依赖与 lombok，
//    并在 pom 里补上 hutool 依赖（读文件要用它的工具类）
// 2. 把 user.txt 放进 src/main/resources/ 下；
//    把 user.html 和 js 目录放进 src/main/resources/static/ 下；
//    先用浏览器打开 http://localhost:8080/user.html 确认页面能显示（表格先空着）
// 3. 写实体类 com.itheima.pojo.User（6 个属性 + 三个 Lombok 注解）
// 4. 写请求处理类 com.itheima.controller.UserController：
//    读 user.txt → 每行解析成一个 User → 返回 List<User>
// 5. 启动工程，访问 /list，把响应状态码和响应头里的 Content-Type 抄到文件末尾
// 6. 刷新 user.html 看表格（应有 8 行数据）；
//    再做一次故障演练：把类上那个"返回数据"的注解换成一个"返回页面"的注解
//    （就是题目2-3 里 404 的那一个），重启后访问 /list，把状态码记下来
// ============================================

// 在下面写你的代码：

package com.itheima.controller;

public class UserController {

    // 在这里写"读文件 + 解析 + 返回"的代码

}

// 第 3 步的实体类（也可以写在这里）：
// package com.itheima.pojo;


// 第 5 步：/list 的实测结果
// 状态码：
// Content-Type：

// 第 6 步：故障演练后的状态码
// 状态码：
