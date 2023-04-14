from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider, EthereumTesterProvider
from eth_account import Account
import json



# url = "https://mainnet.infura.io/v3/880d51093ef44c17b98a4ab2341f01eb"
# url = "https://mainnet.infura.io/v3/880d51093ef44c17b98a4ab2341f01eb"   # 测试能用
url = "https://goerli.infura.io/v3/880d51093ef44c17b98a4ab2341f01eb"
w = Web3(Web3.HTTPProvider(url))
# w = Web3(EthereumTesterProvider())    # 连接到模拟节点
print(w.isConnected())
"""
# 创建账户
name = w.eth.account.create()
key = name.key.hex()
print("账户：",name.address)
print('钥：',key)
# 验证地址是否合法
s = w.isAddress(name.address)

# 第二种方式创建
account = Account.create()    # 创建账户
print("账户：",account.address)
# 账户的私钥
key = account.key.hex() # 获取账户的key
print('钥:',key)
"""

# 导入key
# key = "0xe13df15f084648a0c3f0c4ad17ab571e1338ce12dfbc92e5712b95ec639fafaf"
# account = Account.from_key(key)
# print(account.address)  # 导入秘钥得到key
# print(account.key.hex())
# 获取账户列表
# accounts = w.eth.accounts    # 这个会根据你设置的目标地址来获取
# 获取默认账户
# s = w.eth.default_account
# 获取最新的区块
# s = w.eth.get_block('latest')  # 需要连接到目标地址
# 获取余额
# yue = w.eth.getBalance(account.address)   # 需要地址
# 转账交易
a = '0x58F428758eF21b37fA36310459B4F939525A5fEe'
b = '0x85aD32FC574d9D8E4A87AEA167cF54EbFd55B828'
# 编造数据格式
data = {
    'from': a,
    'to': b,
    'value':w.toWei(1, 'ether')
}
# xx = w.eth.sendTransaction(data)    # 开始交易,要地址
# 获取交易信息
# tx = w.eth.getTransaction(xx)    # 需要地址
# 获取交易收据
# w.eth.getTransactionReceipt(tx)
# 获取Nonce
# nonce = w.eth.getTransactionCount(账户)
# 合约调用
"""
files = '测试.json'
text = open(files, encoding='utf-8').read()
jsonObj = json.loads(text)
dz = '合约地址'
usdt = w.eth.contract(address=dz,abi=jsonObj['abi'])
print(usdt)
"""

# y = "0xF055775eBD516e7419ae486C1d50C682d4170645"
# s = Account.from_key("0xe13df15f084648a0c3f0c4ad17ab571e1338ce12dfbc92e5712b95ec639fafaf")
# print(s.address)


# 查看我的余额
u = "0x8f9FfA8e3fF0C17F498c18a840741d3c955c4163"
u = "0x03118E2c88676d31ee397E1eEf7789fECfbC40b9"
s = w.eth.get_balance(u)
# 获取更多的地址
import re
f = open('区块链.txt', 'a', encoding='utf-8')
num = 1
while True:
    dz = w.eth.account.create()
    if re.findall("^0xXU\w+",dz.address) or re.findall("^0xxu\w+",dz.address) or re.findall("^0xgui\w+",dz.address) or\
        re.findall("^0xGUI\w+",dz.address):
        yao = dz.key.hex()
        f.write("地址："+dz.address+'\n')
        f.write("钥匙："+yao+'\n'+'\n')
        break
    
f.close()
print("完成")