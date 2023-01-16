import yaml
from utils import FuckPupedu

with open('config.yml', 'r') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    fucker = FuckPupedu(cfg)
    
fucker.login()
fucker.learn()