import redis_dumper

r = redis_dumper.redis_dumper()
each_record_size = 200
records = 200000
r.dump_records_bytes(records, each_record_size)


