from factorio_process import FormalVector
from factorio_process import raw
from factorio_process import manufactured
from factorio_process import optimize
from factorio_process import format_optimize_result


# vim macro for converting:
# "foo", ingredients, n, m
# to
# foo = manufactured("foo", ingredients, seconds=n, out_multiplier=m)
#
# 0vvyPa = manufactured("ea"f,f,a seconds=lxf,laout_multiplier=

zero = FormalVector.zero()

iron_ore = raw("iron_ore")
brick = raw("brick")
stone = raw("stone")
coal = raw("coal")
iron = raw("iron")
copper = raw("copper")
steel = raw("steel")
water = raw("water")
crude = raw("crude")
u235 = raw("u235")
u238 = raw("u238")
wood = raw("wood")

petrol = raw("petrol")
heavy_oil = raw("heavy_oil")

pipe = manufactured("pipe", iron, seconds=0.5)
underground_pipe = manufactured("underground_pipe", 5*iron + 10*pipe, seconds=0.5, out_multiplier=2)
gear = manufactured("gear", 2*iron, seconds=0.5)
engine = manufactured("engine", steel + gear + 2*pipe, seconds=10)

stone_furnace = manufactured("stone_furnace", 5*stone, seconds=0.5)
steel_furnace = manufactured("steel_furnace", 6*steel + 10*brick, seconds=3)

wire = manufactured("wire", copper, seconds=0.5, out_multiplier=2)
green_chip = manufactured("green_chip", iron + 3*wire, seconds=0.5)

refinery = manufactured("refinery", 15*steel + 10*gear + 10*green_chip + 10*pipe + 10*brick, seconds=8)
chemical_plant = manufactured("chemical_plant", 5*steel + 5*gear + 5*green_chip + 5*pipe, seconds=5)

lubricant = manufactured("lubricant", 10*heavy_oil, seconds=1, out_multiplier=10)
sulfur = manufactured("sulfur", 30*petrol + 30*water, seconds=1, out_multiplier=2)
acid = manufactured("acid", iron + 100*water + 5*sulfur, seconds=1, out_multiplier=50)
battery = manufactured("battery", copper + iron + 20*acid, seconds=4)
motor = manufactured("motor", engine + 15*lubricant + 2*green_chip, seconds=10)
robot_frame = manufactured("robot_frame", steel + 3*green_chip + 2*battery + 1*motor, seconds=20)

plastic = manufactured("plastic", coal + 20*petrol, seconds=1, out_multiplier=2)
low_density_struct = manufactured(
    "low_density_struct", 20*copper + 5*plastic + 2*steel, seconds=20,
)

red_chip = manufactured("red_chip", 4*wire + 2*green_chip + 2*plastic, seconds=6)
blue_chip = manufactured("blue_chip", 2*red_chip + 20*green_chip + 5*acid, seconds=10)

yellow_science = manufactured("yellow_science", robot_frame + 3*low_density_struct + 2*blue_chip, seconds=21, out_multiplier=3)

rod = manufactured("rod", iron, seconds=0.5, out_multiplier=2)
rail = manufactured("rail", steel + stone + rod, seconds=0.5, out_multiplier=2)
electric_furnace = manufactured("electric_furnace", 5*red_chip + 10*steel + 10*brick, seconds=5)
productivity_mod = manufactured("productivity_mod", 5*red_chip + 5*green_chip, seconds=15)
purple_science = manufactured("purple_science", electric_furnace + productivity_mod + 30*rail, seconds=21, out_multiplier=3)

roboport = manufactured("roboport", 45*(steel + gear + red_chip), seconds=5)
iron_chest = manufactured("iron_chest", 8*iron, seconds=0.5)
steel_chest = manufactured("steel_chest", 8*steel, seconds=0.5)
any_logistics_chest = manufactured("logistics_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)
yellow_chest = manufactured("yellow_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)
red_chest = manufactured("red_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)
blue_chest = manufactured("blue_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)
purple_chest = manufactured("purple_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)
green_chest = manufactured("green_chest", steel_chest + 3*green_chip + red_chip, seconds=0.5)

explosives = manufactured("explosives", coal + sulfur + 10*water, seconds=4, out_multiplier=2)
barrel = manufactured("barrel", steel, seconds=1)
grenade = manufactured("grenade", 10*coal + 5*iron, seconds=8)
poison = manufactured("poison", 10*coal + 3*steel + 3*green_chip, seconds=8)
cliff_explosives = manufactured("cliff_explosives", 10*explosives + barrel + grenade, seconds=8)

ammo = manufactured("ammo", 4*iron, seconds=1)
red_ammo = manufactured("red_ammo", 5*copper + steel + ammo, seconds=3)

construction_bot = manufactured("construction_bot", robot_frame + 2*green_chip, seconds=0.5)
logistics_bot = manufactured("logistics_bot", robot_frame + 2*red_chip, seconds=0.5)

iron_stick = manufactured("iron_stick", iron, seconds=0.5, out_multiplier=2)
rail = manufactured("rail", stone + iron + iron_stick, seconds=0.5, out_multiplier=2)
train_stop = manufactured("train_stop", 6*iron + 3*steel + 6*iron_stick + 5*green_chip, seconds=0.5)
signal = manufactured("signal", 5*iron + green_chip, seconds=0.5)
chain_signal = manufactured("chain_signal", 5*iron + green_chip, seconds=0.5)
locomotive = manufactured("locomotive", 30*steel + 10*green_chip + 20*engine, seconds=4)
wagon = manufactured("wagon", 20*iron + 20*steel + 10*gear, seconds=1)
fluid_tank = manufactured("fluid_tank", 20*iron + 5*steel, seconds=3)
fluid_wagon = manufactured("fluid_wagon", 16*steel + 10*gear + fluid_tank + 8*pipe, seconds=1.5)
car = manufactured("car", 20*iron + 5*steel + 8*engine, seconds=2)

grass = manufactured("grass", 20*stone, seconds=0.5)

steel_plate_fast = manufactured("steel_plate_fast", 5*iron, seconds=8)

yellow_inserter = manufactured("yellow_inserter", iron + gear + green_chip, seconds=0.5)
red_inserter = manufactured("red_inserter", yellow_inserter + iron + gear, seconds=0.5)
blue_inserter = manufactured("blue_inserter", yellow_inserter + 2*iron + 2*green_chip, 0.5)
filter_inserter = manufactured("filter_inserter", 4*green_chip + blue_inserter, 0.5)
stack_inserter = manufactured("stack_inserter", 15*gear + 15*green_chip + red_chip + blue_inserter, 0.5)

fast_refined_ore = manufactured("fast_refined_ore", iron, seconds=(3.2/2))

uranium_fuel_cell = manufactured("uranium_fuel_cell", 10*iron + u235 + 19*u238, seconds=10, out_multiplier=10)

concrete = manufactured("concrete", 100*water + 5*stone + iron_ore, seconds=10, out_multiplier=10)

explosives = manufactured("explosives", coal + sulfur + 10*water, seconds=4, out_multiplier=2)
explosive_cannon_shell = manufactured("explosive_cannon_shell", 2*steel + 2*plastic + 2*explosives, seconds=8)
radar = manufactured("radar", 10*iron + 5*gear + 5*green_chip, seconds=0.5)
artillery = manufactured("artillery", 60*concrete + 60*steel + 40*iron + 20*red_chip, seconds=40)
artillery_shell = manufactured("artillery_shell", 8*explosives + 4*explosive_cannon_shell + radar, seconds=15)

assembler = manufactured("assembler", 9*iron + 5*gear + 3*green_chip, seconds=0.5)
blue_assembler = manufactured("blue_assembler", assembler + 2*steel + 5*gear + 3*green_chip, seconds=0.5)
speed_module = manufactured("speed_module", 5*green_chip + 5*red_chip, seconds=15)
speed_module_2 = manufactured("speed_module_2", 5*red_chip + 5*blue_chip + 4*speed_module, seconds=30)
efficiency_module = manufactured("efficiency_module", 5*green_chip + 5*red_chip, seconds=15)
efficiency_module_2 = manufactured("efficiency_module_2", 4*red_chip + 5*blue_chip + 4*efficiency_module, seconds=30)
green_assembler = manufactured("green_assembler", 2*blue_assembler + 4*speed_module, seconds=0.5)

yellow_belt = manufactured("yellow_belt", iron + gear, 0.5, 2)
red_belt = manufactured("red_belt", 5*gear + yellow_belt, 0.5)
blue_belt = manufactured("blue_belt", 10*gear + red_belt + 20*lubricant, 0.5)

yellow_underground = manufactured("yellow_underground", 10*iron + 5*yellow_belt, 1, 2)
red_underground = manufactured("red_underground", 40*gear + 2*yellow_underground, 2, 2)
blue_underground = manufactured("blue_underground", 80*gear + 4*red_underground + 80*lubricant, 2, 2)

yellow_splitter = manufactured("yellow_splitter", 5*iron + 5*green_chip + 4*yellow_belt, 1)
red_splitter = manufactured("red_splitter", 10*gear + 10*green_chip + yellow_splitter, 2)
blue_splitter = manufactured("blue_splitter", 10*gear + 10*red_chip + red_splitter + 80*lubricant, 2)

small_pole = manufactured("small_pole", wood + 2*wire, seconds=0.5, out_multiplier=2)
medium_pole = manufactured("medium_pole", 2*copper + 2*steel + 4*iron_stick, seconds=0.5)
big_pole = manufactured("big_pole", 5*copper + 5*steel + 8*iron_stick, seconds=0.5)
substation = manufactured("substation", 4*copper + 5*steel + 5*red_chip, seconds=0.5)

modular_armor = manufactured("modular_armor", 50*steel + 30*red_chip, seconds=15)
power_armor = manufactured("power_armor", 40*steel + 40*blue_chip + 20*motor, seconds=20)
power_armor_2 = manufactured("power_armor_2", 60*blue_chip + 40*motor + 30*low_density_struct + 25*speed_module_2 + 25*efficiency_module_2, seconds=25)

personal_battery = manufactured("personal_battery", 10*steel + 5*battery, seconds=10)
personal_battery_2 = manufactured("personal_battery_2", 15*blue_chip + 5*low_density_struct + 10*personal_battery, seconds=10)
exoskeleton = manufactured("exoskeleton", 20*steel + 10*blue_chip + 30*motor, seconds=10)
personal_roboport = manufactured("personal_roboport", 20*steel + 45*battery + 40*gear + 10*red_chip, seconds=10)
personal_roboport_2 = manufactured("personal_roboport_2", 100*blue_chip + 20*low_density_struct + 5*personal_roboport, seconds=20)

energy_shield = manufactured("energy_shield", 10*steel + 5*red_chip, seconds=10)
energy_shield_2 = manufactured("energy_shield_2", 5*blue_chip + 5*low_density_struct + 10*energy_shield, seconds=10)


boiler = manufactured("boiler", 4*pipe + stone_furnace, seconds=0.5)
steam_engine = manufactured("steam_engine", 10*iron + 8*gear + 5*pipe, seconds=0.5)

solar_panel = manufactured("solar_panel", 5*copper + 5*steel + 15*green_chip, seconds=10)
portable_solar_panel = manufactured("portable_solar_panel", 5*steel + 2*red_chip + solar_panel, seconds=10)

portable_fusion_reactor = manufactured("portable_fusion_reactor", 200*blue_chip + 50*low_density_struct, seconds=10)
belt_immunity = manufactured("belt_immunity", 10*steel + 5*red_chip, seconds=10)

turret = manufactured("turret", 20*iron + 10*copper + 10* gear, seconds=8)
laser_turret = manufactured("laser_turret", 20*steel + 12*battery + 20*green_chip, seconds=20)
personal_laser_turret = manufactured("personal_laser_turret", 20*blue_chip + 5*low_density_struct + 5*laser_turret, seconds=10)

nuclear_reactor = manufactured("nuclear_reactor", 500*copper + 500*steel + 500*red_chip + 500*concrete, seconds=8)
heat_pipe = manufactured("heat_pipe", 20*copper + 10*steel, seconds=1)
heat_exchanger = manufactured("heat_exchanger", 100*copper + 10*steel + 10*pipe, seconds=3)
steam_turbine = manufactured("steam_turbine", 50*copper + 50*gear + 20*pipe, seconds=3)

burner_drill = manufactured("burner_drill", 3*iron + 3*gear + stone_furnace, seconds=2)
electric_drill = manufactured("electric_drill", 10*iron + 5*gear + 3*green_chip, seconds=2)
offshore_pump = manufactured("offshore_pump", gear + 2*green_chip + pipe, seconds=0.5)
pumpjack = manufactured("pumpjack", 5*steel + 10*gear + 5*green_chip + 10*pipe, seconds=5)

lab = manufactured("lab", 10*gear + 10*green_chip + 4*yellow_belt, seconds=2)

repair_pack = manufactured("repair_pack", 2*gear + 2*green_chip, seconds=0.5)

beacon = manufactured("beacon", 10*steel + 10*wire + 20*green_chip + 20*red_chip, seconds=15)




