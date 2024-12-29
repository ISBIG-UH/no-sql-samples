# Bases de datos llave-valor





## Ejemplo 1: DNS

### Escenario

Un *Domain Name System* (**DNS**) actúa como una agenda de contactos dentro de Internet, asociando nombres de dominio a direcciones IP. Estos sistemas simplifican el acceso a recursos online mediante el uso de nombres como `google.com` o `wikipedia.org`. 

> [!NOTE]
>
> En este curso hemos utilizado un DNS para establecer conexión con el sistema gestor de bases de datos de MySQL, usando direcciones como`localhost:3306` o `mysqllab:3306`, `localhost` es traducido a `127.0.0.1` por el sistema operativo, mientras que `mysqllab` es traducido a por el DNS de Docker al IP del contenedor (computadora virtual) que ejecuta el sistema gestor.

Una explicación profunda de estos sistemas la van a recibir en el curso de **Redes de Computadoras** por lo que para los propósitos de este curso nos centraremos solo en unos pocos aspectos de la implementación de estos sistemas. 

- **Simplicidad conceptual**: Es un escenario sencillo desde el punto de vista informacional, solo es necesario almacenar los nombres de dominio y las direcciones IP. Además las consultas se limitan a obtener el IP asociado a un nombre de dominio.
- **Gran volumen de continuas operaciones de lectura y escritura**: El escenario es muy dinámico, con dispositivos entrando y saliendo de la red mientras se comunican entre sí (es decir, deben de buscar sus IPs).
- **Alta disponibilidad**: La caída de un sistema DNS significaría la interrupción de una gran parte de las comunicaciones en la red, por tanto se debe garantizar la disponibilidad del sistema.

### Sistema Gestor

**etcd** es un sistema gestor de bases de datos llave-valor gratuita y de código abierto, usualmente utilizado para almacenar y manejar la información crítica que necesitan los sistemas distribuidos para funcionar.

Este sistema está diseñado y construido con el propósito de servir como los cimientos informacionales de los sistemas distribuidos y podemos distinguir entre sus cualidades:

- **Completamente replicado:** Cada nodo en un clúster de etcd tiene acceso a la totalidad del almacén de datos.
- **Altamente disponible:** etcd está diseñado para no tener un único punto de fallo y tolerar de manera eficiente fallos de hardware y particiones de red.
- **Consistencia confiable:** Cada "lectura" de datos devuelve el último "escritura" realizada en todos los clústeres.
- **Rápido:** etcd ha sido probado para manejar hasta 10,000 escrituras por segundo.
- **Seguro:** etcd soporta el uso automático de Transport Layer Security (TLS) y autenticación opcional mediante certificados SSL de cliente. Dado que etcd almacena datos de configuración vitales y altamente sensibles, los administradores deben implementar controles de acceso basados en roles dentro de la implementación y asegurarse de que los miembros del equipo que interactúan con etcd tengan un acceso limitado al mínimo nivel de privilegios necesario para realizar sus tareas.
- **Sencillo:** Cualquier aplicación, desde aplicaciones web simples hasta motores de orquestación de contenedores altamente complejos como Kubernetes, puede leer o escribir datos en etcd utilizando herramientas estándar HTTP/JSON.

### Experimento

En este experimento vamos a comparar el rendimiento de etcd y MySQL para el manejo de una base de datos para un sencillo DNS.

La simulación del escenario consiste en la realización de $N$ operaciones sobre un mapeo `domain => ip`, por simpleza solo se consideraron operaciones de inserción, lectura y eliminación cada una con una probabilidad de ocurrencia del 30%. El código de para generar las operaciones a simular se encuentra en el archivo `simulation.py`.

Se desplegó una red en Docker consistente en una instancia de etcd, una de MySQL y una de JupyterLab. En Jupyterlab instalamos el cliente de etcd y mysql y ejecutamos las operaciones generadas.

Para un total de 100000 operaciones etcd tomó solo 2 min y 36 segs mientras MySQL tomó 23 mins y 30 segs, unas 10 veces más tiempo. Si bien hay que considerar las posibles diferencias en la implementación de los clientes en Python para cada sistema. El código del experimento se encuentra en el archivo `experiment.ipynb`

## Ejemplo 2: Cache (In - Memory)

