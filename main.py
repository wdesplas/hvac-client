from flask import Flask
import os
import hvac
import json
from loguru import logger
import urllib3
import datetime
import uuid

urllib3.disable_warnings()

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))



class hvaccli(object):
   def __init__(self,vault_host,vault_token,vault_root):
      self.vault_host=vault_host
      self.vault_token=vault_token
      self.vault_root=vault_root
      logger.info(self.vault_host)
      logger.info(self.vault_token)
      logger.info(self.vault_root)
      self.client = hvac.Client(url=self.vault_host,token=self.vault_token,verify=False)
      
      

@app.route('/v1/health')
def health():
   vcap=json.loads(os.getenv("VCAP_SERVICES"))

   cli=hvaccli(vault_host=str(vcap['vault'][0]['credentials']['vault']),vault_token=str(vcap['vault'][0]['credentials']['token']),vault_root=str(vcap['vault'][0]['credentials']['root']))
   logger.info("is seald?: " +str(cli.client.is_sealed()))
   now = datetime.datetime.now()
   logger.info("Try to writte baz='bar', lease='1h' into "+cli.vault_root)
   cli.client.write(cli.vault_root, baz='bar', lease='1h', random_uuid=str(uuid.uuid4()),creation_time=str(now.strftime("%Y-%m-%d %H:%M:%S")))

   logger.info("Try to retrive information from "+cli.vault_root)
   logger.info(str(cli.client.read(cli.vault_root)))
   return str(json.dumps(cli.client.read(cli.vault_root)))


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
