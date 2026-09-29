// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2.x + MyBatis + MySQL，Java 17）
// 包名：com.itheima，下面分 controller / service / service.impl / mapper / pojo
// 数据库：MySQL，库名 tlias（主机 localhost、端口 3306）
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// emp 表（员工基本信息）：
//   id           int unsigned  主键、自增          （ID）
//   username     varchar(20)   非空、唯一          （用户名）
//   password     varchar(32)   默认 NULL           （密码）
//   name         varchar(10)   非空                （姓名）
//   gender       tinyint       非空                （性别, 1 男 2 女）
//   phone        varchar(11)                       （手机号）
//   job          tinyint                           （职位, 1 班主任 2 讲师 3 学工主管 4 教研主管 5 咨询师）
//   salary       int                               （薪资）
//   image        varchar(300)                      （头像）
//   entry_date   date                              （入职日期）
//   dept_id      int unsigned                      （关联的部门ID）
//   create_time  datetime                          （创建时间）
//   update_time  datetime                          （修改时间）
//
// emp_expr 表（员工工作经历，一个员工可以有多条）：
//   id       int unsigned  主键、自增
//   emp_id   int unsigned  员工ID（关联 emp.id）
//   begin    date          开始时间
//   end      date          结束时间
//   company  varchar(50)   公司名称
//   job      varchar(50)   职位
//
// 实体类 com.itheima.pojo.Emp 的属性：
//   id Integer / username String / password String / name String / gender Integer
//   phone String / job Integer / salary Integer / image String / entryDate LocalDate
//   deptId Integer / createTime LocalDateTime / updateTime LocalDateTime
//   exprList List<EmpExpr>（工作经历列表 ← 回显要把工作经历装进这里）
//
// 实体类 com.itheima.pojo.EmpExpr 的属性：
//   id Integer / empId Integer / begin LocalDate / end LocalDate / company String / job String
//
// 统一响应结果类 com.itheima.pojo.Result（已存在，不用自己写）：
//   code Integer（1 成功，0 失败）/ msg String / data Object
//   Result.success()          → 成功，不带数据
//   Result.success(Object)    → 成功，带数据
//
// 已有的类 / 方法（前面几篇做的，直接调用即可）：
//   EmpController 里已有分页查询 page(...)、新增员工 save(...)、删除员工 delete(...)
//   EmpService / EmpServiceImpl / EmpMapper / EmpExprMapper 都已存在
//   EmpExprMapper 里已有：
//     void insertBatch(List<EmpExpr> exprList);    // 批量保存工作经历
//     void deleteByEmpIds(List<Integer> empIds);   // 按员工ID批量删除工作经历
//   EmpMapper 里已有：deleteByIds(List<Integer> ids)（批量删除员工）
//
// 接口文档《2.4 根据ID查询》片段（点「编辑」时先调它）：
//   请求路径：/emps/{id}
//   请求方式：GET
//   接口描述：该接口用于根据主键ID查询员工的信息
//   参数格式：路径参数
//   参数说明：id  number  必须  员工ID         请求样例：/emps/1
//   响应 data 里的字段：
//     id / username / name / password / entryDate / gender / image / job
//     / salary / deptId / createTime / updateTime
//     exprList   object[]  非必须  工作经历列表
//       ├─ id / company / job / begin / end / empId
//
// 接口文档《2.5 修改员工》片段（点「保存」时调它）：
//   请求路径：/emps
//   请求方式：PUT
//   接口描述：该接口用于修改员工的数据信息
//   参数格式：application/json
//   参数说明：
//     id          number    必须    id
//     username    string    必须    用户名
//     name        string    必须    姓名
//     gender      number    必须    性别, 1 男 2 女
//     image       string    非必须  图像
//     deptId      number    非必须  部门id
//     entryDate   string    非必须  入职日期
//     job         number    非必须  职位
//     salary      number    非必须  薪资
//     exprList    object[]  非必须  工作经历列表（id / company / job / begin / end / empId）
//   响应：统一响应结果（code / msg / data）
//
// 页面交互（两处按钮）：
//   列表每行的「编辑」→ 打开表单并填好数据（先查）→ 用户改完点「保存」（再改）
// ==========================================================================


// ==========================================================================
// 题目2-1：点「编辑」时，把员工和他的工作经历一起带出来（三层）
// ==========================================================================
// 需求：
//   前端在列表里点了某一行「编辑」，只知道这个员工的 id（比如 41），要打开一张表单、
//   把这位员工的基本信息和他的所有工作经历都填进去。后端要提供一个查询接口：
//   接住这个 id、交给业务层和数据访问层，返回统一响应结果，
//   data 里是这位员工（工作经历要能一起装进去）。三层都要写。
//
// 完成以下操作：
// 1. 写出控制层方法、业务层方法（接口 + 实现）、数据访问层的方法签名
// 2. 写完后回答：这个 id 应该用什么注解接收？为什么？
//    （完整的查询 SQL 与结果映射写在 test_75_结果映射与动态更新.xml 里）
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（com.itheima.controller.EmpController）：


// ② 业务层接口 + 实现类（com.itheima.service.EmpService / com.itheima.service.impl.EmpServiceImpl）：


// ③ 数据访问层方法签名（com.itheima.mapper.EmpMapper）：


// 第 2 步的回答：
//


// ==========================================================================
// 题目2-2：保存修改：一次提交要动两张表（三层 + 讲清"先删后插"）
// ==========================================================================
// 需求：
//   用户在修改表单里改完基本信息、又增删了几行工作经历，点「保存」把整份数据
//   （含工作经历列表）以 JSON 提交到 /emps（PUT）。后端要：
//     - 改这个员工的基本信息（顺手记下最后修改时间）；
//     - 把这个员工原有的工作经历换成表单里的那份。
//   两步都必须实现，并且要么一起成功、要么一起不做。
//
// 完成以下操作：
// 1. 写出控制层方法、业务层方法（接口 + 实现）、数据访问层要用的方法签名
// 2. 说明工作经历那一步要怎么操作才能做到"表单里剩几条，库里就有几条"：
//    如果只新增不删除会怎样？如果只删除不新增会怎样？用户一段经历都不填时又要怎么处理？
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（com.itheima.controller.EmpController）：


// ② 业务层接口 + 实现类（com.itheima.service.EmpService / com.itheima.service.impl.EmpServiceImpl）：


// ③ 数据访问层方法签名（com.itheima.mapper.EmpMapper）：


// 第 2 步的回答：
// 让"表单里剩几条、库里就有几条"的做法：
//
// 只新增不删除会怎样：
//
// 只删除不新增会怎样：
//
// 用户一段经历都不填时：
//


// ==========================================================================
// 综合题：照着课程把"编辑 → 回显 → 改 → 保存"整条链路走一遍
// ==========================================================================
// 完成以下操作：
// 1. 三层补齐两个接口：查询回显（GET，带路径变量，多表查询 + 自定义结果集）
//    和修改数据（PUT，接收 JSON，改基本信息 + 换工作经历），
//    更新语句用"只更新传了值的字段"那版
//    （查询的结果映射与更新语句都写在 test_75_结果映射与动态更新.xml 里）
// 2. 先造一条带 2 段工作经历的数据：用新增接口新增一名员工（例如 username 用 zhangwei），
//    记下后端生成的 id
// 3. 发一次查询回显请求 GET /emps/<id>，把返回的 JSON 抄下来
//    —— 确认 data 是一个对象、里面 exprList 是 2 条，记下这两条经历的 id
// 4. 发一次修改请求 PUT /emps：把姓名改掉、职位/薪资/部门改掉，
//    工作经历换成 3 条（注意 JSON 里必须带 id）
// 5. 把服务端日志里这次请求发出的 SQL 按顺序抄下来（应该有三条），并去库里查：
//      select * from emp where id = <id>;
//      select * from emp_expr where emp_id = <id>;
//    基本信息改对了吗？经历有几条？
// 6. 再发一次 GET /emps/<id>，把新经历的 id 和第 3 步记下的老 id 比一比，
//    然后解释：为什么 id 会变？
// 7. 回答下面的两个问题
// ==========================================================================

// 第 2 步的记录（新员工 id / 经历条数）：
//
//

// 第 3 步的记录（回显返回的 JSON / 两条经历的 id）：
//
//
//

// 第 4～5 步的记录（三条 SQL 的顺序 / 改完查库的结果）：
//
//
//

// 第 6 步的记录（新经历的 id / 与老 id 的对比）：
//
//

// 第 7 步的回答：
// ① 三条 SQL 为什么是这个顺序？如果改成"先插新经历、再删老经历"会发生什么？
//
//
// ② 用户在工作经历里点了几次「添加工作经历」、又删掉了一行，后端怎么知道该存哪几条？
//
//
