#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from oa_controller import app



if __name__ == '__main__':
    app.run()
    #app.run(debug=True,host='0.0.0.0',port=5256)