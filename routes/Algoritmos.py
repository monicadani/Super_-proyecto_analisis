import pyphi
import numpy as np


def proceso_prueba(id,matrizTPM,matrizCM,estado, nodos,medicion, particion):
    # Setup
    tpm = np.array(matrizTPM)
    cm = np.array(matrizCM)
    network = pyphi.Network(tpm, node_labels=nodos)

    """Tipos de medicion, 'EMD', 'L1', 'KLD', 'ENTROPY_DIFFERENCE', 'PSQ2', 'MP2Q', 'BLD', 'KLM']"""
    pyphi.config.MEASURE = 'EMD'
    """Tipos de particion, 'BI', 'TRI', 'ALL'] """
    pyphi.config.PARTITION_TYPE = 'BI'


    state = estado
    nodes = nodos
    subsystem = pyphi.Subsystem(network, state, nodes)

    # Cause/effect repertoires (mechanism-level information)

    indice_nodos = subsystem.node_indices

    mechanism = (indice_nodos[0],)
    purview = indice_nodos
    cr = subsystem.cause_repertoire(mechanism, purview)

    flat_cr = pyphi.distribution.flatten(cr)

    # Minimum-information partitions (mechanism-level integration)

    mechanism = indice_nodos
    purview = indice_nodos
    mip = subsystem.effect_mip(mechanism, purview)

    # Maximally-irreducible cause-effect repertoires (mechanism-level exclusion)

    mechanism = indice_nodos[1:len(indice_nodos )]
    mic = subsystem.mic(mechanism)

    # Concepts

    mechanism = (indice_nodos[0])
    concept = subsystem.concept(mechanism)

    full_cr = concept.expand_cause_repertoire()
    full_er = concept.expand_effect_repertoire()

    # Cause-effect structures (system-level information)

    ces = pyphi.compute.ces(subsystem)

    # Irreducible cause-effect structures (system-level integration)

    sia = pyphi.compute.sia(subsystem)

    # Complexes (system-level exclusion)

    state = estado
    major_complex = pyphi.compute.major_complex(network, state)

    print("----------------------Matriz "+id+" "+medicion+" "+particion+"------------------------")
    print("----MIP----")
    print(mip)
    print("----MIC(opcional)----")
    print(mic)
    print("----valor de phi----")
    print(sia.phi)
    print("----corte----")
    print(sia.cut)


def test1():
    nodosA=[
    {"dato": "NOT1", "id": "1"},
    {"dato": "AND1", "id": "2"},
    {"dato": "OR1", "id": "3"},
    {"dato": "XOR1", "id": "4"}
    ]

    aristasA=[
    {"inicio": 1, "fin": 2, "peso": 2},
    {"inicio": 2, "fin": 1, "peso": 3},
    {"inicio": 1, "fin": 3, "peso": 5},
    {"inicio": 2, "fin": 2, "peso": 10},
    {"inicio": 3, "fin": 4, "peso": 20},
    {"inicio": 4, "fin": 1, "peso": 50},
    ]

    nodosA=["NOT1","AND1","OR1","XOR1"];

    aristas={1:[2,3],2:[1,2],3:[4],4:[1]}

    matrizTPM=[[0,0,0,0],[0,1,1,1],[1,0,1,0],[1,1,1,1],[1,1,0,1],[1,0,1,0],[1,1,1,1],[1,0,1,0],[1,0,1,0],[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,0,1,0]]

    matrizCM=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for arista in aristas.keys():
        for camino in aristas[arista]:
            matrizCM[arista-1][camino-1]=1


    estado=(0, 0, 0,0)
    nodos=("NOT1","AND1","OR1","XOR1")

    print("-----------Matriz 0------------")
    proceso_prueba('0',matrizTPM,matrizCM,estado,nodos,'EMD','BI')










if __name__ == '__main__':
    test1()

