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
// emp_expr 表（员工工作经历）：
//   id       int unsigned  主键、自增
//   emp_id   int unsigned  员工ID（关联 emp.id）
//   begin    date          开始时间
//   end      date          结束时间
//   company  varchar(50)   公司名称
//   job      varchar(50)   职位
//
// 实体类 com.itheima.pojo.Emp 的属性（与 emp 表字段对应）：
//   id Integer / username String / password String / name String / gender Integer
//   phone String / job Integer / salary Integer / image String / entryDate LocalDate
//   deptId Integer / createTime LocalDateTime / updateTime LocalDateTime
//   deptName String（部门名称，查询时封装）
//   exprList List<EmpExpr>（工作经历列表 ← 新增接口靠它接住 JSON 里的 exprList）
//
// 实体类 com.itheima.pojo.EmpExpr 的属性：
//   id Integer / empId Integer / begin LocalDate / end LocalDate / company String / job String
//
// 统一响应结果类 com.itheima.pojo.Result（已存在，不用自己写）：
//   code Integer（1 成功，0 失败）/ msg String / data Object
//   Result.success()          → 成功，不带数据
//   Result.success(Object)    → 成功，带数据
//   Result.error(String msg)  → 失败
//
// 已有的类（前面几篇做分页查询时建的，直接调用即可）：
//   DeptMapper / DeptService / DeptServiceImpl / DeptController
//   EmpMapper.list(EmpQueryParam) / EmpService.page(EmpQueryParam) / EmpController.page(...)
//
// 接口文档《2.3 添加员工》片段：
//   请求路径：/emps
//   请求方式：POST
//   接口描述：该接口用于添加员工的信息
//   参数格式：application/json
//   参数说明：
//     username   string    必须    用户名
//     name       string    必须    姓名
//     gender     number    必须    性别，1 男 2 女
//     image      string    非必须  图像
//     deptId     number    非必须  部门id
//     entryDate  string    非必须  入职日期
//     job        number    非必须  职位，1 班主任 2 讲师 3 学工主管 4 教研主管 5 咨询师
//     salary     number    非必须  薪资
//     exprList   object[]  非必须  工作经历列表
//   响应：统一响应结果（code / msg / data）
// ==========================================================================


// ==========================================================================
// 题目2-1：开发"新增员工"的接口（基本信息部分）
// ==========================================================================
// 需求：
//   前端把新增员工表单以 JSON 提交到 /emps（POST）。三层都要写：
//     - 控制层：接收这个 JSON 参数、打一行日志、调用业务层、返回统一响应结果；
//     - 业务层：保存前先把"创建时间"和"修改时间"补上当前时间，再交给数据访问层；
//     - 数据访问层：用一条 insert 把用户名、姓名、性别、手机号、职位、薪资、头像、
//                   入职日期、所属部门 id、创建时间、修改时间写进 emp 表
//                   （密码不由这里写，主键是数据库自增的）。
//
// 完成以下操作：
// 1. 三层代码写在下面（方法名自取，课堂工程里叫 save / insert）
// 2. 写完后回答：为什么"补全创建时间/修改时间"要放在业务层，而不是控制层？
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（com.itheima.controller.EmpController）：


// ② 业务层接口 + 实现类（com.itheima.service.EmpService / com.itheima.service.impl.EmpServiceImpl）：


// ③ 数据访问层（com.itheima.mapper.EmpMapper）：


// 第 2 步的回答：
//
//


// ==========================================================================
// 题目2-2：插完基本信息，把数据库生成的主键拿回来
// ==========================================================================
// 需求：
//   员工的主键是数据库自增出来的，Java 对象在插入前它的 id 是 null。
//   业务层保存完基本信息后，要立刻拿到这个新员工的 id，用它给每一条工作经历
//   填上"属于哪个员工"（emp_expr.emp_id），然后再去保存工作经历。
//
// 完成以下操作：
// 1. 给"保存员工基本信息"的那个数据访问方法补上必要的注解，使业务层在插入后能取到新主键
// 2. 写出业务层"保存基本信息 → 取新 id → 给工作经历赋 empId"这几行代码
// 3. 回答：如果这一步没做，数据库里会出现什么样的数据？
// ==========================================================================

// 在下面写你的代码：

// ① 数据访问层的插入方法（注解 + 方法签名）：


// ② 业务层里从插入到赋值的代码：


// ③ 第 3 步的回答：
//
//


// ==========================================================================
// 题目2-4：把"两次插入"的顺序和关联讲清楚
// ==========================================================================
// 需求：
//   有人把业务层写成"先批量保存工作经历，再保存员工基本信息"，
//   也有人忘了给工作经历填员工 id。请说明：
//   ① 这两步的正确顺序以及为什么；
//   ② 每段工作经历上的"员工 id"是什么时候、从哪儿来的；
//   ③ 如果用户一段工作经历都没填，代码要怎么处理。
//
// 完成以下操作：
// 1. 用一个代码片段把正确的写法写出来（业务层）
// 2. 回答上面三个问题
// ==========================================================================

// 在下面写你的代码：


// 第 2 步的回答：
// ①
//
// ②
//
// ③
//


// ==========================================================================
// 综合题：照着课程把"新增员工"从页面做到数据库（附一次失败实验）
// ==========================================================================
// 完成以下操作：
// 1. 三层补齐"新增员工"：控制层接收 JSON、业务层补时间 + 保存基本信息 +
//    给经历赋 empId + 批量保存经历、数据访问层写两句 SQL
//    （批量保存工作经历的 SQL 写在 test_69_批量插入XML.xml 里）
// 2. 启动工程，用 Apifox（或用 JSON 文件 + curl --data-binary @body.json，文件必须是 UTF-8）
//    发一次 POST /emps，请求体带两段工作经历，把返回的 JSON 抄下来
// 3. 去客户端查库：
//    select * from emp order by id desc limit 1;
//    select * from emp_expr where emp_id = <刚才那个 id>;
//    记录新员工的 id 和经历的条数，确认两段经历的 emp_id 都等于新员工 id
// 4. 把服务端日志里批量插入那条 SQL 抄下来（数一数 values 后面有几组括号）
// 5. 做对照实验：把业务层里"保存工作经历"那一步注释掉（或改成故意抛异常），
//    再发一次新增请求，然后查库——员工和经历各有几条？把结果记下来
// 6. 回答下面的两个问题
// ==========================================================================

// 第 2 步的记录（返回的 JSON）：
//
//

// 第 3 步的记录（新员工 id / 经历条数 / emp_id 是否相等）：
//
//

// 第 4 步的记录（日志里的 SQL）：
//
//

// 第 5 步的记录（对照实验后 emp 与 emp_expr 各几条）：
//
//

// 第 6 步的回答：
// ① 如果保存基本信息成功、保存经历失败，数据库会变成什么样？为什么说"不可以"？
//
//
// ② 要在代码里避免这种情况，下一步该引入什么机制？
//
//
