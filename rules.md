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

#### Positioning
All players simply move the units they want to move between **Areas** they control. Units in _contested_ **Areas** are, however, _pinned_ until the _Pushing Phase_ and cannot move in this phase. Units can use their full movement points in this phase but if they move in this phase, they cannot be moved (besides retreating) in the _Micromanagement Phase_. Therefore, group/mark units that have moved.

### Micromanagement Phase

Units that did not move in the _Positioning Phase_ can make so-called _pushes_ into _uncontrolled_ and _contested_ **Areas** in the _Micromanagement Phase_. During a _push_, one or more combat rounds can occour, however, at modt one per **Area** in each round.

#### Pushes
In the _current player turn order_, each player can make a push with a so-called **Control Group**. When the push is over, the units in the **Control Group** cannot be part of another push later this round.

To make a push, select a group of units (your **Control Group**) that can all reach an **Area** that is not under _control_ that they wish to _engage_ and that is adjacent to their current **Area** (which doesn't have to be the same). Units in _contested_ **Areas** can be part of a **Control Group** and can safely move to the target **Area**. Units that are already in the targeted **Area** will automatically be part of the **Control Group** and will simply stay where they are. You cannot target an **Area** that you have already targeted this round. Now, place one of your **Control Markers** on the **Game Board Area**. Then move the **Control Group** to the target **Player Board Area** and (if relevant) keep note on how many movement point each unit has left. 

There are 3 possible scenarios when _pushing_ into an **Area**:

1. If the **Area** is _neutral_, remove the _neutral_ **Control Marker**. You now control the **Area**. 

2. If the **Area** is under _control_ by an enemy player, the player controlling the **Area** has to say whether or not they have any units or buildings in that **Area**.

* If there are no units or buildings in the **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the **Area**.

* If there are units or buildings in the **Area**, immediately move them and the **Control Group** to the **Game Board Area** so they become visible to everyone. Any of the defending units can decide immediately to _retreat_ to an adjacent **Area** under control (if there are any) without taking part of the combat. Units that have _retreated_ cannot be part of a _push_ later this round. Units that have already _pushed_, always have the option to _retreat_ when being engaged, regardless of how much they have moved, except if there are no adjacent **Area** under _control_. If the defending player does not have vision to see any of the attacking units, _retreating_ is also not an option. If all enemy units and buildings are eliminated during combat, the _pushing_ player gains control over the **Area**. If the **Area** remains _contested_, keep both players' **Control Markers**, units, and buildings on the **Game Board Area**.

A **Control Group** can be moved multiple times if they have enough movement points. It is not allowed to split up the **Control Groups** and _micro_ them individually. You can, however, leave behind some of the units in a **Control Groups** and continue to move with another subset of the units, e.g. if some units are faster than the others, or if some units will stay and fight while others will move forward to harass another **Area**. When units are left behind, their _activation_ ends, and they can no longer move, nor _retreat_, until next round. This means that you only have to remember how many movement points are left for the units within the _active_ **Control Group**, since all other units either cannot move anymore or have not been _microed_ yet. In the late-game, it can become necessary to mark **Control Group** that have been _microed_.

#### Moving a Control Group
To initiate a movement of a **Control Group**, first, select a group of units under your control that have not yet been _microed_ yet and move them to an **Area** that they can all reach (see how many movement points they have). Units in _contested_ **Areas** can be _microed_ normally. If you _control_ the target **Area**, simply move them to the **Player Board Area** so their location is secret to others. If you do not _control_ the **Area**, an _engagement_ will occour. 

After moving a **Control Group** and resolving any _engagements_, you can either declare the _activation_ finished or you can continue moving with some or all of the units in the **Control Groups**, given they have enough movement points left. Remember that units that are left behind cannot be _microed_ again later.

#### Engagement
If a **Control Group** moves into an **Area** that they do not _control_ or _contest_, place a **Control Marker** on the **Game Board Area** to indicate you are _engaging_. 

There are 3 possible scenarios for an _engagement_:

1. If the **Area** is _neutral_, remove the _neutral_ **Control Marker**. You now control the _engaged_ **Area**. 

2. If the **Area** is under _control_ by enemy players, the player controlling the **Area** has to say whether or not they have any units or buildings in that **Area**.

* If there are no units or buildings in the _engaged_ **Area**, keep your **Control Marker** on the **Game Board Area** and remove any enemy **Control Markers**. You now control the _engaged_ **Area**.

* If there are units or buildings, immediately move all units that are in the corresponding **Player Board Areas**, including the _engaging_ units, onto the **Game Board Area** so they become visible to everyone. New upgrades must be declared immediately while research that enables new spells can be kept secret until used.
If all enemy units and buildings are eliminated during combat, you gain control over the **Area**, otherwise, it remains _contested_ (keep both players' **Control Markers**, units, and buildings on the **Game Board Area**).

### Combat
A _combat_ is performed in several _combat steps_ where units with the long _range_ attack before units with short _range_. In each _combat step_, units and buildings that share the same _range_ value of the current _combat step_ can attack and cast spells. A _combat round_ thus starts with the highest range of any unit in the **Area**, then the second highest, the third, and so on, until all units have had a change to attack (unless they are killed first). 

During a _combat step_ at _range_ X, the following happens:

1. If the _enganging_ player has any unit with greater _sight_ than X, any unit under control can be _microed_ to _retreat_ (if they haven't been _microed_ previously this round). _Retreating_ simply means that you immediately moves the _retreating_ units to an **Area** they can be reached and that are under _control_ or _contested_. Since _retreating_ requires _micromanagement_ these units cannot be _microed_ again this round.

2. If the _defending_ player has any unit with greater _sight_ than X, any unit under control can be _microed_ to _retreat_ following the same rules as above.

3. Both _engaging_ and _defending_ units that match the _range_ value of the current _combat step_ can attack or cast spells. The _engaging_ player allocates damage first, followed by the _defending_ player, while the damage of this _combat step_ is dealt simulatenously. The amount of damage each unit deals is described in the next section. Remove any units that died and place damage tokens to reflect any damage to surviving units and buildings. In the rare situation that both players have lost all their units and buildings in the **Area** during one _combat step_, the _defending_ player will keep one unit or building of choice alive with 1 HP left.

The _active_ **Control Group** cannot retreat during combat if they _engaged_ the combat in this round _up a ramp_. Simply ignore step #1 in this case. 

Units and buildings can only ever attack once per round, even if they take part in multiple combat sitatuions.

### Damage

