# Game Rules

## Overview
A Turn-based Real-Time Strategy (TRTS) game is played over a series of rounds and ends in one of the following ways:

- The final round has ended and several players are still in the game, in which case the player with the most **Areas** under control wins*.
- A player is eliminated by losing all their buildings. The victory conditions in this case differs from the match type:
  - In a **2-player** match, the eliminated player lose the game, and the remaining player wins.
  - In a **team** match, the team of the elimnated player lose the game, and the other team wins.
  - In a **free-for-all** match, the player with the most **Areas** under _control_ wins*.
  - In a **last-man-standing** match, the game continues as long as there are two or more players remaining, otherwise the remaining player claims the victory.

*In case of a tie, it is the player with the most units (counted by their supply cost) that wins. In the unlikely event that it is still a tie, the player currently in front of the starting player line round wins.

## Setup

Place the **Game Board** somewhere on the table so it can be reached by all players.

Randomly determine the **Starting Location** on the map of each player and sit somewhere near your starting **Area**.

Each player places a **Player Board** in front of them and collects all the **Unit Models**, **Building Tokens** and **Upgrade Tokens**, as well as a set of **Resource Counters** (25 mineral and 25 gas tokens) and place all of it right in front of the **Player Board**.

It is important that no player can see the other players' **Player Board**.

Place the **Starting Player Tokens** next to the **Turn Sequence Board** in a random order and move the first **Starting Player Token** to the _Macromanagement_ phase on the **Turn Sequence Board**.

Place the **Turn Marker** on the first square on the on the **Turn Tracker** on the **Turn Sequence Board**.

## Turn Sequence 

Each round starts with a _Macromanagement_ phase that is followed by a _Micromanagement_ phase. The **Starting Player Token** on the **Turn Sequence Board** is used to indicate the current phase of the round.

When the first round is over, the **Starting Player Token** is moved to the end of the **Starting Player Line** and the **Turn Marker** is moved one square forward on the **Turn Tracker** on the **Turn Sequence Board**. Then, the next **Starting Player Token** is placed on the _Macromanagement_ phase on the **Turn Sequence Board** to initiate a new round.

### Macromanagement Phase

The _Macromanagement Phase_ consists of four sub-phases that are done in order but are performed indepentendly and secretely by each player. When all players have said they are "Done!", the round will proceed to the _Micromanagement Phase_.

#### Income
In the _Income Phase_, you collect resources from **Areas** you _control_ or _contest_. Read the game-specific rules for collecting resources. Move any collected resources to the **Resources Area** on your **Player Board**.

#### Deployment
Units that were produced in last round are deployed in the _Deployment phase_, as well as research, upgrades, and buildings. Research and upgrades are small tokens that you can place on your **Player Board** on the **Research** and **Upgrade Tracks**.

#### Production
You can train units, build buildings, do research, and produce upgrades in the _Production Phase_. Simply pay the cost in resources by removing them from your **Resources Area** to your **Player Board Resource Pool**. 

When producing units, upgrades, and research, place the models or tokens on the building that is producing it. When building a building, place the corresponding **Building Tile** in the **Area** of the constructing worker(s) and place the worker(s) ontop of the **Building Tile**.

If a unit is being summoned by another unit, put a special token under the unit model and place it near its summoner.

#### Movement
Players can secretely and independently move their units between **Player Board Areas** they _control_. Units in _contested_ **Areas** are, however, _pinned_ until the _Pushing Phase_ and cannot move in this phase. The movement points used in this phase cannot be used in the _Micromanagement Phase_. Therefore, group and mark units that have moved with the number of movement points they have left.

### Micromanagement Phase
All units can make _pushes_ into _uncontrolled_ and _contested_ **Areas** in the _Micromanagement Phase_ if they have enough movement points left from the _Macromanagement Phase_. During a _push_, one or more combat rounds can occour. Units that are already in a _contested_ **Area** can instead _pushing_ also _regroup_ to retract themselves from the _contested_ **Area**.

In the _current player turn order_, each player can _regroup_ or make a _push_ with a so-called **Control Group**. When the _regrouping_ or _push_ is over, the units in the **Control Group** cannot be activated again until next round while they are allowed to _retreat_ from new _engagements_ if they have enough movement points left. When all players _pass_, a new round of the game begins with a new _Macromanagement Phase_.

#### Pushes
To make a _push_, select a group of units (your **Control Group**) that can reach an _uncontrolled_ **Area** you wish to _engage_. Units in a **Control Group** do not have to start in the same **Area** and they can move through _controlled_ **Areas** only. Units in _contested_ **Areas** can also be part of a **Control Group** and can safely move out of their **Area**. Each player is only allowed to _engage_ the same **Area** one time each round. Units that are already in the targeted **Area** will automatically be part of the **Control Group** and will simply stay where they are. You cannot target an **Area** that you have already targeted this round. Now, place one of your **Control Markers** on the **Game Board Area**. Then move the **Control Group** to the target **Player Board Area** and (if relevant) keep note on how many movement point each unit has left.

There are 3 possible scenarios when _pushing_ into an **Area**:

1. If the **Area** is _neutral_, remove the _neutral_ **Control Marker**. You now control the **Area**. 

2. If the **Area** is under _control_ by an enemy player, the player controlling the **Area** has to say whether or not they have any units or buildings in that **Area**.

* If there are no units or buildings in the **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the **Area**.

* If there are enemy units or buildings in this **Area**, follow the Revealing rules bellow. 

When the _engagement_ is over, units in the **Control Group** that have not yet attacked or cast spells in this _push_ can decide to _push forward_ if they have enough movement points left. If you _push forward_, you must follow the same rules as described above but remember that units can only attack and cast spells once per turn. You can exploit this rule to _run by_ the enemy's defensive line to harass their main base. Units that do not _push forward_, will stay in the _engaged_ **Area** and cannot be activated later.   

#### Revealing
When units or buildings are revealed, it means that they are moved from the **Player Board Area** to the **Game Board Area**. Revealed buildings stay on the **Game Board Area** until they are destroyed (or moved) while units are moved back to the **Player Board Area** if the enemy loses sight of the units. Revealed production buildings can be _cloned_ so they also appear on the **Player Board Area**, so production and upgrades can be done secretely.

Follow these steps when engaging an **Area** that has enemy units or buildings in it:

1. The attacker reveals all his units.
2. The defender can decide to _retreat_ with some units, whereafter all units and defensive buildings in the **Area** must be revealed. If no defensive units or buildings are left in the **Area**, then the attacker gains control of it.
3. The attacker can decide to _retreat_ to the square they came from with any of their units without spending movement points. Retreating units are no longer part of the push. If some units _retreat_, the defending units that have greater range than the highest sight value of the attacking units can immediately attack the retreating units. 
6. If any units or buildings from both sides remains in the **Area**, then reveal any remaining buildings in the **Area** and perform a combat round. If all units and buildings of one side is destroyed in combat, the other player gains control over the **Area**, or otherwise, it remains _contested_.

#### Regrouping
Instead of making a _push_, you can also _regroup_, meaning that you move from a _contested_ **Area** to a reachable **Area** under _control_ (if any). Units that _regroup_ cannot be activated until next round.

Units can also decide to _regroup_ instead of _pushing forward_.

#### Combat
A _combat round_ is performed in several _combat steps_ where units with the long range attack before units with short range. In each _combat step_, units and buildings that share the same range value of the current _combat step_ can attack and cast spells. A _combat round_ thus starts with the highest range of any unit in the **Area**, then the second highest, the third, and so on, until all units have had a change to attack (unless they are killed first). 

During each _combat step_, the following happens: Both _engaging_ and _defending_ units that match the range value of the current _combat step_ can attack or cast spells. The _engaging_ player allocates damage first, followed by the _defending_ player, while the damage is dealt simultaneously. The amount of damage each unit deals is described in the next section. Remove any units that died and place damage tokens to reflect any damage to surviving units and buildings. In the rare situation that both players have lost all their units and buildings in the **Area** during a _combat step_, the _defending_ player will keep one unit or building of choice alive with 1 HP left.

Units and buildings can only ever attack once per round, even if they take part in multiple combat sitatuions. Units can also hold back their attack for a later combat step, either to target the same unit or to deal with special types of units.

### Allocating Damage

The _enaging_ player allocates damage first in a _combat round_ and then the _defending_ player, while the damage is dealt simulatenously. The units that can allocate damage in a _combat round_ are those that match the range value of the _combat step_. We will call these the _attacking units_. Attacks at range 1 is also called _melee_ attacks, and have some special rules.

When allocating damage, direct damage from your _attacking_ units to any number of enemy units that the units can target. Here are the core _targeting_ rules while there may be more in the game-specific rules:

- Air units can only be targeted by air attack
- Ground units can only be targeted by ground attack
- Melee attacks has to target units with the lowest range first following the _melee targeting_ rules (described later)
- Melee attacks cannot target units that have range attack and are faster than the attacker, unless the defender allows it
- Invisible units cannot be targeted unless they are made visible by units with the _detector_ ability or other game-specific rules

#### Splitting Damage
Normally, all damage from a unit has to be assigned to the same enemy unit but if the amount of damage surpasses the health points of the targeted unit, the remaining damage can be allocated to other enemy units, if the following requirements are met:

- Shorter ranged attackers cannot split damage onto longer ranged defenders, unless the attackers are faster than the defenders.
- _Splash_ damage cannot be split between units but has its own special rules (described later) 

#### Melee Targeting
Melee units can block other melee units from attacking ranged units, unless one side can overrun the other. 
To start with, melee units has to target other melee units. If, however, they manage to assign at least one melee damage to all enemy melee units, they can assign the remaining damage to units with the second lowest range value. If all those units can be assigned at least one melee damage, the attackers can proceed to the next, and so on.

Faster ranged units normally cannot be targeted by slower melee units but the defender can decide to use them to block, forcing the attacker to target them before higher range units.

#### Splash Damage
If an attack deals X splash damage, it deals 1 damage (with any modifiers) to X units.

### Dealing Damage
When the damage of a _combat round_ have been assigned by both sides, they are dealt. For each unit, first subtract the armor value from the number of assigned damage points. If the assigned damage is greater than or equal to the unit's health points, it is killed and thus remove it from the game. If the assigned damage is less than the unit's health points, it survives. Units that don't have full health, must have tokens next to them to indicate their remaining health points.

Some units have shield points as well that simply counts as additional health points, while they have game-specific rules for how they are replenished.
