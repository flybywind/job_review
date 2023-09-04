"""
广告价格权重
如下例：
广告id为1的出现权重是1.0
广告id为2的出现权重是2.0
广告id为3的出现权重是1.0
那么在重复展示广告4000次的情况下：
id为1的广告出现次数接近1000，
id为2的广告出现次数接近2000，
id为3的广告出现次数接近1000
"""

# input: 
# pair: ad_id:bid, ad_id:bid

# invoke: 
# int getRandomAd(pairs_list): 

from random import sample, random
from collections import Counter
from functools import reduce
class AdsServer:
    def __init__(self, ads_campaign_pair) -> None:
        self.ads_campaign = {}
        self.ads_freq = {}
        self.ads_list = []
        self.min_bid = 0.01
        # self.max_bid = 1_000_000_000
        # max_bid = 0
        for ads, bid in ads_campaign_pair:
            # assume the minimum bidding unit is Cent, namely 0.01 Yuan
            self.ads_campaign[ads] = int(max(self.min_bid, bid)*100)
            self.ads_freq[ads] = 0
            self.ads_list.append(ads)
        self.ads_count = len(ads_campaign_pair)

    def getRadomAd(self):
        # MOD: add a dedicated func for randomly selection strategy
        def select_randomly(cand):
            ads = sample(cand, 1)[0]
            self.ads_freq[ads] += 1
            return ads
        
        # first find the ads that don't have impression first
        ads_zero_impr = [a for a, f in self.ads_freq.items() if f == 0]
        if len(ads_zero_impr) > 0:
            return select_randomly(ads_zero_impr)
        else:
            # calculate the weight of the ads
            # MOD: diff by diff, namely relative ratio of ratio, instead of abolute number ratio
            freq_min = reduce(min, (v for _, v in self.ads_freq.items()))
            campain_min = reduce(min, (v for _, v in self.ads_campaign.items()))
            ads_weight = {a:1-f*campain_min/(freq_min*self.ads_campaign[a]) for a, f in self.ads_freq.items()}
            ads_cumulate_prob = {}
            accum = 0
            for a, w in ads_weight.items():
                accum += w
                ads_cumulate_prob[a] = accum
            # MOD: fix the case when the counter reach to the top limit
            if accum == 0:
                self.ads_freq = {a:0 for a in self.ads_list}
                return select_randomly(self.ads_list)
            
            ads_cumulate_prob = {a: w/accum for a, w in ads_cumulate_prob.items()}

            random_val = random()
            last_w = 0
            ads = "No"
            for a, w in ads_cumulate_prob.items():
                if last_w < random_val and random_val <= w:
                    ads = a
                    break
                last_w = w
            self.ads_freq[ads] += 1
            assert(ads!="No")
            return ads
        
if __name__ == "__main__":
    # test distribute of ads
    ads_pair = [("ad1", 100), ("ad2", 20), ("ad3", 50), ("ad4", 1), ("ad5", 0.1)]
    adsServer = AdsServer(ads_pair)
    ads_impr = Counter({})
    for i in range(100_000):
        ads = adsServer.getRadomAd()
        ads_impr[ads] += 1

    campaign_min = reduce(min, (v for _, v in ads_pair))
    freq_min = reduce(min, (v for _, v in ads_impr.items()))
    ads_impr_diff = {a:1-f*freq_min/(campaign_min*ads_impr[a]) for a, f in ads_pair}
    print(f"ads impression counter: {ads_impr},\nads_campaign: {ads_pair},\ndiff = {ads_impr_diff}")