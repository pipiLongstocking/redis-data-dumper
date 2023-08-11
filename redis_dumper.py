import data_generator
import redis

def split_integer(n):
    half = n // 2
    if n % 2 == 0:
        return half, half
    else:
        return half, half + 1

class redis_dumper:
    def __init__(self, host='localhost', port=6379,db=0):
        self.host = host
        self.port = port
        self.db = db

    def dump_records_bytes(self, number_records, bytes_per_record):
        #TODO: add support for multiple data types via a schema
        if bytes_per_record <= 0:
            return
        records_left = number_records
        r = redis.Redis(host=self.host, port=self.port, db=self.db)
        less,more = split_integer(bytes_per_record)
        while records_left > 0:
            if bytes_per_record == 1:
                r.set(data_generator.n_size_string(1), "")
            else:
                r.set(data_generator.n_size_string(more), data_generator.n_size_string(less))
            records_left -= 1
        r.close()

