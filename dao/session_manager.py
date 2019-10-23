from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import ordered_dict_factory
from cassandra import Unauthorized, Unavailable, AuthenticationFailed, OperationTimedOut, ReadTimeout


class SessionManager(object):

    __instance = None
    username = None
    password = None
    keyspace = None
    secure_connect_bundle_path = None
    initialized = False
    _session = None

    ping_query = "SELECT data_center FROM system.local"

    @staticmethod
    def get_instance():
        if SessionManager.__instance is None:
            SessionManager()
        return SessionManager.__instance

    def __init__(self):
        SessionManager.__instance = self

    def save_credentials(self, username, password, keyspace, secure_connection_bundle_path):
        self.username = username
        self.password = password
        self.keyspace = keyspace
        self.secure_connect_bundle_path = secure_connection_bundle_path
        self.initialized = True

    def test_credentials(self, username, password, keyspace, secure_connection_bundle_path):
        temp_session = None
        success = False
        try:
            apollo_config = {
                'secure_connect_bundle': secure_connection_bundle_path
            }

            cluster = Cluster(cloud=apollo_config, auth_provider=PlainTextAuthProvider(username, password))

            temp_session = cluster.connect(keyspace=keyspace)
            result = temp_session.execute(self.ping_query)
            success = True
        except (Unauthorized, Unavailable, AuthenticationFailed, OperationTimedOut, ReadTimeout) as e:
            print e
        finally:
            if temp_session is not None:
                temp_session.shutdown()
            return success

    def connect(self):
        if self.initialized is False:
            raise Exception('Please initialize the connection parameters first with SessionManager.save_credentials')

        if self._session is None:
            apollo_config = {
                'secure_connect_bundle': self.secure_connect_bundle_path
            }

            cluster = Cluster(cloud=apollo_config, auth_provider=PlainTextAuthProvider(self.username, self.password))
            self._session = cluster.connect(keyspace=self.keyspace)
            self._session.row_factory = ordered_dict_factory

        return self._session

    def check_connection(self):
        try:
            result = self.connect().execute(self.ping_query)
            return True
        except (Unauthorized, Unavailable, AuthenticationFailed, OperationTimedOut, ReadTimeout) as e:
            return False

    def close(self):
        if self.initialized and self._session is not None:
            self._session.shutdown()
