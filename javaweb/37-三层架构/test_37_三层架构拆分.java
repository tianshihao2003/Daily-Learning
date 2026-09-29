// ============================================
// 题目2-1：把"全塞在 Controller 里"的代码拆成三层
// ============================================
// 下面这个类能跑，但所有事都挤在一个方法里：
//
//     @RestController
//     public class UserController {
//         @RequestMapping("/list")
//         public List<User> list() throws Exception {
//             // 1. 读文件
//             InputStream in = this.getClass().getClassLoader().getResourceAsStream("user.txt");
//             ArrayList<String> lines = IoUtil.readLines(in, StandardCharsets.UTF_8, new ArrayList<>());
//             // 2. 解析封装
//             List<User> userList = lines.stream().map(line -> {
//                 String[] parts = line.split(",");
//                 Integer id = Integer.parseInt(parts[0]);
//                 String username = parts[1];
//                 String password = parts[2];
//                 String name = parts[3];
//                 Integer age = Integer.parseInt(parts[4]);
//                 LocalDateTime updateTime = LocalDateTime.parse(parts[5],
//                         DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
//                 return new User(id, username, password, name, age, updateTime);
//             }).collect(Collectors.toList());
//             // 3. 响应数据
//             return userList;
//         }
//     }
//
// 完成以下操作：
// 1. 拆出数据访问层：一个接口 + 一个实现类（包名 com.itheima.dao 与
//    com.itheima.dao.impl），接口里定义"取数据"的方法，实现类里只保留"读文件"
// 2. 拆出业务逻辑层：一个接口 + 一个实现类（包名 com.itheima.service 与
//    com.itheima.service.impl），实现类里调 dao 拿数据、做解析封装，
//    返回用户对象集合
// 3. 控制层只留下"接收请求、响应数据"（读文件和解析的代码一行都不许剩）
// 4. 每个 package 声明上面用一行中文注释写清：这是哪一层、职责是什么
// 5. 拆完在文件末尾回答：对外接口（访问路径、返回内容）有没有变？为什么？
// ============================================

// 在下面写你的代码：

// ========== 数据访问层（接口） ==========
// package com.itheima.dao;


// ========== 数据访问层（实现类） ==========
// package com.itheima.dao.impl;


// ========== 业务逻辑层（接口） ==========
// package com.itheima.service;


// ========== 业务逻辑层（实现类） ==========
// package com.itheima.service.impl;


// ========== 控制层 ==========
// package com.itheima.controller;


// 第 5 步的回答：
// 对外接口有没有变：
// 为什么：
