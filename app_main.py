#
from apps.nup_app import NupApp
import sys
import getopt
import numpy as np
'''
from apps.ogml.ogml_app import OgmlApp
#from apps.tp.tp_app import TpApp
from apps.rxgb.rxgb_app import RxgbApp
from apps.asml.asml_app import AsmlApp
from apps.asdk.asdk_app import AsdkApp
from apps.tcv.tcv_app import TcvApp
from apps.fmml.fmml_app import FmmlApp
from apps.wxs.wxs_app import WxsApp
'''
from apps.nup_app import NupApp
from apps.sop.sop_app import SopApp
from apps.ots.ots_app import OtsApp
from apps.drl.drl_app import DrlApp
from biz.dct.dct_app import DctApp

# 启动命令行参数默认值
params = {
    'version': '0.0.1',
    'mode': '1',
    'exp': ''
}

def main(argv={}):
    # 解析命令行参数
    opts, args = getopt.getopt(argv, 'v:i', ['mode=', 'exp=']) # args是未加选项的字符串列表
    for opt, val in opts:
        if opt=='-i':
            print('易经量化交易平台')
        elif opt=='-v':
            params['version'] = val
        elif opt=='--mode':
            params['mode'] = val
        elif opt=='--exp':
            params['exp'] = val
    # 根据mode选项相应的应用
    if params['mode'] == 'ots':
        app = OtsApp()
    elif params['mode'] == 'drl':
        app = DrlApp()
    elif params['mode'] == 'dct':
        app = DctApp()
    else:
        app = NupApp()
    app.startup()

if '__main__' == __name__:
    '''
    命令行启动参数示例：python app_main.py -i -v 0.0.1 --mode iqt --exp tt a1 a2 a3
    '''
    argv = sys.argv[1:]
    main(argv)




def norm_batch_tasks(batch_vals, task_num):
    arrs = []
    batch_size = len(batch_vals) // task_num
    for i in range(task_num):
        arrs.append(np.array(batch_vals[i*batch_size : (i+1)*batch_size]).reshape((batch_size,1)))
    return np.hstack(tuple(arrs)).mean(axis=1)

def exp():
    #app = OgmlApp()
    #app = TpApp()
    #app = RxgbApp()
    #app = AsmlApp()
    #app = AsdkApp()
    #app = TcvApp()
    #app = FmmlApp()
    #app = SopApp()
    pass