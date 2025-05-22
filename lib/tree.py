class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, target_id):
    return self._search(self.root,target_id)
  
  def _search(self, node, target_id):
        if node.get('id') == target_id:
            return node
        for child in node.get('children', []):
            result = self._search(child, target_id)
            if result:
                return result
        return None
