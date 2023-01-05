
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input( '../figures/Board position.png', width=5, height=5, to="(-1,0,0)"),

    # to_Conv("conv1", 10, 2, offset="(0,0,0)", to="(0,0,0)", height=20, depth=20, width=1),
    to_Conv("conv1", 10, 2, offset="(0,0,0)", to="(0,0,0)", height=20, depth=20, width=1),
    to_Relu("relu1", offset="(0,0,0)", to="(conv1-east)", height=20, depth=20, width=.5, opacity=.4),

    to_Conv("conv2", 8, 64, offset="(1,0,0)", to="(relu1-east)", height=16, depth=16, width=10),
    to_Relu("relu2", offset="(0,0,0)", to="(conv2-east)", height=16, depth=16, width=.5, opacity=.4),
    to_connection("relu1", "conv2"),

    to_Conv("conv3", 6, 64, offset="(1,0,0)", to="(conv2-east)", height=12, depth=12, width=10),
    to_Relu("relu3", offset="(0,0,0)", to="(conv3-east)", height=12, depth=12, width=.5, opacity=.4),
    to_connection("relu2", "conv3"),

    to_fc("fc1", 100, offset="(2,0,0)", to="(relu3-east)", height=1, width=1, depth=25),
    to_Relu("relu4", offset="(0,0,0)", to="(fc1-east)", height=1, depth=25, width=.5, opacity=.4),
    to_DensilyDashed("relu3","fc1"),
    to_connection("relu3", "fc1"),

    to_fc("fc3", 1, offset="(1,0,0)", to="(relu4-east)", height=1, width=1, depth=1),
    to_Tanh("tanh1", offset="(0,0,0)", to="(fc3-east)", height=1, depth=1, width=.5, opacity=.4),
    to_connection("relu4", "fc3"),

    to_end()
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
