# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer[]}

def do_inorder_traversal(stack, answer)
  until stack.empty?
    node = stack.pop
    if node
      stack << node.right if node.right
      stack << node << nil
      stack << node.left if node.left
    else
      answer << stack.pop.val
    end
  end
end

def inorder_traversal(root)
  answer = []
  stack = []
  stack << root if root
  do_inorder_traversal(stack, answer)
  answer
end
