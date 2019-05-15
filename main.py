from flask import Flask
import os
import hvac
import json
from loguru import logger

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))



class hvaccli(object):
   def __init__(self,vault_host,vault_token,vault_root):
      self.vault_host=vault_host
      self.vault_token=vault_token
      self.root=vault_root
      logger.info(self.vault_host)
      logger.info(self.vault_token)
      logger.info(self.root)
      self.client=hvac.Client(url=self.vault_host, token=self.vault_token, verify=False)
      

@app.route('/v1/health')
def health():
   vcap=json.loads(os.getenv("VCAP_SERVICES"))

   cli=hvaccli(vault_host=str(vcap['vault'][0]['credentials']['vault']),vault_token=str(vcap['vault'][0]['credentials']['token']),vault_root=str(vcap['vault'][0]['credentials']['root']))
   logger.info("Authentication status to "+cli.vault_host+ " using token "+cli.vault_token+" : "+str(cli.client.is_authenticated()))
   return str(vcap['vault'][0])


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
