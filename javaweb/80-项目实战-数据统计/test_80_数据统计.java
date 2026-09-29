// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2 + MyBatis + Lombok）
//   工程里已经有员工管理、班级管理、学员管理的三层代码
//   （ClazzController / StudentController / StudentMapper 都已就位）
//   现在要新增的是"数据统计"这一块：给"员工信息统计"页面的两张图表提供数据
//
// 接口文档片段（02. 接口文档 "报表统计" 分组）：
//   ① GET /report/studentCountData  班级人数统计
//        响应：{"code":1,"msg":"success","data":{
//                "clazzList":["JavaEE就业163期","前端就业90期",...],
//                "dataList":[6,3,...]}}
//        data.clazzList ：string[]  班级列表
//        data.dataList  ：integer[] 班级人数列表（与 clazzList 下标一一对应）
//   ② GET /report/studentDegreeData 学员学历统计
//        响应：{"code":1,"msg":"success","data":[
//                {"name":"初中","value":1},
//                {"name":"高中","value":4}]}
//        data 是列表：每一行 name 是学历名称、value 是人数
//   两条都是 GET、都不带请求参数，路径前缀都是 /report
//   （课程要求：所有功能全部严格根据接口文档进行开发，并进行前后端联调）
//
// 现成的类（直接用，不用自己写）：
//   com.itheima.pojo.Result        ：Result.success()、Result.success(Object)、Result.error(String)
//   com.itheima.pojo.Student       ：学员实体（Lombok 的 @Data），字段含
//                                    id / name / no / gender / phone / idCard / isCollege / address
//                                    / degree / graduationDate / clazzId / violationCount / violationScore
//                                    / createTime / updateTime
//   com.itheima.mapper.StudentMapper ：本练习的数据访问层接口（两个统计方法加在这里）
//
// 数据库：MySQL 的 tlias 库（clazz 表 6 条、student 表 18 条）
//   连接信息：主机 localhost、端口 3306，用户名/密码用你自己 MySQL 的
//   （课程示例是 root / 1234，动手时把 password 换成你自己 MySQL 的密码）
//   两张表的关键字段（完整建表脚本见 资料\03. 表结构\表结构.sql）：
//
//   create table clazz(                          -- 班级表
//       id int unsigned primary key auto_increment,
//       name varchar(30) not null unique,        -- 班级名称
//       room varchar(20),                        -- 班级教室
//       begin_date date not null,                -- 开课时间
//       end_date date not null,                  -- 结课时间
//       master_id int unsigned,                  -- 班主任ID
//       subject tinyint unsigned not null,       -- 学科
//       create_time datetime, update_time datetime
//   ) comment '班级表';
//
//   create table student(                        -- 学员表
//       id int unsigned primary key auto_increment,
//       name varchar(10) not null,
//       no char(10) not null unique,             -- 学号
//       gender tinyint unsigned not null,        -- 性别, 1:男, 2:女
//       phone varchar(11) not null unique,
//       id_card char(18) not null unique,
//       is_college tinyint unsigned not null,
//       address varchar(100),
//       degree tinyint unsigned,                 -- 最高学历, 1:初中,2:高中,3:大专,4:本科,5:硕士,6:博士
//       graduation_date date,
//       clazz_id int unsigned not null,          -- 班级ID, 关联班级表ID
//       violation_count tinyint unsigned default 0 not null,
//       violation_score tinyint unsigned default 0 not null,
//       create_time datetime, update_time datetime
//   ) comment '学员表';
//
// 本机数据概况（用来核对统计结果）：
//   clazz 6 条，id 是 1 / 4 / 5 / 6 / 7 / 8；
//   student 18 条，按 clazz_id 分布：2 → 7 人，1 → 6 人，8 → 2 人，4 → 3 人；
//     注意：clazz 表里并没有 id=2 的班级（课程数据本身如此）
//   学历分布：初中 1、高中 4、大专 3、本科 8、硕士 2
//
// 运行起来之后：应用在 8080 端口，两条接口的地址形如
//   http://localhost:8080/report/studentCountData
//   http://localhost:8080/report/studentDegreeData
//
// 本练习的题目分布：
//   题目2-1（班级人数统计的 SQL）写在 test_80_统计SQL.sql
//   题目2-3（学历统计的 SQL）   写在 test_80_统计SQL.sql，Java 部分写在本文件
//   综合题的两条 SQL 写在 test_80_统计SQL.sql
// ==========================================================================


// ==========================================================================
// 题目2-2：班级人数统计的三层实现（Java 部分）
// ==========================================================================
// 需求（SQL 见 test_80_统计SQL.sql 的题目2-1，SQL 写在那里）：
//   接口 GET /report/studentCountData 要返回
//     data = {clazzList:[班级名...], dataList:[人数...]}（两个数组下标一一对应）
//   数据访问层方法已经定好（现在就可以直接用）：
//     List<Map<String,Object>> getStudentCount();   // 一行一个 Map：cname=班级名, scount=人数
//   请完成 Java 侧的三部分：
//   1. 写一个封装类（两个属性：班级列表、人数列表），并用 Lombok 注解让它
//      能直接 new 出来（想想 Service 里 new 它用的是哪个构造器）；
//   2. 写业务层方法：把"一行一个 Map"的统计结果拆成两个 List，装进封装类；
//   3. 写 Controller 方法（请求方式、路径，返回值用 Result 包起来）。
// ==========================================================================

// 在下面写你的代码：




// ==========================================================================
// 题目2-3：学员学历统计（Java 部分）
// ==========================================================================
// 需求（SQL 见 test_80_统计SQL.sql 的题目2-3，SQL 写在那里）：
//   接口 GET /report/studentDegreeData 要返回
//     data = [{"name":"初中","value":1},{"name":"高中","value":4}, ...]
//     （一个列表，每一项是"学历名 + 人数"）
//   请完成 Java 侧的部分：
//   1. 写数据访问层的方法签名（返回类型是什么？统计结果没有对应的实体类）；
//   2. 写业务层方法——想一想：SQL 查出来的结果，是不是已经就是前端要的形状了？
//      还需要像题目2-2 那样再用 stream 拆一遍吗？
//   3. 写 Controller 方法（请求方式、路径、返回值）。
// ==========================================================================

// 在下面写你的代码：




// 第 3 问的回答（Service 要不要再加工、为什么）：
//


// ==========================================================================
// 题目2-4：读懂两段响应，把数据交给 ECharts，并核对数字
// ==========================================================================
// 下面两段是同一台机器上的真实响应（学员 18 名、班级 6 个）：
//
//   ① {"code":1,"msg":"success","data":{
//        "clazzList":["JavaEE就业163期","前端就业90期","JavaEE就业167期","JavaEE就业165期","JavaEE就业166期","大数据就业58期"],
//        "dataList":[6,3,2,0,0,0]}}
//   ② {"code":1,"msg":"success","data":[
//        {"name":"初中","value":1},{"name":"高中","value":4},{"name":"大专","value":3},
//        {"name":"本科","value":8},{"name":"硕士","value":2}]}
//
// 请回答并写出配置片段：
//   1. 两段响应分别来自哪个接口？哪个喂柱状图、哪个喂环形图？
//   2. 分别写出把 data 交给 ECharts 的配置片段（柱状图用哪两个字段、
//      环形图怎么用整个数组）；
//   3. ①里各项相加是 11，而学员一共 18 名，差的 7 人是怎么回事？
//      ②里各项相加是 18，为什么这里一个不差？
//   4. ①里哪几个班级的人数是 0？它们为什么没被统计掉？
// ==========================================================================

// 第 1 问的回答（两个接口 + 图表对应）：
//

// 第 2 问的配置片段（ECharts）：
//


// 第 3 问的回答（11 与 18 的差 / 18 刚好对上）：
//

// 第 4 问的回答（0 人班级与原因）：
//


// ==========================================================================
// 综合题：从头做完两个统计接口，并核对统计结果
// ==========================================================================
// 目标：把 Controller → Service → Mapper（SQL）三层都自己写一遍，
//       启动后用真实数据核对两个接口的响应，并和前端页面联调。
//
// 完成以下操作：
// 1. 新建 ClazzCountOption：两个 List 属性（clazzList、dataList），
//    类上标好 Lombok 三件套；
// 2. 在 ReportController 里写两个 GET 方法：/studentCountData 与 /studentDegreeData，
//    分别返回 Result.success(clazzCountOption) 与 Result.success(dataList)
//    （类上 @RestController + @Slf4j + @RequestMapping("/report")，注入 ReportService）；
// 3. 写 ReportService 接口与 ReportServiceImpl 实现（@Service，注入 StudentMapper）：
//    班级人数统计拆两个数组装封装类；学历统计直接返回；
// 4. 数据访问层写两个统计方法（SQL 见 test_80_统计SQL.sql 的综合题）：
//    班级人数那条要"以班级表为主"、保证 0 人的班级也出现；
//    学历那条要把 degree 翻成中文、两个列别名是 name 和 value；
// 5. 启动应用，分别发 GET http://localhost:8080/report/studentCountData
//    与 GET http://localhost:8080/report/studentDegreeData，把两段响应抄到下面；
// 6. 核对三件事：
//    ① 班级人数各项相加是多少？和学员总数 18 差在哪里（提示：看 clazz_id=2）？
//    ② 学历各项相加是多少，和 18 对上了吗？
//    ③ 哪些班级的人数是 0，它们为什么没有消失？
// 7. 前后端联调：打开统计页面，把柱状图的横轴班级、柱子高度和环形图的
//    扇区、图例与接口响应逐个对照；如果图出不来，先查字段名
//    （clazzList / dataList / name / value）和接口路径有没有写错；
// 8. 收尾：如果实验里动过班级或学员数据，把它恢复成 6 个班级 / 18 名学员。
// ==========================================================================

// 在下面写你的代码（综合题的三层代码）：




// 第 5 步的记录（两段完整响应）：
//

// 第 6 步的核对结果（三个小问）：
// ①
//
// ②
//
// ③
//

// 第 7 步的联调记录（页面上的数字与接口响应是否一致、有没有踩坑）：
//

// 第 8 步的收尾记录：
