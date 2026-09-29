// ============================================
// 题目2-1：从零搭起一个能查用户数据的 MyBatis 工程
// ============================================
// 需求：
//   新建一个 SpringBoot 工程，连上 web01 库的 user 表，
//   用 MyBatis 把 5 条用户数据全部查出来并在控制台打印。
//
// 完成以下操作：
// 1. 建工程：创建一个 SpringBoot 工程，引入"MyBatis 与 SpringBoot 的整合依赖"
//    和"MySQL 驱动"（也可以再加上 Lombok）
// 2. 准备数据：把下面这份 user 建表与数据脚本执行一遍（5 条数据）
//    （素材·建表脚本）
//      create table user(
//          id int unsigned primary key auto_increment comment 'ID,主键',
//          username varchar(20) comment '用户名',
//          password varchar(32) comment '密码',
//          name varchar(10) comment '姓名',
//          age tinyint unsigned comment '年龄'
//      ) comment '用户表';
//    5 条数据：(1,'daqiao','123456','大乔',22)、(2,'xiaoqiao','123456','小乔',18)、
//              (3,'diaochan','123456','貂蝉',24)、(4,'lvbu','123456','吕布',28)、
//              (5,'zhaoyun','12345678','赵云',27)
//    （素材·实体类，属性名与列名一一对应）
//      package com.itheima.pojo;
//      @Data @NoArgsConstructor @AllArgsConstructor
//      public class User {
//          private Integer id; private String username; private String password;
//          private String name; private Integer age;
//      }
// 3. 配置数据源：在 application.properties 里写四行连接信息
//    （库名 web01、用户名 root、密码换成你自己 MySQL 的密码）
// 4. 写持久层接口：定义 UserMapper 接口（接口上要加"让框架自动生成实现类对象"的注解），
//    用"查询注解"写一句查所有用户的 SQL，返回 List<User>
// 5. 写测试：在与引导类同包（或其子包）的测试类上加"加载 SpringBoot 环境"的注解，
//    注入 UserMapper，调用查询方法并逐条打印
// 6. 跑测试：确认控制台打出 5 行 User(...)
//
// 跑通之后回答（写在文件末尾的作答区）：
//   ① 这个持久层接口没有实现类，为什么能调用？
//   ② 接口上那个必须加的注解，它到底做了什么？
// ============================================

// 在下面写你的代码：

// 第 1 步：把 pom.xml 需要的依赖写在这里（组名 / 构件名 / 版本）
//
//

// 第 3 步：application.properties 的四行写在这里
//
//
//
//

// 第 4 步：UserMapper 接口写在这里（文件位置 src/main/java/com/itheima/mapper/UserMapper.java）
//

// 第 5 步：测试类写在这里（文件位置 src/test/java/com/itheima/ 下）
//

// 跑通后的两个回答：
// ①
// ②

// ============================================
// 综合题3-1：从零把入门工程跑通，并完成辅助配置的验证
// ============================================
// 需求：在 2-1 的工程基础上，把两项辅助配置做完，每一步都留下可验证的记录。
//
// 完成以下操作：
// 7. 在 application.properties 里加上"MyBatis 日志输出"的配置项，重新跑一次测试
// 8. 把控制台里 SQL 日志的三行抄到下面，标出每一行分别说明什么
// 9. 在 IDEA 里配好 MySQL 数据库连接（Database 面板 → Data Source → MySQL，
//    填 Host / Port / User / Password / Database），观察 @Select 里那段 SQL
//    在配置前、配置后有什么变化（配置前长什么样、配置后能不能提示和跳转）
// 10. 回答：这套工程里你自己写的"业务代码"一共有几行？
//     连接信息、SQL 分别放在了哪里？
// ============================================

// 在下面写你的代码：

// 第 8 步：三行日志抄在这里，并逐行标注作用
//
//
//

// 第 9 步：配置 SQL 提示前后，@Select 里那段 SQL 的变化写在这里
//

// 第 10 步：第 10 步的回答写在这里
//
