// ============================================
// 题目2-2：把 user.txt 的一行解析成对象
// ============================================
// 给定 user.txt 里的第一行文本：
//     1,daqiao,1234567890,大乔,22,2024-07-15 15:05:45
//
// 实体类 com.itheima.pojo.User 的 6 个属性，顺序和上面 6 段一一对应：
//     Integer id、String username、String password、String name、
//     Integer age、java.time.LocalDateTime updateTime
//
// 完成以下操作：
// 1. 把这一行文本切成 6 段
// 2. 按实体类每个属性的类型做转换（该是数字的转数字，该是时间的转时间，
//    时间字符串的格式要和文本完全一致）
// 3. 用全参构造方法组装成一个 User 对象
// 4. 把对象打印出来，确认 6 个属性都有值
//    （打印出来的时间字段形如 2024-07-15T15:05）
// ============================================

// 在下面写你的代码：

package com.itheima;

public class ParseLineTest {

    public static void main(String[] args) {
        String line = "1,daqiao,1234567890,大乔,22,2024-07-15 15:05:45";

        // 在这里写你的解析代码

    }
}
