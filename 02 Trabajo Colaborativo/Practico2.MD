# PROGRAMACIÓN Ⅰ

## Práctico 2: Git y GitHub

## Alumno: Maximiliano Xavier Rodriguez

### 1) Contestar las siguientes preguntas utilizando las guías y documentación proporcionada (Desarrollar las respuestas) : 

¿Qué es GitHub?
GitHub es una plataforma de alojamiento de código basada en Git que permite a los desarrolladores gestionar proyectos, colaborar en código y realizar control de versiones de manera eficiente.
¿Cómo crear un repositorio en GitHub?
Para crear un repositorio en Github primero se debe iniciar sesión. Luego podemos crear un repositorio desde la barra de menú presionando en el icono “+” y seleccionando la opción “New repository”. Allí le colocamos un nombre al repositorio, seleccionamos si es público o no y podemos agregar un archivo “README. Por último se presiona el botón "Create repository" y con eso el repositorio ya está creado en GitHub.
¿Cómo crear una rama en Git? 
Para crear una nueva rama en Git desde la terminal de comandos debemos ejecutar la siguiente sentencia “git branch nombre_de_la_rama” esto crea una nueva rama sin cambiar a ella.
¿Cómo cambiar a una rama en Git? 
Para cambiar a otra rama en Git desde la terminal de comandos se debe ejecutar la sentencia “git checkout nombre_de_la_rama” o “git switch nombre_de_la_rama” en versiones más actuales de Git
¿Cómo fusionar ramas en Git? 
Para fusionar dos ramas en Git se debe posicionar sobre la rama donde se aplicaran los cambios y desde la terminal de comandos ejecutar “git merge nombre_de_la_rama” llamando a la rama donde están los cambios que deseamos implementar en la rama que estamos posicionados. Esto puede generar conflictos que se resuelven automáticamente o de manera manual.
¿Cómo crear un commit en Git? 
Para crear un commit en Git debemos ejecutar desde la terminal la sentencia “git commit -m “Descripción del cambio” agregando “-m” a la sentencia se puede dejar un mensaje para hacer más claro lo que se guarda en ese commit 
 ¿Cómo enviar un commit a GitHub?
Para enviar un commit a GitHub desde un proyecto local debemos primero ejecutar un “git add” para agregar los nuevos cambios y un “git commit” para guardarlos y luego de eso ejecutar en la terminal “git push -u -u origin nombre_de_la_rama


 ¿Qué es un repositorio remoto? 
Es una versión del repositorio almacenada en un servidor, como GitHub, que permite colaboración entre desarrolladores.
¿Cómo agregar un repositorio remoto a Git?
Para agregar un repositorio remoto a Git se debe ejecutar la siguiente sentencia en la terminal de comandos “git remote add origin URL_DEL_REPOSITORIO” todo esto luego de iniciar git en un repositorio local y hacer un “git add” y un “git commit”
¿Cómo empujar cambios a un repositorio remoto? 
Luego de realizar el respectivo “Git add” y el “Git commit” se debe ejecutar la sentencia “git push origin nombre_de_la_rama” para enviar los cambios locales al repositorio remoto 
¿Cómo tirar de cambios de un repositorio remoto? 
Para bajar los cambios realizados en el repositorio remoto a un repositorio local se debe ejecutar la sentencia “git pull origin nombre_de_la_rama” en la terminal
¿Qué es un fork de repositorio? 
Un fork es una copia de un repositorio en la cuenta de otro usuario, permitiendo hacer cambios sin afectar el original.
¿Cómo crear un fork de un repositorio?
Primero se ingresa al repositorio que se desea realizar la copia y se presiona en la opción “Fork”. Luego se le puede cambiar el nombre y la descripción al repositorio y presionando en “Create fork” se creará una copia del repositorio de un tercero en nuestra cuenta de GitHub.
¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
Para realizar un pull request a un repositorio primero debemos realizar un “git push origin nombre_de_la_rama” y luego dirigirnos a GitHub donde presionamos en la opción “Pull request” y en “New pull request” allí comparamos los cambios que realizamos con la rama original y dejamos un comentario explicando dichos cambios y para finalizar presionamos en “Create pull request”
¿Cómo aceptar una solicitud de extracción?
Dentro del repositorio en Github vamos a la pestaña “Pull request” y verificamos la pull request que deseamos aprobar si estamos de acuerdo presionamos en “Merge pull request” para que los cambios se apliquen en el código y para finalizar presionamos en “Confirm merge”.
¿Qué es un etiqueta en Git?
Es un marcador que apunta a un punto específico del historial, generalmente usado para versiones de software.
¿Cómo crear una etiqueta en Git?
Para crear una etiqueta en Git ejecutamos la sentencia “git tag -a v1.0 -m "Versión 1.0"” en la terminal de comandos 
¿Cómo enviar una etiqueta a GitHub?
Para enviar una etiqueta del repositorio local a GitHub ejecutamos la sentencia “git push origin v1.0” en la terminal de comandos y si deseamos enviar todas las etiquetas que generamos ejecutamos la sentencia “git push origin --tags”


¿Qué es un historial de Git?
Es el registro de todos los commits realizados en un repositorio.
¿Cómo ver el historial de Git?
Para ver el historial de todos los commits realizados ejecutamos la sentencia “git reflog” en la terminal de comandos 
¿Cómo buscar en el historial de Git?
Para buscar en el historial de Git por los mensajes de los commit ejecutamos la sentencia “git log --grep="palabra clave"” en la terminal de comandos 
¿Cómo borrar el historial de Git?
No es posible eliminar el historial de cambios de Git pero se puede resetear con “git reset --hard hash-commit”
¿Qué es un repositorio privado en GitHub?
En GitHub un repositorio privado es un repositorio que tienen acceso sólo usuarios con permisos para ingresar al mismo a verlo y realizar cambios
¿Cómo crear un repositorio privado en GitHub?
Para crear un repositorio privado se debe dar de alta un repositorio en GitHub y en la sección de privacidad del repositorio elegir privado  
¿Cómo invitar a alguien a un repositorio privado en GitHub?
Dentro del repositorio en GitHub en la pestaña de “Settings” podemos agregar colaboradores ingresando el mail o nombre de usuario de la persona en GitHub podemos enviar un acceso al repositorio privado 
¿Qué es un repositorio público en GitHub?
Un repositorio público en GitHub es un repositorio que cualquier usuario dentro de la plataforma puede visualizar sin la necesidad de permisos 
¿Cómo crear un repositorio público en GitHub?
Para crear un repositorio público se debe dar de alta un repositorio en GitHub y en la sección de privacidad del repositorio elegir público 
¿Cómo compartir un repositorio público en GitHub?
Solo compartiendo el link del repositorio con otra persona ya puede tener acceso al repositorio público 

### 2) 
      Link al repositorio creado: 
      https://github.com/RodriguezMaximilianoX/Actividad_TUP
### 3) 
      Link al repositorio clonado
      https://github.com/RodriguezMaximilianoX/UTN-TUPaD-P1#
