#!/usr/bin/env python
import random, time, json
import argparse
import pika, logging
from jsonclient import JSONClient

rpc = JSONClient(("localhost", 1234))

def getDataOld(sigma):
    x,y,z = random.randint(0,2), random.randint(0,2), random.randint(0,2)
    dat = {}
    dat["x"], dat["y"], dat["z"] = random.normalvariate(x,sigma), random.normalvariate(y,sigma), random.normalvariate(z,sigma)
    dat["gp"] = 9 * x + 3 * y + z
    return dat

def getData(streamname):
    return rpc.call("RPCFunc.Get", streamname)

def registerData(streamname, method, filename):
    return rpc.call("RPCFunc.Register", streamname + ", " + method + ", " + filename)

 
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description='Generate and enqueue psudo sensor data')
    parser.add_argument('--speed', '-P', type=int, default = 1)
    parser.add_argument('--count', '-N', type=int, default = 100)
    parser.add_argument('--filename', '-F', default = "test.csv")
    parser.add_argument('--streamname', '-T', default = "test")
    parser.add_argument('--seed', '-S', default = 0)
    parser.add_argument('--silent', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials = pika.PlainCredentials('jubatus','jubatus')))
    channel = connection.channel()
    channel.queue_declare(queue='sensor')

    registerData(args.streamname, "gaussian", args.filename)

    random.seed(args.seed)
    for cnt in xrange(args.count):
        da = getData(args.streamname)
        channel.basic_publish(exchange='',
                      routing_key='sensor',
                      body= str(cnt) + " " + da)
        if not args.silent :
            print cnt, da
            time.sleep( 1.0 / args.speed)
    connection.close()

