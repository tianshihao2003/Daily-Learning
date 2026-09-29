// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2.x + MyBatis + MySQL，Java 17）
// 包名：com.itheima，下面分 controller / service / service.impl / mapper / pojo
// 数据库：MySQL，库名 tlias（主机 localhost、端口 3306）
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// 本题写的是学员管理里的「违纪处理」，用到的类：
//   controller/StudentController.java、service/StudentService.java、
//   service.impl/StudentServiceImpl.java、mapper/StudentMapper.java
//   （这些类在 test_79_学员管理.java 那道题里会一起搭起来）
//   实体类 pojo/Student 已存在；统一响应结果类的几个方法：
//     Result.success() / Result.success(Object) / Result.error(String msg)
//
// student 表里与违纪有关的两列：
//   violation_count  tinyint unsigned  非空、默认 0   违纪次数
//   violation_score  tinyint unsigned  非空、默认 0   违纪扣分
//   （表里还有 update_time datetime：最后修改时间，列表按它倒序排序）
//
// 页面原型上的交互与规则（学员管理页）：
//   每行操作列里有「违纪」按钮，点它弹出标题为"学员违纪处理"的小弹窗，
//   里面只有"违纪扣分"一个输入框，加「确定」「取消」两个按钮。
//   规则：1). 每一次违纪处理，就需要将违纪次数往上累加一次。
//         2). 每一次违纪处理，需要将违纪分数累加。
//
// 接口文档《4.6 违纪处理》片段（严格按文档开发）：
//   请求路径：/students/violation/{id}/{score}
//   请求方式：PUT
//   接口描述：该接口用于修改学员的数据信息
//   参数格式：路径参数
//   参数说明：
//     id      number  必须  学员ID
//     score   number  必须  扣除分数
//   响应数据样例：{"code":1,"msg":"success","data":null}
//   （注意：不是查询参数、也不是请求体，两个值都在路径里）
//
// 库里的参考数据（课程数据，可用来对照"累加"的结果）：
//   id=1  段誉    violation_count=0   violation_score=0     ← 可以用它做第 2 步
//   id=12 崔百泉  violation_count=6   violation_score=17    ← 就是一次次累加出来的
//   id=18 郑成功  violation_count=2   violation_score=7
// ==========================================================================


// ==========================================================================
// 题目3-1：照着课程把"违纪处理"从接口做到数据库，并验证数据是"累加"的
// ==========================================================================
// 完成以下操作：
// 1. 按接口文档 4.6 写出违纪处理的三层实现：
//    控制层接两个路径参数、业务层透传、数据访问层写那条 update
// 2. 找一个没被处理过的学员，记下他的 id 和当前的 violation_count /
//    violation_score（可查：select id, name, violation_count, violation_score
//    from student where violation_count = 0;）
// 3. 启动工程，发一次请求：
//    PUT http://localhost:8080/students/violation/<id>/5
//    把响应的 JSON 抄下来
// 4. 再查一次库，把 violation_count 与 violation_score 的新值抄下来，
//    数一数次数涨了几、分数涨了几
// 5. 用同一个 id 再发一次 PUT /students/violation/<id>/3（这次扣 3 分），
//    再查库，把两个字段的新值抄下来
// 6. 从 StudentMapper 里把这条 SQL 原文抄出来，圈出"哪一部分是次数 +1"、
//    "哪一部分是分数累加"、"哪一部分保证只改这一个学员"
// 7. 回答下面的问题
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（com.itheima.controller.StudentController）：


// ② 业务层（service.StudentService / service.impl.StudentServiceImpl）：


// ③ 数据访问层（mapper.StudentMapper，写 SQL 时注意三件事：
//    次数在原值上加 1、分数在原值上加上这次扣的分、只改这一个学员）：



// 第 2 步的记录（学员 id / 姓名 / 处理前的次数与分数）：
//
//


// 第 3 步的记录（请求地址 / 返回的 JSON）：
//
//


// 第 4 步的记录（第一次处理后的次数与分数 / 各自涨了多少）：
//
//


// 第 5 步的记录（再扣 3 分后的次数与分数）：
//
//


// 第 6 步的记录（SQL 原文 / 三处分别是什么）：
//
//
//


// 第 7 步的回答：
// ① 如果把违纪处理改成"先查出来、在 Java 里把次数 +1、分数加上去，
//    再调 update 写回"，会有什么风险？
//
//
// ② 这个接口为什么把"扣多少分"设计成一个路径参数、让前端传，
//    而"违纪次数"却要后端自己加？
//
//
