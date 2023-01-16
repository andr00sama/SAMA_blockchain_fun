from definitions import USDC_WSAMA, USDC_STONE, USDC_WOOD, USDC_IRON, USDC_GOLD, WSAMA_DNA, USDC_DNA, WSAMA_BLOOD, USDC_BLOOD, WSAMA_MOB, USDC_MOB, WSAMA_PUMPK, USDC_PUMPK, WSAMA_DON
from functions import getKhaosPrice, getUSDPrice

usdPrice = getKhaosPrice(USDC_DNA, "USDC", "DNA")
samaPrice = getUSDPrice(getKhaosPrice(WSAMA_DNA, "WSAMA", "DNA"))

print("DNA (USDC pool): " + str(usdPrice))
print("DNA (SAMA pool): " + str(samaPrice))
