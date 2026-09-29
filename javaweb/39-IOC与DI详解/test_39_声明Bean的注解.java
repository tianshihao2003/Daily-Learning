// ============================================
// 题目2-1：给三层的类挑"最贴切"的 bean 注解
// ============================================
// 三层架构工程里有三个类要交给 IOC 容器管理：
//     com.itheima.controller.EmpController        —— 控制层（处理请求、响应数据）
//     com.itheima.service.impl.EmpServiceImpl     —— 业务逻辑层
//     com.itheima.dao.impl.EmpDaoImpl             —— 数据访问层
//
// 完成以下操作：
// 1. 给每个类选一个"最贴切"的注解写在类上（不是全用同一个）
// 2. 说明控制层的类为什么必须用它选的那个注解（PPT 的"注意事项"里有）
// 3. 写出这三个类"默认的 bean 名字"分别是什么
// 4. 再把数据访问层的 bean 名字显式指定成 empDao，写出这一行代码
// ============================================

// 在下面写你的代码：

// ========== 控制层 ==========
// package com.itheima.controller;

public class EmpController {

    // 在这里补上类上的注解

}

// ========== 业务逻辑层 ==========
// package com.itheima.service.impl;

public class EmpServiceImpl {

    // 在这里补上类上的注解

}

// ========== 数据访问层 ==========
// package com.itheima.dao.impl;

public class EmpDaoImpl {

    // 在这里补上类上的注解（第 4 步要显式指定 bean 名字）

}

// 第 2 步的回答：
// 第 3 步的默认 bean 名字：
// EmpController  →
// EmpServiceImpl →
// EmpDaoImpl     →
