from faaskeeper.client import FaaSKeeperClient
from faaskeeper.config import Config

from json import loads

config = Config.deserialize(loads(open("/Users/rahkochar/Projects/mvcc-db/faaskeeper/config/user_config_final.json").read()))
client = None

try:
    client = FaaSKeeperClient(config, 13001, True)
    client.start()
    ret = client.create("/root", b"root")
    print(f"ret: {ret.serialize()}")
    ret1 = client.create("/root/test2", b"test")
    print(ret1)
    ret2 = client.get_data("/root/test2")
    print("Out", ret2.serialize())
    ret_root = client.get_data("/root")
    print("Out root", ret_root.serialize())
    ret3 = client.delete("/root/test2")
    ret4 = client.delete("/root")

except Exception as e:
    print("Exception", e)
finally:
    if client is not None:
        client.stop()
