def on_on_chat():
    global ow
    if ow == 1:
        ow = 0
        player.say("OpenWaterESP off")
    else:
        ow = 1
        player.say("OpenWaterESP on")
    while ow == 1:
        mobs.execute_detect(WATER,
            positions.add(pos(-2, -1, -2), pos(2, -5, 2)),
            "OpenWater found!")
player.on_chat("OpenWaterESP", on_on_chat)

def on_mob_killed_chicken():
    pass
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)

# if you see this, Hi!

def on_on_chat2(item):
    player.teleport(pos(item, 0, 0))
player.on_chat("cx", on_on_chat2)

def on_on_chat3():
    blocks.fill(BED, pos(1, 0, 1), pos(2, 0, 2), FillOperation.REPLACE)
player.on_chat("Tired", on_on_chat3)

def on_on_chat4():
    blocks.fill(DIRT, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.REPLACE)
    blocks.fill(DIRT, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.REPLACE)
player.on_chat("autopp", on_on_chat4)

def on_on_chat5(x5, y5, z5):
    blocks.fill(OBSIDIAN,
        pos(x5, 0, x5),
        pos(z5, y5, z5),
        FillOperation.HOLLOW)
player.on_chat("custombase+", on_on_chat5)

def on_on_chat6():
    player.say("xp amount - gives you xp")
    player.say("day - sets time to day")
    player.say("one-shot - one shot any mob")
    player.say("speedhack - run faster")
    player.say("explode - blow up anything and anyone's base")
    player.say("suicide - kill urself")
    player.say("mass-suicide - kill everyone")
    player.say("mob-suicide - kill every entity")
    player.say("fastbreak - break blocks fast")
    player.say("water-br. - breathe underwater")
    player.say("panic - turns off every hack")
    player.say("nuker - mines blocks")
    player.say("nukeroff - turns nuker off")
    player.say("fullbright - allows you to see in dark")
    player.say("autobase - automatically builds a base for u")
    player.say("type help4 for next page")
player.on_chat("help3", on_on_chat6)

def on_on_chat7(effect, dur, amp):
    mobs.apply_effect(effect, mobs.target(LOCAL_PLAYER), dur, amp)
player.on_chat("effect", on_on_chat7)

def on_on_chat8():
    global ag
    if ag == 1:
        ag = 0
        gameplay.set_game_rule(MOB_GRIEFING, True)
        gameplay.set_game_rule(TNT_EXPLODES, True)
        player.say("Anti-Grief off")
    else:
        ag = 1
        gameplay.set_game_rule(MOB_GRIEFING, False)
        gameplay.set_game_rule(TNT_EXPLODES, False)
        player.say("Anti-Grief on")
player.on_chat("Anti-Grief", on_on_chat8)

def on_on_chat9():
    gameplay.set_game_mode(SURVIVAL, mobs.target(LOCAL_PLAYER))
    mobs.kill(mobs.target(LOCAL_PLAYER))
player.on_chat("suicide", on_on_chat9)

def on_on_chat10():
    shapes.circle(DIAMOND_BLOCK,
        pos(5, 0, 5),
        5,
        Axis.X,
        ShapeOperation.REPLACE)
    shapes.circle(DIAMOND_BLOCK,
        pos(5, 0, 5),
        5,
        Axis.Y,
        ShapeOperation.REPLACE)
    shapes.circle(DIAMOND_BLOCK,
        pos(5, 0, 5),
        5,
        Axis.Z,
        ShapeOperation.REPLACE)
player.on_chat("Richcircle", on_on_chat10)

def on_on_chat11(num1):
    player.say("food - gives you 16 cooked beef")
    player.say("deez -  nuts")
    player.say("cw - clear weather")
    player.say("portal - gives you 16 obsidian and 1 flint and steel")
    player.say("kit - gives you full netherite armor and tools")
    player.say("gmc - sets gamemode to creative")
    player.say("gms - sets gamemode to survival")
    player.say("bedrock - gives you a stack of bedrock")
    player.say("barrier - gives you a stack of barrier blocks")
    player.say("type help3 for next page")
player.on_chat("help2", on_on_chat11)

def on_on_chat12(radius2):
    shapes.circle(DIAMOND_BLOCK,
        pos(0, 0, 0),
        radius2,
        Axis.X,
        ShapeOperation.REPLACE)
    shapes.circle(DIAMOND_BLOCK,
        pos(0, 0, 0),
        radius2,
        Axis.Y,
        ShapeOperation.REPLACE)
    shapes.circle(DIAMOND_BLOCK,
        pos(0, 0, 0),
        radius2,
        Axis.Z,
        ShapeOperation.REPLACE)
player.on_chat("customrichcircle", on_on_chat12)

def on_on_chat13(item2, Amount):
    mobs.give(mobs.target(LOCAL_PLAYER), blocks.block_by_id(item2), Amount)
player.on_chat("give", on_on_chat13)

def on_on_chat14():
    mobs.give(mobs.target(NEAREST_PLAYER), BOW, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "infinity", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "punch", 2)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "power", 5)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "flame", 1)
player.on_chat("godbow", on_on_chat14)

def on_on_chat15():
    global NoFa, NoFi
    if NoFa == 1:
        NoFa = 0
        gameplay.set_game_rule(FALL_DAMAGE, True)
        player.say("NoFall off")
    else:
        NoFi = 1
        gameplay.set_game_rule(FALL_DAMAGE, False)
        player.say("NoFall on")
player.on_chat("NoFall", on_on_chat15)

def on_travelled_swim_water():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 3, 3)
player.on_travelled(SWIM_WATER, on_travelled_swim_water)

def on_on_chat16(itemid3, amount6):
    mobs.give(mobs.target(LOCAL_PLAYER), itemid3, amount6)
player.on_chat("give", on_on_chat16)

def on_on_chat17():
    mobs.teleport_to_position(mobs.target(LOCAL_PLAYER), world(0, 319, 0))
    mobs.apply_effect(RESISTANCE, mobs.target(NEAREST_PLAYER), 25, 255)
player.on_chat("spawn", on_on_chat17)

def on_on_chat18():
    global c
    c = 0
    gameplay.set_game_rule(SHOW_COORDINATES, False)
    player.say("Coordinates off")
player.on_chat("Coordinatesoff", on_on_chat18)

def on_on_chat19():
    mobs.kill(mobs.target(ALL_ENTITIES))
player.on_chat("anti-lagc", on_on_chat19)

def on_on_chat20(num12):
    gameplay.xp(num12, mobs.target(LOCAL_PLAYER))
    player.say("gave you " + str(num12) + " xp")
player.on_chat("xp", on_on_chat20)

def on_on_chat21(itemid, amount2):
    mobs.give(mobs.target(RANDOM_PLAYER), itemid, amount2)
player.on_chat("lottery", on_on_chat21)

def on_on_chat22():
    global nuker
    nuker = 0
    player.say("Nuker off")
player.on_chat("nukeroff", on_on_chat22)

def on_on_chat23(x3, y3, z3):
    global customnuker
    if customnuker == 1:
        customnuker = 0
        player.say("customnuker off")
    else:
        customnuker = 1
        player.say("customnuker on")
    while customnuker == 1:
        blocks.fill(AIR, pos(x3, y3, x3), pos(z3, 0, z3), FillOperation.DESTROY)
player.on_chat("customnuker", on_on_chat23)

def on_on_chat24():
    mobs.apply_effect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 999999, 5)
player.on_chat("HighJump", on_on_chat24)

def on_on_chat25(x7, z7, blockid3):
    global cs
    if cs == 1:
        cs = 0
        player.say("customscaffold off")
    else:
        cs = 1
        player.say("customscaffold on")
    while cs == 1:
        blocks.fill(blockid3,
            pos(x7, -1, x7),
            pos(z7, -2, z7),
            FillOperation.REPLACE)
player.on_chat("customscaffold", on_on_chat25)

def on_on_chat26():
    global ws
    ws = 0
    player.say("Widescaffold off")
player.on_chat("widescaffoldoff", on_on_chat26)

def on_on_chat27(_7, _8):
    player.say(_7 / _8)
player.on_chat("calculatord", on_on_chat27)

def on_on_chat28():
    global customnuker
    customnuker = 0
    player.say("customnuker off")
player.on_chat("customnukeroff", on_on_chat28)

def on_on_chat29():
    global nuker
    if nuker == 1:
        nuker = 0
        player.say("Nuker off")
    else:
        nuker = 1
        player.say("Nuker on.")
    while nuker == 1:
        blocks.fill(AIR, pos(-5, 0, -5), pos(5, 6, 5), FillOperation.DESTROY)
player.on_chat("nuker", on_on_chat29)

def on_on_chat30():
    global cd
    cd = 0
    player.say("ChestDetector off")
player.on_chat("ChestDetectoroff", on_on_chat30)

def on_on_chat31():
    mobs.give(mobs.target(LOCAL_PLAYER), DRAGON_EGG, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), STRUCTURE_BLOCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), WATER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), LAVA, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), FIRE, 64)
player.on_chat("i.kit", on_on_chat31)

def on_on_chat32():
    mobs.give(mobs.target(LOCAL_PLAYER), TRIDENT, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "mending", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "riptide", 3)
player.on_chat("GodTridents2", on_on_chat32)

def on_on_chat33():
    mobs.give(mobs.target(LOCAL_PLAYER), OBSIDIAN, 16)
    loops.pause(50)
    mobs.give(mobs.target(LOCAL_PLAYER), FLINT_AND_STEEL, 1)
player.on_chat("portal", on_on_chat33)

def on_on_chat34(phrase):
    for index in range(69):
        player.say(phrase)
player.on_chat("annoy", on_on_chat34)

def on_on_chat35(x2, y2, z2):
    blocks.fill(Blockid,
        pos(x2, 0, x2),
        pos(z2, y2, x2),
        FillOperation.REPLACE)
    blocks.fill(Blockid,
        pos(x2, 0, x2),
        pos(x2, y2, z2),
        FillOperation.REPLACE)
    blocks.fill(Blockid,
        pos(z2, 0, x2),
        pos(z2, y2, z2),
        FillOperation.REPLACE)
    blocks.fill(Blockid,
        pos(x2, 0, z2),
        pos(z2, y2, z2),
        FillOperation.REPLACE)
player.on_chat("customwall", on_on_chat35)

def on_on_chat36():
    mobs.apply_effect(ABSORPTION, mobs.target(LOCAL_PLAYER), 999999, 255)
    mobs.apply_effect(HEALTH_BOOST, mobs.target(LOCAL_PLAYER), 999999, 255)
    mobs.apply_effect(REGENERATION, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("infinihealth", on_on_chat36)

def on_on_chat37():
    global NoFi
    if NoFi == 1:
        NoFi = 0
        gameplay.set_game_rule(FIRE_DAMAGE, True)
        player.say("NoFire off")
    else:
        NoFi = 1
        gameplay.set_game_rule(FIRE_DAMAGE, False)
        player.say("NoFire on")
player.on_chat("NoFire", on_on_chat37)

def on_on_chat38():
    mobs.apply_effect(HASTE, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("Speedfastbreak", on_on_chat38)

def on_on_chat39():
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 999999, 1)
player.on_chat("criticals", on_on_chat39)

def on_on_chat40():
    global nw
    nw = 0
    gameplay.set_game_rule(WEATHER_CYCLE, True)
    player.say("NoWeather off")
player.on_chat("NoWeatheroff", on_on_chat40)

def on_on_chat41():
    player.say("XP+ - Xp + satisfying = awesome!")
    player.say("W.TNTScaffold - What's better than tnt scaffold? 9x the output!")
    player.say("W.TNTScaffoldoff - turns off widetntscaffold")
    player.say("OpenWaterESP - detects if where you're fishing can yield treasure")
    player.say("OpenWaterESPoff - turns off OpenWaterESP")
    player.say("AerialStrike - Drops bombs from the sky.")
    player.say("Nuke - you know what (now use customnuke)")
    player.say("Coordinates - Automatically shows your coordinates")
    player.say("Coordinatesoff - turns off Coordinates")
    player.say("ChestDetector - detects if a chest is below or above you.")
    player.say("ChestDetectoroff - turns off ChestDetector")
    player.say("type help9 for more commands")
player.on_chat("help8", on_on_chat41)

def on_on_chat42():
    mobs.apply_effect(NIGHT_VISION, mobs.target(LOCAL_PLAYER), 999999, 1)
player.on_chat("fullbright", on_on_chat42)

def on_on_chat43(x8, z8, power):
    blocks.fill(REDSTONE_BLOCK,
        pos(x8, 50, x8),
        pos(z8, 50, z8),
        FillOperation.REPLACE)
    blocks.fill(REDSTONE_LAMP,
        pos(x8, 49, x8),
        pos(z8, 49, z8),
        FillOperation.REPLACE)
    loops.pause(699)
    player.say("3")
    loops.pause(699)
    blocks.fill(AIR, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.REPLACE)
    loops.pause(699)
    player.say("2")
    loops.pause(699)
    blocks.fill(REDSTONE_LAMP,
        pos(x8, 49, x8),
        pos(z8, 49, z8),
        FillOperation.REPLACE)
    loops.pause(699)
    player.say("1")
    loops.pause(699)
    player.say("nuke initiated")
    loops.pause(69)
    blocks.fill(AIR, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.REPLACE)
    loops.pause(69)
    for index2 in range(power):
        blocks.fill(TNT, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.REPLACE)
    loops.pause(69)
    for index3 in range(power):
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(8, 28, -8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(-8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(8, 28, -8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, 8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-12, 28, -12), pos(12, 28, -12)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-12, 28, -12), pos(-12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(12, 28, -12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, 12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-15, 28, -15), pos(15, 28, -15)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-15, 28, -15), pos(-15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(15, 28, -15), pos(15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, 15), pos(15, 28, 15)))
player.on_chat("customnuke", on_on_chat43)

def on_on_chat44():
    gameplay.set_game_mode(SURVIVAL, mobs.target(LOCAL_PLAYER))
player.on_chat("gms", on_on_chat44)

def on_on_chat45():
    global ws
    if ws == 1:
        ws = 0
        player.say("Widescaffold off")
    else:
        ws = 1
        player.say("Widescaffold on")
    while ws == 1:
        blocks.fill(Blockid,
            pos(-1, -1, -1),
            pos(1, -2, 1),
            FillOperation.REPLACE)
player.on_chat("widescaffold", on_on_chat45)

def on_on_chat46():
    global Scaffoldhack
    Scaffoldhack = 0
    player.say("Scaffold off.")
player.on_chat("stopscaffold", on_on_chat46)

def on_on_chat47():
    global NoFi
    NoFi = 0
    gameplay.set_game_rule(FIRE_DAMAGE, True)
    player.say("NoFire off")
player.on_chat("NoFireoff", on_on_chat47)

def on_on_chat48():
    global NoFa
    NoFa = 0
    gameplay.set_game_rule(FALL_DAMAGE, True)
    player.say("NoFall off")
player.on_chat("NoFalloff", on_on_chat48)

def on_on_chat49():
    global am
    am = 0
    gameplay.set_game_rule(MOB_SPAWNING, True)
    player.say("Anti-Mob off")
player.on_chat("Anti-Moboff", on_on_chat49)

def on_on_chat50():
    mobs.apply_effect(RESISTANCE, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("NoDMGLegit", on_on_chat50)

def on_on_chat51():
    mobs.kill(mobs.target(ALL_ENTITIES))
player.on_chat("mob-suicide", on_on_chat51)

def on_on_chat52():
    mobs.apply_effect(RESISTANCE, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("NoDMG", on_on_chat52)

def on_on_chat53():
    global wts
    wts = 0
    player.say("WideTNTScaffold off")
player.on_chat("W.TNTScaffoldoff", on_on_chat53)

def on_on_chat54(speed):
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 999999, speed)
player.on_chat("customspeed", on_on_chat54)

def on_on_chat55():
    gameplay.set_weather(CLEAR)
player.on_chat("cw", on_on_chat55)

def on_on_chat56(item3):
    player.teleport(pos(0, item3, 0))
player.on_chat("cy", on_on_chat56)

def on_on_chat57():
    player.say("cx number - teleport on the x axis ")
    player.say("cy number - same as cx but on the y axis")
    player.say("cz number - same as cx but on the z axis")
    player.say("scaffold - places blocks under you")
    player.say("stopscaffold - stops scaffold")
    player.say("give itemid amount - gives you any item")
    player.say("link to id list: https://www.digminecraft.com/lists/item_id_list_edu.php")
    player.say("sblock blockid - changes scaffold block")
    player.say("dia - gives you 10 diamonds")
    player.say("type help2 for next page")
player.on_chat("help", on_on_chat57)

def on_on_chat58():
    global Scaffoldhack
    if Scaffoldhack == 1:
        Scaffoldhack = 0
        player.say("Scaffold off")
    else:
        Scaffoldhack = 1
        player.say("Scaffold on.")
    while Scaffoldhack == 1:
        blocks.fill(Blockid, pos(0, -1, 0), pos(0, -2, 0), FillOperation.REPLACE)
player.on_chat("scaffold", on_on_chat58)

def on_on_chat59(item4):
    player.teleport(pos(0, 0, item4))
player.on_chat("cz", on_on_chat59)

def on_on_chat60(x6, y6, z6):
    blocks.fill(BEDROCK,
        pos(x6, 0, x6),
        pos(z6, y6, z6),
        FillOperation.HOLLOW)
player.on_chat("custombase++", on_on_chat60)

def on_on_chat61(radius):
    global cnn
    if cnn == 1:
        cnn = 0
        player.say("customcirclenuker off")
    else:
        cnn = 1
        player.say("customcirclenuker on")
    while cnn == 1:
        shapes.circle(AIR, pos(0, 0, 0), radius, Axis.X, ShapeOperation.REPLACE)
        shapes.circle(AIR, pos(0, 0, 0), radius, Axis.Z, ShapeOperation.REPLACE)
player.on_chat("customcirclenuker", on_on_chat61)

def on_on_chat62():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("Superspeed", on_on_chat62)

def on_travelled_walk():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 3, 1)
player.on_travelled(WALK, on_travelled_walk)

def on_on_chat63():
    mobs.give(mobs.target(LOCAL_PLAYER), EGG, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), SNOWBALL, 64)
player.on_chat("kb.kit", on_on_chat63)

def on_on_chat64(_9):
    player.say(Math.sqrt(_9))
player.on_chat("calculatorsr", on_on_chat64)

def on_on_chat65():
    shapes.sphere(DIAMOND_BLOCK, pos(0, 0, 0), 5, ShapeOperation.REPLACE)
player.on_chat("Richsphere", on_on_chat65)

def on_on_chat66():
    global Scaffoldhack, nuker, cn, ws, wts, ow, cd, t
    mobs.clear_effect(mobs.target(LOCAL_PLAYER))
    Scaffoldhack = 0
    nuker = 0
    gameplay.set_game_rule(FALL_DAMAGE, True)
    gameplay.set_game_rule(FIRE_DAMAGE, True)
    cn = 0
    ws = 0
    wts = 0
    ow = 0
    cd = 0
    t = 0
    gameplay.set_game_rule(WEATHER_CYCLE, True)
    gameplay.set_game_rule(SHOW_COORDINATES, False)
    gameplay.set_game_rule(DROWNING_DAMAGE, True)
    gameplay.set_game_rule(MOB_SPAWNING, True)
    gameplay.set_game_rule(MOB_GRIEFING, True)
    gameplay.set_game_rule(TNT_EXPLODES, True)
player.on_chat("panic", on_on_chat66)

def on_on_chat67():
    global Ak
    Ak = 0
    gameplay.set_game_rule(KEEP_INVENTORY, False)
    player.say("Autokeep off")
player.on_chat("Autokeepoff", on_on_chat67)

def on_on_chat68():
    player.say("Gave you 16 steak.")
    mobs.give(mobs.target(LOCAL_PLAYER), COOKED_BEEF, 16)
player.on_chat("food", on_on_chat68)

def on_on_chat69():
    global am
    if am == 1:
        am = 0
        gameplay.set_game_rule(MOB_SPAWNING, True)
        player.say("Anti-Mob off")
    else:
        am = 1
        gameplay.set_game_rule(MOB_SPAWNING, False)
        player.say("Anti-Mob on")
player.on_chat("Anti-Mob", on_on_chat69)

def on_on_chat70():
    mobs.apply_effect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 999999, 1)
player.on_chat("water-br.", on_on_chat70)

def on_on_chat71():
    player.say("nuts")
    mobs.give(mobs.target(LOCAL_PLAYER), POTATO, 1)
player.on_chat("deez", on_on_chat71)

def on_on_chat72():
    mobs.give(mobs.target(LOCAL_PLAYER), TNT, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), MINECART_WITH_T_N_T, 8)
    mobs.give(mobs.target(LOCAL_PLAYER), POWERED_RAIL, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), DETECTOR_RAIL, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), CHEST, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TRAPPED_CHEST, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), UNPOWERED_COMPARATOR, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), REDSTONE_WIRE, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), UNPOWERED_REPEATER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), STICKY_PISTON, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), PISTON, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), OBSIDIAN, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), DISPENSER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), POINTED_DRIPSTONE, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TRIPWIRE_HOOK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TRIPWIRE, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), ARROW, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), END_CRYSTAL, 64)
player.on_chat("t.kit", on_on_chat72)

def on_on_chat73():
    global tp
    tp = 0
    player.say("tp-aura off")
player.on_chat("tp-auraoff", on_on_chat73)

def on_on_chat74():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 999999, 20)
player.on_chat("speedhack", on_on_chat74)

def on_on_chat75():
    mobs.teleport_to_player(mobs.target(ALL_PLAYERS), mobs.target(LOCAL_PLAYER))
player.on_chat("MassTP", on_on_chat75)

def on_on_chat76():
    blocks.fill(BEDROCK, pos(-5, -1, -5), pos(5, 8, 5), FillOperation.HOLLOW)
player.on_chat("Autobase++", on_on_chat76)

def on_on_chat77():
    global cn
    cn = 0
    player.say("circle nuker off")
player.on_chat("Circlenukeroff", on_on_chat77)

def on_on_chat78(hjamp):
    mobs.apply_effect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 999999, hjamp)
player.on_chat("customHighJump", on_on_chat78)

def on_on_chat79():
    for index4 in range(369):
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
player.on_chat("explode", on_on_chat79)

def on_on_chat80():
    gameplay.set_game_mode(CREATIVE, mobs.target(LOCAL_PLAYER))
player.on_chat("gmc", on_on_chat80)

def on_on_chat81():
    player.say("MassTP - Tp's everyone to you")
    player.say("NoDMG - take no dmg")
    player.say("autopp - automatically build's a pp")
    player.say("autofloor - automatically build's a floor")
    player.say("autowall - automatically builds a wall")
    player.say("spawn - tp's you to spawn")
    player.say("NoDMGLegit - take reduced dmg")
    player.say("Autobase+ - automatically builds a obsidian base  ")
    player.say("type help5 for next page")
player.on_chat("help4", on_on_chat81)

def on_on_chat82(ppid2):
    blocks.fill(ppid2, pos(-15, 0, -6), pos(12, 9, 3), FillOperation.REPLACE)
    blocks.fill(ppid2, pos(-6, 10, -6), pos(3, 30, 3), FillOperation.REPLACE)
player.on_chat("supercustompp", on_on_chat82)

def on_on_chat83():
    global cn
    if cn == 1:
        cn = 0
        player.say("circle nuker off")
    else:
        cn = 1
        player.say("circle nuker on")
    while cn == 1:
        shapes.circle(AIR, pos(1, 0, 1), 6, Axis.X, ShapeOperation.REPLACE)
    while cn == 1:
        shapes.circle(AIR, pos(1, 0, 1), 6, Axis.Z, ShapeOperation.REPLACE)
player.on_chat("Circlenuker", on_on_chat83)

def on_on_chat84():
    player.say("Gave you 10 diamonds.")
    mobs.give(mobs.target(LOCAL_PLAYER), DIAMOND, 10)
player.on_chat("dia", on_on_chat84)

def on_on_chat85(radius3):
    shapes.sphere(DIAMOND_BLOCK, pos(0, 0, 0), radius3, ShapeOperation.REPLACE)
player.on_chat("customrichsphere", on_on_chat85)

def on_on_chat86():
    global lxr
    lxr = 0
    player.say("UPDxray off")
    blocks.fill(AIR, pos(-18, 0, -18), pos(18, 8, 18), FillOperation.REPLACE)
player.on_chat("UPDxrayoff", on_on_chat86)

def on_on_chat87():
    blocks.fill(OBSIDIAN,
        pos(-5, -1, -5),
        pos(5, 8, 5),
        FillOperation.HOLLOW)
player.on_chat("Autobase+", on_on_chat87)

def on_on_chat88():
    global xr
    xr = 0
    player.say("xray off")
player.on_chat("xrayoff", on_on_chat88)

def on_on_chat89():
    global Ak
    if Ak == 1:
        Ak = 0
        gameplay.set_game_rule(KEEP_INVENTORY, False)
        player.say("Autokeep off")
    else:
        Ak = 1
        gameplay.set_game_rule(KEEP_INVENTORY, True)
        player.say("Autokeep on")
player.on_chat("Autokeep", on_on_chat89)

def on_on_chat90():
    blocks.fill(DIRT, pos(-5, -1, -5), pos(5, -1, 5), FillOperation.REPLACE)
player.on_chat("autofloor", on_on_chat90)

def on_on_chat91():
    player.say("customnuke (x z) (power) - customize nuke's size with custom power")
    player.say("customscaffold  (xz) (block)  - scaffold but with a custom width & block.")
    player.say("customscaffoldoff - turns customscaffoldoff")
    player.say("effect (effect) (duration) (amp) - gives you a custom effect with a custom duration and amplifier.")
    player.say("custombase (xyz) - autobase but with custom dimensions")
    player.say("custombase+ (xyz) - autobase+ but with custom dimensions")
    player.say("custombase++ (xyz) - autobase++ but with custom dimensions")
    player.say("NOTE: All custombase should be at least y3.")
    player.say("customnuker (xyz) - nuker but with customizable size")
    player.say("customnukeroff - turns off customnuker")
    player.say("customwall (xyz) - lets you make a wall that surrounds you with customizable dimensions")
    player.say("customfloor (xz) (block) - lets you make a floor made out of a custom block & dimensions.")
    player.say("calculatora (1st term)  (2nd term) - a addition calculator with customizable terms but with a limit of 2 terms. ")
    player.say("calculators (1st term) (2nd term) - a subtraction calculator with customizable terms but with a limit of 2 terms. ")
    player.say("calculatorm (1st term) (2nd term) - a multiplication calculator with customizable terms but with a limit of 2 terms. ")
    player.say("calculatord (1st term) (2nd term) - a dividion calculator with customizable terms but with a limit of 2 terms. ")
    player.say("calculatorsr (1st term) (2nd term) - a squareroot calculator with customizable terms but with a limit of 2 terms. ")
    player.say("type help11 for next page of commands")
player.on_chat("help10", on_on_chat91)

def on_on_chat92(amount22):
    for index5 in range(amount22):
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
player.on_chat("customexplode", on_on_chat92)

def on_on_chat93(health):
    mobs.apply_effect(ABSORPTION, mobs.target(NEAREST_PLAYER), 999999, health)
    mobs.apply_effect(HEALTH_BOOST, mobs.target(NEAREST_PLAYER), 999999, health)
    mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 999999, 255)
player.on_chat("customhealth", on_on_chat93)

def on_on_chat94():
    global c
    if c == 1:
        c = 0
        gameplay.set_game_rule(SHOW_COORDINATES, False)
        player.say("Coordinates off")
    else:
        c = 1
        gameplay.set_game_rule(SHOW_COORDINATES, True)
        player.say("Coordinates on")
player.on_chat("Coordinates", on_on_chat94)

def on_on_chat95():
    global ag
    ag = 0
    gameplay.set_game_rule(MOB_GRIEFING, True)
    gameplay.set_game_rule(TNT_EXPLODES, True)
    player.say("Anti-Grief off")
player.on_chat("Anti-Griefoff", on_on_chat95)

def on_on_chat96(_5, _6):
    player.say(_5 * _6)
player.on_chat("calculatorm", on_on_chat96)

def on_on_chat97():
    player.say("annoy (phrase) - repeats the phrase you said many times. (Now only numbers such as 69).")
    player.say("customcirclenuker (radius)- circlenuker but with customizable radius.")
    player.say("customcirclenukeroff - turns off customcirclenuker")
    player.say("lottery (itemid) (amount) - gives a random person a custom item & amount of that item")
    player.say("customkb (amount) (amount) - gives you a custom amount of the kb kit")
    player.say("customexplode (amount) - explode but with custom tnt output")
    player.say("customrichcircle (radius) - richcircle but with a custom radius")
    player.say("customrichsphere (radius) - richsphere but with a custom radius")
    player.say("custombedrock (amount) - gives yourself a custom amount of bedrock")
    player.say("customxp (xp amount) - rains a custom amount of satisfying xp bottles")
    player.say("customHighJump (height) - HighJump but with a custom height")
    player.say("give (itemid) (amount) - gives yourself anything with any amount")
    player.say("customspeed (speed) - run at a custom speed")
    player.say("customhealth (health) - get a custom amount of health (health = input x4)")
    player.say("InfinihealthLegit - have more health")
    player.say("custompp - autopp but with custom block")
    player.say("superpp - autopp but big")
    player.say("supercustompp - superpp but with custom block")
    player.say("ppexplode - a tnt pp that detonates itself")
    player.say("ppnuker - mines blocks the shape of a pp")
    player.say("ppnukeroff - turns off ppnuker")
    player.say("xray - a somewhat laggy but working xray (not recommended for moblie;use by walking) ")
    player.say("UPDxray - a even better xray")
    player.say("xrayoff - turns off xray")
    player.say("UPDxrayoff - turns off laggyxray")
    player.say("anti-lagc - removes unnecessary lag but keeps you on creative mode")
    player.say("anti-lags - removes unnecessary lag but keeps you on survival mode")
    player.say("tp-aura - tps all entities to you and kills them (also automatically swims you out of water)")
    player.say("tp-auraoff - turns tp-aura off")
player.on_chat("help11", on_on_chat97)

def on_on_chat98():
    global lxr
    if lxr == 1:
        lxr = 0
        player.say("UPDxray off")
    else:
        lxr = 1
        player.say("UPDxray on")
    while lxr == 1:
        blocks.fill(STONE,
            pos(-18, 0, -18),
            pos(18, 8, 18),
            FillOperation.REPLACE)
        blocks.fill(AIR, pos(-18, 0, -18), pos(18, 8, 18), FillOperation.REPLACE)
        player.run_chat_command("Speedfastbreak")
player.on_chat("UPDxray", on_on_chat98)

def on_on_chat99():
    global tp
    if tp == 1:
        tp = 0
        player.say("tp-aura off")
    else:
        tp = 1
        player.say("tp-aura on")
    while tp == 1:
        mobs.teleport_to_player(mobs.target(ALL_ENTITIES), mobs.target(LOCAL_PLAYER))
        player.run_chat_command("infinihealth")
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
        blocks.fill(BEDROCK,
            pos(-1, -1, -1),
            pos(1, -1, 1),
            FillOperation.REPLACE)
player.on_chat("tp-aura", on_on_chat99)

def on_on_chat100():
    player.say("Autokeep - keep inventory!")
    player.say("HighJump - jump higher")
    player.say("NoWeather - It'll always be a sunny day.")
    player.say("NoWeatheroff - Turns off NoWeather")
    player.say("Speedfastbreak - break blocks even faster than fastbreak.")
    player.say("Autokeepoff - turns off Autokeep")
    player.say("Tired - a bed for bedtime")
    player.say("TNTScaffold - Rain tnt on anything under you")
    player.say("TNTScaffoldoff - turns off TNTScaffold")
    player.say("type help8 for more commands")
player.on_chat("help7", on_on_chat100)

def on_on_chat101(num13):
    global Blockid
    Blockid = num13
player.on_chat("sblock", on_on_chat101)

def on_on_chat102():
    player.say("Set time to day.")
    gameplay.time_set(gameplay.time(DAY))
player.on_chat("day", on_on_chat102)

def on_on_chat103():
    global t
    t = 0
    player.say("TNTScaffold off")
player.on_chat("TNTScaffoldoff", on_on_chat103)

def on_on_chat104():
    global ppn
    if ppn == 1:
        ppn = 0
        player.say("ppnuker off")
    else:
        ppn = 1
        player.say("ppnuker on")
    while ppn == 1:
        blocks.fill(AIR, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.REPLACE)
        blocks.fill(AIR, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.REPLACE)
player.on_chat("ppnuker", on_on_chat104)

def on_on_chat105():
    global ow
    ow = 0
    player.say("OpenWaterESP off")
player.on_chat("OpenWaterESPoff", on_on_chat105)

def on_on_chat106():
    gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
    mobs.kill(mobs.target(ALL_PLAYERS))
player.on_chat("mass-suicide", on_on_chat106)

def on_on_chat107():
    blocks.fill(TNT, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.REPLACE)
    blocks.fill(TNT, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.REPLACE)
    blocks.fill(REDSTONE_BLOCK,
        pos(-1, 11, -1),
        pos(-1, 11, -1),
        FillOperation.REPLACE)
player.on_chat("ppexplode", on_on_chat107)

def on_on_chat108():
    blocks.fill(REDSTONE_BLOCK,
        pos(-6, 40, -6),
        pos(6, 40, 6),
        FillOperation.REPLACE)
    blocks.fill(REDSTONE_LAMP,
        pos(-6, 39, -6),
        pos(6, 39, 6),
        FillOperation.REPLACE)
    loops.pause(699)
    player.say("3")
    loops.pause(699)
    blocks.fill(AIR, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.REPLACE)
    loops.pause(699)
    player.say("2")
    loops.pause(699)
    blocks.fill(REDSTONE_LAMP,
        pos(-6, 39, -6),
        pos(6, 39, 6),
        FillOperation.REPLACE)
    loops.pause(699)
    player.say("1")
    loops.pause(699)
    player.say("nuke initiated")
    loops.pause(69)
    blocks.fill(AIR, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.REPLACE)
    loops.pause(69)
    for index6 in range(28):
        blocks.fill(TNT, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.REPLACE)
    for index7 in range(69):
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(8, 28, -8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(-8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(8, 28, -8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, 8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-12, 28, -12), pos(12, 28, -12)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-12, 28, -12), pos(-12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(12, 28, -12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, 12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-15, 28, -15), pos(15, 28, -15)))
        mobs.spawn(PRIMED_TNT,
            positions.add(pos(-15, 28, -15), pos(-15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(15, 28, -15), pos(15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, 15), pos(15, 28, 15)))
player.on_chat("Nuke", on_on_chat108)

def on_on_chat109():
    player.execute("give @s barrier 64")
player.on_chat("barrier", on_on_chat109)

def on_travelled_sneak():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 3, 8)
player.on_travelled(SNEAK, on_travelled_sneak)

def on_on_chat110(x, z, block):
    blocks.fill(Blockid, pos(x, -1, x), pos(z, -1, z), FillOperation.REPLACE)
player.on_chat("customfloor", on_on_chat110)

def on_on_chat111():
    global cs
    cs = 0
    player.say("customscaffold off")
player.on_chat("customscaffoldoff", on_on_chat111)

# https://www.youtube.com/watch?v=IIJM3S9H5m0

def on_on_chat112():
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_HELMET, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_CHESTPLATE, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_LEGGINGS, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_BOOTS, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), DIAMOND_SWORD, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_PICKAXE, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_AXE, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), NETHERITE_SWORD, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), ENCHANTED_APPLE, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TOTEM, 5)
    mobs.give(mobs.target(LOCAL_PLAYER), SHIELD, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), ARROW, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), BOW, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), BOAT, 2)
player.on_chat("kit", on_on_chat112)

def on_on_chat113():
    global ad
    ad = 0
    gameplay.set_game_rule(DROWNING_DAMAGE, True)
    player.say("Anti-Drown off")
player.on_chat("Anti-Drownoff", on_on_chat113)

def on_on_chat114():
    mobs.apply_effect(ABSORPTION, mobs.target(NEAREST_PLAYER), 999999, 8)
    mobs.apply_effect(HEALTH_BOOST, mobs.target(NEAREST_PLAYER), 999999, 8)
    mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 999999, 108)
player.on_chat("InfinihealthLegit", on_on_chat114)

def on_on_chat115():
    player.say("Autobase++ - builds a bedrock base")
    player.say("NoFire - take no fire damage")
    player.say("Circlenuker - nuker but a circle")
    player.say("Circlenukeroff - turns off circle nuker")
    player.say("NoFall - take no fall damage")
    player.say("NoFireoff - turns off nofire")
    player.say("NoFalloff - turns off nofall")
    player.say("Richcircle - impress anyone with ur richness")
    player.say("Richsphere - the same as Richcircle but better.")
    player.say("Auto-CC - automatically charges creepers")
    player.say("r.kit - All the redstone materials you'll need")
    player.say("t.kit - perfect for making traps")
    player.say("type help6 for next page")
player.on_chat("help5", on_on_chat115)

def on_on_chat116():
    blocks.fill(PLANKS_OAK,
        pos(-5, 0, -5),
        pos(5, 5, 5),
        FillOperation.HOLLOW)
player.on_chat("autobase", on_on_chat116)

def on_on_chat117():
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, 64)
player.on_chat("bedrock", on_on_chat117)

def on_on_chat118(_3, _4):
    player.say(_3 - _4)
player.on_chat("calculators", on_on_chat118)

def on_on_chat119():
    gameplay.set_game_mode(CREATIVE, mobs.target(LOCAL_PLAYER))
    loops.pause(69)
    mobs.kill(mobs.target(ALL_ENTITIES))
    loops.pause(69)
    gameplay.set_game_mode(SURVIVAL, mobs.target(LOCAL_PLAYER))
player.on_chat("anti-lags", on_on_chat119)

def on_on_chat120():
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 999999, 255)
player.on_chat("one-shot", on_on_chat120)

def on_on_chat121(x4, y4, z4):
    blocks.fill(PLANKS_OAK,
        pos(x4, 0, x4),
        pos(z4, y4, z4),
        FillOperation.HOLLOW)
player.on_chat("custombase", on_on_chat121)

def on_on_chat122(amount3, amount4):
    mobs.give(mobs.target(NEAREST_PLAYER), SNOWBALL, amount3)
    mobs.give(mobs.target(NEAREST_PLAYER), EGG, amount4)
player.on_chat("customkb", on_on_chat122)

def on_on_chat123():
    mobs.give(mobs.target(LOCAL_PLAYER), TRIDENT, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "loyalty", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "impaling", 5)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "channeling", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "mending", 1)
player.on_chat("GodTridents1", on_on_chat123)

def on_on_chat124():
    player.say("Anti-Drown - prevents drowning damage")
    player.say("Anti-Drownoff - turns off Anti-Drown")
    player.say("Anti-Mob - stops all mobs from spawning")
    player.say("Anti-Moboff - turns off Anti-Mob")
    player.say("Anti-Grief - prevents anyone from griefing")
    player.say("Anti-Griefoff - turns off Auto-Grief")
    player.say("infinihealth - infinite health")
    player.say("superspeed - move so fast that no one can see you")
    player.say("type help10 for more commands")
player.on_chat("help9", on_on_chat124)

def on_on_chat125():
    global cd
    if cd == 1:
        cd = 0
        player.say("ChestDetector off")
    else:
        cd = 1
        player.say("ChestDetector on")
    while cd == 0:
        mobs.execute_detect(CHEST,
            positions.add(pos(0, 319, 0), pos(0, -319, 0)),
            "Chest found!")
player.on_chat("ChestDetector", on_on_chat125)

def on_on_chat126():
    global xr
    if xr == 1:
        xr = 0
        player.say("xray off")
    else:
        xr = 1
        player.say("xray on")
    while xr == 1:
        blocks.fill(AIR, pos(-8, 0, -8), pos(8, 6, 8), FillOperation.REPLACE)
        mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 69, 38)
player.on_chat("xray", on_on_chat126)

def on_on_chat127():
    global t
    if t == 1:
        t = 0
        player.say("TNTScaffold off")
    else:
        t = 1
        player.say("TNTScaffold on")
    while t == 1:
        blocks.fill(REDSTONE_BLOCK,
            pos(0, -1, 0),
            pos(0, -2, 0),
            FillOperation.REPLACE)
        blocks.fill(TNT, pos(0, -3, 0), pos(0, -3, 0), FillOperation.REPLACE)
player.on_chat("TNTScaffold", on_on_chat127)

def on_on_chat128():
    global cnn
    cnn = 0
    player.say("customcirclenuker off")
player.on_chat("customcirclenukeroff", on_on_chat128)

def on_on_chat129():
    global ppn
    ppn = 0
    player.say("ppnuker off")
player.on_chat("ppnukeroff", on_on_chat129)

def on_on_chat130():
    blocks.fill(DIRT, pos(-5, 0, -5), pos(5, 6, 5), FillOperation.REPLACE)
    blocks.fill(DIRT, pos(-5, 0, -5), pos(-5, 6, 5), FillOperation.REPLACE)
    blocks.fill(DIRT, pos(5, 0, -5), pos(5, 6, 5), FillOperation.REPLACE)
    blocks.fill(DIRT, pos(-5, 0, 5), pos(5, 6, 5), FillOperation.REPLACE)
player.on_chat("autowall", on_on_chat130)

def on_on_chat131():
    mobs.give(mobs.target(LOCAL_PLAYER), OBSERVER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), STICKY_PISTON, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), PISTON, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), REDSTONE_BLOCK, 128)
    mobs.give(mobs.target(LOCAL_PLAYER), DROPPER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), DISPENSER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), UNPOWERED_REPEATER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), UNPOWERED_COMPARATOR, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), REDSTONE_TORCH, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), REDSTONE_LAMP, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TARGET, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), CHEST, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), DAYLIGHT_SENSOR, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), HOPPER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), LEVER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), BAMBOO_BUTTON, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), STONE_PRESSURE_PLATE, 64)
player.on_chat("r.kit", on_on_chat131)

def on_on_chat132():
    mobs.apply_effect(HASTE, mobs.target(LOCAL_PLAYER), 999999, 18)
player.on_chat("fastbreak", on_on_chat132)

def on_on_chat133(ppid):
    blocks.fill(ppid, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.REPLACE)
    blocks.fill(ppid, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.REPLACE)
player.on_chat("custompp", on_on_chat133)

def on_on_chat134(_1, _2):
    player.say(_1 + _2)
player.on_chat("calculatora", on_on_chat134)

def on_on_chat135(num14):
    mobs.give(mobs.target(LOCAL_PLAYER), WATER_BUCKET, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), HAY_BLOCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), HONEY_BLOCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), SLIME_BLOCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), COBWEB, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), VINES, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), LADDER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), TNT, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), FLINT_AND_STEEL, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), ENDER_PEARL, 16)
    mobs.give(mobs.target(LOCAL_PLAYER), END_CRYSTAL, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), OBSIDIAN, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), SADDLE, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), WARPED_FUNGUS_ON_A_STICK, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), FISHING_ROD, 1)
    mobs.give(mobs.target(LOCAL_PLAYER), TOTEM, 5)
player.on_chat("c.kit", on_on_chat135)

def on_on_chat136():
    blocks.fill(DIRT, pos(-15, 0, -6), pos(12, 9, 3), FillOperation.REPLACE)
    blocks.fill(DIRT, pos(-6, 10, -6), pos(3, 30, 3), FillOperation.REPLACE)
player.on_chat("superpp", on_on_chat136)

def on_on_chat137():
    for index8 in range(696):
        mobs.spawn(XP_BOTTLE, pos(0, 0, 0))
player.on_chat("XP+", on_on_chat137)

def on_on_chat138(xpamt):
    for index9 in range(xpamt):
        mobs.spawn(XP_BOTTLE, pos(0, 0, 0))
player.on_chat("customxp", on_on_chat138)

def on_on_chat139():
    global ad
    if ad == 1:
        ad = 0
        gameplay.set_game_rule(DROWNING_DAMAGE, True)
        player.say("Anti-Drown off")
    else:
        ad = 1
        gameplay.set_game_rule(DROWNING_DAMAGE, False)
        player.say("Anti-Drown on")
player.on_chat("Anti-Drown", on_on_chat139)

def on_on_chat140():
    global nw
    if nw == 1:
        nw = 0
        gameplay.set_game_rule(WEATHER_CYCLE, True)
        player.say("NoWeather off")
    else:
        nw = 1
        gameplay.set_game_rule(WEATHER_CYCLE, False)
        player.say("NoWeather on")
player.on_chat("NoWeather", on_on_chat140)

def on_on_chat141():
    blocks.fill(REDSTONE_BLOCK,
        pos(-6, 51, -6),
        pos(6, 51, 6),
        FillOperation.REPLACE)
    for index10 in range(28):
        blocks.fill(TNT, pos(-6, 50, -6), pos(6, 50, 6), FillOperation.REPLACE)
player.on_chat("AerialStrike", on_on_chat141)

def on_on_chat142():
    player.say("widescaffold - scaffold but wide")
    player.say("widescaffoldoff - stops wide scaffold")
    player.say("EntityESP - see all entities")
    player.say("PlayerESP - see all players")
    player.say("c.kit - perfect for clutching")
    player.say("criticals -automatically does crit damage.")
    player.say("kb.kit - knock anything back, perfect for void traps")
    player.say("godbow - gives you a god bow (note: hold on the bow in hotbar).")
    player.say("GodTridents1 - Enchanted tridents coming right up! (Must hold on item in hotbar)")
    player.say("GodTridents2 - Enchanted tridents coming right up! (Riptide, must hold on item in hotbar)")
    player.say("type help7 for next page.")
player.on_chat("help6", on_on_chat142)

def on_on_chat143(amount5):
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, amount5)
player.on_chat("custombedrock", on_on_chat143)

def on_on_chat144():
    global wts
    if wts == 1:
        wts = 0
        player.say("WideTNTScaffold off")
    else:
        wts = 1
        player.say("WideTNTScaffold on")
    while wts == 1:
        blocks.fill(REDSTONE_BLOCK,
            pos(-1, -1, -1),
            pos(1, -2, 1),
            FillOperation.REPLACE)
        blocks.fill(TNT, pos(-1, -3, -1), pos(1, -3, 1), FillOperation.REPLACE)
player.on_chat("W.TNTScaffold", on_on_chat144)

ad = 0
ppn = 0
xr = 0
lxr = 0
tp = 0
Ak = 0
t = 0
cn = 0
cnn = 0
wts = 0
am = 0
nw = 0
cd = 0
ws = 0
cs = 0
customnuker = 0
nuker = 0
c = 0
NoFi = 0
NoFa = 0
ag = 0
ow = 0
Scaffoldhack = 0
Blockid = 0
item5 = DIRT
Blockid = 3
Scaffoldhack = 0
player.say("EDU CLIENT V5")
player.say("type help for a list of commands")