import itertools

def create_groups():

    file = "Z:/Groupes-cours/NAND999-A15-N01/pub/_info/shading_groups_car.txt"
    
    file = open(file, 'r')
    
    content = file.read().splitlines()
    
    
    splitter = '#'
    
    content = [list(y) for x, y in itertools.groupby(content, lambda z: z == splitter) if not x]
    
    shaders = {}
    for shader in content:
        shader_name = shader.pop(0)
        shaders[shader_name.replace("-", "")] = shader
    
    try:
        selected_node = hou.selectedNodes()[0]
    except:
        print("Please select a node")
        return
    
    i = 0
    group_nodes = []
    for shader, groups in shaders.items():
        master_node = selected_node.parent()
        group_node = master_node.createNode("group")
        group_node.moveToGoodPosition()
        group_node.setName(shader)
        group_node.setColor(hou.Color((0.4, 1, 0.4)))
        group_node.parm("docreategrp").set(0)
        group_node.parm("combineentity").set(2)
        group_node.parm("grpequal").setExpression("$OS")
        group_node.parm("grp1").set(" ".join(groups))
        group_nodes.append(group_node)
        if i == 0:
            group_node.setInput(0, selected_node)
        else:
            group_node.setInput(0, group_nodes[i-1])
        i += 1
    
    delete_group_string = ["^" + string for string in shaders.keys()]
    delete_group_string = " ".join(delete_group_string)
        
    delete_group_node = master_node.createNode("group")
    delete_group_node.moveToGoodPosition()
    delete_group_node.setName("delete_unused_groups")
    delete_group_node.parm("docreategrp").set(0)
    delete_group_node.parm("destroyname").set("* " + delete_group_string)
    delete_group_node.setInput(0, group_nodes[-1])
    
    
    
    i = 0
    group_nodes = []
    for shader, groups in shaders.items():
        group_node = master_node.createNode("alembicgroup")
        group_node.moveToGoodPosition()
        group_node.setName(shader + "_alembic")
        group_node.setColor(hou.Color((0.4, 1, 0.4)))
        group_node.parm("group0").set("$OS:s/_alembic//")
        group_nodes.append(group_node)
        if i > 0:
            group_node.setInput(0, group_nodes[i-1])
        i += 1
    
    
create_groups()