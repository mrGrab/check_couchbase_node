<h3>Nagios plugin to check state of Couchbase nodes</h3>
Python script which sends GET request to couchbase cluster REST api: http://cluster_dns/pools/nodes
<pre>
Usage: check_couchbase_node.py [OPTIONS]

Options:
  -v, --verbose        Verbose logging
  -C, --cluster DNS    Couchbase cluster address  [required]
  -u, --user TEXT      User with access to cluster information  [default: Administrator; required]
  -p, --password TEXT  Password for couchbase user  [required]
  -w, --warning INT    Warning threshold for nodes count in cluster [required]
  -c, --critical INT   Critical threshold for nodes count in cluster [required]
  --help               Show this message and exit.
</pre>
Run example:
<pre>
    check_couchbase_node.py -C my_cluster.example.com -u Administrator -p password -c1 -w2
</pre>
That's it. Enjoy.