# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


bl_info = {
    "name": "Channel Isolate and Frame",
    "author": "Jason van Gumster (Fweeb)",
    "version": (0, 3, 1),
    "blender": (2, 73, 0),
    "location": "Graph Editor > Channel > Isolate and Frame",
    "description": "Isolates and frames a selected channel in the Graph Editor.",
    "wiki_url": "http://wiki.blender.org/index.php?title=Extensions:2.6/Py/Scripts/Animation/Channel_Isolate_and_Frame",
    "tracker_url": "https://github.com/Fweeb/blender_isolate_and_frame/issues",
    "category": "Animation"}


import bpy

class IsolateAndFrame(bpy.types.Operator):
    bl_idname = "graph.channels_isolate_and_frame"
    bl_label = "Isolate and Frame"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'GRAPH_EDITOR'

    def execute(self, context):
        bpy.ops.graph.hide(unselected=True)
        bpy.ops.screen.region_flip('EXEC_REGION_CHANNELS')
        bpy.ops.graph.view_all('EXEC_REGION_WIN')
        bpy.ops.screen.region_flip('EXEC_REGION_CHANNELS')
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(IsolateAndFrame.bl_idname)


def register():
    bpy.utils.register_class(IsolateAndFrame)
    bpy.types.GRAPH_MT_channel.append(menu_func)

    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name = "Graph Editor", space_type = 'GRAPH_EDITOR')
    kmi = km.keymap_items.new("graph.channels_isolate_and_frame", 'V', 'PRESS', shift = True)
    kmi.active = True


def unregister():
    bpy.utils.unregister_class(IsolateAndFrame)
    bpy.types.GRAPH_MT_channel.remove(menu_func)

    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps["Graph Editor"]
    km.keymap_items.remove(km.keymap_items["graph.channels_isolate_and_frame"])

if __name__ == "__main__":
    register()
