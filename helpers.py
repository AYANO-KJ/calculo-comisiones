import math
from constants import *
import click
from termcolor import colored

class Comisiones:
    def __init__(self, niveles: str, pv: str, tipo: str) -> None:
        self.niveles = int(niveles)
        self.pv = int(pv)
        self.precio_13_puntos = self.__precio13Puntos(self.pv)
        self.porcentaje_patrocino = self.__porcentajePatrocinio(self.pv)
        self.tipo = tipo

    def listar(self):
        comision_binario = 0
        comision_mlm = 0
        bronces = 0
        platas = 0
        oros = 0
        zafiros = 0
        rubis = 0
        diamantes = 0
        for i in range(self.niveles):
            if (i + 1) == self.niveles:
                continue
            pb_afiliado = self.__puntosBinario(self.pv, self.niveles, 1 + i)
            pb_nivel = pb_afiliado * self.__personasPorNivel(i + 1)
            rango = self.__rango(pb_afiliado)
            comision_binario += pb_nivel * (rango['comision_binario'] / 100)
            comision_mlm += pb_nivel * (rango['comision_mlm'] / 100)

            if rango['name'] == 'Bronce':
                bronces += self.__personasPorNivel(i + 1)
            elif rango['name'] == 'Plata':
                platas += self.__personasPorNivel(i + 1)
            elif rango['name'] == 'Oro':
                oros += self.__personasPorNivel(i + 1)
            elif rango['name'] == 'Zafiro':
                zafiros += self.__personasPorNivel(i + 1)
            elif rango['name'] == 'Rubi':
                rubis += self.__personasPorNivel(i + 1)
            elif rango['name'] == 'Diamante':
                diamantes += self.__personasPorNivel(i + 1)
        
        dinero_ingresado = self.__dineroIngresado(self.pv, self.precio_13_puntos, self.__totalAfiliados(self.niveles))
        comision_patrocinio = (self.__totalAfiliados(self.niveles) - 1) * self.pv * (self.porcentaje_patrocino)
        # total_comisiones = comision_binario + comision_mlm + comision_patrocinio
        total_comisiones = comision_binario + comision_patrocinio
        beneficio_dinero = dinero_ingresado - total_comisiones
        beneficio_porcentaje = (beneficio_dinero / dinero_ingresado) * 100

        if self.tipo == "afiliacion":
            return {
                'total_afiliados': self.__totalAfiliados(self.niveles),
                'dinero_ingresado': dinero_ingresado,
                'puntos_generados': self.__puntosGenerados(self.pv, self.__totalAfiliados(self.niveles)),
                'comisiones_patrocinio': comision_patrocinio,
                'comisiones_binario': comision_binario,
                # 'comisiones_mlm': comision_mlm,
                'comisiones_mlm': 0,
                'total_comisiones': total_comisiones,
                'beneficio_dinero': beneficio_dinero,
                'beneficio_porcentaje': beneficio_porcentaje,
                'bronces': bronces,
                'platas': platas,
                'oros': oros,
                'zafiros': zafiros,
                'rubis': rubis,
                'diamantes': diamantes,
            }
        elif self.tipo == "reconsumo":
            new_total_comisiones =  comision_binario + comision_mlm
            new_beneficio_dinero = dinero_ingresado - new_total_comisiones
            new_beneficio_porcentaje = (new_beneficio_dinero / dinero_ingresado) * 100
            return {
                'total_afiliados': self.__totalAfiliados(self.niveles),
                'dinero_ingresado': dinero_ingresado,
                'puntos_generados': self.__puntosGenerados(self.pv, self.__totalAfiliados(self.niveles)),
                'comisiones_patrocinio': 0,
                'comisiones_binario': comision_binario,
                'comisiones_mlm': comision_mlm,
                'total_comisiones': new_total_comisiones,
                'beneficio_dinero': new_beneficio_dinero,
                'beneficio_porcentaje': new_beneficio_porcentaje,
                'bronces': bronces,
                'platas': platas,
                'oros': oros,
                'zafiros': zafiros,
                'rubis': rubis,
                'diamantes': diamantes,
            }
    
    def __puntosGenerados(self, pv: int, afiliados: int) -> int:
        return pv * afiliados

    def __dineroIngresado(self, pv: int, paquete: int, afiliados: int) -> int:
        print(pv, paquete, afiliados)
        return pv * (paquete / 13) * afiliados

    def __totalAfiliados(self, niveles: int) -> int:
        return math.pow(2, niveles) - 1
    
    def __porcentajePatrocinio(self, pv: int) -> int:
        if pv >= 100:
            return 1
        else:
            return 0.7
        
    def __precio13Puntos(self, pv: int) -> int:
        if pv >= 39:
            return 81
        else:
            return 90
    def __personasPorNivel(self, nivel):
        return math.pow(2, nivel - 1)
    
    def __rango(self, pb_afiliado):
        rangos = []
        for rango in RANGOS:
            if rango['brazo_pago'] <= pb_afiliado:
                rangos.append(rango)
        return rangos[-1]
    
    def __puntosBinario(self, pv: int, niveles: int, nivel: int) -> int:
        return pv * (math.pow(2, niveles - nivel) - 1)

def validarPv(numero):
    return int(numero) % 13 == 0

def validarTipo(tipo: str):
    return tipo == 'reconsumo' or tipo == 'afiliacion'