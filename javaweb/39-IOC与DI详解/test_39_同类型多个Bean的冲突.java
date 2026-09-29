// ============================================
// 题目2-3：两个同类型的 bean 打起来了，给三个解决方案
// ============================================
// 工程里有一个业务接口 UserService，现在有两个实现类都交给了容器：
//
//     @Service
//     public class UserServiceImpl implements UserService { /* …… */ }
//
//     @Service
//     public class UserServiceImpl2 implements UserService { /* …… */ }
//
// 控制层里是这么写的：
//
//     @RestController
//     public class UserController {
//         @Autowired
//         private UserService userService;
//         // ……
//     }
//
// 启动工程时直接失败，报错里最关键的一句是：
//
//     Field userService in com.itheima.controller.UserController required a single bean,
//     but 2 were found:
//         - userServiceImpl: defined in URL [...]
//         - userServiceImpl2: defined in URL [...]
//
// 完成以下操作：
// 1. 解释这句报错为什么会发生（说清"注入规则 + 有几个候选"）
// 2. 写出三种能让工程正常启动的改法（说明改哪里、改什么），
//    并分别写清"最后注入的是哪一个"
// 3. 回答：如果不改代码，有没有办法让"消费者接受多个 bean"？
//    写出一种写法（提示：注入时把类型写成集合或 Map）
// 4. 回答：怎么用"数据特征"一眼看出注入的到底是哪一个实现？
// ============================================

// 在下面写你的代码：

// 第 1 步：报错原因
// 

// 第 2 步：三种改法
// 方案一：
// 方案二：
// 方案三：

// 第 3 步：接受多个 bean 的写法（写在下面）
package com.itheima.controller;

public class UserController {

    // 在这里写"接受多个 bean"的成员变量声明

}

// 第 4 步：怎么用数据特征判断注入了哪一个
// 
