selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    node.type().definition().updateFromNode(node)