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
        aristas_inv = {};


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

        """Se analizan las aristas de forma inversa"""
        for arista in grafo.aristas:
            inicio=int(arista['inicio'])
            fin=int(arista['fin'])

            if fin not in aristas_inv :
                aristas_inv [fin]=[inicio]
            else:
                aristas_inv [fin].append(inicio)

        print(nodos)
        print(aristas)
        print(aristas_inv)


        estado=[1] * len(nodos);
        matrizTPM=self.generaMatrizNPM(nodos,aristas,aristas_inv)
        matrizCM=[([0] * len(nodos)) for i in range(len(nodos))]

        for arista in aristas.keys():
            for camino in aristas[arista]:
                matrizCM[arista-1][camino-1]=1

        cut="a"
        sia="b"
        mip,mic,sia,cut=self.proceso_prueba('0',matrizTPM,matrizCM,estado,nodos,'EMD','BI')
        print(mip)
        print(mic)
        print(sia)
        print(cut)


        return sia,cut


    def correAlgoritmoAlt(self,grafo):
        nodos=[];
        aristas={};
        aristas_inv = {};


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

        """Se analizan las aristas de forma inversa"""
        for arista in grafo.aristas:
            inicio=int(arista['inicio'])
            fin=int(arista['fin'])

            if fin not in aristas_inv :
                aristas_inv [fin]=[inicio]
            else:
                aristas_inv [fin].append(inicio)

        print(nodos)
        print(aristas)
        print(aristas_inv)


        estado=[1] * len(nodos);
        matrizTPM=self.generaMatrizNPM(nodos,aristas,aristas_inv)
        matrizCM=[([0] * len(nodos)) for i in range(len(nodos))]

        for arista in aristas.keys():
            for camino in aristas[arista]:
                matrizCM[arista-1][camino-1]=1

        cut="a"
        sia="b"
        mip,mic,sia,cut=self.proceso_prueba('0',matrizTPM,matrizCM,estado,nodos,'EMD','BI')
        print(mip)
        print(mic)
        print(sia)
        print(cut)


        return sia,cut


    def generaMatrizNPM(self,nodos,aristas,aristas_inv):
        matrizTPM=[([0] * len(nodos)) for i in range(2**len(nodos))];

        for i in range(2**len(nodos)):
            lista=self.combinacion(i,len(nodos))

            for j in range(len(nodos)+1):
                dato_booleano = 1
                if j in aristas_inv:
                    ##print("--inicio--")

                    nodo_tmp=nodos[j-1]
                    ##print(nodo_tmp)

                    """Si es un and"""
                    if(nodo_tmp.startswith("AND")):
                       for k in aristas_inv[j]:
                           dato_booleano=(dato_booleano and lista[k-1])

                    """Si es un or"""
                    if(nodo_tmp.startswith("OR")):
                       for k in aristas_inv[j]:
                           dato_booleano=(dato_booleano or lista[k-1])

                    """Si es un not"""
                    if(nodo_tmp.startswith("NOT")):
                       for k in aristas_inv[j]:
                           dato_booleano=(dato_booleano and lista[k-1])
                           if dato_booleano is 1:dato_booleano=0
                           else:dato_booleano=1

                    """Si es un xor"""
                    if(nodo_tmp.startswith("XOR")):
                       for k in aristas_inv[j]:
                           dato_booleano=dato_booleano ^ lista[k-1]


                matrizTPM[i][j-1]=dato_booleano


        return matrizTPM


    def combinacion(self,iteracion,numero):
        num = bin(iteracion)[2:]
        lista = [0] * numero;
        for j in range(len(num)):
            lista[len(num) - 1 - j] = int(num[j])
        return lista
