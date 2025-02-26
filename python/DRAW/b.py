import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_pig_head(ax):
    # 设置颜色
    pink = '#FFC0CB'
    dark_pink = '#FFB6C1'
    black = '#000000'
    white = '#FFFFFF'
    
    # 画头部（圆形）
    head = patches.Ellipse((0.5, 0.5), 0.7,0.6, facecolor=pink, edgecolor=black, linewidth=2)
    ax.add_patch(head)
    
    # 画左耳朵
    left_ear = patches.Ellipse((0.3, 0.75), 0.1, 0.15, angle=120, facecolor=dark_pink, edgecolor=black, linewidth=2)
    ax.add_patch(left_ear)
    
    # 画右耳朵
    right_ear = patches.Ellipse((0.7, 0.75), 0.1, 0.15, angle=-120, facecolor=dark_pink, edgecolor=black, linewidth=2)
    ax.add_patch(right_ear)
    
    # 画左眼睛
    left_eye = patches.Ellipse((0.4, 0.6), 0.04,0.06, facecolor=black)
    ax.add_patch(left_eye)
    
    # 画右眼睛
    right_eye = patches.Ellipse((0.6, 0.6),0.04,0.06, facecolor=black)
    ax.add_patch(right_eye)
    
    # 画鼻子
    nose = patches.Ellipse((0.5, 0.45), 0.2, 0.15, facecolor=black)
    ax.add_patch(nose)
    
    # 画鼻孔
    nostril1 = patches.Circle((0.48, 0.455), 0.01, facecolor=white)
    nostril2 = patches.Circle((0.52, 0.455), 0.01, facecolor=white)
    ax.add_patch(nostril1)
    ax.add_patch(nostril2)
    
    # 画微笑
    smile = patches.Arc((0.5, 0.35), 0.15, 0.1, angle=0, theta1=200, theta2=340, edgecolor=black, linewidth=2)
    ax.add_patch(smile)

def main():
    # 创建绘图
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # 绘制小猪头部
    draw_pig_head(ax)
    
    # 设置坐标范围
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # 隐藏坐标轴
    ax.axis('off')
    
    # 添加文本
    # 设置字体属性，确保字体支持中文
    plt.text(0.5, 0.1, "姝洁天天开心！", fontsize=26, fontproperties='SimHei',
             ha='center', va='center', color='black')
    
    # 显示绘图
    plt.show()

if __name__ == "__main__":
    main()
