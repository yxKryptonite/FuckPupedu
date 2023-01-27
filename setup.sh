pip install -r requirements.txt
touch config.yml
echo "# 请在下方填写你的学号和密码
ID:                    # 学号
PASSWORD:              # 密码

# 以下为可选项
# 视频选项
VIDEO:
    NAME:          视频  
    START_CHAPTER: 1   # 从第几讲开始
    START_TITLE:   1   # 从这一讲的第几个视频开始

# PPT选项
PPT:
    NAME:          PPT
    START_CHAPTER: 1   # 从第几讲开始
    START_TITLE:   1   # 无需更改

# 笔记选项
NOTES:
    NAME:          笔记
    START_CHAPTER: 1   # 从第几讲开始
    START_TITLE:   1   # 无需更改
    MY_NOTES:      马克思主义理论将劳动问题进行哲学化、理论化、思想化的探讨和研究。   # 笔记内容

# 测验选项
TEST:
    NAME:          测验
    START_CHAPTER: 1   # 从第几讲开始
    START_TITLE:   1   # 无需更改" > config.yml
