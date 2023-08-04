import sys
import bpy


#clean out the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


print(f"{sys.argv[0]}: Input file: {sys.argv[-2]}")
print(f"{sys.argv[0]}: Ouput file: {sys.argv[-1]}")
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
bpy.ops.export_scene.fbx(filepath=sys.argv[-1], path_mode='COPY', embed_textures=True)

