import os.path

from tornado.options import define


define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

settings = {}
settings["static_path"] = os.path.join(os.path.dirname(__file__), "static")
settings["template_path"] = os.path.join(os.path.dirname(__file__), "templates")
settings['ovs_remote'] = 'unix:/var/run/openvswitch/db.sock'
settings['ovs_schema'] = '/usr/share/openvswitch/vswitch.ovsschema'
settings['ext_schema'] = '/usr/share/openvswitch/vswitch.extschema'
