from pymysqlreplication import BinLogStreamReader
from kafka_pub.kafka_pub import Pub


class MysqlLogsListener(object):

    def __init__(self, mysqlsettings, serverid):
        self.mysqlsettings = mysqlsettings
        self.serverid = serverid

    def run(self):
        stream = BinLogStreamReader(
            connection_settings=self.mysqlsettings,
            blocking=True,
            server_id=self.serverid
        )

        for binlogevent in stream:
            binlogevent.dump()
