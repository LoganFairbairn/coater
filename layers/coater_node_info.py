# This folder handles getting specific layer information, generally layer nodes.

import bpy

def get_channel_nodes(context):
    '''Returns a list of all channel nodes that exist.'''
    active_material = context.active_object.active_material
    material_nodes = context.active_object.active_material.node_tree.nodes

    base_color_group = material_nodes.get(active_material.name + "_" + "BASE_COLOR")
    metallic_group = material_nodes.get(active_material.name + "_" + "METALLIC")
    roughness_group = material_nodes.get(active_material.name + "_" + "ROUGHNESS")
    height_group = material_nodes.get(active_material.name + "_" + "HEIGHT")
    emission_group = material_nodes.get(active_material.name + "_" + "EMISSION")

    group_nodes = []
    if base_color_group != None:
        group_nodes.append(base_color_group)
        
    if metallic_group != None:
        group_nodes.append(metallic_group)

    if roughness_group != None:
        group_nodes.append(roughness_group)

    if height_group != None:
        group_nodes.append(height_group)

    if emission_group != None:
        group_nodes.append(emission_group)

    return group_nodes

def get_channel_node_group(context):
    '''Returns the active channel node group.'''
    layer_stack = context.scene.coater_layer_stack
    active_material = context.active_object.active_material

    if active_material != None:
        group_node_name = active_material.name + "_" + str(layer_stack.channel)
        node_group = bpy.data.node_groups.get(group_node_name)
        return node_group
    
    else:
        return None

def get_channel_node(context):
    '''Returns the active channel node (Node that connects to Principled BSDF).'''
    active_material = context.active_object.active_material

    if active_material != None:
        material_nodes = context.active_object.active_material.node_tree.nodes
        layer_stack = context.scene.coater_layer_stack

        return material_nodes.get(active_material.name + "_" + str(layer_stack.channel))

    return None

def get_layer_nodes(context, layer_index):
    '''Returns a list of all layer nodes that exist within the specified layer'''
    node_group = get_channel_node_group(context)
    nodes = []

    # Color nodes.
    color_node = node_group.nodes.get("Color_" + str(layer_index))
    if color_node != None:
        nodes.append(color_node)

    coord_node_name = node_group.nodes.get("Coord_" + str(layer_index))
    if coord_node_name != None:
        nodes.append(coord_node_name)

    mapping_node = node_group.nodes.get("Mapping_" + str(layer_index))
    if mapping_node != None:
        nodes.append(mapping_node)

    opacity_node = node_group.nodes.get("Opacity_" + str(layer_index))
    if opacity_node != None:
        nodes.append(opacity_node)

    mix_node = node_group.nodes.get("MixLayer_" + str(layer_index))
    if mix_node != None:
        nodes.append(mix_node)

    # Mask Nodes
    mask_node = node_group.nodes.get("Mask_" + str(layer_index))
    if mask_node != None:
        nodes.append(mask_node)

    mask_coord_node = node_group.nodes.get("MaskCoords_" + str(layer_index))
    if mask_coord_node != None:
        nodes.append(mask_coord_node)

    mask_mapping_node = node_group.nodes.get("MaskMapping_" + str(layer_index))
    if mask_mapping_node != None:
        nodes.append(mask_mapping_node)

    mask_levels_node = node_group.nodes.get("MaskLevels_" + str(layer_index))
    if mask_levels_node != None:
        nodes.append(mask_levels_node)

    mask_mix_node = node_group.nodes.get("MaskMix_" + str(layer_index))
    if mask_mix_node != None:
        nodes.append(mask_mix_node)

    return nodes

def get_self_layer_nodes(self, context):
    '''Gets layer nodes using the self object.'''
    node_group = get_channel_node_group(context)
    nodes = []

    coord_node = node_group.nodes.get(self.coord_node_name)
    if coord_node != None:
        nodes.append(coord_node)

    mapping_node = node_group.nodes.get(self.mapping_node_name)
    if mapping_node != None:
        nodes.append(mapping_node)

    color_node = node_group.nodes.get(self.color_node_name)
    if color_node != None:
        nodes.append(color_node)

    opacity_node = node_group.nodes.get(self.opacity_node_name)
    if opacity_node != None:
        nodes.append(opacity_node)
        
    mix_layer_node = node_group.nodes.get(self.mix_layer_node_name)
    if mix_layer_node != None:
        nodes.append(mix_layer_node)

    mask_node = node_group.nodes.get(self.mask_node_name)
    if mask_node != None:
        nodes.append(mask_node)
        
    mask_mix_node = node_group.nodes.get(self.mask_mix_node_name)
    if mask_mix_node != None:
        nodes.append(mask_mix_node)

    mask_coord_node = node_group.nodes.get(self.mask_coord_node_name)
    if mask_coord_node != None:
        nodes.append(mask_coord_node)

    mask_mapping_node = node_group.nodes.get(self.mask_mapping_node_name)
    if mask_mapping_node != None:
        nodes.append(mask_mapping_node)

    mask_levels_node = node_group.nodes.get(self.mask_levels_node_name)
    if mask_levels_node != None:
        nodes.append(mask_levels_node)

    return nodes

def get_node(context, node_name, index):
    '''Returns a specific coater node from a specific layer index. Returns None if it doesn't exist.'''
    layers = context.scene.coater_layers
    channel_node_group = get_channel_node_group(context)

    if channel_node_group != None and index > -1:
        if node_name == 'COLOR':
            return channel_node_group.nodes.get(layers[index].color_node_name)

        if node_name == 'OPACITY':
            return channel_node_group.nodes.get(layers[index].opacity_node_name)

        if node_name == 'MIX':
            return channel_node_group.nodes.get(layers[index].mix_layer_node_name)
        
        if node_name == 'MASK':
            return channel_node_group.nodes.get(layers[index].mask_node_name)

        if node_name == 'MAPPING':
            return channel_node_group.nodes.get(layers[index].mapping_node_name)

        if node_name == 'MASK_MAPPING':
            return channel_node_group.nodes.get(layers[index].mask_mapping_node_name)

    else:
        return None

def get_self_node(self, context, node_name):
    '''Returns a specific node from the self object. Returns none if it doesn't exist.'''
    channel_node_group = get_channel_node_group(context)

    if channel_node_group != None:
        if node_name == 'OPACITY':
            return channel_node_group.nodes.get(self.opacity_node_name)

        if node_name == 'MIX':
            return channel_node_group.nodes.get(self.mix_layer_node_name)

def get_layer_image(context, layer_index):
    # Returns a layer image from the given layer index, returns None if it does not exist.
    color_node = get_node(context, 'COLOR', layer_index)

    if color_node != None:
        if color_node.bl_static_type == 'TEX_IMAGE':
            return color_node.image
        else:
            return None
    else:
        return None

def get_layer_mask_image(context, layer_index):
    # Returns the image used as a mask for the selected layer if one exists.
    mask_node = get_node(context, 'MASK', layer_index)

    if mask_node != None:
        if mask_node.bl_static_type == 'TEX_IMAGE':
            return mask_node.image
        else:
            return None
    else:
        return None
