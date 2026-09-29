// ============================================
// 综合题：给 UserService 写一个"带全套注解和断言"的测试类
// ============================================
// 被测的 UserService 有两个方法：
//     public Integer getAge(String idCard)     —— 返回年龄
//     public String  getGender(String idCard)  —— 返回"男"/"女"，身份证不合法时抛 IllegalArgumentException
//
// 要求（按步骤做）：
// 1. 用 @DisplayName 给测试类起一个中文名
// 2. 用 @BeforeEach 统一创建被测对象（而不是每个测试方法里各 new 一次）
// 3. 写两个测试方法，分别断言：
//    getAge("100000200010011011") 返回 25、getGender("100000200010011011") 返回 "男"（断言都要带 msg）
// 4. 再加一个测试方法，断言"传入不合法的身份证号（比如 "123" 或 null）会抛 IllegalArgumentException"
// 5. 再加一个参数化测试，用 @ValueSource 传 3 个男性身份证号，断言性别都是"男"
// 6. 运行整个测试类，把 Tests run / Failures / Errors 那一行抄下来；
//    然后故意把第 3 步里年龄的预期值改成 100，再跑一次，
//    把失败输出里 expected: ... but was: ... 那一行、以及指到你代码的行号记下来
// ============================================

// 在下面写你的代码：

package com.itheima;

public class UserServiceFullTest {

    // 在这里写测试类

}

// 第 6 步：两次运行的结果抄在这里
// 全部通过时：
// 故意写错预期后：

// 失败输出里的关键两行：
