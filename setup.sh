pip install -r requirements.txt
touch config.yml
echo "# 请在下方填写你的学号和密码"  > config.yml
echo "ID:                # 学号" >> config.yml
echo "PASSWORD:          # 密码" >> config.yml

echo "# 以下为可选项" >> config.yml
echo "START_CHAPTER: 1   # 从第几讲开始" >> config.yml
echo "START_TITLE:   1   # 从这一讲的第几个视频开始" >> config.yml