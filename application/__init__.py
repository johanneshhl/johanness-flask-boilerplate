 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import Flask


app = Flask(__name__)
app.config.from_object('applicationConfig')



import application.views