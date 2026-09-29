// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2.x + MyBatis + MySQL，Java 17）
// 包名：com.itheima，下面分 controller / service / service.impl / mapper / pojo
// 数据库：MySQL，库名 tlias（主机 localhost、端口 3306）
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// 本章需要你自己新建的类（第 11 章的起步代码里没有）：
//   controller/StudentController.java
//   service/StudentService.java、service/impl/StudentServiceImpl.java
//   mapper/StudentMapper.java + resources/com/itheima/mapper/StudentMapper.xml
// 已经有的（前面几篇做的，直接调用即可）：
//   pojo/Result、pojo/PageResult、pojo/Student（资料 04. 基础代码 直接给了）、
//   exception/BusinessException、exception/GlobalExceptionHandler
//   （重复键会被 handleDuplicateKeyException 转成 {"code":0,"msg":"'xxx' 已存在"}）
//
// student 表（学员表，课程数据 18 条）：
//   id               int unsigned   主键、自增
//   name             varchar(10)    非空            姓名
//   no               char(10)       非空、唯一        学号
//   gender           tinyint        非空            性别, 1: 男, 2: 女
//   phone            varchar(11)    非空、唯一        手机号
//   id_card          char(18)       非空、唯一        身份证号
//   is_college       tinyint        非空            是否来自院校, 1: 是, 0: 否
//   address          varchar(100)                   联系地址
//   degree           tinyint                       最高学历, 1:初中 2:高中 3:大专 4:本科 5:硕士 6:博士
//   graduation_date  date                          毕业时间
//   clazz_id         int unsigned   非空            班级ID（关联 clazz.id）
//   violation_count  tinyint        非空、默认 0     违纪次数
//   violation_score  tinyint        非空、默认 0     违纪扣分
//   create_time      datetime                      创建时间
//   update_time      datetime                      修改时间
//
// 实体类 com.itheima.pojo.Student（属性与表列一一对应，另有 clazzName 属性：
//   它不是表里的列，是列表查询关联班级表时查出来的班级名称）：
//   Integer id / String name / String no / Integer gender / String phone /
//   String idCard / Integer isCollege / String address / Integer degree /
//   LocalDate graduationDate / Integer clazzId / Short violationCount /
//   Short violationScore / LocalDateTime createTime / LocalDateTime updateTime /
//   String clazzName
//
// 统一响应结果类 com.itheima.pojo.Result（已存在）：
//   Result.success() / Result.success(Object) / Result.error(String msg)
// 分页结果封装类 com.itheima.pojo.PageResult（已存在）：total + rows
//
// 接口文档《4. 学员管理》片段（严格按文档开发）：
//   4.1 学员列表查询   GET  /students
//         参数格式：queryString
//         name（姓名，否）、degree（学历，否）、clazzId（班级ID，否）
//         page（页码，默认 1）、pageSize（每页记录数，默认 10）
//         样例：/students?name=张三&degree=1&clazzId=2&page=1&pageSize=5
//   4.2 删除学员      DELETE /students/{ids}
//         参数格式：路径参数；ids 学员的 ID 数组；样例：/students/1,2,3
//   4.3 添加学员      POST /students
//         参数格式：application/json（请求体是学员 JSON）
//         必须：name / no / gender / phone / degree / clazzId
//         非必须：idCard / isCollege / address / graduationDate
//   4.4 根据ID查询    GET /students/{id}
//         参数格式：路径参数；id 学员ID；样例：/students/8
//   4.5 修改学员      PUT /students
//         参数格式：application/json（请求体是学员 JSON，带 id）
//   响应统一是：{"code":1,"msg":"success","data":...}
//
// 页面上的入口（学员管理页）：
//   顶部三个查询条件：姓名（模糊）、最高学历（下拉）、所属班级（下拉）
//   表格上方：「+ 新增学员」「- 批量删除」两个按钮
//   每行的操作列：「编辑」「违纪」「删除」
//   查询结果按最后操作时间倒序、分页展示；列表里的"班级"列显示班级名称
// ==========================================================================


// ==========================================================================
// 题目2-1：新增学员（三层全写）
// ==========================================================================
// 需求：
//   点「+ 新增学员」弹窗，填完提交；前端把学员信息（姓名、学号、性别、手机号、
//   身份证号、是否来自院校、联系地址、学历、毕业时间、班级ID）以 JSON 放进
//   请求体，POST 到 /students。
//   控制层把请求体接成学员对象；业务层补上创建时间与修改时间；
//   数据访问层把记录写进 student 表。
//
// 完成以下操作：
// 1. 写出控制层方法、业务层方法（接口 + 实现）、数据访问层方法（含 SQL）
// 2. 回答：insert 语句里为什么不写 violation_count、violation_score 两列？
// 3. 回答：如果学号和库里已有学员重复，接口会返回什么？
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（com.itheima.controller.StudentController）：


// ② 业务层（service.StudentService / service.impl.StudentServiceImpl）：


// ③ 数据访问层（mapper.StudentMapper）：


// 第 2 步的回答：
//


// 第 3 步的回答：
//


// ==========================================================================
// 题目2-2：学员列表的条件分页查询（三层全写）
// ==========================================================================
// 需求：
//   页面顶部三个查询条件：姓名（模糊查询）、最高学历（精确）、所属班级（精确），
//   三个都可以不填；列表里"班级"这一列要显示班级名称（student 表里只有 clazz_id）；
//   查询结果按最后操作时间倒序、分页展示。
//
// 完成以下操作：
// 1. 写出控制层方法、业务层方法（接口 + 实现）、数据访问层方法（含 XML 里的 SQL）
// 2. 回答：列表 SQL 里为什么要关联班级表？用 left join 有什么好处？
// ==========================================================================

// 在下面写你的代码：

// ① 控制层：


// ② 业务层：


// ③ 数据访问层（StudentMapper 接口方法 + StudentMapper.xml 里的 select）：


// 第 2 步的回答：
//


// ==========================================================================
// 题目2-3：学员的「编辑」流程——详情回显 + 按需修改
// ==========================================================================
// 需求：
//   点行尾的「编辑」，弹窗先按 ID 把该学员的信息查出来回显（GET /students/8）；
//   改完点保存，前端把学员 JSON（带 id）以 PUT 发到 /students，
//   只有提交上来的字段才更新，最后修改时间由后端补。
//
// 完成以下操作：
// 1. 写出这两个接口的三层实现（详情用注解 SQL 即可；修改的 SQL 写在 XML 里）
// 2. 回答：<set> 标签帮了什么忙？
// 3. 回答：为什么字符串字段的条件要判 != null 且 != ''？数字字段呢？
// ==========================================================================

// 在下面写你的代码：

// ① 控制层（两个方法）：


// ② 业务层（两个方法）：


// ③ 数据访问层（详情注解 + 修改的 XML update）：


// 第 2 步的回答：
//


// 第 3 步的回答：
//


// ==========================================================================
// 题目2-4：批量删除学员（注意是路径参数）
// ==========================================================================
// 需求：
//   表格勾选若干行点「批量删除」，前端把选中的学员 id 拼成 1,2,3 放进路径里，
//   发到 /students/1,2,3；单行的「删除」只传一个 id，走同一个接口。
//
// 完成以下操作：
// 1. 写出三层实现（控制层的接参要按接口文档的"参数格式"来，SQL 写在 XML 里）
// 2. 回答：它和删除员工的接口 DELETE /emps?ids=1,2,3 在参数格式上差在哪？
//    控制层注解因此有什么不同？
//     （可对照 74 篇《删除员工》里员工那套写法）
// ==========================================================================

// 在下面写你的代码：

// ① 控制层：


// ② 业务层：


// ③ 数据访问层（接口方法 + XML 里的 delete）：


// 第 2 步的回答：
//
