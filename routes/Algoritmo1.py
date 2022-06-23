import pyphi
import numpy as np

class Algoritmo1:
    def proceso_prueba(self,id,matrizTPM,matrizCM,estado, nodos,medicion, particion):
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

        return mip,mic,sia.phi,sia.cut



    def correAlgoritmo(self,grafo):
        nodos=[];
        aristas={};


        """Se analizan los nodos"""
        for nodo in grafo.nodos:
            nodos.append(nodo['dato']+""+nodo['id'])

        """Se analizan las aristas"""
        for arista in grafo.aristas:
            inicio=int(arista['inicio'])
            fin=int(arista['fin'])

            if inicio not in aristas:
                aristas[inicio]=[fin]
            else:
                aristas[inicio].append(fin)


        estado=[1] * len(nodos);
        matrizTPM=self.generaMatrizNPM(nodos,aristas)
        matrizCM=[([0] * len(nodos)) for i in range(len(nodos))]

        for arista in aristas.keys():
            for camino in aristas[arista]:
                matrizCM[arista-1][camino-1]=1

        mip,mic,sia,cut=self.proceso_prueba('0',matrizTPM,matrizCM,estado,nodos,'EMD','BI')

        print("-----")
        print(mip)
        print("-----")
        print(sia)


        return sia,cut


    def generaMatrizNPM(self,nodos,aristas):
        matrizTPM=[([1] * len(nodos)) for i in range(2**len(nodos))];
        return [[0,0,0,0],[0,1,1,1],[1,0,1,0],[1,1,1,1],[1,1,0,1],[1,0,1,0],[1,1,1,1],[1,0,1,0],[1,0,1,0],[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,0,1,0]]


