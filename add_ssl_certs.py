"""Adds SSL Certs to Dynatrace"""
# IMPORTS GO HERE
import change_pythonpath # Must be first import
import dynatrace.cluster.ssl as ssl
import user_variables as uv
import json

# YOUR SCRIPT GOES HERE
ssl_dir = "txt"
private_key_name = "private.key.pem"
public_cert_name = "public.cert.pem"
ca_chain_cert_name = "ca-chain.public.pem"
CLUSTER = uv.FULL_SET['CLUSTER_NAME']
NODE_IDS = [1]

with open(ssl + "/" + private_key_name, 'r') as current_file:
  private_key = current_file.read()
with open(ssl + "/" + public_cert_name, 'r') as current_file:
  public_cert = current_file.read()
with open(ssl + "/" + ca_chain_cert_name, 'r') as current_file:
  ca_chain = current_file.read()

ssl_json = {
  "privateKeyEncoded": private_key,
  "publicKeyCertificateEncoded": public_cert,
  "certificateChainEncoded": ca_chain
}

for node_id in NODE_IDS:
  print (ssl.set_cert(CLUSTER, 'SERVER', node_id, ssl_json))

