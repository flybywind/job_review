package maxprofit

import "math"

func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	var lastMin, latestMax, minp, maxp = math.MaxInt, math.MinInt, 0, 0
	var profit = 0
	for i := 0; i < len(prices); i++ {

		if lastMin > prices[i] {
			lastMin = prices[i]
			minp = i
		}
		if latestMax < prices[i] || (maxp < minp && prices[i] > lastMin) {
			latestMax = prices[i]
			maxp = i
		}
		if maxp > minp {
			if p := latestMax - lastMin; p > profit {
				profit = p
			}
		}
	}

	return profit
}
