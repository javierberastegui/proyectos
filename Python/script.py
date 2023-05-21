import re

html = '<p>Como ya hemos visto con anterioridad, <a href="https://javierberastegui.dev/python/las-listas-los-diccionarios-y-las-tuplas-en-python"><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"><span _istranslated="1" style="color:#1155cc">los diccionarios y las listas</span></span></span></a><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"> son muy &uacute;tiles en Python, en lo que se refiere la manipulaci&oacute;n y a la estructura de datos. Como sabemos, las listas y los diccionarios en Python no son m&aacute;s que una forma de organizar objetos, las listas y </span></span><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial">diccionarios anidados pueden hacer nuestro trabajo mucho m&aacute;s profesional si lo que queremos es trabajar con estructura de datos.</span></span></p>

<p _msthash="245" _msttexthash="165181354"><span style="font-size:11pt"><span style="font-family:Arial">La clave para entender porque se usa los diccionarios y las listas anidadas es que estos son &uacute;tiles cuando quieres </span></span><span style="font-size:11pt"><span style="font-family:Arial"><strong>guardar informaci&oacute;n que tiene m&aacute;s de una dimensi&oacute;n o nivel</strong></span></span><span style="font-size:11pt"><span style="font-family:Arial">. Por ejemplo, si quieres guardar los datos de una persona, puedes usar un diccionario con sus atributos como llaves y sus valores como valores. Pero si quieres guardar los datos de varias personas, puedes usar una lista de diccionarios, donde cada diccionario representa a una persona. </span></span><span style="font-size:11pt"><span style="font-family:Arial"><strong>As&iacute; puedes acceder a la informaci&oacute;n de cada persona por su posici&oacute;n en la lista y por su atributo en el diccionario</strong></span></span><span style="font-size:11pt"><span style="font-family:Arial">.</span></span></p>

<p _msthash="244" _msttexthash="16882528">Los diccionarios y <span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial">las listas anidadas te permiten </span></span><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"><strong _istranslated="1">organizar mejor la informaci&oacute;n y acceder a ella de forma m&aacute;s f&aacute;cil y r&aacute;pida</strong></span></span><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"> que si usaras solo diccionarios o listas simples.</span></span></p>

<p><span style="font-size:11pt"><span _msthash="243" _msttexthash="10433267" style="font-family:Arial">Los diccionarios y las listas anidadas tienen ventajas y desventajas dependiendo del uso que les quieras dar. Algunas de sus ventajas son:</span></span></p>

<ul>
	<li style="list-style-type:disc"><span _msthash="240" _msttexthash="5732779" style="font-size:11pt">Te permiten guardar informaci&oacute;n compleja y relacionada entre s&iacute; de forma ordenada y estructurada.</span></li>
	<li style="list-style-type:disc"><span _msthash="241" _msttexthash="3729986" style="font-size:11pt">Te facilitan el acceso y la modificaci&oacute;n de los elementos por su &iacute;ndice o llave.</span></li>
	<li style="list-style-type:disc"><span _msthash="242" _msttexthash="5480176" style="font-size:11pt">Te ofrecen flexibilidad para guardar diferentes tipos de datos y objetos en una misma colecci&oacute;n.</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="239" _msttexthash="4078139" style="font-family:Arial">Tambien las listas y los diccionarios anidados cuentan con alguna desventaja como:</span></span></p>

<ul>
	<li style="list-style-type:disc"><span _msthash="236" _msttexthash="6553261" style="font-size:11pt">Pueden ocupar m&aacute;s memoria que las listas o los diccionarios simples, ya que tienen m&aacute;s elementos y niveles.</span></li>
	<li style="list-style-type:disc"><span _msthash="237" _msttexthash="6375980" style="font-size:11pt">Pueden ser m&aacute;s dif&iacute;ciles de recorrer o iterar, ya que requieren de bucles anidados o funciones especiales.</span></li>
	<li style="list-style-type:disc"><span _msthash="238" _msttexthash="7898527" style="font-size:11pt">Pueden generar errores o confusiones si no se usan correctamente las llaves o los &iacute;ndices para acceder a los elementos.</span></li>
</ul>

<h2><span style="font-size:16pt"><span _msthash="235" _msttexthash="2522884" style="font-family:Arial">&iquest;Qu&eacute; m&eacute;todos se usan con los diccionarios y las listas anidadas?&nbsp;</span></span></h2>

<p _msthash="234" _msttexthash="37525527"><a _istranslated="1" href="https://javierberastegui.dev/python/uso-de-los-metodos-como-trabajar-con-las-cadenas-de-caracteres" style="text-decoration-line:none"><span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"><span _istranslated="1" style="color:#1155cc">Los m&eacute;todos de Python</span></span></span></a> que se <span _istranslated="1" style="font-size:11pt"><span _istranslated="1" style="font-family:Arial"> usan con los diccionarios y las listas anidadas son funciones que se aplican sobre estos objetos para realizar diferentes operaciones, como agregar, eliminar, modificar, buscar o ordenar elementos. Algunos de los m&eacute;todos m&aacute;s comunes son:</span></span></p>

<h4><span style="font-size:12pt"><span style="font-family:Arial"><span _msthash="233" _msttexthash="439335" style="color:#666666">Para los diccionarios:</span></span></span></h4>

<ul>
	<li style="list-style-type:disc"><span _msthash="226" _msttexthash="3137030" style="font-size:11pt">keys(): devuelve un objeto de vista con todas las claves del diccionario.</span></li>
	<li style="list-style-type:disc"><span _msthash="227" _msttexthash="3450590" style="font-size:11pt">values(): devuelve un objeto de vista con todos los valores del diccionario.</span></li>
	<li style="list-style-type:disc"><span _msthash="228" _msttexthash="5424042" style="font-size:11pt">items(): devuelve un objeto de vista con todos los pares clave-valor del diccionario como tuplas.</span></li>
	<li style="list-style-type:disc"><span _msthash="229" _msttexthash="6079151" style="font-size:11pt">get(): devuelve el valor asociado a una clave del diccionario o un valor por defecto si la clave no existe.</span></li>
	<li style="list-style-type:disc"><span _msthash="230" _msttexthash="6273436" style="font-size:11pt">update(): actualiza el diccionario con los pares clave-valor de otro diccionario o de un objeto iterable.</span></li>
	<li style="list-style-type:disc"><span _msthash="231" _msttexthash="7168642" style="font-size:11pt">pop(): elimina y devuelve el valor asociado a una clave del diccionario o un valor por defecto si la clave no existe.</span></li>
	<li style="list-style-type:disc"><span _msthash="232" _msttexthash="1881737" style="font-size:11pt">clear(): elimina todos los elementos del diccionario.</span></li>
</ul>

<h4><span style="font-size:12pt"><span style="font-family:Arial"><span _msthash="225" _msttexthash="506324" style="color:#666666">Para las listas anidadas:</span></span></span></h4>

<ul>
	<li style="list-style-type:disc"><span _msthash="217" _msttexthash="1514786" style="font-size:11pt">append(): agrega un elemento al final de la lista.</span></li>
	<li style="list-style-type:disc"><span _msthash="218" _msttexthash="3021746" style="font-size:11pt">insert(): inserta un elemento en una posici&oacute;n determinada de la lista.</span></li>
	<li style="list-style-type:disc"><span _msthash="219" _msttexthash="3603925" style="font-size:11pt">remove(): elimina el primer elemento de la lista que coincida con el valor dado.</span></li>
	<li style="list-style-type:disc"><span _msthash="220" _msttexthash="6664411" style="font-size:11pt">pop(): elimina y devuelve el elemento de una posici&oacute;n determinada de la lista o el &uacute;ltimo si no se especifica.</span></li>
	<li style="list-style-type:disc"><span _msthash="221" _msttexthash="2524288" style="font-size:11pt">sort(): ordena los elementos de la lista seg&uacute;n un criterio dado.</span></li>
	<li style="list-style-type:disc"><span _msthash="222" _msttexthash="2034903" style="font-size:11pt">reverse(): invierte el orden de los elementos de la lista.</span></li>
	<li style="list-style-type:disc"><span _msthash="223" _msttexthash="4606147" style="font-size:11pt">index(): devuelve el &iacute;ndice del primer elemento de la lista que coincida con el valor dado.</span></li>
	<li style="list-style-type:disc"><span _msthash="224" _msttexthash="2833740" style="font-size:11pt">count(): devuelve el n&uacute;mero de veces que aparece un valor en la lista.</span></li>
</ul>

<h2><span style="font-size:16pt"><span _msthash="216" _msttexthash="2574702" style="font-family:Arial">&iquest;C&oacute;mo iterar los elementos de una lista y un diccionario anidado?</span></span></h2>

<p><span style="font-size:11pt"><span _msthash="215" _msttexthash="12304799" style="font-family:Arial">Para recorrer o iterar un diccionario o una lista anidada en Python, puedes usar el bucle for con diferentes m&eacute;todos o funciones. Algunas opciones son:</span></span></p>

<ul>
	<li style="list-style-type:disc"><span _msthash="214" _msttexthash="10773620" style="font-size:11pt">Para recorrer las claves de un diccionario, puedes usar el m&eacute;todo keys() que devuelve un objeto de vista con todas las claves del diccionario.&nbsp;</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="213" _msttexthash="1141829" style="font-family:Arial">Por ejemplo: for i in dict.keys(): print(i).</span></span></p>

<p>&nbsp;</p>

<ul>
	<li style="list-style-type:disc"><span _msthash="212" _msttexthash="11547900" style="font-size:11pt">Para recorrer los valores de un diccionario, puedes usar el m&eacute;todo values() que devuelve un objeto de vista con todos los valores del diccionario.&nbsp;</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="211" _msttexthash="1258296" style="font-family:Arial">Por ejemplo: for i in dict.values(): print(i).</span></span></p>

<p>&nbsp;</p>

<ul>
	<li style="list-style-type:disc"><span _msthash="210" _msttexthash="16796897" style="font-size:11pt">Para recorrer los pares clave-valor de un diccionario, puedes usar el m&eacute;todo items() que devuelve un objeto de vista con todos los pares clave-valor del diccionario como tuplas.&nbsp;</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="209" _msttexthash="1404156" style="font-family:Arial">Por ejemplo: for i, x in dict.items(): print(i, x).</span></span></p>

<p>&nbsp;</p>

<ul>
	<li style="list-style-type:disc"><span _msthash="208" _msttexthash="12325976" style="font-size:11pt">Para recorrer una lista anidada, puedes usar un bucle for anidado que recorra cada elemento de la lista externa y luego cada elemento de la lista interna.&nbsp;</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="207" _msttexthash="2253667" style="font-family:Arial">Por ejemplo: for list in list_anidada: for x in list: print(x).</span></span></p>

<p>&nbsp;</p>

<ul>
	<li style="list-style-type:disc"><span _msthash="206" _msttexthash="17673214" style="font-size:11pt">Para recorrer un diccionario anidado, puedes usar un bucle for anidado que recorra cada par clave-valor del diccionario externo y luego cada par clave-valor del diccionario interno.&nbsp;</span></li>
</ul>

<p><span style="font-size:11pt"><span _msthash="205" _msttexthash="8181615" style="font-family:Arial">Por ejemplo: for clave1, valor1 in dict_anidado.items(): for clave2, valor2 in valor1.items(): print(clave1, clave2, valor2).</span></span></p>

<p><span style="font-size:11pt"><span _msthash="204" _msttexthash="1880008" style="font-family:Arial">Un ejemplo para que entendamos todo esto mejor ser&iacute;a:&nbsp;</span></span></p>

<script src="https://gist.github.com/javierberastegui/22d2feb50a389699a6a8a30b596a8f72.js"></script>

<p _msthash="202" _msttexthash="27883739"><span style="font-size:11pt"><span style="font-family:Arial">Este c&oacute;digo de python</span></span>, lo que har&aacute; ser&aacute; meter dos listas dentro de un diccionario, <span style="font-size:11pt"><span style="font-family:Arial"><strong>en el caso contrario, lo que har&aacute; ser&aacute; introducir un diccionario dentro de una lista.</strong></span></span> <span style="font-size:11pt"><span style="font-family:Arial"> Finalmente se recorrer&eacute; el diccionario con el m&eacute;todo deseado.</span></span></p>'
pattern = '(?!<h1>|</h1>|<h2>|</h2>|<h3>|</h3>|<h4>|</h4>|<p>|</p>|<ul>|</ul>|<li>|</li>|<a href="">|</a>|<strong>|</strong>).+'
html_con_etiquetas = re.sub(pattern, "", html, flags=re.DOTALL)
print(html_con_etiquetas)
