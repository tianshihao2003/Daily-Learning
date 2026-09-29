// ============================================================
// test_104_登录退出与令牌.js
// 第 104 篇《登录退出与令牌管理》练习文件（一）
// 用法：每道题的要求写在注释块里，素材用
//       "// ---- 素材开始 ----" / "// ---- 素材结束 ----" 圈出来，
//       在"在下面写你的代码"的空白处作答。
// 本文件写的是"登录页 + 布局顶栏"这两处的逻辑代码（不是拦截器，
// 拦截器在 test_104_拦截器.js 里）。
// ============================================================


// ============================================================
// 题目1：让登录按钮真的登录（src/views/login/index.vue）
// ============================================================
// 需求：
//   1. 页面上有"用户名""密码"两个输入框和一个"登 录"按钮、一个"重 置"按钮；
//   2. 点"登 录"把两个输入框里的内容发给后端的登录接口；
//      成功 → 提示"登录成功" + 把返回的那份登录信息存起来 + 跳到首页；
//      失败 → 把后端给的失败原因弹出来，人留在登录页；
//   3. 点"重 置"把两个输入框清空；
//   4. 两个输入框的内容要装在一个对象里（双向绑定）。
//
// 素材（登录接口 + 页面骨架）：
//
// ---- 素材开始 ----
// POST /login        请求体：{ "username": "用户名", "password": "密码" }
// 响应：{ "code": 1, "msg": "success",
//         "data": { "id": 1, "username": "shinaian", "name": "施耐庵", "token": "eyJh..." } }
// （code=1 成功、0 失败；失败时 msg 里有原因）
//
// 界面骨架：
//   <el-form label-width="80px">
//     <p class="title">Tlias智能学习辅助系统</p>
//     <el-form-item label="用户名"><el-input v-model="____" placeholder="请输入用户名"></el-input></el-form-item>
//     <el-form-item label="密码"><el-input type="password" v-model="____" placeholder="请输入密码"></el-input></el-form-item>
//     <el-form-item>
//       <el-button class="button" type="primary" @click="____">登 录</el-button>
//       <el-button class="button" type="info" @click="____">重 置</el-button>
//     </el-form-item>
//   </el-form>
//
// 可用的工具：
//   import { ElMessage } from 'element-plus'          // 顶部消息提示
//   import { useRouter } from 'vue-router'            // 组合式 API 里拿路由对象
//   import { loginApi } from '@/api/login'            // 已经封装好的登录请求
// ---- 素材结束 ----
//
// 检查点：① 两个框里打字点"重 置"立刻变空；
//         ② 账号密码正确 → 顶部提示"登录成功"、地址变成首页；
//         ③ 密码填错 → 弹出后端返回的原因、停在登录页；
//         ④ 登录请求是 POST /login、请求体是 {"username": "...", "password": "..."}。
//
// 在下面写你的代码：




// ============================================================
// 题目2：把登录信息（含令牌）存到浏览器本地，并用一遍四个 API
// ============================================================
// 需求：
//   1. 登录成功之后，把后端返回的那份登录信息（id、用户名、姓名、令牌）
//      存到浏览器本地存储里，键名用 loginUser；
//   2. 存进去之后要能在别的地方读出来一个"对象"（不是一坨字符串）；
//   3. 写一个"取出当前登录信息"的小函数（没有存过时返回 null，不报错）；
//   4. 再写一个"清掉登录信息"的小函数；
//   5. 最后把本地存储的四个 API 各写一行示例：存一条、读一条、删一条、清空全部。
//
// 素材（要存的东西）：
//
// ---- 素材开始 ----
// 登录接口成功时的 data：
//   { "id": 1, "username": "shinaian", "name": "施耐庵", "token": "eyJhbGciOiJIUzI1NiJ9..." }
//
// 浏览器本地存储的四个方法（只认字符串）：
//   存：localStorage.setItem(key, value)
//   取：localStorage.getItem(key)          // 这个键不存在时得到 null
//   删：localStorage.removeItem(key)
//   清空：localStorage.clear()
// 对象与字符串互转：JSON.stringify(对象) / JSON.parse(字符串)
// ---- 素材结束 ----
//
// 检查点：① 登录后 F12 → Application → Local Storage 里能看到一条 loginUser；
//         ② 取出来的能直接 .name、.token 用；
//         ③ 不加 JSON.stringify 直接存对象会变成 [object Object]（能说清原因）；
//         ④ 刷新页面后这条记录还在。
//
// 在下面写你的代码：




// ============================================================
// 题目3：顶栏显示当前登录用户，并能退出登录（src/views/layout/index.vue）
// ============================================================
// 需求：
//   1. 主布局顶栏右侧要有"退出登录 【当前登录人的姓名】"，
//      姓名从本地存的那份登录信息里取（页面一加载就显示，不用等接口）；
//   2. 点"退出登录"先弹确认框：标题"提示"、内容"确认退出登录吗?"、
//      两个按钮"取消""确定"、带警告图标；
//   3. 点"确定"之后做三件事——提示"退出登录成功"、
//      把本地存的登录信息清掉、跳回登录页；
//   4. 点"取消"什么都不做。
//
// 素材（页面位置与可用工具）：
//
// ---- 素材开始 ----
// 顶栏右上角（src/views/layout/index.vue）：
//   <span class="right_tool">
//     <a href="">
//       <el-icon><EditPen /></el-icon> 修改密码 &nbsp;&nbsp;&nbsp; |  &nbsp;&nbsp;&nbsp;
//     </a>
//     <a href="javascript:void(0)" @click="____">
//       <el-icon><SwitchButton /></el-icon> 退出登录 【____】
//     </a>
//   </span>
//
// 本地存储里那条记录的键名是 loginUser，
// 值是 { id, username, name, token }（第 2 题存进去的）。
//
// 可用的工具：
//   import { ref, onMounted } from 'vue'
//   import { ElMessage, ElMessageBox } from 'element-plus'
//   import { useRouter } from 'vue-router'
//   ElMessageBox.confirm(内容, 标题, { confirmButtonText, cancelButtonText, type })
//   .then(() => { /* 点了确定 */ })
//   跳转：router.push('/login')
// ---- 素材结束 ----
//
// 检查点：① 登录后顶栏显示自己的姓名；
//         ② 点"退出登录"先弹确认框，点"取消"什么都不发生；
//         ③ 点"确定"→ 提示"退出登录成功"、地址变 /login、
//            F12 里 loginUser 不见了；
//         ④ 退出后再访问业务页面会被拦回登录页（本地没令牌了）。
//
// 在下面写你的代码：
