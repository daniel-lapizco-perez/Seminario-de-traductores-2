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

![Tokens](https://user-images.githubusercontent.com/50065724/205696816-387557dd-6f1f-404e-86d5-f0582eedca4a.png)

<h5>Etapa 2: Analizador Sintactico</h5>

<p>
Esta etapa se crea para demostrar el funcionamiento de la pila y cómo es que las entradas recibidad se validan. Para poder llevar a cabo
este proceso se usa una grámatica que contiene un gran número de reglas, archivo el cuál se puede encontrar dentro de este repositorio como 
"compilador.lr"
</p>

![compilador lr](https://user-images.githubusercontent.com/50065724/205696947-6383fe2d-c247-48fa-90cf-76392710c317.PNG)
![compilador lr2](https://user-images.githubusercontent.com/50065724/205696998-3be0e91d-06df-4800-a14b-1514739030d9.PNG)


<h5>Etapa 3: Árbol Sintactico</h5>

<p>
El árbol sintactico se utiliza para demostrar el correcto funcionamiento del análisis sintactico. El funcionamiento de este es que cada
que se realiza una reducción en el análisis sintactico, el nodo se encarga de guardar cada elemento que se elimina, estos pueden contener
otros elementos no terminales que por consecuencia tendrán más nodos dentro de ese nodo en cuestión.
Como ya se emncionó, para poder llevar a cabo esta etapa, se decidió usar los nodos para un trabajo más fácil con problemas grandes.
</p>

![Arbol1](https://user-images.githubusercontent.com/50065724/205697075-e25ff58b-4dcd-46ff-9e53-f179d18e99b1.PNG)
![Arbol2](https://user-images.githubusercontent.com/50065724/205697115-b77836d9-e350-46d7-ada9-409c65b602bc.PNG)
![Arbol3](https://user-images.githubusercontent.com/50065724/205697137-5b7200d1-a3be-434e-ab5b-2302660f38ad.PNG)


<h5>Etapa 4: Árbol Semantico</h5>


<p>
En esta etapa lo único que se agrega es la salida de poder observar en aspecto de tabla la salida de simbolos y en caso de que existan, errores.
</p>

<p>Entrada</p>

![Entrada no valida](https://user-images.githubusercontent.com/50065724/205697269-b0e43c2f-5b10-4a1f-a8f3-4ee2c032396d.PNG)

<p>Entrada Aceptada</p>

![Entrada aceptada](https://user-images.githubusercontent.com/50065724/205697207-4b24d424-37bf-4d72-b7e2-de7abe29f4ec.PNG)

<p>Entrada No Aceptada</p>

![Salida no valida](https://user-images.githubusercontent.com/50065724/205697734-21d6051d-a594-4f29-b425-c00b35d161ff.PNG)

<h5>Etapa final: Generador de código</h5>

<p>
En esta última etapa se busca generar un archvio .asm el cual contenga el código en ensamblador.
</p>

<p>Ejemplo de código:</p>

![Entrada no valida](https://user-images.githubusercontent.com/50065724/205697269-b0e43c2f-5b10-4a1f-a8f3-4ee2c032396d.PNG)

<p>Archivo asm generado:</p>

![Archivo masm32](https://user-images.githubusercontent.com/50065724/205697990-9609d112-b354-4fe9-a02d-0b3d6da39fa1.PNG)

<p>
Este archivo es la traduccion en codigo ensamblador. Al no existir una funcion "print" en el lenguaje, 
cada que se realiza una asignacion se imprime en pantalla en el archivo asm la el valor de la variable a la que se le realizo la asgnacion.
</p>

<p>Para poder crear los archivos .exe y .obj se utilizó el programa MASM32</p>

![Generacion de archivos con MASM32](https://user-images.githubusercontent.com/50065724/205698050-2867f83a-cfa8-4cf5-a521-dc9599825b49.PNG)

![Archivos generados](https://user-images.githubusercontent.com/50065724/205698087-c1b65b7c-66cd-40d5-8f73-26b7b66d9ef4.PNG)

<p>Salida:</p>

![Salida final](https://user-images.githubusercontent.com/50065724/205698143-96709c0d-5017-4d83-9944-a7b7d69d7f9e.PNG)
