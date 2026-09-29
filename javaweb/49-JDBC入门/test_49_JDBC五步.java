// ==========================================================================
// 题目2-1：把 user 表里 id 为 1 的年龄改成 25
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
// 素材一（pom.xml 里要有的 MySQL 驱动依赖，Maven 会自动下载）：
//   <dependency>
//       <groupId>com.mysql</groupId>
//       <artifactId>mysql-connector-j</artifactId>
//       <version>8.0.33</version>
//   </dependency>
//
// 素材二（工程还要有 JUnit，用来单独运行这个方法）：
//   <dependency>
//       <groupId>org.junit.jupiter</groupId>
//       <artifactId>junit-jupiter</artifactId>
//       <version>5.9.3</version>
//       <scope>test</scope>
//   </dependency>
//
// 连接信息：主机 localhost、端口 3306、库 web01
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// 需求：
//   连上本机 MySQL 的 web01 库，把 user 表里 id 为 1 的那条记录的年龄改成 25，
//   并在控制台打印出"这次改了几行"。
//
// 完成以下操作：
// 1. 按"连接数据库要做的五个动作"的顺序写代码，每个动作上面写一行中文注释
// 2. 把这次执行的影响行数打印到控制台
// 3. 写成一个能在 IDE 里单独运行的方法（课程用的是 JUnit 测试方法，点方法左边的绿色箭头就能跑）
// 4. 运行一次，看控制台输出
// 5. 再跑一次对照实验：把条件里的 id 改成 100（表里没有这个 id），再运行一次，看输出
// 6. 在文件末尾回答两个问题
// ==========================================================================

// 在下面写你的代码：

package com.itheima;

public class JdbcUpdateTest {

    // 在这里写你的测试方法

}

// 第 4 步的记录（把控制台输出原样抄在下面）：
//
//

// 第 5 步的记录（id 改成 100 之后的输出）：
//
//

// 第 6 步的回答：
// ① 打印出来的这个数字代表什么？
//
//
// ② 换成 id = 100 之后这个数字会变成多少？会不会报错？为什么？
//
//
