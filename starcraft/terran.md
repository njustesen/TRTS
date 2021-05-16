# Terran

## Special Rules

- _Burning Buildings_: Terran buildings with 1 HP left by the end of the turn will be destroyed.
- _Add-ons_: Add-ons are small buildings that can be added onto another building. Add-ons can be constructed without an SCV while the main building cannot be used for anything else until the add-on is deployed. Buildings can at most have one add-on and only those listed in their rules.
- _Lift Off_: Terran buildings with the _Lift Off_ ability can become flying with speed 1. This ability can only be used in the Movement phase and the building cannot move after _lifting off_. When _lifted_, the building can land during the movement phase. Any add-ons on the lifted building remain on the ground and cannot be used but can be attached to any landing building that fits with the add-on.

## Units 

Unit           | Min  | Gas | Sup. | Speed | HP | Armor | Size | Range | Ground | Air | Sight | Type |
:------------- | ---: | --: | ---: | ----: | -: | ----: | ---: | ----: | -----: | --: | ----: | ---- | 
SCV            | 1    | 0   | 1    |     2 |  1 |     0 |    S |     1 |    1/2 |     |     7 | Mech |
Marine         | 1    | 0   | 1    |     2 |  1 |     0 |    S |     4 |      1 |     |     7 |  Bio |
Firebat        | 1    | 1   | 1    |     2 |  1 |     1 |    S |     2 |    2cs |     |     7 |  Bio |
Medic          | 1    | 1   | 1    |     2 |  1 |     0 |    S |       |        |     |     9 |  Bio |
Ghost          | 1    | 1   | 1    |     2 |  1 |     1 |    S |     7 |     2c |     |     9 |  Bio |
Vulture        | 2    | 0   | 2    |     3 |  2 |     0 |    M |     5 |     2c |     |     8 | Mech |
Spider Mine    |      |     |      |     4 |  1 |     0 |    S |     1 |    2es |     |     3 | Mech |
Tank           | 3    | 2   | 2    |     2 |  3 |     1 |    L |     7 |     2e |     |    10 | Mech |
_Siege Tank_   |      |     |      |     0 |  3 |     1 |    L |    12 |    3es |     |    10 | Mech |
Goliath        | 2    | 1   | 2    |     2 |  3 |     1 |    L |     5 |      2 |  3e |     8 | Mech |
Dropship       | 2    | 2   | 2    |     2 |  3 |     1 |    L |       |        |     |    11 | Mech |
Wraith         | 3    | 2   | 2    |     3 |  2 |     0 |    L |     5 |      1 |  3e |     7 | Mech |
Science Vessel | 2    | 5   | 2    |     2 |  4 |     1 |    L |       |        |     |    10 | Mech |
Valkyrie       | 6    | 2   | 3    |     3 |  4 |     2 |    L |     6 |        | 3es |     8 | Mech |

e: Explosive Attack, c: Concussive Attack, s: Splash Damage

### SCV

**Abilities**:
- _Hovering_
- _Resource Gathering_: SCVs can collect 1 mineral (max. one per mineral field) or 1 gas (requires an assimilaor) in the income phase.
- _Constructing_: SCVs can contruct a building by paying its cost. The SCV and the buildings under constructions cannot be used before the Deployment phase and the building has half HP (rounded down).
- _Reparing_: SCVs can repair any Terran building or mech unit for 1 mineral giving them up to 3 lost HP.

### Marine

**Abilities**:
- _Stim Pack_ (Researched at Academy): Allows Marines to gain double attack and double speed in a combat round. However, they lose 1 HP and die if not healed immediately after. 

### Firebat

**Abilities**:
- _Stim Pack_ (Researched at Academy): Allows the Marine to +1 attack and +1 speed in a combat round. However, they will die if not healed at the end of this round and any damage before armor will kill it.

### Medic

Medics have 1/4 energy.

**Abilities**:
- _Heal_ [1 energy]: Allows the Medic to heal a Terran biological unit at any point during a combat to deny 1 damage. 
- _Restoration_ [1 energy]: Allows the Medic to remove remove any harmful effects on a unit, such as Lockdown, Optic Flares, Irradiate, Plague, Ensnare and Parasites, except Stasis Field.
- _Optical Flare_ [2 energy]: Allows the Medic to permanently reduced the sight of any unit in the same area to 1.

## Buildings

Building             | Min. | Gas | Sup. | HP | Armor | Size | Range | Ground | Air    | Sight |
:------------------- | ---: | --: | ---: | -: | ----: | ---: | ----: | -----: | -----: | ----: |
Command Center       | 8    | 0   | +1   | 30 |     1 |    L |       |        |        |       |
ComSat Station       | 1    | 1   |      | 15 |     0 |    L |       |        |        |       |
Nuclear Silo         | 8    | 0   |      | 10 |     0 |    L |       |        |        |       |
Supply Depot         | 8    | 0   | +1   | 10 |     0 |    L |       |        |        |       |
Refinery             | 2    | 0   |      | 10 |     1 |    L |       |        |        |       |

### Command Center

Required in an area to collect resources.
Gives +1 Supply.

**Abilities**:
- _Lift Off_

**Produces**: 
- SCV [1 min, 1 sup]

**Add-ons**
* ComSat Station [1 min, 1 sup]
* Nuclear Silo [1 min, 1 sup]

### Comsat Station

Comsat Stations starts with 1/4 energy.

**Abilities**:
* Scan [1 Energy]:
  - Reveals everything in an area, including cloaked units. If used during a combat round, the effect stops when the round is over, otherwise it stops immedieately after inspecting the area.

### Nuclear Silo

**Produces**:
* Nuke [8 min, 4 sup]
  - A Nuclear Silo can at most hold one Nuke.

### Supply Depot

Gives +1 Supply.

### Refinery

Required on a Gas Geyser before gas can be extracted.

### Barracks
