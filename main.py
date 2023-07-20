from web3 import Web3

# 로컬 이더리움 노드에 연결합니다
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/1c5c85dcb5a64c3aa5ca637f46a52aa0'))


# 트랜잭션 이벤트를 처리하는 함수
def handle_transaction(event):
    transaction_hash = event['transactionHash'].hex()
    transaction = w3.eth.get_transaction(transaction_hash)

    # 트랜잭션 정보를 원하는 방식으로 저장합니다
    # 여기에서는 간단히 터미널에 출력합니다
    print(f"Transaction Hash: {transaction_hash}")
    print(f"From: {transaction['from']}")
    print(f"To: {transaction['to']}")
    print(f"Value: {transaction['value']} wei")
    print("")


# 트랜잭션 이벤트를 구독합니다
def subscribe_transactions():
    subscription = w3.eth.subscribe('pending_transactions', handle_transaction)

    # 프로그램을 종료하기 전까지 계속해서 이벤트를 처리합니다
    while True:
        pass


# 메인 함수
def main():
    subscribe_transactions()


if __name__ == '__main__':
    main()
