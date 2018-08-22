#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import oa_controller



if __name__ == '__main__':
    oa_controller.app.run()
    #app.run(debug=True,host='0.0.0.0',port=5256)