#!/usr/bin/env python

import sys
import pika
import json
import msgpackrpc
from anomaly import client
from anomaly import types
from jubatus.common.datum import Datum


NAME = "jubatus_anomaly"

#See http://jubat.us/ja/faq_rpc_err_workaround.html
def analyze_jubatus(datum_):
    anomaly_client = client.Anomaly("127.0.0.1", 9199, NAME)
    retry_max = 1
    retry_interval = 1
    score = -1.0
    try:
        retry_count = retry_max
        while True:
            try:
                score = anomaly_client.calc_score(datum_)
                break
            except (msgpackrpc.error.TransportError, msgpackrpc.error.TimeoutError) as e:
                retry_count -= 1
                if retry_count <= 0:
                    raise

                anomaly.get_client().close()
                anomaly = client.Anomaly("127.0.0.1", 9199, NAME)

                time.sleep(retry_interval)
                continue

    except msgpackrpc.error.RPCError as e:
        raise

    finally:
        anomaly_client.get_client().close()

    return score

connection = pika.BlockingConnection(pika.ConnectionParameters(
   host=sys.argv[1], credentials = pika.PlainCredentials(sys.argv[2], sys.argv[2])))
channel = connection.channel()
channel.queue_declare(queue=sys.argv[3])

def callback(ch, method, properties, body):
    id_, val_ = json.loads(body)
    # id_ not used
    datum_ = Datum({"x":val_["x"],"y":val_["y"], "z":val_["z"]})
    score = analyze_jubatus(datum_)
    print score

channel.basic_consume(callback, queue='sensor', no_ack=True)
channel.start_consuming()
