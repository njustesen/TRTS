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

In the _Micromanagement Phase_, players can _micromanage_ (or just _micro_) their units. In the _current player turn order_ one **Control Group** is _activated_ at a time to perform one or more _Micro Actions_. After a **Control Group** has performed one or more _Micro Actions_, they cannot be _activated_ until the next turn. Units can only perform _Micro Actions_ when they are _activated_ making already-_activated_ units fragile from attacks. 

When a **Control Group** is finished with its _activatation_, it becomes the next player to _activate_ a **Control Group** or _pass_. When a player _passes_, that player's _Micromanagement Turn_ is simply skipped. In the next _Micromanagement Turn_, that player can decide again to_activate_ a **Control Group** or _pass_. When all players have _passed_ in a round, the _Micromanagement Phase_ is over and a new turn starts.

When finishing the _activation_ of a **Control Group**, the current player can optionally decide to continue to perform _micro actions_ with subgroups of the **Control Group** before that player's _Micromanagement Turn_ ends.

A **Control Group** is simply a set of units that performs the same _Micro Action_. They do not have to start in the same **Area** but their _micro actions_ must target the same **Area**. It is good practice to place units in a **Control Group** close together in an **Area** so it is easy to remember that they are either _active_ now or have been _activated_.

Some units can perform special _Micro Actions_ which are described in their _special rules_, while (almost) all units can do a _Move Action_, an _Attack Action_, and a _Hold Position Action_. 

#### Move Action

This action allows you to move a **Control Group** through **Areas** that you _control_ or _contest_ to an **Area** that you also _control_ or _contest_. All the units must, however, have enough _Movement Points_ to reach the **Area**. Move the units to the **Player Board Area** and place them together to indicate that they have been _activated_. If you moved through any contested areas, you have to briefly reveil the **Control Group** and let everyone know which **Areas** they passed through. Opponent units cannot attack your units as they _pass through_ contested **Areas** as they are busy fighting the existing units. If **Control Group** moves into an **Area** that they do not control or _contest_, place a **Control Marker** on the **Game Board Area** to indicate an _engagement_. 

Here, there are 3 possible scenarios:

1. If the **Area** is _neutral_, remove the **Neutral Control Marker** and you now control the engaged **Area**. 

2. If the **Area** is under control by enemy players, the players controlling the **Area** has to say whether or not they have any units or buildings.

* If there are no units/buildings in the engaged **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the engaged **Area**.

* If there are units or buildings, immediately move all units that are in the corresponding **Player Board Areas**, including the engaging units, onto the **Game Board Area** so they become visible to everyone. Then, carry out a _Combat_ round (described later).

When the _Move Action_ (and any _Combat_) is over, the **Control Group** is allowed to continue its activation.

#### Attack Action
A **Control Group** in an **Area** with enemy units or buildings can initiate a _Combat_ round if they have not attacked yet this turn.

#### Hold Position Action
This defensive actions ends the _activation_ of a **Control Group** but allows them to _attack_ during _Combat_ rounds in their **Area** that will occour until they become _activated_ again.

Units cannot perform a _Hold Position Action_ if they have attacked this turn.

Units will automatically perform a _Hold Position Action_ when they end their _activation_ if haven't attacked yet this turn.

Newly deployed units are not in _Hold Position_ until they are _activated_ which makes them fragile to attacks.

#### Retreat (Re-)Action
Immedieatly when non-_activated_ units are being _engaged_ by an enemy **Control Group**, thay may decide to _retreat_ to and through **Areas** that are _controlled_ or _contested_ except for the **Area** from which the _engaging_ **Control Group** came from. The _retreating_ **Control Group** ends their _activation_ in _Hold Position_ but they do not initiate any _Combat_ in the **Area** they _retreated_ into.

### Combat
A _combat round_ is performed in several _combat steps_ where units with the long range attack first. In each _combat step_, units and buildings that share the _range_ value of the current _combat step_ can _attack_ and _cast spells_. A _combat round_ thus starts with the highest range of any unit in the **Area**, then the next highest, the third, and so on until all units have had a change. 

During a _combat step_, the following happens:

1. All units with a greater _sight_ value than the _range_ value of the current _combat step_ can retreat to any adjacent **Area** with an owned **Control Marker**, given they have enough movement points left.

2. Units that match the _range_ value of the current _combat step_ can attack or cast spells. This is done in the _player turn order_ but the damage are allocated simulatenously. The amount of damage each unit deals is described in the next section. Remove any units that died and place damage tokens to reflect any damage to surviving units/buildings.

3. In the **player turn order** units that match the _range_ value of the current _combat step_ can retreat to any adjacent **Area** under control or contested by the units' owner, if they have enough movement points left. 

Retreating units can use all their movement points to move severeal **Areas** away from the engaged **Area**. 

Retreating units cannot move anymore this turn. 

Units cannot reatreat if they have performed _Micromanagement Actions_ previously in this.

Units and buildings can only attack one time in a turn even if they take part of multiple combat rounds. 

### Damage

