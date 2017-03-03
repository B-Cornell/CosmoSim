# CosmoSim
This project is split into 3 parts.

Part 1
This involved finding all of the potential mergers.
I first used an SQL search to find all of the halos with more than one descendant and at least one descendant's mass is over 1E14. I then used python to filter these to get only the halos with more than one descendant with mass over 1E14.
Query_1e14.txt to get 1e14_as_the_desc_mass_limit.csv
Find_doubles_in_text.py and "".csv to get Doubles_1e14.txt

Part 2
This involved finding the merger trees of the halo mergers found in Doubles_1e14.txt
Used treeroot.py and the .txt file to create SQL queries that took the id's and foudn all of the tree roots over 1E13. They are saved in the Final Trees folder

Part 3
This part was the visualization and more indepth analysis on one halo merger.
I saved one tree from part 2 and saved it as TestTree.csv, where I used GraphCosmosim.p to graph it in a 3D space. THis is where I saw that the Rockstar Halo Finder had not found all of the subhalos in the merger. This meant that I couldn't see al of the movement of the two individual halos after they merged.
I tried to get more subhalos using more SQL searches but did not find anything that I could use. This is when I abandoned the project
