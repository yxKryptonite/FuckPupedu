import yaml
from utils import FuckPupedu
from configargparse import ArgumentParser

# 学习任务种类, learn_type = [VIDEO, TEST, NOTES, PPT]
parser = ArgumentParser()
parser.add_argument("-d", "--DEBUG", action="store_true", help="debug mode")
parser.add_argument("-v", "--DO_VIDEO", action="store_true", help="learn videos")
parser.add_argument("-t", "--DO_TEST", action="store_true", help="do test")
parser.add_argument("-n", "--DO_NOTES", action="store_true", help="take notes")
parser.add_argument("-p", "--DO_PPT", action="store_true", help="learn ppt")
args = vars(parser.parse_args())

LOGIN_URL      = "http://www.pupedu.cn/app/login/login.do"
COURSE_NAME    = "北京大学新时代劳动教育理论课 - 北京大学 - BJDX000100"
    
def main():
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        cfg = {**cfg, **args} # merge `args` into `cfg`
        fucker = FuckPupedu(cfg)
    
    if fucker.login(LOGIN_URL):
        print("========= 登录成功 =========")
    else:
        print("========= 登录失败 =========")
        return
            
    if not fucker.get_into_course(COURSE_NAME):
        print("========= 进入课程失败 =========")
        return
        
    if args["DO_VIDEO"]:
        print("========= 视频学习 =========")
        fucker.learn("VIDEO")
    if args["DO_PPT"]:
        print("========= PPT学习 =========")
        fucker.learn("PPT")
    if args["DO_NOTES"]:
        print("========= 记笔记 =========")
        fucker.learn("NOTES")
    if args["DO_TEST"]:
        print("========= 做测验 =========")
        fucker.learn("TEST")
    

if __name__ == "__main__":
    print("========= 程序开始 =========")
    main()
    print("========= 程序结束 =========")