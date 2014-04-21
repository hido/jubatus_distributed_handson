#!/usr/bin/env python

import sys
import argparse
import pika
import json
import msgpackrpc
from util import convert
from anomaly import client
from anomaly import types

parser = argparse.ArgumentParser(description='jubatus anomaly update')
parser.add_argument('--host', '-p', default = "localhost")
parser.add_argument('--stream','-T', default = "normal")
args = parser.parse_args()

NAME = "jubatus_anomaly"

#See http://jubat.us/ja/faq_rpc_err_workaround.html
def update_jubatus(datum_):
    anomaly_client = client.Anomaly("127.0.0.1", 9199, NAME)
    retry_max = 1
    retry_interval = 1
    try:
        retry_count = retry_max
        while True:
            try:
                id = anomaly_client.add(datum_)
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

connection = pika.BlockingConnection(pika.ConnectionParameters(
   host=args.host, credentials = pika.PlainCredentials("jubatus", "jubatus")))
channel = connection.channel()
channel.queue_declare(queue=args.stream)

def callback(ch, method, properties, body):
    id_, datum_ = convert(body)
    update_jubatus(datum_)
    print "update succeeded (ID: " + str(id_) + ")"

channel.basic_consume(callback, queue=args.stream, no_ack=True)
channel.start_consuming()
