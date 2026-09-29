// ============================================
// 题目2-1：写一个返回用户列表的接口
// ============================================
// 工程里已经准备好：
//   1. src/main/resources/user.txt —— 8 行用户数据，每行 6 段、用逗号分隔
//   2. com.itheima.pojo.User —— 实体类，6 个属性依次是：
//      Integer id、String username、String password、String name、
//      Integer age、java.time.LocalDateTime updateTime
//   3. pom 里已经有 web、lombok、hutool 三个依赖
//
// 完成以下操作：
// 1. 写一个请求处理类（放在 com.itheima.controller 包里，类名叫 UserController）
// 2. 让浏览器访问 http://localhost:8080/list 时，进入这个类里的查询方法
// 3. 方法里把 user.txt 读出来（从 classpath 读，不许写死磁盘绝对路径），按行拿到文本
// 4. 把每一行解析成一个 User 对象，收集成 List<User> 返回
// 5. 返回值到浏览器上必须是 JSON 数组，而不是一个页面名字
// ============================================

// 在下面写你的代码：

package com.itheima.controller;

public class UserController {

    // 在这里写查询方法

}
