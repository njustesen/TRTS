# Game Rules

## Overview
A TRTS game is played over a series of rounds and ends in one of the following ways:

- The final round has ended and several players are still in the game, in which case the player with the most **areas** under control wins*.
- A player is eliminated. The victory conditions in this case differs from the match type:
  - In a **2-player** match, the eliminated player lose the game, and the remaining player wins.
  - In a **team** match, the team of the elimnated player lose the game, and the other team wins.
  - In a **free-for-all** match, the player with the most **areas** under controls win*.
  - In a **last-man-standing** match, the game continues if there are more than two player remaining, otherwise the remaining player claims the victory.

*In case of a tie, it is the player with the most units (counted by their supply cost) that wins. In the unlikely event that it is still a tie, the player in front of the starting player of the current round wins.

## Setup

Place the **Game Board** somewhere on the table so it can be reached by all players.

Randomly determine the **Starting Location** on the map of each player and sit somewhere near your starting area.

Each player places a **Player Board** in front of them and collects all the **Unit Models**, **Building Tokens** and **Upgrade Tokens**, as well as a set of **Resource Counters** (25 mineral and gas tokens) and place all of it right in front of the **Player Board**.

It is important that no player can see what is behind the other players' **Player Boards**.

Place the **Starting Player Tokens** next to the **Turn Sequence Board** in a random order and move the first **Starting Player Token** to the _Macromanagement_ phase on the **Turn Sequence Board**.

Place the **Turn Marker** on the first square on the on the **Turn Tracker** on the **Turn Sequence Board**.

...

## Turn Sequence 

Each round starts with a _Macromanagement_ phase that is followed by a _Micromanagement_ phase. The **Starting Player Token** on the **Turn Sequence Board** is used to indicate the current phase of the turn.

When the first round is over, the **Starting Player Token** is moved to the end of the line of **Starting Player Tokens** and the **Turn Marker** is moved one square forward on the **Turn Tracker** on the **Turn Sequence Board**. Then, the next **Starting Player Token** is used placed on the _Macromanagement_ phase on the **Turn Sequence Board** to initiate a new round.

### Macromanagement Phase

The macromanagement phase consists of three sub-phases that are done in order but are performed indepentendly and secretely by each player. When all players have said they are "Done!", the turn will proceed to the Micromanagement phase.

#### Income

#### Deployment

#### Production

### Micromanagement Phase

In the _Micromanagement Phase_, players can move units between connected **Areas** on the map which sometimes involves combat. 

In the _current player turn order_, one **Control Group** is "_microed_" at a time. When the _active_ **Control Group** is done being _microed_, they cannot be _microed_ again this turn. Units can only perform _Movement Actions_, which includes _retreating_ from _Combat_, when they are _active_, making already-_microed_ units fragile when left out in the open. 

When a **Control Group** is done being _microed_, it becomes the next player to _micro_ a **Control Group**. When a full _Micromanagement_ round has been made without any _combat_ or _engagements_ (will be explained later), the phase stops. However, before a new turn begins with the _Macromanagement Phase_, all players can (simultaneosuly and secretely) move all units that have not been _activated_ that are in **Areas** under _control_.

Units can only be moved in so-called **Control Groups**, even if a **Control Group** only consists of a single unit. A **Control Group** is simply a set of units that perform the same action in the _Micromanagement Phase_. All units in a **Control Groups** do not have to start in the same **Area** but they must always target the same **Area** when moving. It is good practice to place units in a **Control Group** close together in their **Area** so it is easy to remember that they have been _microed_ together. 

Players can continue to move the same **Control Groups** multiple times if they have enough movement points. It is not allowed to split up the **Control Groups** and _micro_ the individually. You can, however, leave behind some of the units in a **Control Groups** and continue to move with a subset of the units, e.g. if some units are faster than others, or if some units will stay and fight while others will move forward to harass another **Areas**. When units are left behind, their _activation_ ends, and they can no longer move for the rest of the turn. This means that you only have to remember how many movement points are left for the units within the _active_ **Control Group**, sinve all other units either cannot move anymore or have not been _microed_ yet. In the late-game, it can become necessary to mark control groups to remember that they have been _microed_.

#### Moving a Control Group
To initiate a movement of a **Control Group**, first, select a group of units under your control, that have not yet been _microed_ yet, and move them to an **Area** that they can all reach (see how many movement points they have). Units in _contested_ **Areas** are also allowed to be _microed_. If you _control_ the target **Area**, simply move them to the **Player Board Area**. If you do not _control_ the **Area**, an _engagement_ will happen. 

After moving the units and resolving any _engagements_, you can either declare the _activation_ finished or you can continue moving with some or all of the units in the **Control Groups**, given they have enough movement points left. Units that are left behind cannot be _microed_ again later.

#### Engagement
If a **Control Group** moves into an **Area** that they do not _control_ or _contest_, place a **Control Marker** on the **Game Board Area** to indicate you are _engaging_. 

There are 3 possible scenarios for an _engagement_:

1. If the **Area** is _neutral_, remove the _neutral_ **Control Marker**. You now control the engaged **Area**. 

2. If the **Area** is under control by enemy players, the players controlling the **Area** has to say whether or not they have any units or buildings in that **Area**.

* If there are no units/buildings in the engaged **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the engaged **Area**.

* If there are units or buildings, immediately move all units that are in the corresponding **Player Board Areas**, including the engaging units, onto the **Game Board Area** so they become visible to everyone. New upgrades must be declared while research that enables new actions and spells can be kept secret until used.
The _defending_ player can then decide _retreat_ with units in the _engaged_ **Area**. If some _defending_ units or buildings remain, you must carry out a _Combat_ round (described later), otherwise you gain control over the **Area**.

When the movement (and any _Combat_) is over, the **Control Group** (or a subgroup) is allowed to continue its activation.

#### Attack
A **Control Group** in an **Area** with enemy units or buildings can initiate a _Combat_ round if they have not attacked yet this turn. _Combat_ is described later.

#### Hold Position Action
This defensive actions ends the _activation_ of a **Control Group** but allows them to _attack_ during _Combat_ rounds in their **Area** that will occour until they become _activated_ again.

Units cannot perform a _Hold Position Action_ if they have attacked this turn.

Units that haven't attacked yet this turn will automatically perform a _Hold Position Action_ when they end their _activation_.

Units that have not been _acitvated_ yet this turn will always be in _Hold Position_.

Buildings are always in _Hold Position_.

#### Retreat Action
Immedieatly when non-_activated_ units are being _engaged_ by an enemy **Control Group** (or as part of a _Combat_), they can be _activated_ and _retreat_ to and through **Areas** that are _controlled_ or _contested_ given they have anough movement points left. When retreating before combat, units cannot retreat to the **Area** from which the _engaging_ **Control Group** came from. The _retreating_ **Control Group** ends their _activation_ (in _Hold Position_ if they have not attacked this turn) but they do not initiate any new _Combat_ rounds in the **Area** they _retreated_ into. 

If all units in the _engaged_ **Area** are _retreating_ and they do not control any buildings in the **Area**, remove their **Control Marker** and the _engaging_ player new controls the **Area**.

### Combat
A _combat round_ is performed in several _Combat Steps_ where units with the long range attack first. In each _Combat Step_, units and buildings that share the _range_ value of the current _combat step_ can _attack_ and _cast spells_. A _combat round_ thus starts with the highest range of any unit in the **Area**, then the next highest, the third, and so on until all units have had a change. 

During a _Combat Step_, the following happens:

1. Both _engaging_ and _defending_ units that match the _range_ value of the current _combat step_ can attack or cast spells. The _engaging_ players allocates damage first followed by the _defending_ players, while the damage of a _Combat Step_ is dealt simulatenously. The amount of damage each unit deals is described in the next section. Remove any units that died and place damage tokens to reflect any damage to surviving units/buildings. In the rare situation that both players will loose all their units and buildings in the **Area** during one _combat step_, the _defending_ player will keep a unit of choice alive with 1 HP left.

2. Any units in the _active_ **Control Group** can _retreat_ to any adjacent **Area** under control or contested by the units' owner without initiating any new _Combat_ rounds. Any retreating units end their _activation_ after _retreiting_ and thus cannot move anymore this turn. 

the _active_ **Control Group** cannot retreat during combat if the _engagement_ occoured this turn _up a ramp_. Thus ignore step #2 in this case. 

Units and buildings can only ever attack once per turn, and only if the are in the _active_ **Control Group** or are in _Hold Position_.

Defending units cannot _retreat_ during the _Combat_ round. They have to make a _Retreat_ action immediately when _engaged_.

### Damage

