// ==========================================================================
// 素材（不用改，照着理解即可）
// ==========================================================================
// 工程：tlias-web-management（SpringBoot 3.2 + MyBatis + Lombok）
//   pom.xml 里已经有 lombok 依赖（所以 Lombok 的注解可以直接用）
//   Logback 的依赖由 SpringBoot 的起步依赖传递进来（不用自己加）
//   工程里已经有 DeptController / DeptService / DeptMapper 的部门管理接口
//   日志配置见同一个练习目录下的 test_63_logback配置.xml（配好后放进 src/main/resources）
//
// 现成的类（直接用，不用自己写）：
//   com.itheima.pojo.Dept    ：属性 id / name / createTime / updateTime（Lombok 的 @Data，toString 会打印全部属性）
//   com.itheima.pojo.Result  ：静态方法 Result.success()、Result.success(Object)、Result.error(String)
//
// 相关的接口（Controller 里已有的方法）：
//   GET    /depts        查询全部部门      list()
//   DELETE /depts?id=8   根据ID删除部门    delete(Integer id)
//   POST   /depts        新增部门          add(Dept dept)
//   GET    /depts/{id}   根据ID查询部门    getInfo(Integer id)
//   PUT    /depts        修改部门          update(Dept dept)
// ==========================================================================


// ==========================================================================
// 题目2-3：用日志替换 Controller 里的打印
// ==========================================================================
// 素材（现在这个 Controller 用 System.out.println 打印，而且没有 Logger）：
//
//   @RestController
//   @RequestMapping("/depts")
//   public class DeptController {
//       @Autowired
//       private DeptService deptService;
//
//       @DeleteMapping
//       public Result delete(Integer id){
//           System.out.println("根据ID删除部门: " + id);   // <- 改成日志
//           deptService.deleteById(id);
//           return Result.success();
//       }
//
//       @PostMapping
//       public Result add(@RequestBody Dept dept){
//           // <- 在这里补一行日志（把整个部门对象记录下来）
//           deptService.add(dept);
//           return Result.success();
//       }
//   }
//
// 需求：
//   1. 用一个 Lombok 注解让类里自动拥有 Logger 对象（不要手写 LoggerFactory.getLogger(...) 那一行）；
//   2. 把删除接口里的打印改成日志，并且用占位符代替字符串拼接；
//   3. 给新增接口补一行日志，把整个部门对象传给占位符（跑起来看看对象被打印成什么样）；
//   4. 回答：日志写法比 System.out.println("根据ID删除部门: " + id) 好在哪三点？
//
// 完成以下操作：
// 1. 类上加注解
// 2. 两处语句改成日志（注意参数怎么传给占位符）
// 3. 启动应用，调一次新增和一次删除接口，把控制台输出抄到下面
// 4. 回答第 4 问
// ==========================================================================

// 在下面写你的代码：



// 第 3 步的记录（控制台输出，把带时间与类名的那一整行抄下来）：
//

// 第 4 步的回答：
// ①
//
// ②
//
// ③
//


// ==========================================================================
// 综合题：给 Tlias 案例接上日志，并把级别开关做一遍（代码部分）
// ==========================================================================
// 目标：把 DeptController 里所有的 System.out.println 都换成日志，
//       让它配合 test_63_logback配置.xml 的那份配置，在控制台和文件里都留下记录。
//
// 完成以下操作：
// 1. 类上加 Lombok 注解生成 Logger（原来手写 Logger 的那行不用写）；
// 2. 把五个方法（查询全部、删除、新增、根据ID查询、修改）里所有的打印都换成日志：
//    - 有参数的用占位符写法（消息里留出空位、参数从后面传进去）
//    - 整个对象也可以直接当参数传给占位符
//    - 原来那些 println 注释掉留在源码里，方便对照
// 3. 启动应用，依次调用五个接口，抄三条控制台日志到下面；
// 4. 按 test_63_logback配置.xml 里的第 5 步，把总开关改成 WARN 重启再调一遍，
//    记录控制台还剩几条日志、为什么；
// 5. 回答：一行日志里的"时间""哪个请求线程""哪个类""干了什么"，
//    分别对应日志格式里的哪个占位符？
// ==========================================================================

// 在下面写你的代码：



// 第 3 步的记录（三条控制台日志）：
//

// 第 4 步的记录与回答（改成 WARN 后剩几条、为什么）：
//

// 第 5 步的回答（时间 / 线程 / 类 / 消息 分别对应哪个占位符）：
//
