# Seminario-de-traductores-2

<h1>Proyecto Seminario de Solución de Problemas de Traductores de Lenguajes 2</h1>

<h3>Lapizco Pérez Daniel</h3>
<h3>218744716</h3>

<h5>Etapa 1: Analizador Léxico</h5>

<p>
En esta etapa inicial lo que se pretende hacer es reconocer los tokens de una entrada, con el fin de poder identificar que es el token que se está leyendo
y con esto saber si es que el token es válido o no más delante en el proceso del compilador.
A continuación se muestra la lista de tokens con la que se estará trabjando
</p>

#Imagen del lexico

<h5>Etapa 2: Analizador Sintactico</h5>

<p>
Esta etapa se crea para demostrar el funcionamiento de la pila y cómo es que las entradas recibidad se validan. Para poder llevar a cabo
este proceso se usa una grámatica que contiene un gran número de reglas, archivo el cuál se puede encontrar dentro de este repositorio como 
"compilador.lr"
</p>

#Captura del archivo de compilador

<h5>Etapa 3: Árbol Sintactico</h5>

<p>
El árbol sintactico se utiliza para demostrar el correcto funcionamiento del análisis sintactico. El funcionamiento de este es que cada
que se realiza una reducción en el análisis sintactico, el nodo se encarga de guardar cada elemento que se elimina, estos pueden contener
otros elementos no terminales que por consecuencia tendrán más nodos dentro de ese nodo en cuestión.
Como ya se emncionó, para poder llevar a cabo esta etapa, se decidió usar los nodos para un trabajo más fácil con problemas grandes.
</p>

#Captura de un árbol


<h5>Etapa 4: Árbol Semantico</h5>

<p>
En esta etapa lo único que se agrega es la salida de poder observar en aspecto de tabla la salida de simbolos y en caso de que existan, errores.
</p>

#Captura de entrada

#Captura de entrada correcta

#Captura de entrada incorrecta

<h5>Etapa final: Generador de código</h5>

<p>
En esta última etapa se busca generar un archvio .asm el cual contenga el código en ensamblador.
</p>

<p>Ejemplo de código:</p>
#Captura del ejemplo de código
<p>Archivo asm generado:</p>
#Captura del archivo asm
<p>
Este archivo es la traduccion en codigo ensamblador. Al no existir una funcion "print" en el lenguaje, 
cada que se realiza una asignacion se imprime en pantalla en el archivo asm la el valor de la variable a la que se le realizo la asgnacion.
</p>

<p>Para poder crear los archivos .exe y .obj se utilizó el programa MASM32</p>
#Captura de archivos

<p>Salida:</p>
#Captura de salida de ejecutable
