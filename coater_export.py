import bpy
from bpy.types import Operator

class COATER_OT_export(Operator):
    bl_idname = "coater.export"
    bl_label = "Export"
    bl_options = {'REGISTER', 'UNDO'}

    @ classmethod
    def poll(cls, context):
        return context.active_object.active_material
    
    def execute(self, context):
        return {'FINISHED'}

class COATER_OT_export_base_color(Operator):
    bl_idname = "coater.export_base_color"
    bl_label = "Export Base Color"
    bl_options = {'REGISTER', 'UNDO'}

    @ classmethod
    def poll(cls, context):
        return context.active_object.active_material
    
    def execute(self, context):
        return {'FINISHED'}

class COATER_OT_export_roughness(Operator):
    bl_idname = "coater.export_roughness"
    bl_label = "Export Roughness"
    bl_options = {'REGISTER', 'UNDO'}

    @ classmethod
    def poll(cls, context):
        return context.active_object.active_material
    
    def execute(self, context):
        return {'FINISHED'}

class COATER_OT_export_metallic(Operator):
    bl_idname = "coater.export_metallic"
    bl_label = "Export Metallic Channel"
    bl_options = {'REGISTER', 'UNDO'}

    @ classmethod
    def poll(cls, context):
        return context.active_object.active_material
    
    def execute(self, context):
        return {'FINISHED'}

class COATER_OT_export_normals(Operator):
    bl_idname = "coater.export_normals"
    bl_label = "Export Normals"
    bl_options = {'REGISTER', 'UNDO'}

    @ classmethod
    def poll(cls, context):
        return context.active_object.active_material
    
    def execute(self, context):
        return {'FINISHED'}