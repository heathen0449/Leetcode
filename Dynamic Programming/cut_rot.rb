# @param {Integer} length the length of the rod
# @param {Symbol => Interger} prices the prices of different lengths of rod
def cut_rot (length, prices)
  dp = Array.new(length+1, 0) # dp[i] is the max price of length i
  (1..length).each do |i|
    prices.each do |length, price|
      dp[i] = [dp[i], dp[i-length]+price].max if i >= length
      # 需要dp[0] 来保证逻辑统一
    end
  end
  pp dp
  dp[length]
end

prices = {1=>1, 2=>5, 3=>8, 4=>9}
pp cut_rot(4, prices)
