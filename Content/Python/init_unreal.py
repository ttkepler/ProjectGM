import unreal

#https://www.youtube.com/watch?v=0guOMTiwmhk&ab_channel=UnrealEngine
#https://www.youtube.com/watch?v=6bg1lTN67HA&ab_channel=AlexQuevillon%5BEn%5D
#https://docs.unrealengine.com/5.1/en-US/PythonAPI/class/SystemLibrary.html#unreal-systemlibrary
#http://www.kosmokleaner.de/ownsoft/UE4CVarBrowser.html
console_commands = ['t.MaxFPS 30', 'r.VSyns true']

world = unreal.EditorLevelLibrary.get_editor_world()
for command in console_commands:
    unreal.SystemLibrary.execute_console_command(world, command)