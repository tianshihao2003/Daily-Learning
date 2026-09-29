// ============================================
// 题目2-3：写一个只依赖 test 范围 jar 的测试类
// ============================================
// 被测的 UserService 有两个方法：
//     public Integer getAge(String idCard)     —— 返回年龄
//     public String  getGender(String idCard)  —— 返回"男"/"女"
//
// 要求：
// 1. 类名按命名规范起，类里写两个测试方法：
//    一个测 getAge("100000200010011011") 返回 25，一个测 getGender("100000200010011011") 返回 "男"
//    （都要用断言，断言要带提示信息）
// 2. 在文件末尾的注释里回答两个问题：
//    ① 这个类的代码放在哪个目录（src/main/java 还是 src/test/java）？
//    ② 如果把 pom 里 junit 的 <scope>test</scope> 改成 <scope>runtime</scope>，
//       这个测试类还能编译/运行吗？为什么？
// ============================================

// 在下面写你的代码：

package com.itheima;

public class UserServiceTest {

    // 在这里写两个测试方法

}

// 下面写你的回答：
// ①
// ②
