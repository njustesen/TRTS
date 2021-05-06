# Game Rules

## Overview
A Turn-based Real-Time Strategy (TRTS) game is played over a series of rounds and ends in one of the following ways:

- The final round has ended and several players are still in the game, in which case the player with the most **Areas** under control wins*.
- A player is eliminated by losing all their buildings. The victory conditions in this case differs from the match type:
  - In a **2-player** match, the eliminated player lose the game, and the remaining player wins.
  - In a **team** match, the team of the elimnated player lose the game, and the other team wins.
  - In a **free-for-all** match, the player with the most **Areas** under _control_ win*.
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

#### Deployment

#### Production

#### Movement
Players can secretely and independently move their units between **Player Board Areas** they _control_. Units in _contested_ **Areas** are, however, _pinned_ until the _Pushing Phase_ and cannot move in this phase. The movement points used in this phase cannot be used in the _Micromanagement Phase_. Therefore, group and mark units that have moved with the number of movement points they have left.

### Micromanagement Phase
All units can make _pushes_ into _uncontrolled_ and _contested_ **Areas** in the _Micromanagement Phase_ if they have enough movement points left from the _Macromanagement Phase_. During a _push_, one or more combat rounds can occour. Units that are already in a _contested_ **Area** can instead _pushing_ also _regroup_ to retract themselves from the _contested_ **Area**.

In the _current player turn order_, each player can _regroup_ or make a _push_ with a so-called **Control Group**. When the _regrouping_ or _push_ is over, the units in the **Control Group** cannot be activated again unitl next round while they are allowed to _retreat_ from an attack if they have enough movement points left. When all players _pass_, a new round of the game begins with a new _Macromanagement Phase_.

#### Pushes
To make a _push_, select a group of units (your **Control Group**) that can reach an _uncontrolled_ **Area** you wish to _engage_. Units in a **Control Group** do not have to start in the same **Area** and they can move through _controlled_ **Areas** only. Units in _contested_ **Areas** can also be part of a **Control Group** and can safely move out of their **Area**. Each player is only allowed to _engage_ the same **Area** one time each round. Units that are already in the targeted **Area** will automatically be part of the **Control Group** and will simply stay where they are. You cannot target an **Area** that you have already targeted this round. Now, place one of your **Control Markers** on the **Game Board Area**. Then move the **Control Group** to the target **Player Board Area** and (if relevant) keep note on how many movement point each unit has left.

There are 3 possible scenarios when _pushing_ into an **Area**:

1. If the **Area** is _neutral_, remove the _neutral_ **Control Marker**. You now control the **Area**. 

2. If the **Area** is under _control_ by an enemy player, the player controlling the **Area** has to say whether or not they have any units or buildings in that **Area**.

* If there are no units or buildings in the **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the **Area**.

* If there are enemy units or buildings in this **Area**, immediately move them and the **Control Group** to the **Game Board Area** so they become visible to everyone. Any of the defending units can decide immediately to _retreat_ to a reachable **Area** under control (if there are any) without taking part of the combat. If the defending player does not have vision to see any of the attacking units, _retreating_ is not an option. If all enemy units and buildings have _retreated_ or are eliminated during combat, the _pushing_ player gains control over the **Area**. If the **Area** remains _contested_, keep both players' **Control Markers**, units, and buildings on the **Game Board Area**. If the defending player kept some units back on the **Area**, perform a round of combat before continuing.

When the _engagement_ is over, units in the **Control Group** that have not yet attacked or cast spells in this _push_ can decide to _push forward_ if they have enough movement points left. If you _push forward_, you must follow the same rules as described above but remember that units can only attack and cast spells once per turn. You can exploit this rule to _run by_ the enemy's defensive line to harass their main base. Units that do not _push forward_, will stay in the _engaged_ **Area** and cannot be activated later.   

### Regrouping
Instead of making a _push_, you can also _regroup_, meaning that you move from a _contested_ **Area** to a reachable **Area** under _control_ (if any). Units that _regroup_, cannot be activated until next round.

Units can also decide to _regroup_ instead of _pushing forward_ and it will end the _push_ immediately.

### Combat
A _combat round_ is performed in several _combat steps_ where units with the long range attack before units with short range. In each _combat step_, units and buildings that share the same range value of the current _combat step_ can attack and cast spells. A _combat round_ thus starts with the highest range of any unit in the **Area**, then the second highest, the third, and so on, until all units have had a change to attack (unless they are killed first). 

During each _combat step_, the following happens: Both _engaging_ and _defending_ units that match the range value of the current _combat step_ can attack or cast spells. The _engaging_ player allocates damage first, followed by the _defending_ player, while the damage is dealt simulatenously. The amount of damage each unit deals is described in the next section. Remove any units that died and place damage tokens to reflect any damage to surviving units and buildings. In the rare situation that both players have lost all their units and buildings in the **Area** during a _combat step_, the _defending_ player will keep one unit or building of choice alive with 1 HP left.

Units and buildings can only ever attack once per round, even if they take part in multiple combat sitatuions.

### Damage

