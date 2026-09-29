// ==========================================================================
// 题目2-3：找错（这段 JDBC 代码有 5 处问题）
// ==========================================================================
// 库：web01，表：user（表结构与上面两题相同）
//
// 背景：
//   下面是同学交上来的代码（只贴了方法体，其余部分省略）。
//   编译能过，跑起来却连不上、也改不动数据。这段代码里一共有 5 处问题。
//
//     public void testUpdate() throws Exception {
//         Class.forName("com.mysql.jdbc.Driver");
//         String url = "jdbc:mysql://localhost:3306";
//         Connection connection = DriverManager.getConnection(url, "root", "123456");
//         Statement statement = connection.prepareStatement("update user set age = 25 where id = 1");
//         ResultSet rs = statement.executeQuery("update user set age = 25 where id = 1");
//         statement.close();
//     }
//
//   （连接信息里的密码换成你自己 MySQL 的密码再跑）
//
// 需求：
//   把 5 处问题一处不落地找出来，说明"哪里错、错了会发生什么"，
//   再写出改好的完整方法。
//
// 完成以下操作：
// 1. 逐行检查，把 5 处问题按"第几处 / 哪一行 / 错了什么 / 会怎样"记到下面
// 2. 写出改好的完整方法（放回下面的类里）
// 3. 把它跑一遍，确认控制台打印出影响行数
// 4. 收尾回答：这 5 处里，哪一处不会让程序报错、但会悄悄留下隐患？（说清隐患是什么）
// ==========================================================================

// 在下面写你的代码：

package com.itheima;

public class JdbcBrokenTest {

    // 在这里写改好的测试方法

}

// 第 1 步的记录（5 处问题）：
// 第 1 处：
//
// 第 2 处：
//
// 第 3 处：
//
// 第 4 处：
//
// 第 5 处：
//

// 第 3 步的记录（跑通后的控制台输出）：
//
//

// 第 4 步的回答（哪一处不报错、只留下隐患，隐患是什么）：
//
//
