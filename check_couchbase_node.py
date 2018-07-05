#!/usr/bin/env python3
#coding: UTF-8

import sys
import click
import requests
import json

@click.command()
@click.option('--verbose', '-v', is_flag=True, default=False, help='Verbose logging')
@click.option('--cluster', '-C', metavar='DNS', required=True, help='Couchbase cluster address')
@click.option('--user', '-u', required=True, show_default=True, default="Administrator", help='User with access to cluster information')
@click.option('--password', '-p', required=True, default="", help='Password for couchbase user')
@click.option('--warning', '-w', metavar='INT', type=int, required=True, default=2, help='Warning threshold for nodes count in cluster')
@click.option('--critical', '-c', metavar='INT', type=int, required=True, default=1, help='Critical threshold for nodes count in cluster')

def main (cluster, user, password, warning, critical, verbose):
	try:
		req = requests.get("http://" + cluster + "/pools/nodes", auth=(user, password))
		if req.status_code != 200: raise Exception()
	except BaseException:
		print ("UKNOWN - can't connect to server or wrong http response")
		sys.exit(3)

	healthy = 0
	for node in req.json()["nodes"]:
		print ("Node %s is %s" % (node['hostname'], node['status'])) if verbose else ()
		if str(node['status']) == "healthy":
			healthy += 1
	
	print ("%s nodes are healthy" % healthy)
	if healthy <= critical:
		sys.exit(2)
	elif healthy <= warning and healthy > critical:
		sys.exit(1)
	elif healthy > warning:
		sys.exit(0)
	
if __name__ == '__main__':
	main()
