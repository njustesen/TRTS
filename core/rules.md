# Game Rules

## Overview
A TRTS game is played over a series of rounds and ends in one of the following ways:

- The final round has ended and several players are still in the game, in which case the player with the most **areas** under control wins*.
- A player is eliminated. The victory conditions in this case differs from the match type:
  - In a **2-player** match, the eliminated player lose the game, and the remaining player wins.
  - In a **team** match, the team of the elimnated player lose the game, and the other team wins.
  - In a **free-for-all** match, the player with the most **areas** under controls win*.
  - In a **last-man-standing** match, the game continues if there are more than two player remaining, otherwise the remaining player claims the victory.

*In case of a tie, it is the player with the most units (counted by supply) that wins.

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

In the _Micromanagement Phase_, players perform a sereis of _Micromanagement Actions_ with a _group of units_ in the _current player turn order_ until all players have passed in the same round. When the group of units are done with their their _Micromanagement Actions_, they can no longer move or retreat this turn. They can, however, make an _attack_ while defending if they did not make an _attack_ in this turn. After performing a _Micromanagement Action_, it becomes the next player in _current player turn order_ to perform a _Micromanagement Action_ or to _pass_. When a player _passes_, they can still perform _Micromanagement Actions_ lather in the _Micromanagement Phase_ while it ends when all players are _passing_.

A _Micromanagement Action_ is performed by first selecting a group of units that must execute the same _Micromanagement Action_. Some units can perform special _Micromanagement Actions_ which is described in their own ruleset, while the main _Micromanagement Action_ is either _Move Actions_, _Engagement Actions_ or _Combat Actions_ which are described below.

#### Move Action

This action allows you to move a group of units through **Areas** that you _control_ or _contest_ to an **Area** that you also _control_ or _contest_. All units in the group must, however, have enough _Movement Points_ to reach the **Area**. Move the units to the **Player Board Area** and place them together to indicate that they have acted. If you moved through any contested areas, you have to briefly reveil the group of units and let everyone know which **Areas** they passed through. Opponent units cannot attack your units as they pass through contested **Areas** as they are busy fighting the existing units. 

#### Engagement Action

To move into an **Area** that you do not _control_ or _contest_, you must make an _Engagement Action_. Select a group of units, which can come from different **Areas**, and move them to a target **Player Board Area**. You cannot move through **Areas** that you do not either _control_ or _contest_. Then, indicate that you maded an _engagement_ to the **Area** by placing a **Control Marker** on the **Game Board Area**. 

Here, there are 3 possible scenarios:

1. If the **Area** is _neutral_, remove the **Neutral Control Marker** and you now control the engaged **Area**. 

2. If the **Area** is under control by enemy players, the players controlling the **Area** has to say whether or not they have any units or buildings.

* If there are no units/buildings in the engaged **Area**, keep your **Control Marker** on the **Game Baord Area** and remove any **Control Markers** of other players. You now control the engaged **Area**.

* If there are units or buildings, immediately move all units that are in the corresponding **Player Areas** onto the **Game Board Area** so they become visible to anyone, including the engaging units. Then, carry out a _combat_ round, described in the next section.

3. If the **Area** is already contested by you, move the units directly to the new **Game Board Area** and perform a round of combat.

Moving from one **Area** to an adjacent **Area** costs one movement point. Units cannot move or retreat if they are out of _movement points_. 

After making an _engagement_ (and after any _combat rounds_), _the group of units_ can immediately continue to perform another _Micromanagement Action_. Units can, however, only attack on time per _turn_ and units cannot move anymore if they are out of _movement points_. Units that have survived a _combat round_ without attacking are still allowed to attack in any proceeding _combat rounds_. Thus, deciding not to attack in a _combat round_ can allow units to move further into the opponents **Areas** and then attack. 

When the sequence of _engagements_ are over for the group of units, they can no longer move or retreat in this turn.

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

