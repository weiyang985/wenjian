
# 1. 导入工具
import tkinter as tk   # tkinter是Python自带的窗口工具，用来画界面
import random          # random用来生成随机数，比如随机颜色、随机位置

# 2. 定义话语内容
# 话语
care_messages = [
    "今天的你也在努力呢，辛苦了",      # 第1句话
    "记得多喝水，对身体好",             # 第2句话
    "累了就休息，别太勉强自己",         # 第3句话
    # ... 无穷的话，无尽
    "你已经很棒了，给自己一个拥抱吧",
    "无论发生什么，我都在这里",
    "希望你今天心情美美的",
    "要好好照顾自己哦",
    "你值得拥有最好的",
    "想对你说：你真的很了不起",
    "辛苦了，好好休息一下",
    "愿你被这个世界温柔以待",
    "相信自己，你可以的",
    "有你的日子真好",
    "你是我心中最重要的人",
    "愿你每天都充满阳光",
    "要记得按时吃饭呀",
    "再忙也要照顾好自己",
    "你笑起来真好看",
    "我一直都在想你",
    "你是我最珍贵的宝贝",
    "愿你被爱包围",
    "有我在，你不会孤单",
    "你是我生命中的光",
    "愿你的所有美好都如约而至",
    "我为你骄傲",
    "你值得被好好疼爱",
    "每天都在心里默默关心你",
    "愿你所有的心愿都能实现",
    "你是我最想守护的人",
    "天冷了，记得加衣服",
    "别忘了给自己一个小奖励",
    "你做的事情很有意义",
    "希望你的每一天都顺顺利利",
    "不要太在意别人的看法，你已经很好了",
    "累了就抬头看看天空吧",
    "你是我见过最努力的人",
    "愿你的烦恼都能随风飘散",
    "记得微笑哦，你笑起来很温暖",
    "我希望你知道，有人一直在乎你",
    "不管多晚，我都会等你",
    "你是我生命中最美的遇见",
    "愿你的生活永远甜甜蜜蜜",
    "有困难记得说出来，我一直都在",
    "你比你自己想象的更强大",
    "好好睡一觉，明天又是新的开始",
    "我永远相信你",
    "你是我最想见到的人",
    "不管发生什么，你都不是一个人",
    "愿你被幸福围绕",
    "记得吃早餐，一天都要精神满满",
    "你值得被珍惜",
    "愿你的努力都有回报",
    "希望今天有好事发生在你身上",
    "你是我最想保护的人",
    "每一天都要好好爱自己",
    "愿你永远保持这份善良",
    "我会一直支持你的决定",
    "你是我最牵挂的人",
    "希望你今天遇到的所有人都是温柔的",
    "别忘了，你对我来说很特别",
    "愿你拥有美好的一天",
    "记得偶尔也要偷懒放松一下",
    "有你在身边真好",
    "你的努力我看得到",
    "愿你永远被温柔以待",
    "你是我最想珍惜的缘分",
    "希望你的眼睛永远明亮",
    "别忘了多看看窗外的风景",
    "你是我心里最柔软的地方",
    "愿你的梦里都是美好的事情",
    "我会一直陪着你走下去",
    "你是我最想拥抱的人",
    "希望你今天比昨天更开心",
    "你做的事情很有价值",
    "愿你永远保持热爱",
]

# 3. 定义颜色
# 标签的背景颜色，可以换
bg_colors = [
    "#FFB6C1",  # 浅粉色
    "#FFC0CB",  # 粉色
    "#FF69B4",  # 热粉色
    "#FF1493",  # 深粉色
    "#FF6B6B",  # 珊瑚红
    "#FFE4E1",  # 薄雾玫瑰
    "#FFF0F5",  # 薰衣草腮红
    "#FFE4B5",  # 杏仁饼
    "#FFDAB9",  # 桃子
    "#F5F5DC",  # 米色
    "#E6E6FA",  # 淡紫色
    "#F0FFF0",  # 薄荷糖
    "#FDFD96",  # 柠檬
    "#F0E68C",  # 卡其布
    "#E0FFFF",  # 淡青色
    "#BDFCC9",  # 淡绿色
    "#C9C9FF",  # 淡蓝色
    "#FFC9C9",  # 浅红色
    "#C9FFC9",  # 浅绿色
    "#FFFFC9",  # 浅黄色
    "#FFD700",  # 金色
    "#FFA07A",  # 浅鲑鱼色
    "#98FB98",  # 浅绿色
    "#DDA0DD",  # 梅红色
]

#  漂浮标签类，这个类负责创建一个会飘动的小标签
class FloatingLabel:
    """
    作用：创建一个会移动的小标签
    - 它会自己慢慢飘动
    - 有自己的位置(x,y坐标)
    - 有自己的移动速度(dx,dy)
    """
    
    def __init__(self, parent, text, x, y):
        """
        初始化：创建一个新的漂浮标签
        参数说明：
        - parent: 父窗口，就是把它放在哪个窗口里
        - text: 显示的文字内容
        - x: 初始位置的X坐标（水平方向）
        - y: 初始位置的Y坐标（垂直方向）
        """
        self.parent = parent  # 保存父窗口
        self.text = text      # 保存文字
        self.x = x            # 当前位置X
        self.y = y            # 当前位置Y
        # ---------- 移动速度 ----------
        # dx: X方向速度，正数往右，负数往左
        # dy: Y方向速度，正数往下，负数往上
        self.dx = random.choice([-3, -2.5, -2, 2, 2.5, 3])
        self.dy = random.choice([-2.5, -2, -1.5, 1.5, 2, 2.5])
        
        # ddx, ddy: 加速/减速，让移动更自然
        self.ddx = random.choice([-0.08, 0, 0.08])
        self.ddy = random.choice([-0.08, 0, 0.08])
        
        # ---------- 创建标签 ----------
        self.label = tk.Label(
            parent,
            text=text,                           # 显示的文字
            font=("Microsoft YaHei", random.randint(10, 15)),  # 字体和大小
            fg=random.choice(["#333333", "#444444", "#555555", "#DC143C", "#FF69B4", "#FF1493", "#8B4513"]),  # 文字颜色
            bg=random.choice(bg_colors),          # 背景颜色
            padx=15,                             # 左右内边距
            pady=8,                              # 上下内边距
            bd=0,                                # 边框宽度
            highlightthickness=0,               # 高亮边框
            relief="flat",                       # 扁平样式
            wraplength=200                       # 超过200字宽就换行
        )
        self.label.place(x=x, y=y)  # 放到指定位置
        
        # 绑定鼠标事件
        # 鼠标右键点击：删除这个标签
        self.label.bind("<Button-3>", self.on_right_click)
        # 鼠标左键点击：更换文字
        self.label.bind("<Button-1>", self.on_click)
    
    #  鼠标右键发生？
    def on_right_click(self, event):
        """右键点击时，删除这个标签"""
        self.remove()
    
    # -鼠标左键事件
    def on_click(self, event):
        """左键点击时，随机换一句话"""
        self.label.config(text=random.choice(care_messages))
    
    #  删除标签
    def remove(self):
        """销毁这个标签"""
        self.label.destroy()
    
    # 更新位置
    def update_pos(self, screen_w, screen_h):
        """
        更新标签的位置（让它移动）
        
        参数：
        - screen_w: 屏幕宽度
        - screen_h: 屏幕高度
        """
        # 当前位置 + 速度 = 新位置
        self.x += self.dx
        self.y += self.dy
        
        #  边界检测
        # 如果碰到屏幕边缘，就反弹（改变方向）
        if self.x <= 5 or self.x >= screen_w - 180:
            self.dx = -self.dx  # 反方向
            self.ddx = random.choice([-0.08, 0.08])  # 随机改变加速度
        
        if self.y <= 50 or self.y >= screen_h - 80:
            self.dy = -self.dy  # 反方向
            self.ddy = random.choice([-0.08, 0.08])
        
        # 第二行是限制速度
        self.dx += self.ddx
        self.dy += self.ddy
        
        # 限制最大速度，避免速度不太合理
        self.dx = max(-5, min(5, self.dx))
        self.dy = max(-5, min(5, self.dy))
        
        # 更新标签的实际位置
        self.label.place(x=int(self.x), y=int(self.y))


# 5. 主程序类
class DesktopLoveApp:
    """
    主程序类 - 管理整个应用
    
    负责：
    - 创建窗口
    - 创建所有漂浮标签
    - 控制动画循环
    """
    
    def __init__(self):
        """
        初始化：创建整个应用
        """
        #创建主窗口
        self.root = tk.Tk()  # 创建一个窗口
        self.root.title("Desktop Love")  # 窗口标题
        self.root.attributes('-topmost', True)  # 永远会在最前面
        self.root.attributes('-transparentcolor', 'white')  # 白色变透明
        self.root.configure(bg='white')  # 背景设为白色（会变透明）
        self.root.overrideredirect(True)  # 去掉窗口边框（最大化、最小化那些按钮）
        
        # 获取屏幕大小
        screen_w = self.root.winfo_screenwidth()   # 屏幕宽度
        screen_h = self.root.winfo_screenheight()  # 屏幕高度
        
        # 设置窗口大小覆盖整个屏幕
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        
        #初始化变量
        self.labels = []  # 存放所有漂浮标签的列表
        self.running = True  # 控制程序是否运行
        
        # 创建初始标签
        # 一次创建35-50个标签
        for _ in range(random.randint(35, 50)):
            self.create_random_label()
        
        # 绑定快捷键
        # ESC键：退出程序
        self.root.bind("<Escape>", lambda e: self.close())
        # 鼠标右键（空白处）：退出程序
        self.root.bind("<Button-3>", lambda e: self.close())
        # F5键：刷新标签（重新生成）
        self.root.bind("<F5>", lambda e: self.refresh_labels())
        
        #开始动画
        self.animate()
        
        # 运行程序
        self.root.mainloop()
    
    #创建随机标签
    def create_random_label(self):
        """
        在随机位置创建一个新的漂浮标签
        """
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # 随机位置（留一些边距）
        x = random.randint(30, screen_w - 220)
        y = random.randint(60, screen_h - 100)
        
        # 随机选一句话
        text = random.choice(care_messages)
        
        # 创建标签并添加到列表
        label = FloatingLabel(self.root, text, x, y)
        self.labels.append(label)
    
    # 删除随机标签
    def remove_random_label(self):
        """随机删除一个标签（保持数量平衡）"""
        if self.labels:  # 如果还有标签
            label = random.choice(self.labels)  # 随机选一个
            label.remove()  # 删除它
            self.labels.remove(label)  # 从列表中也移除
    
    #刷新所有标签
    def refresh_labels(self):
        """
        删除所有旧标签，重新创建新的
        """
        # 先删除所有旧的
        for label in self.labels[:]:  # [:]是复制一份，避免边删边遍历出问题
            label.remove()
        self.labels.clear()  # 清空列表
        
        # 再创建新的
        for _ in range(random.randint(35, 50)):
            self.create_random_label()
    
    #动画循环
    def animate(self):
        """
        不断更新所有标签的位置
        就像动画片一样，每隔一小会儿更新一次
        """
        if not self.running:  # 如果程序不运行了，就停止
            return
        
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # 更新每个标签的位置
        for label in self.labels:
            label.update_pos(screen_w, screen_h)
        
        # 随机添加新标签（0.8%的概率）
        if random.random() < 0.008:
            self.create_random_label()
        
        # 随机删除标签（0.3%的概率，但至少保留30个）
        if random.random() < 0.003 and len(self.labels) > 30:
            self.remove_random_label()
        
        # 35毫秒后再执行一次（每秒钟约28次）
        self.root.after(20, self.animate)
    
    # 关闭程序
    def close(self):
        """关闭程序"""
        self.running = False  # 停止动画
        self.root.destroy()   # 关闭窗口


# 6. 程序入口
if __name__ == "__main__":
    # 如果直接运行这个文件，就启动程序
    DesktopLoveApp()

# 代码框架总结
"""
整个程序的框架：

1. 导入工具
   import tkinter as tk   → 画窗口的库
   import random          → 生成随机数

2. 准备数据
   care_messages = [...] → 所有要说的话
   bg_colors = [...]     → 所有背景颜色

3. 定义FloatingLabel类（漂浮标签）
   - 创建一个会动的小标签
   - 记录位置、速度
   - 左键换文字，右键删除
   - 碰到边会反弹

4. 定义DesktopLoveApp类（主程序）
   - 创建透明窗口
   - 生成35-50个漂浮标签
   - 不断更新位置（动画）
   - 随机添加/删除标签

5. 启动程序
   if __name__ == "__main__":
       DesktopLoveApp()

操作说明：
- ESC键 / 右键点击空白处：退出程序
- 左键点击标签：换一句话
- 右键点击标签：删除那个标签
- F5键：重新生成所有标签
"""
