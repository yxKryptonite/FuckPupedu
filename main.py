import yaml
from fucker import FuckPupedu
from configargparse import ArgumentParser
from logger import Logger

# 学习任务种类, learn_type = [VIDEO, PPT, NOTES, TEST] # VPNT
parser = ArgumentParser()
parser.add_argument("-d", "--DEBUG", action="store_true", help="debug mode")
parser.add_argument("-v", "--DO_VIDEO", action="store_true", help="learn videos")
parser.add_argument("-p", "--DO_PPT", action="store_true", help="learn ppt")
parser.add_argument("-n", "--DO_NOTES", action="store_true", help="take notes")
parser.add_argument("-t", "--DO_TEST", action="store_true", help="do test")
args = vars(parser.parse_args())

LOGIN_URL      = "http://www.pupedu.cn/app/login/login.do"
COURSE_NAME    = "北京大学新时代劳动教育理论课 - 北京大学 - BJDX000100"
    
def main():
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        cfg = {**cfg, **args} # merge `args` into `cfg`
        Fucker = FuckPupedu(cfg)
    
    if Fucker.login(LOGIN_URL):
        Logger.log("登录成功")
    else:
        Logger.log("登录失败")
        return
            
    if not Fucker.get_into_course(COURSE_NAME):
        Logger.log("进入课程失败")
        return
        
    if args["DO_VIDEO"]:
        Logger.echo("========= 开始视频学习 =========")
        Fucker.learn("VIDEO")
    if args["DO_PPT"]:
        Logger.echo("========= 开始PPT学习 =========")
        Fucker.learn("PPT")
    if args["DO_NOTES"]:
        Logger.echo("========= 开始记笔记 =========")
        Fucker.learn("NOTES")
    if args["DO_TEST"]:
        Logger.echo("========= 开始做测验 =========")
        Fucker.learn("TEST")
    

if __name__ == "__main__":
    Logger.echo("========= 程序开始 =========")
    main()
    Logger.echo("========= 程序结束 =========")