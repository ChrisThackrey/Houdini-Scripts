selected_nodes = hou.selectedNodes()
if len(selected_nodes) > 0:
    for node in selected_nodes:
        print("Successfully cooked: " + node.name())
        node.cook(force=True)


hou.hscript("geocache -c")
hou.hscript("texcache -c")
hou.hscript("glcache -c")
hou.hscript("objcache -c")
hou.hscript("sopcache -c")