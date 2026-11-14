# Tu Taller Car Center · Sistema VB (demo)

Demo del sistema de gestión para **talleres y car centers**: mecánica, electricidad, **car audio**, **alarmas** y **accesorios**, con **menú digital** para clientes, **turnos online** y **Club de fidelización**. Desarrollado por **VINCULAR BUSINESS**.

- **Sistema del taller:** https://raveholding.github.io/tallermecnicoSVBdemo/
- **Menú digital que ven los clientes:** https://raveholding.github.io/tallermecnicoSVBdemo/#menu

Archivo único: `index.html`. Abre en cualquier navegador y funciona sin internet. Los datos se guardan en el navegador del equipo o celular donde se usa.

## Cómo se usa la demo
- **Abre con datos de ejemplo** (negocio ficticio “Tu Taller Car Center”). Se elige un perfil sin clave (dueño, jefe de taller, recepción o mecánico) para ver qué puede hacer cada rol. En *Configuración* se pueden restablecer los datos de ejemplo.
- **Menú digital:** desde el ingreso, el botón del costado *Ver menú digital* o `#menu`. Lo que se pide ahí aparece en *Menú digital y pedidos*.
- **Sistema vacío:** *Probar el sistema vacío* (o `#real`) arranca de cero, con clave del dueño, como lo usaría un negocio real. Su menú es `#real-menu`.

## Módulos
Panel · Órdenes de trabajo · Ventas de mostrador · Turnos · **Menú digital y pedidos** · Clientes y vehículos · **Club y fidelización** · **Garantías** · Repuestos e inventario · Proveedores y compras · Caja · Equipamiento · Seguridad y ambiente · **Personal y RR. HH.** · **Tareas** · Reportes · Configuración.

## Lo que suma esta demo para un negocio completo
- **Áreas de trabajo:** Mecánica, Electricidad, Car audio y multimedia, Alarmas y seguridad, Accesorios y estética. Cada orden lleva su tipo de trabajo. Las instalaciones suman el **control del estado eléctrico previo** (batería, tablero, levantavidrios, audio original, llaves y controles), que se imprime en la orden, y van al **box de instalaciones** de la agenda. Hay un técnico de car audio y alarmas de ejemplo.
- **Catálogo de servicios** (27 de ejemplo) con área, descripción para el cliente, precio neto, “precio desde”, duración, **garantía en meses** y si se publica en el menú. Es el mismo catálogo que se usa en las órdenes.
- **Productos de car audio, alarmas y accesorios** en el inventario (multimedia, parlantes, subwoofer, potencias, alarmas, cierre centralizado, sensores, GPS, cámaras, LED, polarizado, levantavidrios), con proveedores, stock y garantía.
- **Menú digital público con tienda** (celular primero), que abre en la **Tienda**:
  - **46 productos de ejemplo** en 9 categorías: car audio, alarmas y seguridad, accesorios, iluminación, interior y confort, limpieza y cuidado, emergencia y auxilio, lubricantes y baterías.
  - Destacados, buscador y ficha de cada producto.
  - Estado de stock (“Disponible”, “Últimas unidades”, “Sin stock”), nunca la cantidad ni el costo.
  - Botón **“Con instalación”**, que suma el producto y el servicio de instalación que le corresponde.
  - Servicios por área con precio final con IVA, duración y garantía.
  - **Carrito** que arma el pedido (retiro o instalación) y lo **envía por WhatsApp**, más WhatsApp, Instagram y “Cómo llegar”.
  - En el sistema se elige qué se publica, qué es destacado y la garantía de cada producto.
- Si alguien abrió una versión anterior de la demo, el navegador carga solo los datos de ejemplo nuevos.
- **Turnos online:** el cliente elige servicio y día y ve **solo los horarios libres** (según la agenda, el puesto que corresponde y la duración; sábados de 9 a 13, domingos cerrado). El pedido queda para confirmar en el sistema, que crea cliente, vehículo y turno, controla que no se pisen horarios y abre el WhatsApp de confirmación o de rechazo.
- **Pedidos del menú en el sistema:** bandeja con aviso en el panel y en el menú lateral. Un pedido se puede **pasar a la venta de mostrador** con un toque, convertir en turno, responder por WhatsApp, marcar como atendido o descartar.
- **Club y fidelización:** puntos por cada $ gastado en órdenes entregadas y ventas con cliente identificado (configurable; lo pagado con puntos no suma). Tiene **niveles** Bronce, Plata y Oro por puntos acumulados, **premios para canjear**, **canje de puntos como medio de pago** al cobrar la orden, ajustes auditados, libro de movimientos y tarjeta imprimible tamaño tarjeta de crédito. Desde el menú el cliente se **suma al Club** (mayor de 18, con consentimiento) y **ve su tarjeta** con WhatsApp y fecha de nacimiento: puntos, nivel, sus vehículos con el próximo service y sus garantías vigentes.
- **Recordatorios por WhatsApp listos para mandar:** próximo service (vencido o en 30 días), cumpleaños del mes con el beneficio, garantías por vencer y clientes que no vienen hace más de 6 meses.
- **Garantías:** se crean solas al entregar una orden o vender un equipo con garantía. Muestra el **N.º de serie** del equipo, el estado (vigente, por vencer o vencida) y los **reclamos**, que pueden abrir una orden de trabajo.
- **Personal y RR. HH.:**
  - **Legajos:** DNI y CUIL validado, contacto de emergencia, área, “reporta a”, ingreso y antigüedad, contratación, horario, sueldo básico, documentación con vencimientos y capacitaciones.
  - **Asistencia:** cada persona marca su entrada y salida en “Mi día”. Muestra llegadas tarde, horas del mes y exportación a CSV.
  - **Vacaciones y licencias:** pedidos del empleado, aprobación del dueño, control de superposición y saldo de vacaciones por antigüedad [VERIFICAR con el contador y el convenio].
  - **Organigrama** visual armado con los legajos, que muestra quién está presente y sus tareas.
  - **Sueldos y adelantos:** estimación interna con básico, comisión sobre la mano de obra entregada y adelantos. Los adelantos en efectivo salen de la caja. No es un recibo de sueldo.
- **Tareas (organigrama de tareas):**
  - **Mi día** para cada persona, también en el panel: fichar, tareas pendientes y lo que le toca a su puesto.
  - **Tablero del equipo** con Pendiente, En curso y Hecha, filtros por persona y área, prioridades, vencimientos y aviso por WhatsApp al asignar.
  - **Tareas recurrentes** diarias, semanales y mensuales que se crean solas.
  - **Responsabilidades por puesto**, que edita el dueño.
  - Avisos de documentación por vencer, pedidos para aprobar y tareas vencidas.
- Todo lo del sistema base: flujo de la orden con diagnóstico y fotos, mecánico sin precios, presupuesto, cobro con adicionales y descuentos, condición frente a ARCA y alta completa del cliente, inventario con equivalencias y trazabilidad, compras, caja, seguridad e higiene, reportes, roles, claves y respaldo.

## Diseño Sistema VB (esqueleto V27.2, sección 7)
Capa de diseño común a los dos sistemas (`tools/vb_ux.js`). No quita funciones: reordena y agrega.
- **Barra lateral por secciones plegables:** Operación del taller · Logística e inventario · Clientes y fidelidad · Equipo · Sistema. Arriba van los botones principales **Vender [F1]** y **Nueva orden [F2]**, y en la barra se ven los avisos (órdenes, stock bajo en amarillo, pedidos y tareas).
- **Barra superior:** nombre del negocio, estado (modo, caja abierta o cerrada, de un día anterior en rojo), **buscador Ctrl + K**, **campana de avisos** con lista, **tema** (Automático → Claro → Oscuro), acceso al menú público y usuario con su rol.
- **Buscador universal (Ctrl + K):**
  - Busca por patente, cliente (nombre, teléfono o CUIT), N.º de OT, repuesto (código exacto, parcial o descripción) y pantallas.
  - Tolera errores de tipeo: “arqeo” lleva a Caja.
  - Un repuesto elegido se agrega a la venta. Sólo muestra lo que el rol puede abrir.
- **Tema claro, oscuro y automático:** sólo cambia variables CSS, lo hace en < 5 ms y recuerda la elección en cada equipo. El menú público queda siempre en claro.
- **Ayuda en contexto:** cada pantalla tiene una línea que dice para qué sirve y por dónde empezar.
- **Panel “Hoy”** (dueño y jefe de taller):
  - Cobrado hoy contra ayer, órdenes abiertas con presupuestos esperando, turnos y stock en alerta.
  - Últimos cobros y tendencia de los últimos 7 días contra la semana anterior.
  - Sin indicadores repetidos.
- **Caja:** tablero del turno con estado (verde abierta, gris cerrada, rojo si es de un día anterior), **4 pasos del día** con el paso actual marcado y como atajo, ingresos y egresos, duración y ticket promedio.
- **Módulos activables** (Configuración → Módulos): menú digital, Club, garantías, tareas y RR. HH. avanzado. Apagarlos sólo los oculta; los datos quedan.
- **Créditos** completos: Celular (387) 4484132 · www.vincularbusiness.com.ar · correo, con botones WhatsApp · Llamar · Página web · Correo.
- **Accesibilidad:**
  - Contraste AA verificado por auditor automático: 0 textos por debajo de 4,5:1 en todas las pantallas de dueño, recepción y mecánico, en claro y en oscuro, más ventanas, ingreso y menú público.
  - Controles de ≥ 44 px, sin desbordes de 320 a 1440 px y respeta “reducir movimiento”.
- Pruebas en `tools/pruebas/` (ver LEEME).

## Datos y respaldo (v5)

Pantalla **Sistema → Datos y respaldo** (solo el dueño). Funciona sin internet y sin servicios externos.

- **Respaldo completo**: archivo `.json` con todo el sistema, o `.vbk` **cifrado** con clave (AES-256-GCM, clave derivada con PBKDF2-SHA256). Si se pierde la clave del respaldo cifrado, no se puede abrir: anotarla en un lugar seguro.
- **Restaurar**: valida el archivo y, antes de reemplazar, deja una copia automática del estado actual. El sistema real no acepta respaldos de práctica o de demostración.
- **Copias automáticas en el equipo**: una por día y otra antes de cada restauración o importación; se guardan las últimas 10 en el navegador. No reemplazan al respaldo en un pendrive o en la nube.
- **Exportar**: cada tabla (clientes, vehículos, órdenes, ventas, repuestos, stock, proveedores, compras, caja, turnos, servicios, garantías, Club, personal, asistencia, tareas, auditoría) en Excel, CSV o JSON, o un Excel completo con todas las hojas. El CSV usa `;` y viene protegido contra fórmulas peligrosas.
- **Importar** desde Excel (.xlsx), CSV o JSON: clientes con vehículos, proveedores, servicios, actualización de precios por código y repuestos. Reconoce encabezados con distintos nombres, muestra una vista previa con las filas aceptadas y rechazadas (con el motivo) y recién después aplica. No lee el formato viejo .xls: guardarlo antes como .xlsx.

## Sin internet (v5)

- Después de abrirlo una vez con internet, el sistema **vuelve a abrir y trabaja sin conexión** (queda guardado en el equipo). Arriba aparece "● Sin internet" mientras no hay conexión.
- **Instalar como app**: botón **📲 Instalar aplicación** visible en la pantalla de ingreso y en la barra superior (también en Datos y respaldo). Donde el navegador lo permite (Chrome, Edge, Android) abre el aviso de instalación; en iPhone/Safari y otros muestra los pasos para agregarla a la pantalla de inicio. Se oculta solo cuando la app ya está instalada. El código está en `tools/vb_datos.js`.
- **Almacenamiento permanente**: pedirlo en la misma pestaña, para que el navegador no borre los datos al quedarse sin espacio.
- **Copia del programa**: botón para descargar el `.html`, que abre con doble clic en cualquier computadora aunque no haya internet.
- Los datos viven **en ese navegador y ese equipo**: hacer un respaldo al menos una vez por semana y guardarlo fuera del equipo. Borrar los datos del navegador borra el sistema.
- Lo que necesita internet: compartir por WhatsApp, abrir mapas y recibir las versiones nuevas (cuando hay una, aparece el aviso para actualizar).

## Configuración dinámica y acceso oculto (v6)

- **Configuración por secciones**: Datos del negocio, Módulos, Funcionamiento, Mano de obra, Menú digital, Usuarios y accesos, Datos y respaldo y Auditoría. Están todas las opciones de antes.
- **Buscador de ajustes** arriba ("IVA", "horario", "clave"…): lleva directo al ajuste y lo resalta. Tolera errores de tipeo.
- **Puesta en marcha**: barra de progreso y lista de lo que falta (datos de contacto, precios sin cargar, respaldo vencido). Cada pendiente es un botón que lleva al lugar.
- **Se guarda solo**: los datos del negocio y los precios se guardan mientras se escribe (aparece "✓ Guardado") y la vista previa muestra cómo lo ve el cliente. El nombre no se guarda si queda vacío.
- **Interruptores** en lugar de casillas, con la explicación de cada opción.
- **Mano de obra**: búsqueda, filtro por área y "Sin precio", precio con IVA al lado, acepta "10.000" y **aumento o baja por porcentaje** a todos o a los filtrados (redondea a la decena; las órdenes cargadas no cambian).
- **Acceso oculto al panel**: en el menú digital público, **doble clic (o doble toque en el celular) sobre el logo** abre el ingreso al sistema. No se ve ningún botón y sigue pidiendo usuario y clave. Se apaga en Configuración → Menú digital.

## Impresiones (v7)

Pantalla **Operación → Impresiones** (dueño, jefe de taller y recepción) y botones en cada lugar: "🖨 Más impresiones…" dentro de cada orden, 🖨 en cada venta y en cada orden de compra, y aviso para imprimir el ticket apenas se cobra una venta.

- **Para el cliente**: presupuesto, orden de trabajo, comprobante interno (con la X y "Documento no válido como factura"), recibo de cada cobro con el importe en letras, constancia de entrega con garantías y próximo service, ticket de venta, estado de cuenta y etiqueta de próximo service (10 × 6 cm).
- **Para el taller**: agenda del día (turnos, vehículos en el taller y tareas, con casillas), orden de compra, pedido de reposición por proveedor, lista de precios de mano de obra y cartel A4 con el QR del menú digital.
- **Formato**: hoja A4, ticket de 80 mm o de 58 mm (impresoras térmicas). Para un PDF, "Guardar como PDF" en la ventana de impresión. Funciona sin internet.
- **Factura**: el sistema **no emite facturas ni pide CAE**. Se emite en ARCA (web o facturador) y después se **registra a mano** el tipo, punto de venta, número y, si se quiere, el CAE, para que quede vinculada a la orden o a la venta y salga en los papeles. Sugiere la letra según la condición del negocio y del cliente [VERIFICAR con el contador].
- **Configuración → Impresión y datos fiscales**: CUIT (con control del dígito verificador), condición frente al IVA, Ingresos Brutos, inicio de actividades, texto al pie y condiciones de garantía. Hasta que se completen, la puesta en marcha lo marca como pendiente.
- El QR usa la biblioteca qrcode-generator 2.0.4 (Kazuhiko Arase, licencia MIT), incluida dentro del archivo.

## Ejemplos de ventas y compras, y demo limpia (v7.1)

- Los datos de ejemplo suman 5 ventas de mostrador (consumidor final, monotributista y responsable inscripto, con distintos medios de pago), una de ellas con factura registrada, y 2 órdenes de compra pendientes. Así se pueden mostrar el ticket, el recibo, la orden de compra y el registro de factura sin cargar nada antes.
- La versión de los datos de ejemplo pasó a `car5`: los datos de **práctica** guardados con la versión anterior se reemplazan solos por los nuevos. Los datos reales no se tocan.
- **Demo limpia**: en el ingreso de la demo, "🧹 Probar el sistema limpio, con mis datos" abre el sistema vacío para que el taller cree su dueño y cargue lo suyo. Arriba queda la barra "DEMO LIMPIA" con "Volver a los datos de ejemplo" y "Vaciar y empezar de cero". Las dos opciones también están en Configuración → Datos y respaldo. Los datos de ejemplo y los de la prueba limpia se guardan por separado.
- La demo trae datos fiscales de ejemplo (marcados "ejemplo") para que los comprobantes se vean completos.

## Límites (no afirmar más que esto)
- **Sin nube en la demo:** los pedidos, turnos y altas al Club que se hacen desde el menú quedan en el navegador donde se hicieron (en la demo, el mismo equipo) y además se envían por WhatsApp. Para que lleguen solos a todos los equipos del taller hace falta la nube del Sistema VB (servidor).
- El pedido del menú es una **consulta por WhatsApp**, no un cobro: no hay pago online. Los precios del menú son de referencia y el taller los confirma.
- La tarjeta del Club se consulta en el menú. No hay Apple Wallet ni Google Wallet.
- Los mensajes de WhatsApp se abren armados y los envía una persona: no hay envíos automáticos ni API de WhatsApp Business.
- El QR del menú no se genera dentro del sistema: se arma con cualquier generador a partir del enlace.
- La asistencia es un registro interno (no es un reloj biométrico) y los sueldos son una estimación: la liquidación legal la hace el contador.
- Sin facturación electrónica: la condición frente a ARCA es un dato de registro.
- Los datos del negocio, las personas, los clientes, los vehículos, los precios y los productos de la demo son ficticios o de ejemplo. Normativa de polarizado y abonos de GPS: **[VERIFICAR]**.

## Cómo se arma (para desarrollo)
La demo se genera a partir del sistema de SebaChavez Car Service, para que las mejoras del sistema del cliente lleguen también a la demo:

```sh
sh tools/build.sh /ruta/a/Sebachavezcarervice/tools/base.html
```

- La base es `tools/base.html` del repo Sebachavezcarervice: `sh tools/build.sh /ruta/a/Sebachavezcarervice/tools/base.html`. Los módulos de `tools/` son los mismos en los dos repos (si se cambian acá, copiarlos allá y volver a armar los dos).
- `tools/mk_demo.py`: quita los datos del cliente y pone los del negocio de ejemplo (nombre, logo, datos, base local propia).
- `tools/demo_seed.js`: áreas, catálogo, productos, Club y datos de ejemplo de los módulos extra.
- `tools/demo_ext.js`: menú digital, pedidos y turnos web, catálogo, Club, garantías y tipos de trabajo.
- `tools/demo_rrhh_seed.js` y `tools/demo_rrhh.js`: Personal y RR. HH. (legajos, asistencia, licencias, organigrama, sueldos) y Tareas.
- `tools/vb_ux.js`: capa de diseño del Sistema VB (barra, Ctrl + K, avisos, tema, panel Hoy, tablero de caja, módulos, créditos).
- `tools/demo_patch.py`: engancha los módulos al sistema.

Desarrollado por **VINCULAR BUSINESS** · (387) 4484132 · vincularbusiness@gmail.com · “Tu idea, en buenas manos.”
