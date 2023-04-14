from web3 import Web3, EthereumTesterProvider

url = "https://mainnet.infura.io/v3/"
# w3 = Web3(Web3.EthereumTesterProvider())
w3 = Web3(Web3.HTTPProvider(url))
print(w3.isConnected())
ac = w3.eth.accounts    # 获取账户
# 查看账户余额
u1 = ac[1]
u2 = ac[2]
s = "0x58F428758eF21b37fA36310459B4F939525A5fEe"   # 这个账户余额为0
ye = w3.eth.get_balance(u1)
# 转换成eth
w3.fromWei(ye, 'ether')
# 获取区块数据
q_data = w3.eth.get_block('latest')
# print(q_data)
# 交易
data = {
    'from':u1,
    'to':u2,
    'value':w3.toWei(1, 'ether'),
    'gas':21000    # 这个应该是手续费
}
tx_hash = w3.eth.send_transaction(data)
print(tx_hash)
# 查看交易
xx = w3.eth.get_transaction(tx_hash)
# print("交易状况",xx)
# 查看余额
print(w3.eth.get_balance(u1))
print(w3.eth.get_balance(u2))




