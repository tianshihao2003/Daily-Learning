// ============================================
// 题目2-2：给三层加上 IOC/DI 改造
// ============================================
// 下面是一个能跑的三层工程（依赖全是自己创建的）：
//
//     // dao 层实现类
//     public class UserDaoImpl implements UserDao {
//         @Override
//         public List<String> list() {
//             InputStream in = this.getClass().getClassLoader().getResourceAsStream("user.txt");
//             return IoUtil.readUtf8Lines(in, new ArrayList<>());
//         }
//     }
//
//     // service 层实现类
//     public class UserServiceImpl implements UserService {
//         private UserDao userDao = new UserDaoImpl();
//         @Override
//         public List<User> list() {
//             List<String> lines = userDao.list();
//             return lines.stream().map(line -> { /* 解析封装…… */ }).toList();
//         }
//     }
//
//     // controller
//     @RestController
//     public class UserController {
//         private UserService userService = new UserServiceImpl();
//         @RequestMapping("/list")
//         public List<User> list() {
//             return userService.list();
//         }
//     }
//
// 完成以下操作：
// 1. 让数据访问层、业务逻辑层的实现类都交给容器管理（注解加在类的什么位置？）
// 2. 让控制层需要业务对象、业务层需要数据访问对象时，都不再自己创建，
//    改成由容器把对象送进来
// 3. 每处改动旁边写中文注释，说明"这一行原来是谁干的、现在谁来干"
// 4. 在文件末尾回答两个问题：
//    ① 容器是在什么时候把依赖送进来的？（启动时还是每次请求时）
//    ② 改造后 UserController 里还剩几个 new？
// ============================================

// 在下面写你的代码：

// ========== dao 层实现类 ==========
// package com.itheima.dao.impl;


// ========== service 层实现类 ==========
// package com.itheima.service.impl;


// ========== 控制层 ==========
// package com.itheima.controller;

public class UserController {

    // 在这里写成员变量与查询方法

}

// 第 4 步的回答：
// ① 
// ② 
