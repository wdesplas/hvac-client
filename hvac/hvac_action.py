import hvac
from pprint import pprint
import time
import os import getenv


vault_client = {}

class hvaccli(object):
   def vault_i(self):
      self.vault_host=getenv('vault_host')
      self.root_token=getenv('vault_token')
      self.org=getenv('vault_org')
      self.client=hvac.Client(url=vault_host, token=vault_token)
      
   def vault_r(self):
      client=self.client
      result=client.read('secret/{}'.format(name))
      if result is None:
         raise Exception('Unable to find secret {}'.format(name))
      else:
         try:
              print("Retrieved secret from Vault using key {}".format(name))
              return result['data']['value']
         except KeyError:
              print('Unable to find key in response data from Vault')
              raise Exception('Unable to find key in response data from Vault')


   def main():
      print("Launchin testing class")
      cli=vault_i()
      print_r(cli.vault_r(cli))


main()
      

     
      


