# Magic Tricks

## Tabla de Contenidos
- [Descripción](#Descripción)
- [Presentación](#Presentación)
- [Estructuración del Código](#estructuración-del-código)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Instalación](#instalación)
- [Autor](#autor)
- [Contacto](#contacto)

## Descripción:

Magic Tricks fue creado para la organización civil sin fines de lucro "Pensar Futuro" con el objetivo de gestionar datos en su carga, actualización, borrado, así como su organización para la facilitación de su lectura y posterior toma de decisiones, fortaleciendo la formación democrática y brindando herramientas para fundamentar, con una fuente empírica, la toma de decisiones por parte de las conducciones; sin vulnerar las libertades, derechos y obligaciones que tiene cada participante de las elecciones universitarias.

## Presentación:

La presente aplicación fue desarrollado enteramente en Python a excepción de dos funciones. El frontend fue escrito con el framework de Reflex, y consta de tres páginas:
* El Ingeso: el ingreso. La página es privada, por lo que no cuenta con un botón de registrarse, al montase la pagina se ejecuta el borrado del Local Storege, esto es utilizado como metodo de seguridad.

* La Carga:  La carga de datos, que se presenta en dos bloques. El primero recepciona las variables y, a través de tres botones, permite la gestión del ingreso, actualización y borrado de los datos. El segundo muestra en formato de tabla los resultados a partir del ingreso de tres variables: universidad, año y día, en combinación con un botón de listado. También se presenta el botón de descarga para una rápida exportación de los datos.

* Alquimia: Denominada Alquimia porque se suele nombrar afectuosa y cómicamente como magia las lecturas de los datos y la toma de decisiones en consecuencia. Nos presenta dos bloques. El primero tiene dos grandes ingresos de datos: en primer lugar, con el rellenado de Universidad, Año y la depuración que se quiera hacer, se nos presentan los datos de un modo muy gráfico, con los totales, el conteo preliminar de los datos propios y sus debidos porcentajes, y los que corresponderían al rival. Además de un gráfico de torta que lo mostraría de un modo más visual, y un gráfico de barras que discriminaría por día el desempeño cuantitativo propio en relación al total. El segundo es para pormenorizar el desempeño durante el día, por eso se debe ingresar Universidad, Año y Día, esto con el objetivo de detectar los mejores momentos del día. Se representan en forma de gráficos de barras y de líneas donde el eje X representa el paso del tiempo en el día en horas y el eje Y la cantidad que corresponde a ese momento del día. El segundo gran bloque dentro de esta página son las Alquimias propiamente dichas, con tres grandes sistemas: el sistema D'Hondt, el sistema de Cociente Electoral y restos, y el Sistema de Mayorías y Minorías. Estas herramientas trabajan enteramente con los datos ingresados por el usuario, ya que son para tratar de dimensionar en tiempo real el estado general de la elección, es decir, tienen una gran parte de especulación.

## Estructuración del Código

### Backend:

El backend principal fue desarrollado en Python, con la herramienta FastAPI. Se utilizan dos sistemas de almacenamiento de base de datos: para los usuarios, la base de datos no relacional MongoDB; para el resto de los datos, la base de datos relacional MySQL.
Documentación del Backend: "(inserte URL de documentación)"

repositorio: https://github.com/Dafiron/magic-back/tree/master

### Frontend:

El frontend fue desarrollado enteramente en Reflex y con el lenguaje Python, lo que permite tener un backend para operaciones menores.

#### Orden del codigo:

El codigo para su correcta lectura esta comparmentizado  en elementos dividido por su interelacion como su complejidad y su importancia relativa.

* Estados: Todos los estados se encuentran en la carpeta "State" y cada uno de ellos tiene relación con un componente a excepción de dos estados, Login, quien se encarga de algunos aspectos de seguridad por lo que tiene injerencia en todas las páginas, y Load que se encarga de todos los aspectos en relación a la carga, actualización y borrado de datos.

* Estilos: Si bien se buscó estandarizar todo lo que se pudo el estilado, en futuras actualizaciones se mejorará este aspecto. Los estilos están en la carpeta "Styles".

* View: Son componentes en general bastante estáticos que se repiten en cada página con pocas variaciones.

* Componentes: Estos los divido en mayores y menores:
    * Menores: Están en la carpeta components en el archivo components. Son las funciones de las que parten el resto de los armados.
    * Mayores: Están compuestas de más de un componente o revisten de mucha importancia circunstancial. Se representan en la carpeta components con su nombre particularizado, como ensambles para la renderización directa.

## Instalación

Las bibliotecas que se requieren instalar son:

#### frontend:
- python
- reflex 
- requests

#### backend:
- fastapi
- passlib[bcrypt]
- python-jose[cryptography]
- dotenv
- pymongo
- uvicorn

En ambos casos se utilizaron máquinas virtuales por separado.

## Autor

El presente código fue producido por Dafiron, con ayuda de toda la comunidad de programadores de forma directa o indirecta.

## Contacto

El feedback es bien recibido si puede ser por email: dafironxd@gmail.com

