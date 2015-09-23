selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    node.matchCurrentDefinition()