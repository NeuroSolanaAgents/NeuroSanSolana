from solana.rpc.api import Client
from solders.pubkey import Pubkey
from neuro_san.interfaces.tools import CodedTool

class GetBalance(CodedTool):
      """Get the balance of a Solana wallet."""

    def __init__(self):
              super().__init__(
                            name="get_balance",
                            description="Get the balance of a Solana wallet address. Input is a public key string.",
              )
              self.client = Client("https://api.devnet.solana.com")

    def execute(self, address: str) -> str:
              try:
                            pubkey = Pubkey.from_string(address)
                            response = self.client.get_balance(pubkey)
                            balance = response.value
                            return f"The balance of {address} is {balance / 1e9:.4f} SOL ({balance} lamports)."
except Exception as e:
            return f"Error getting balance: {str(e)}"
