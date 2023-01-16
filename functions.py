def getCoingeckoPrice(tokenName):
    import requests, json
    link = "https://api.coingecko.com/api/v3/coins/" + tokenName
    dictionary = json.loads(requests.get(link).text)
    return dictionary.get('tickers')[0].get('last')

def getCurrentBlock():
    from datetime import datetime
    import requests, json
    timestamp = str(round(datetime.timestamp(datetime.now())))
    link = "https://explorer.exosama.com/api?module=block&action=getblocknobytime&timestamp=" + timestamp + "&closest=before"
    dictionary = json.loads(requests.get(link).text)
    return dictionary.get("result").get("blockNumber")

def getKhaosPrice(contract, token1, token2):
    import requests, json
    startBlock = str(int(getCurrentBlock()) - 10000)
    link = "https://explorer.exosama.com/api?module=account&action=tokentx&address=" + contract + "&start_block=" + startBlock
    dictionary = json.loads(requests.get(link).text)
    hash = dictionary.get('result')[0].get('hash')
    for x in range (0,5):
        if dictionary.get('result')[x].get('hash') == hash:
            if dictionary.get('result')[x].get('tokenSymbol') ==  token1:
                divisor = 1000000000000000000
                if token1 == "USDC": 
                            divisor = 1000000
                numerator = (int(dictionary.get('result')[x].get('value')) / divisor)
            if dictionary.get('result')[x].get('tokenSymbol') == token2:
                divisor = 1000000000000000000
                if token2 == "USDC":
                        divisor = 1000000
                denominator =  (int(dictionary.get('result')[x].get('value')) / divisor)
    return round(numerator/denominator, 5)

def getUSDPrice(samaPrice):
    from definitions import USDC_WSAMA
    usdSama = getKhaosPrice(USDC_WSAMA, "USDC", "WSAMA")
    return round(samaPrice*usdSama,5)
