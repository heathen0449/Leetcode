# Definition for a binary tree node.

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param root [TreeNode]
# @return {Boolean}
def is_valid_bst(root)
  answer = true
  prev = -Float::INFINITY
  stack = []
  stack << root
  while !stack.empty?
    now_stack = stack.pop
    if now_stack
      stack.push(now_stack.right) if now_stack.right
      stack.push(now_stack)
      stack.push(nil)
      stack.push(now_stack.left) if now_stack.left
    else
      now = stack.pop
      answer = false if now.val <= prev
      return answer unless answer
      prev = now.val
    end
  end
  answer
end
