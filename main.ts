player.onChat("OpenWaterESP", function on_on_chat() {
    
    if (ow == 1) {
        ow = 0
        player.say("OpenWaterESP off")
    } else {
        ow = 1
        player.say("OpenWaterESP on")
    }
    
    while (ow == 1) {
        mobs.executeDetect(WATER, positions.add(pos(-2, -1, -2), pos(2, -5, 2)), "OpenWater found!")
    }
})
mobs.onMobKilled(CHICKEN, function on_mob_killed_chicken() {
    
})
//  if you see this, Hi!
player.onChat("cx", function on_on_chat2(item: number) {
    player.teleport(pos(item, 0, 0))
})
player.onChat("Tired", function on_on_chat3() {
    blocks.fill(BED, pos(1, 0, 1), pos(2, 0, 2), FillOperation.Replace)
})
player.onChat("autopp", function on_on_chat4() {
    blocks.fill(DIRT, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.Replace)
    blocks.fill(DIRT, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.Replace)
})
player.onChat("custombase+", function on_on_chat5(x5: number, y5: number, z5: number) {
    blocks.fill(OBSIDIAN, pos(x5, 0, x5), pos(z5, y5, z5), FillOperation.Hollow)
})
player.onChat("help3", function on_on_chat6() {
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
})
player.onChat("effect", function on_on_chat7(effect: number, dur: number, amp: number) {
    mobs.applyEffect(effect, mobs.target(LOCAL_PLAYER), dur, amp)
})
player.onChat("Anti-Grief", function on_on_chat8() {
    
    if (ag == 1) {
        ag = 0
        gameplay.setGameRule(MOB_GRIEFING, true)
        gameplay.setGameRule(TNT_EXPLODES, true)
        player.say("Anti-Grief off")
    } else {
        ag = 1
        gameplay.setGameRule(MOB_GRIEFING, false)
        gameplay.setGameRule(TNT_EXPLODES, false)
        player.say("Anti-Grief on")
    }
    
})
player.onChat("suicide", function on_on_chat9() {
    gameplay.setGameMode(SURVIVAL, mobs.target(LOCAL_PLAYER))
    mobs.kill(mobs.target(LOCAL_PLAYER))
})
player.onChat("Richcircle", function on_on_chat10() {
    shapes.circle(DIAMOND_BLOCK, pos(5, 0, 5), 5, Axis.X, ShapeOperation.Replace)
    shapes.circle(DIAMOND_BLOCK, pos(5, 0, 5), 5, Axis.Y, ShapeOperation.Replace)
    shapes.circle(DIAMOND_BLOCK, pos(5, 0, 5), 5, Axis.Z, ShapeOperation.Replace)
})
player.onChat("help2", function on_on_chat11(num1: any) {
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
})
player.onChat("customrichcircle", function on_on_chat12(radius2: number) {
    shapes.circle(DIAMOND_BLOCK, pos(0, 0, 0), radius2, Axis.X, ShapeOperation.Replace)
    shapes.circle(DIAMOND_BLOCK, pos(0, 0, 0), radius2, Axis.Y, ShapeOperation.Replace)
    shapes.circle(DIAMOND_BLOCK, pos(0, 0, 0), radius2, Axis.Z, ShapeOperation.Replace)
})
player.onChat("give", function on_on_chat13(item2: number, Amount: number) {
    mobs.give(mobs.target(LOCAL_PLAYER), blocks.blockById(item2), Amount)
})
player.onChat("godbow", function on_on_chat14() {
    mobs.give(mobs.target(NEAREST_PLAYER), BOW, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "infinity", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "punch", 2)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "power", 5)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "flame", 1)
})
player.onChat("NoFall", function on_on_chat15() {
    
    if (NoFa == 1) {
        NoFa = 0
        gameplay.setGameRule(FALL_DAMAGE, true)
        player.say("NoFall off")
    } else {
        NoFi = 1
        gameplay.setGameRule(FALL_DAMAGE, false)
        player.say("NoFall on")
    }
    
})
player.onTravelled(SWIM_WATER, function on_travelled_swim_water() {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 3, 3)
})
player.onChat("give", function on_on_chat16(itemid3: number, amount6: number) {
    mobs.give(mobs.target(LOCAL_PLAYER), itemid3, amount6)
})
player.onChat("spawn", function on_on_chat17() {
    mobs.teleportToPosition(mobs.target(LOCAL_PLAYER), world(0, 319, 0))
    mobs.applyEffect(RESISTANCE, mobs.target(NEAREST_PLAYER), 25, 255)
})
player.onChat("Coordinatesoff", function on_on_chat18() {
    
    c = 0
    gameplay.setGameRule(SHOW_COORDINATES, false)
    player.say("Coordinates off")
})
player.onChat("anti-lagc", function on_on_chat19() {
    mobs.kill(mobs.target(ALL_ENTITIES))
})
player.onChat("xp", function on_on_chat20(num12: number) {
    gameplay.xp(num12, mobs.target(LOCAL_PLAYER))
    player.say("gave you " + ("" + num12) + " xp")
})
player.onChat("lottery", function on_on_chat21(itemid: number, amount2: number) {
    mobs.give(mobs.target(RANDOM_PLAYER), itemid, amount2)
})
player.onChat("nukeroff", function on_on_chat22() {
    
    nuker = 0
    player.say("Nuker off")
})
player.onChat("customnuker", function on_on_chat23(x3: number, y3: number, z3: number) {
    
    if (customnuker == 1) {
        customnuker = 0
        player.say("customnuker off")
    } else {
        customnuker = 1
        player.say("customnuker on")
    }
    
    while (customnuker == 1) {
        blocks.fill(AIR, pos(x3, y3, x3), pos(z3, 0, z3), FillOperation.Destroy)
    }
})
player.onChat("HighJump", function on_on_chat24() {
    mobs.applyEffect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 999999, 5)
})
player.onChat("customscaffold", function on_on_chat25(x7: number, z7: number, blockid3: number) {
    
    if (cs == 1) {
        cs = 0
        player.say("customscaffold off")
    } else {
        cs = 1
        player.say("customscaffold on")
    }
    
    while (cs == 1) {
        blocks.fill(blockid3, pos(x7, -1, x7), pos(z7, -2, z7), FillOperation.Replace)
    }
})
player.onChat("widescaffoldoff", function on_on_chat26() {
    
    ws = 0
    player.say("Widescaffold off")
})
player.onChat("calculatord", function on_on_chat27(_7: number, _8: number) {
    player.say(_7 / _8)
})
player.onChat("customnukeroff", function on_on_chat28() {
    
    customnuker = 0
    player.say("customnuker off")
})
player.onChat("nuker", function on_on_chat29() {
    
    if (nuker == 1) {
        nuker = 0
        player.say("Nuker off")
    } else {
        nuker = 1
        player.say("Nuker on.")
    }
    
    while (nuker == 1) {
        blocks.fill(AIR, pos(-5, 0, -5), pos(5, 6, 5), FillOperation.Destroy)
    }
})
player.onChat("ChestDetectoroff", function on_on_chat30() {
    
    cd = 0
    player.say("ChestDetector off")
})
player.onChat("i.kit", function on_on_chat31() {
    mobs.give(mobs.target(LOCAL_PLAYER), DRAGON_EGG, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), STRUCTURE_BLOCK, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), WATER, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), LAVA, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), FIRE, 64)
})
player.onChat("GodTridents2", function on_on_chat32() {
    mobs.give(mobs.target(LOCAL_PLAYER), TRIDENT, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "mending", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "riptide", 3)
})
player.onChat("portal", function on_on_chat33() {
    mobs.give(mobs.target(LOCAL_PLAYER), OBSIDIAN, 16)
    loops.pause(50)
    mobs.give(mobs.target(LOCAL_PLAYER), FLINT_AND_STEEL, 1)
})
player.onChat("annoy", function on_on_chat34(phrase: any) {
    for (let index = 0; index < 69; index++) {
        player.say(phrase)
    }
})
player.onChat("customwall", function on_on_chat35(x2: number, y2: number, z2: number) {
    blocks.fill(Blockid, pos(x2, 0, x2), pos(z2, y2, x2), FillOperation.Replace)
    blocks.fill(Blockid, pos(x2, 0, x2), pos(x2, y2, z2), FillOperation.Replace)
    blocks.fill(Blockid, pos(z2, 0, x2), pos(z2, y2, z2), FillOperation.Replace)
    blocks.fill(Blockid, pos(x2, 0, z2), pos(z2, y2, z2), FillOperation.Replace)
})
player.onChat("infinihealth", function on_on_chat36() {
    mobs.applyEffect(ABSORPTION, mobs.target(LOCAL_PLAYER), 999999, 255)
    mobs.applyEffect(HEALTH_BOOST, mobs.target(LOCAL_PLAYER), 999999, 255)
    mobs.applyEffect(REGENERATION, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onChat("NoFire", function on_on_chat37() {
    
    if (NoFi == 1) {
        NoFi = 0
        gameplay.setGameRule(FIRE_DAMAGE, true)
        player.say("NoFire off")
    } else {
        NoFi = 1
        gameplay.setGameRule(FIRE_DAMAGE, false)
        player.say("NoFire on")
    }
    
})
player.onChat("Speedfastbreak", function on_on_chat38() {
    mobs.applyEffect(HASTE, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onChat("criticals", function on_on_chat39() {
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 999999, 1)
})
player.onChat("NoWeatheroff", function on_on_chat40() {
    
    nw = 0
    gameplay.setGameRule(WEATHER_CYCLE, true)
    player.say("NoWeather off")
})
player.onChat("help8", function on_on_chat41() {
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
})
player.onChat("fullbright", function on_on_chat42() {
    mobs.applyEffect(NIGHT_VISION, mobs.target(LOCAL_PLAYER), 999999, 1)
})
player.onChat("customnuke", function on_on_chat43(x8: number, z8: number, power: number) {
    blocks.fill(REDSTONE_BLOCK, pos(x8, 50, x8), pos(z8, 50, z8), FillOperation.Replace)
    blocks.fill(REDSTONE_LAMP, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.Replace)
    loops.pause(699)
    player.say("3")
    loops.pause(699)
    blocks.fill(AIR, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.Replace)
    loops.pause(699)
    player.say("2")
    loops.pause(699)
    blocks.fill(REDSTONE_LAMP, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.Replace)
    loops.pause(699)
    player.say("1")
    loops.pause(699)
    player.say("nuke initiated")
    loops.pause(69)
    blocks.fill(AIR, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.Replace)
    loops.pause(69)
    for (let index2 = 0; index2 < power; index2++) {
        blocks.fill(TNT, pos(x8, 49, x8), pos(z8, 49, z8), FillOperation.Replace)
    }
    loops.pause(69)
    for (let index3 = 0; index3 < power; index3++) {
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(8, 28, -8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(-8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(8, 28, -8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, 8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, -12), pos(12, 28, -12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, -12), pos(-12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(12, 28, -12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, 12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, -15), pos(15, 28, -15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, -15), pos(-15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(15, 28, -15), pos(15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, 15), pos(15, 28, 15)))
    }
})
player.onChat("gms", function on_on_chat44() {
    gameplay.setGameMode(SURVIVAL, mobs.target(LOCAL_PLAYER))
})
player.onChat("widescaffold", function on_on_chat45() {
    
    if (ws == 1) {
        ws = 0
        player.say("Widescaffold off")
    } else {
        ws = 1
        player.say("Widescaffold on")
    }
    
    while (ws == 1) {
        blocks.fill(Blockid, pos(-1, -1, -1), pos(1, -2, 1), FillOperation.Replace)
    }
})
player.onChat("stopscaffold", function on_on_chat46() {
    
    Scaffoldhack = 0
    player.say("Scaffold off.")
})
player.onChat("NoFireoff", function on_on_chat47() {
    
    NoFi = 0
    gameplay.setGameRule(FIRE_DAMAGE, true)
    player.say("NoFire off")
})
player.onChat("NoFalloff", function on_on_chat48() {
    
    NoFa = 0
    gameplay.setGameRule(FALL_DAMAGE, true)
    player.say("NoFall off")
})
player.onChat("Anti-Moboff", function on_on_chat49() {
    
    am = 0
    gameplay.setGameRule(MOB_SPAWNING, true)
    player.say("Anti-Mob off")
})
player.onChat("NoDMGLegit", function on_on_chat50() {
    mobs.applyEffect(RESISTANCE, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onChat("mob-suicide", function on_on_chat51() {
    mobs.kill(mobs.target(ALL_ENTITIES))
})
player.onChat("NoDMG", function on_on_chat52() {
    mobs.applyEffect(RESISTANCE, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onChat("W.TNTScaffoldoff", function on_on_chat53() {
    
    wts = 0
    player.say("WideTNTScaffold off")
})
player.onChat("customspeed", function on_on_chat54(speed: number) {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 999999, speed)
})
player.onChat("cw", function on_on_chat55() {
    gameplay.setWeather(CLEAR)
})
player.onChat("cy", function on_on_chat56(item3: number) {
    player.teleport(pos(0, item3, 0))
})
player.onChat("help", function on_on_chat57() {
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
})
player.onChat("scaffold", function on_on_chat58() {
    
    if (Scaffoldhack == 1) {
        Scaffoldhack = 0
        player.say("Scaffold off")
    } else {
        Scaffoldhack = 1
        player.say("Scaffold on.")
    }
    
    while (Scaffoldhack == 1) {
        blocks.fill(Blockid, pos(0, -1, 0), pos(0, -2, 0), FillOperation.Replace)
    }
})
player.onChat("cz", function on_on_chat59(item4: number) {
    player.teleport(pos(0, 0, item4))
})
player.onChat("custombase++", function on_on_chat60(x6: number, y6: number, z6: number) {
    blocks.fill(BEDROCK, pos(x6, 0, x6), pos(z6, y6, z6), FillOperation.Hollow)
})
player.onChat("customcirclenuker", function on_on_chat61(radius: number) {
    
    if (cnn == 1) {
        cnn = 0
        player.say("customcirclenuker off")
    } else {
        cnn = 1
        player.say("customcirclenuker on")
    }
    
    while (cnn == 1) {
        shapes.circle(AIR, pos(0, 0, 0), radius, Axis.X, ShapeOperation.Replace)
        shapes.circle(AIR, pos(0, 0, 0), radius, Axis.Z, ShapeOperation.Replace)
    }
})
player.onChat("Superspeed", function on_on_chat62() {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onTravelled(WALK, function on_travelled_walk() {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 3, 1)
})
player.onChat("kb.kit", function on_on_chat63() {
    mobs.give(mobs.target(LOCAL_PLAYER), EGG, 64)
    mobs.give(mobs.target(LOCAL_PLAYER), SNOWBALL, 64)
})
player.onChat("calculatorsr", function on_on_chat64(_9: number) {
    player.say(Math.sqrt(_9))
})
player.onChat("Richsphere", function on_on_chat65() {
    shapes.sphere(DIAMOND_BLOCK, pos(0, 0, 0), 5, ShapeOperation.Replace)
})
player.onChat("panic", function on_on_chat66() {
    
    mobs.clearEffect(mobs.target(LOCAL_PLAYER))
    Scaffoldhack = 0
    nuker = 0
    gameplay.setGameRule(FALL_DAMAGE, true)
    gameplay.setGameRule(FIRE_DAMAGE, true)
    cn = 0
    ws = 0
    wts = 0
    ow = 0
    cd = 0
    t = 0
    gameplay.setGameRule(WEATHER_CYCLE, true)
    gameplay.setGameRule(SHOW_COORDINATES, false)
    gameplay.setGameRule(DROWNING_DAMAGE, true)
    gameplay.setGameRule(MOB_SPAWNING, true)
    gameplay.setGameRule(MOB_GRIEFING, true)
    gameplay.setGameRule(TNT_EXPLODES, true)
})
player.onChat("Autokeepoff", function on_on_chat67() {
    
    Ak = 0
    gameplay.setGameRule(KEEP_INVENTORY, false)
    player.say("Autokeep off")
})
player.onChat("food", function on_on_chat68() {
    player.say("Gave you 16 steak.")
    mobs.give(mobs.target(LOCAL_PLAYER), COOKED_BEEF, 16)
})
player.onChat("Anti-Mob", function on_on_chat69() {
    
    if (am == 1) {
        am = 0
        gameplay.setGameRule(MOB_SPAWNING, true)
        player.say("Anti-Mob off")
    } else {
        am = 1
        gameplay.setGameRule(MOB_SPAWNING, false)
        player.say("Anti-Mob on")
    }
    
})
player.onChat("water-br.", function on_on_chat70() {
    mobs.applyEffect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 999999, 1)
})
player.onChat("deez", function on_on_chat71() {
    player.say("nuts")
    mobs.give(mobs.target(LOCAL_PLAYER), POTATO, 1)
})
player.onChat("t.kit", function on_on_chat72() {
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
})
player.onChat("tp-auraoff", function on_on_chat73() {
    
    tp = 0
    player.say("tp-aura off")
})
player.onChat("speedhack", function on_on_chat74() {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 999999, 20)
})
player.onChat("MassTP", function on_on_chat75() {
    mobs.teleportToPlayer(mobs.target(ALL_PLAYERS), mobs.target(LOCAL_PLAYER))
})
player.onChat("Autobase++", function on_on_chat76() {
    blocks.fill(BEDROCK, pos(-5, -1, -5), pos(5, 8, 5), FillOperation.Hollow)
})
player.onChat("Circlenukeroff", function on_on_chat77() {
    
    cn = 0
    player.say("circle nuker off")
})
player.onChat("customHighJump", function on_on_chat78(hjamp: number) {
    mobs.applyEffect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 999999, hjamp)
})
player.onChat("explode", function on_on_chat79() {
    for (let index4 = 0; index4 < 369; index4++) {
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
    }
})
player.onChat("gmc", function on_on_chat80() {
    gameplay.setGameMode(CREATIVE, mobs.target(LOCAL_PLAYER))
})
player.onChat("help4", function on_on_chat81() {
    player.say("MassTP - Tp's everyone to you")
    player.say("NoDMG - take no dmg")
    player.say("autopp - automatically build's a pp")
    player.say("autofloor - automatically build's a floor")
    player.say("autowall - automatically builds a wall")
    player.say("spawn - tp's you to spawn")
    player.say("NoDMGLegit - take reduced dmg")
    player.say("Autobase+ - automatically builds a obsidian base  ")
    player.say("type help5 for next page")
})
player.onChat("supercustompp", function on_on_chat82(ppid2: number) {
    blocks.fill(ppid2, pos(-15, 0, -6), pos(12, 9, 3), FillOperation.Replace)
    blocks.fill(ppid2, pos(-6, 10, -6), pos(3, 30, 3), FillOperation.Replace)
})
player.onChat("Circlenuker", function on_on_chat83() {
    
    if (cn == 1) {
        cn = 0
        player.say("circle nuker off")
    } else {
        cn = 1
        player.say("circle nuker on")
    }
    
    while (cn == 1) {
        shapes.circle(AIR, pos(1, 0, 1), 6, Axis.X, ShapeOperation.Replace)
    }
    while (cn == 1) {
        shapes.circle(AIR, pos(1, 0, 1), 6, Axis.Z, ShapeOperation.Replace)
    }
})
player.onChat("dia", function on_on_chat84() {
    player.say("Gave you 10 diamonds.")
    mobs.give(mobs.target(LOCAL_PLAYER), DIAMOND, 10)
})
player.onChat("customrichsphere", function on_on_chat85(radius3: number) {
    shapes.sphere(DIAMOND_BLOCK, pos(0, 0, 0), radius3, ShapeOperation.Replace)
})
player.onChat("UPDxrayoff", function on_on_chat86() {
    
    lxr = 0
    player.say("UPDxray off")
    blocks.fill(AIR, pos(-18, 0, -18), pos(18, 8, 18), FillOperation.Replace)
})
player.onChat("Autobase+", function on_on_chat87() {
    blocks.fill(OBSIDIAN, pos(-5, -1, -5), pos(5, 8, 5), FillOperation.Hollow)
})
player.onChat("xrayoff", function on_on_chat88() {
    
    xr = 0
    player.say("xray off")
})
player.onChat("Autokeep", function on_on_chat89() {
    
    if (Ak == 1) {
        Ak = 0
        gameplay.setGameRule(KEEP_INVENTORY, false)
        player.say("Autokeep off")
    } else {
        Ak = 1
        gameplay.setGameRule(KEEP_INVENTORY, true)
        player.say("Autokeep on")
    }
    
})
player.onChat("autofloor", function on_on_chat90() {
    blocks.fill(DIRT, pos(-5, -1, -5), pos(5, -1, 5), FillOperation.Replace)
})
player.onChat("help10", function on_on_chat91() {
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
})
player.onChat("customexplode", function on_on_chat92(amount22: any) {
    for (let index5 = 0; index5 < amount22; index5++) {
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
    }
})
player.onChat("customhealth", function on_on_chat93(health: number) {
    mobs.applyEffect(ABSORPTION, mobs.target(NEAREST_PLAYER), 999999, health)
    mobs.applyEffect(HEALTH_BOOST, mobs.target(NEAREST_PLAYER), 999999, health)
    mobs.applyEffect(REGENERATION, mobs.target(NEAREST_PLAYER), 999999, 255)
})
player.onChat("Coordinates", function on_on_chat94() {
    
    if (c == 1) {
        c = 0
        gameplay.setGameRule(SHOW_COORDINATES, false)
        player.say("Coordinates off")
    } else {
        c = 1
        gameplay.setGameRule(SHOW_COORDINATES, true)
        player.say("Coordinates on")
    }
    
})
player.onChat("Anti-Griefoff", function on_on_chat95() {
    
    ag = 0
    gameplay.setGameRule(MOB_GRIEFING, true)
    gameplay.setGameRule(TNT_EXPLODES, true)
    player.say("Anti-Grief off")
})
player.onChat("calculatorm", function on_on_chat96(_5: number, _6: number) {
    player.say(_5 * _6)
})
player.onChat("help11", function on_on_chat97() {
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
})
player.onChat("UPDxray", function on_on_chat98() {
    
    if (lxr == 1) {
        lxr = 0
        player.say("UPDxray off")
    } else {
        lxr = 1
        player.say("UPDxray on")
    }
    
    while (lxr == 1) {
        blocks.fill(STONE, pos(-18, 0, -18), pos(18, 8, 18), FillOperation.Replace)
        blocks.fill(AIR, pos(-18, 0, -18), pos(18, 8, 18), FillOperation.Replace)
        player.runChatCommand("Speedfastbreak")
    }
})
player.onChat("tp-aura", function on_on_chat99() {
    
    if (tp == 1) {
        tp = 0
        player.say("tp-aura off")
    } else {
        tp = 1
        player.say("tp-aura on")
    }
    
    while (tp == 1) {
        mobs.teleportToPlayer(mobs.target(ALL_ENTITIES), mobs.target(LOCAL_PLAYER))
        player.runChatCommand("infinihealth")
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
        blocks.fill(BEDROCK, pos(-1, -1, -1), pos(1, -1, 1), FillOperation.Replace)
    }
})
player.onChat("help7", function on_on_chat100() {
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
})
player.onChat("sblock", function on_on_chat101(num13: number) {
    
    Blockid = num13
})
player.onChat("day", function on_on_chat102() {
    player.say("Set time to day.")
    gameplay.timeSet(gameplay.time(DAY))
})
player.onChat("TNTScaffoldoff", function on_on_chat103() {
    
    t = 0
    player.say("TNTScaffold off")
})
player.onChat("ppnuker", function on_on_chat104() {
    
    if (ppn == 1) {
        ppn = 0
        player.say("ppnuker off")
    } else {
        ppn = 1
        player.say("ppnuker on")
    }
    
    while (ppn == 1) {
        blocks.fill(AIR, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.Replace)
        blocks.fill(AIR, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.Replace)
    }
})
player.onChat("OpenWaterESPoff", function on_on_chat105() {
    
    ow = 0
    player.say("OpenWaterESP off")
})
player.onChat("mass-suicide", function on_on_chat106() {
    gameplay.setGameMode(SURVIVAL, mobs.target(ALL_PLAYERS))
    mobs.kill(mobs.target(ALL_PLAYERS))
})
player.onChat("ppexplode", function on_on_chat107() {
    blocks.fill(TNT, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.Replace)
    blocks.fill(TNT, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.Replace)
    blocks.fill(REDSTONE_BLOCK, pos(-1, 11, -1), pos(-1, 11, -1), FillOperation.Replace)
})
player.onChat("Nuke", function on_on_chat108() {
    blocks.fill(REDSTONE_BLOCK, pos(-6, 40, -6), pos(6, 40, 6), FillOperation.Replace)
    blocks.fill(REDSTONE_LAMP, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.Replace)
    loops.pause(699)
    player.say("3")
    loops.pause(699)
    blocks.fill(AIR, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.Replace)
    loops.pause(699)
    player.say("2")
    loops.pause(699)
    blocks.fill(REDSTONE_LAMP, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.Replace)
    loops.pause(699)
    player.say("1")
    loops.pause(699)
    player.say("nuke initiated")
    loops.pause(69)
    blocks.fill(AIR, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.Replace)
    loops.pause(69)
    for (let index6 = 0; index6 < 28; index6++) {
        blocks.fill(TNT, pos(-6, 39, -6), pos(6, 39, 6), FillOperation.Replace)
    }
    for (let index7 = 0; index7 < 69; index7++) {
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(8, 28, -8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, -8), pos(-8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(8, 28, -8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-8, 28, 8), pos(8, 28, 8)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, -12), pos(12, 28, -12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, -12), pos(-12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(12, 28, -12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-12, 28, 12), pos(12, 28, 12)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, -15), pos(15, 28, -15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, -15), pos(-15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(15, 28, -15), pos(15, 28, 15)))
        mobs.spawn(PRIMED_TNT, positions.add(pos(-15, 28, 15), pos(15, 28, 15)))
    }
})
player.onChat("barrier", function on_on_chat109() {
    player.execute("give @s barrier 64")
})
player.onTravelled(SNEAK, function on_travelled_sneak() {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 3, 8)
})
player.onChat("customfloor", function on_on_chat110(x: number, z: number, block: number) {
    blocks.fill(Blockid, pos(x, -1, x), pos(z, -1, z), FillOperation.Replace)
})
player.onChat("customscaffoldoff", function on_on_chat111() {
    
    cs = 0
    player.say("customscaffold off")
})
//  https://www.youtube.com/watch?v=IIJM3S9H5m0
player.onChat("kit", function on_on_chat112() {
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
})
player.onChat("Anti-Drownoff", function on_on_chat113() {
    
    ad = 0
    gameplay.setGameRule(DROWNING_DAMAGE, true)
    player.say("Anti-Drown off")
})
player.onChat("InfinihealthLegit", function on_on_chat114() {
    mobs.applyEffect(ABSORPTION, mobs.target(NEAREST_PLAYER), 999999, 8)
    mobs.applyEffect(HEALTH_BOOST, mobs.target(NEAREST_PLAYER), 999999, 8)
    mobs.applyEffect(REGENERATION, mobs.target(NEAREST_PLAYER), 999999, 108)
})
player.onChat("help5", function on_on_chat115() {
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
})
player.onChat("autobase", function on_on_chat116() {
    blocks.fill(PLANKS_OAK, pos(-5, 0, -5), pos(5, 5, 5), FillOperation.Hollow)
})
player.onChat("bedrock", function on_on_chat117() {
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, 64)
})
player.onChat("calculators", function on_on_chat118(_3: number, _4: number) {
    player.say(_3 - _4)
})
player.onChat("anti-lags", function on_on_chat119() {
    gameplay.setGameMode(CREATIVE, mobs.target(LOCAL_PLAYER))
    loops.pause(69)
    mobs.kill(mobs.target(ALL_ENTITIES))
    loops.pause(69)
    gameplay.setGameMode(SURVIVAL, mobs.target(LOCAL_PLAYER))
})
player.onChat("one-shot", function on_on_chat120() {
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 999999, 255)
})
player.onChat("custombase", function on_on_chat121(x4: number, y4: number, z4: number) {
    blocks.fill(PLANKS_OAK, pos(x4, 0, x4), pos(z4, y4, z4), FillOperation.Hollow)
})
player.onChat("customkb", function on_on_chat122(amount3: number, amount4: number) {
    mobs.give(mobs.target(NEAREST_PLAYER), SNOWBALL, amount3)
    mobs.give(mobs.target(NEAREST_PLAYER), EGG, amount4)
})
player.onChat("GodTridents1", function on_on_chat123() {
    mobs.give(mobs.target(LOCAL_PLAYER), TRIDENT, 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "loyalty", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "impaling", 5)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "channeling", 1)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "unbreaking", 3)
    mobs.enchant(mobs.target(LOCAL_PLAYER), "mending", 1)
})
player.onChat("help9", function on_on_chat124() {
    player.say("Anti-Drown - prevents drowning damage")
    player.say("Anti-Drownoff - turns off Anti-Drown")
    player.say("Anti-Mob - stops all mobs from spawning")
    player.say("Anti-Moboff - turns off Anti-Mob")
    player.say("Anti-Grief - prevents anyone from griefing")
    player.say("Anti-Griefoff - turns off Auto-Grief")
    player.say("infinihealth - infinite health")
    player.say("superspeed - move so fast that no one can see you")
    player.say("type help10 for more commands")
})
player.onChat("ChestDetector", function on_on_chat125() {
    
    if (cd == 1) {
        cd = 0
        player.say("ChestDetector off")
    } else {
        cd = 1
        player.say("ChestDetector on")
    }
    
    while (cd == 0) {
        mobs.executeDetect(CHEST, positions.add(pos(0, 319, 0), pos(0, -319, 0)), "Chest found!")
    }
})
player.onChat("xray", function on_on_chat126() {
    
    if (xr == 1) {
        xr = 0
        player.say("xray off")
    } else {
        xr = 1
        player.say("xray on")
    }
    
    while (xr == 1) {
        blocks.fill(AIR, pos(-8, 0, -8), pos(8, 6, 8), FillOperation.Replace)
        mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 69, 38)
    }
})
player.onChat("TNTScaffold", function on_on_chat127() {
    
    if (t == 1) {
        t = 0
        player.say("TNTScaffold off")
    } else {
        t = 1
        player.say("TNTScaffold on")
    }
    
    while (t == 1) {
        blocks.fill(REDSTONE_BLOCK, pos(0, -1, 0), pos(0, -2, 0), FillOperation.Replace)
        blocks.fill(TNT, pos(0, -3, 0), pos(0, -3, 0), FillOperation.Replace)
    }
})
player.onChat("customcirclenukeroff", function on_on_chat128() {
    
    cnn = 0
    player.say("customcirclenuker off")
})
player.onChat("ppnukeroff", function on_on_chat129() {
    
    ppn = 0
    player.say("ppnuker off")
})
player.onChat("autowall", function on_on_chat130() {
    blocks.fill(DIRT, pos(-5, 0, -5), pos(5, 6, 5), FillOperation.Replace)
    blocks.fill(DIRT, pos(-5, 0, -5), pos(-5, 6, 5), FillOperation.Replace)
    blocks.fill(DIRT, pos(5, 0, -5), pos(5, 6, 5), FillOperation.Replace)
    blocks.fill(DIRT, pos(-5, 0, 5), pos(5, 6, 5), FillOperation.Replace)
})
player.onChat("r.kit", function on_on_chat131() {
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
})
player.onChat("fastbreak", function on_on_chat132() {
    mobs.applyEffect(HASTE, mobs.target(LOCAL_PLAYER), 999999, 18)
})
player.onChat("custompp", function on_on_chat133(ppid: number) {
    blocks.fill(ppid, pos(-5, 0, -2), pos(4, 3, 1), FillOperation.Replace)
    blocks.fill(ppid, pos(-2, 4, -2), pos(1, 10, 1), FillOperation.Replace)
})
player.onChat("calculatora", function on_on_chat134(_1: any, _2: any) {
    player.say(_1 + _2)
})
player.onChat("c.kit", function on_on_chat135(num14: any) {
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
})
player.onChat("superpp", function on_on_chat136() {
    blocks.fill(DIRT, pos(-15, 0, -6), pos(12, 9, 3), FillOperation.Replace)
    blocks.fill(DIRT, pos(-6, 10, -6), pos(3, 30, 3), FillOperation.Replace)
})
player.onChat("XP+", function on_on_chat137() {
    for (let index8 = 0; index8 < 696; index8++) {
        mobs.spawn(XP_BOTTLE, pos(0, 0, 0))
    }
})
player.onChat("customxp", function on_on_chat138(xpamt: any) {
    for (let index9 = 0; index9 < xpamt; index9++) {
        mobs.spawn(XP_BOTTLE, pos(0, 0, 0))
    }
})
player.onChat("Anti-Drown", function on_on_chat139() {
    
    if (ad == 1) {
        ad = 0
        gameplay.setGameRule(DROWNING_DAMAGE, true)
        player.say("Anti-Drown off")
    } else {
        ad = 1
        gameplay.setGameRule(DROWNING_DAMAGE, false)
        player.say("Anti-Drown on")
    }
    
})
player.onChat("NoWeather", function on_on_chat140() {
    
    if (nw == 1) {
        nw = 0
        gameplay.setGameRule(WEATHER_CYCLE, true)
        player.say("NoWeather off")
    } else {
        nw = 1
        gameplay.setGameRule(WEATHER_CYCLE, false)
        player.say("NoWeather on")
    }
    
})
player.onChat("AerialStrike", function on_on_chat141() {
    blocks.fill(REDSTONE_BLOCK, pos(-6, 51, -6), pos(6, 51, 6), FillOperation.Replace)
    for (let index10 = 0; index10 < 28; index10++) {
        blocks.fill(TNT, pos(-6, 50, -6), pos(6, 50, 6), FillOperation.Replace)
    }
})
player.onChat("help6", function on_on_chat142() {
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
})
player.onChat("custombedrock", function on_on_chat143(amount5: number) {
    mobs.give(mobs.target(LOCAL_PLAYER), BEDROCK, amount5)
})
player.onChat("W.TNTScaffold", function on_on_chat144() {
    
    if (wts == 1) {
        wts = 0
        player.say("WideTNTScaffold off")
    } else {
        wts = 1
        player.say("WideTNTScaffold on")
    }
    
    while (wts == 1) {
        blocks.fill(REDSTONE_BLOCK, pos(-1, -1, -1), pos(1, -2, 1), FillOperation.Replace)
        blocks.fill(TNT, pos(-1, -3, -1), pos(1, -3, 1), FillOperation.Replace)
    }
})
let ad = 0
let ppn = 0
let xr = 0
let lxr = 0
let tp = 0
let Ak = 0
let t = 0
let cn = 0
let cnn = 0
let wts = 0
let am = 0
let nw = 0
let cd = 0
let ws = 0
let cs = 0
let customnuker = 0
let nuker = 0
let c = 0
let NoFi = 0
let NoFa = 0
let ag = 0
let ow = 0
let Scaffoldhack = 0
let Blockid = 0
let item5 = DIRT
Blockid = 3
Scaffoldhack = 0
player.say("EDU CLIENT V5")
player.say("type help for a list of commands")
