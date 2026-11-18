import bpy, os, json
info = {
    "blend_filepath": bpy.data.filepath,
    "blend_name": os.path.basename(bpy.data.filepath),
    "dir": os.path.dirname(bpy.data.filepath),
    "is_dirty": bpy.data.is_dirty,
    "is_saved": bpy.data.is_saved,
    "bpy_version": bpy.app.version_string,
    "scene": bpy.context.scene.name,
    "objects": len(bpy.data.objects),
    "collections": [c.name for c in bpy.data.collections],
    "object_names": [o.name for o in bpy.data.objects][:40],
}
print("VERIFY_JSON_START")
print(json.dumps(info, indent=1, ensure_ascii=False))
print("VERIFY_JSON_END")
