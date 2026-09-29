// ============================================
// 题目2-1：找出这几行代码里的耦合点
// ============================================
// 下面是一个三层架构工程的片段（拆过层，但依赖都是自己创建的）：
//
//     // 片段一
//     @RestController
//     public class UserController {
//         private UserService userService = new UserServiceImpl();
//         // ……
//     }
//
//     // 片段二
//     public class UserServiceImpl implements UserService {
//         private UserDao userDao = new UserDaoImpl();
//         // ……
//     }
//
// 完成以下操作：
// 1. 把两个片段里"层与层耦合"的那两行原样抄出来
// 2. 用"耦合/内聚"的话解释：这两行为什么算耦合
//    （说清"上层知道了什么本来不该它管的事"）
// 3. 假设新写了一个 UserServiceImpl2，想换掉原来的实现：
//    分别写出"改造前"和"把依赖交给容器后"各要改哪些地方
// 4. 把这两行改成"只留接口类型、由容器把对象送进来"的样子（注解可以先空着）
// ============================================

// 在下面写你的答案：

// 1. 两行耦合点：
//    

// 2. 为什么算耦合：
//    

// 3. 改造前要改：
//    依赖交给容器后要改：

// 4. 改完的样子：
// package com.itheima.controller;

public class UserController {

    // 在这里写成员变量声明

}

// package com.itheima.service.impl;

public class UserServiceImpl {

    // 在这里写成员变量声明

}
