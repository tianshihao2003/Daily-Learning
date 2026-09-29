// ==========================================================================
// 题目2-1：查出 daqiao 的信息，封装成 User 对象打印
// ==========================================================================
// 库：web01，表：user
// 表结构（user）：
//   id       int unsigned 主键、自增   （ID）
//   username varchar(20)               （用户名）
//   password varchar(32)               （密码）
//   name     varchar(10)               （姓名）
//   age      tinyint unsigned          （年龄）
//
// 表里的数据（课程资料 01. JDBC-数据库表/user.txt 导入）：
//   1 daqiao/123456/大乔/22、2 xiaoqiao/123456/小乔/18、3 diaochan/123456/貂蝉/24、
//   4 lvbu/123456/吕布/28、5 zhaoyun/12345678/赵云/27
//
// 素材一（实体类 User，放在 com.itheima.pojo 包下）：
//   @Data
//   @AllArgsConstructor
//   @NoArgsConstructor
//   public class User {
//       private Integer id;
//       private String username;
//       private String password;
//       private String name;
//       private Integer age;
//   }
//   （三个注解来自 lombok；构造器参数顺序就是上面属性的顺序）
//
// 素材二（pom.xml 里要有的依赖：mysql-connector-j 8.0.33 驱动、
//        junit-jupiter 5.9.3（scope 为 test）、lombok 1.18.30）
//
// 连接信息：主机 localhost、端口 3306、库 web01
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// 需求：
//   连上 web01 库，把 user 表里用户名是 daqiao、密码是 123456 的那条记录查出来，
//   封装成一个对象，并打印到控制台（打印出来应该是一行 User(...) 的样子）。
//
// 完成以下操作：
// 1. 按顺序写：注册驱动、获取连接、获取SQL语句执行对象、执行查询、解析结果集、释放资源
//    （每个动作一行中文注释；SQL 里的条件可以先写死在字符串里）
// 2. 解析结果集时，每个字段都要"按列名"取值
// 3. 方法最后把用到的三个资源都关掉（顺序：结果集 → 执行对象 → 连接）
// 4. 运行，把控制台输出抄到下面
// 5. 回答问题
// ==========================================================================

// 在下面写你的代码：

package com.itheima;

public class JdbcQueryTest {

    // 在这里写你的测试方法

}

// 第 4 步的记录（控制台输出）：
//
//

// 第 5 步的回答：
// ① 取值为什么推荐按列名，而不是按列的编号？
//
//
// ② 这条 SQL 最终查到了几行？循环体里的代码执行了几次？如果没有查到任何数据会怎样？
//
//
