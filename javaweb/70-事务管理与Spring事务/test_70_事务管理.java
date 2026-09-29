// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2.x + MyBatis + MySQL，Java 17）
// 包名：com.itheima，下面分 controller / service / service.impl / mapper / pojo
// 数据库：MySQL，库名 tlias（主机 localhost、端口 3306）
//   用户名/密码用你自己 MySQL 的（课程示例是 root / 1234，
//   动手时把 password 换成你自己 MySQL 的密码）
//
// emp 表（员工基本信息）：id / username / password / name / gender / phone / job
//   / salary / image / entry_date / dept_id / create_time / update_time
// emp_expr 表（员工工作经历）：id / emp_id / begin / end / company / job
//
// 业务层现状（"新增员工"的保存方法，两次数据库操作，中间可能出错）：
//
//   @Service
//   public class EmpServiceImpl implements EmpService {
//       @Autowired private EmpMapper empMapper;
//       @Autowired private EmpExprMapper empExprMapper;
//
//       @Override
//       public void save(Emp emp) {
//           //1. 保存员工基本信息
//           emp.setCreateTime(LocalDateTime.now());
//           emp.setUpdateTime(LocalDateTime.now());
//           empMapper.insert(emp);
//
//           //2. 保存员工工作经历信息
//           List<EmpExpr> exprList = emp.getExprList();
//           if(!CollectionUtils.isEmpty(exprList)){
//               exprList.forEach(empExpr -> empExpr.setEmpId(emp.getId()));
//               empExprMapper.insertBatch(exprList);
//           }
//       }
//   }
//
// 已有的类：EmpController.save(@RequestBody Emp emp) / EmpMapper.insert(Emp) /
//           EmpExprMapper.insertBatch(List<EmpExpr>) / Result（统一响应结果）
//
// 配置文件的现状（application.yml，节选）：
//
//   spring:
//     datasource:
//       url: jdbc:mysql://localhost:3306/tlias
//       driver-class-name: com.mysql.cj.jdbc.Driver
//       username: root
//       password: 1234          # 换成你自己 MySQL 的密码
//
// 返回值的现象（第 70 篇实测）：
//   正常一次新增 → {"code":1,"msg":"success","data":null}
// ==========================================================================


// ==========================================================================
// 题目2-2：让"保存员工"这件事由 Spring 统一管事务
// ==========================================================================
// 需求：
//   业务层的 save 方法里要执行"保存基本信息"和"批量保存工作经历"两次数据库操作。
//   要求：不要在代码里手写任何开启事务/提交/回滚的语句，只要在方法上加一个东西，
//   就能让这两次操作成为一个整体——方法顺利执行完就提交，中途抛异常就整体回滚。
//   另外，为了能看到事务到底有没有在工作，请打开相关的底层日志（日志级别配在配置文件里）。
//
// 完成以下操作：
// 1. 改造后的 save 方法（完整写一遍）写在下面
// 2. 配置文件里要加的内容写在下面（yml 片段）
// 3. 写完后回答：这个"东西"为什么推荐加在业务层的方法上，而不是控制层或数据访问层？
// ==========================================================================

// 在下面写你的代码：

// ① 改造后的业务层方法：


// ② application.yml 里要加的配置：


// ③ 第 3 步的回答：
//
//


// ==========================================================================
// 题目2-3：把"为什么要事务"和四大特性讲清楚
// ==========================================================================
// 需求：
//   有人问你三个问题：
//   ① 为什么"保存员工信息成功了、保存工作经历失败了"这件事不能忍？
//   ② MySQL 不是有事务吗，为什么代码里还会出现这种不一致？
//   ③ 事务的四大特性分别是什么、各自解决了什么问题？
//   请写一段话回答清楚，并用"新增员工"这个案例把四条特性各举一次。
//
// 完成以下操作：
// 1. 在下面写出回答（可以配 SQL 或例子）
// 2. 动手做一次对照：不开事务时故意让第二步失败，把查库结果记到下面
// ==========================================================================

// 在下面写你的回答：
// ①
//
//
// ②
//
//
// ③
//
//
//

// 第 2 步的记录（不开事务、第二步失败的查库结果）：
// emp 表：
// emp_expr 表：
