// ==========================================================================
// 综合题：从零跑通第一个 JDBC 程序（照课程做一遍）
// ==========================================================================
// 目标：把"准备工作两件 + 代码实现"从头到尾走一遍，每一步都留下记录。
//
// 素材一（pom.xml 里要有的三个依赖）：
//   <dependency>
//       <groupId>com.mysql</groupId>
//       <artifactId>mysql-connector-j</artifactId>
//       <version>8.0.33</version>
//   </dependency>
//   <dependency>
//       <groupId>org.junit.jupiter</groupId>
//       <artifactId>junit-jupiter</artifactId>
//       <version>5.9.3</version>
//       <scope>test</scope>
//   </dependency>
//   <dependency>
//       <groupId>org.projectlombok</groupId>
//       <artifactId>lombok</artifactId>
//       <version>1.18.30</version>
//   </dependency>
//
// 素材二（建库建表 + 5 条数据，课程资料 01. JDBC-数据库表/user.txt）：
//   create database if not exists web01;
//   use web01;
//
//   create table user(
//       id int unsigned primary key auto_increment comment 'ID,主键',
//       username varchar(20) comment '用户名',
//       password varchar(32) comment '密码',
//       name varchar(10) comment '姓名',
//       age tinyint unsigned comment '年龄'
//   ) comment '用户表';
//
//   insert into user(id, username, password, name, age) values (1, 'daqiao', '123456', '大乔', 22),
//                                                              (2, 'xiaoqiao', '123456', '小乔', 18),
//                                                              (3, 'diaochan', '123456', '貂蝉', 24),
//                                                              (4, 'lvbu', '123456', '吕布', 28),
//                                                              (5, 'zhaoyun', '12345678', '赵云', 27);
//
// 素材三（实体类 User 的属性和表字段是对应的）：
//   id / username / password / name / age，类型分别是 Integer / String / String / String / Integer
//
// 连接信息：主机 localhost、端口 3306、库 web01
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// 完成以下操作：
// 1. 建 maven 工程：在 pom.xml 里加上上面那三个依赖（驱动、JUnit、lombok）
// 2. 准备数据库表：在 web01 库里建 user 表并插入 5 条数据（用上面的建表语句）
// 3. 准备实体类：写一个 User 类，属性照素材三写，用 lombok 的注解省掉 getter/setter
// 4. 写第一个测试方法：按"连接数据库的五个动作"执行
//    update user set age = 25 where id = 1，把影响行数打印到控制台
// 5. 跑一次：把控制台输出原样抄到下面
// 6. 跑第二次做对照：把条件改成 id = 100（表里没有这个 id）再跑一次，
//    记下影响行数，并解释这次为什么没有报错
// 7. 回去验证数据：在客户端里执行 select * from user where id = 1;
//    确认年龄真的变了，把查到的这一行抄到下面
// 8. 收尾回答最后两个问题
//    （提示：想让 id=1 的年龄回到 22，重新导入一遍 user.txt 就行）
// ==========================================================================

// 在下面写你的代码：

package com.itheima;

public class JdbcLabTest {

    // 在这里写你的测试方法（实体类 User 可以单独建一个文件放在 pojo 包下）

}

// 第 5 步的记录（第一次运行的控制台输出）：
//
//

// 第 6 步的记录（id 改成 100 之后的输出）：
//
//

// 第 7 步的记录（select 查到的那一行）：
//
//

// 第 8 步的回答：
// ① 五个动作里，哪一步才是"真正把 SQL 送到数据库去执行"的那一步？其余几步分别在干什么？
//
//
// ② 如果这次要做的不是"改数据"而是"查数据"，哪一步要换？换成什么？结果又该怎么处理？
//
//
