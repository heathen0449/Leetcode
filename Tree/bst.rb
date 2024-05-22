class BSTNode
  attr_accessor :val, :left, :right, :parent

  def initialize(val)
    @val = val
    @left = nil
    @right = nil
    @parent = nil
  end
end


class BST
  # @!attribute[rw] root
  #   @return [BSTNode] the root node of the tree
  attr_accessor :root

  def initialize(val)
    @root = BSTNode.new(val)
  end

  def get_max(node)
    while node.right
      node = node.right
    end
    node
  end

  def get_min(node)
    while node.left
      node = node.left
    end
    node
  end

  # @param [BSTNode] node
  # @param [Integer] key
  # @return [BSTNode|nil] the node with the key value
  def iterative_tree_search(node, key)
    while node && node.val != key
      if key < node.val
        node = node.left
      else
        node = node.right
      end
    end
    node
  end

  def insert_node(key)
    new_node = BSTNode.new(key)
    parent = nil
    node = @root
    # 找到插入的位置
    while node
      parent = node
      node = key < node.val ? node.left : node.right
    end
    new_node.parent = parent
    # 第一种情况，是否为空树
    if parent.nil?
      @root = new_node
    elsif key < parent.val
      parent.left = new_node
    else
      parent.right = new_node
    end
  end

  def get_successor(node)
    # 右子树不为空，找到右子树的最小值
    return get_min(node.right) if node.right

    # 右子树为空则向上找，直到找到一个节点是其父节点的左孩子
    # 该节点的父节点就是后继节点
    now_node = node
    parent = now_node.parent
    while parent && now_node == parent.right
      now_node = parent
      parent = parent.parent
    end
    parent
  end

  def delete(node)
    left = node.left
    right = node.right
    # 左右子树都为空
    if left == nil && right == nil
      parent.left = nil if parent.left == node
      parent.right = nil if parent.right == node
    end
    # 左右一个为空
    if left == nil || right == nil
      now = left || right
      parent.left = now if parent.left == node
      parent.right = now if parent.right == node
      now.parent = parent
    else
      # 左右都不为
      successor = get_successor(node)
      delete(successor)
      node.val = successor.val
    end
  end
end
