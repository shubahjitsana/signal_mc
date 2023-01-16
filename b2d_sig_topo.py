#!/usr/bin/env python3
import sys
import basf2 as b2
import modularAnalysis as ma
import variables.MCGenTopo as vmc   # module( interface of basf2 to TopoAna)
                                    # to extract out Topological information


# get input file number from the command line
file_name = sys.argv[1]
# file_number = file_name.split("sub00/")
# input_filename = file_number[1]

# # get output folder name from the command line
# output_foldername = sys.argv[2]
# output_filename = input_filename


main = b2.create_path()

# load input ROOT file
ma.inputMdstList(environmentType="default",filelist=f"{file_name}",path=main)


# Output the variables to a ntuple
ma.variablesToNtuple(decayString='',
    variables=vmc.mc_gen_topo(200),     # this variabe contains Topological information
    filename= f"topo_{file_name}",
    treename= 'tree',
    path=main)

# Process the events
b2.process(main)

# Print out the summary
print(b2.statistics)