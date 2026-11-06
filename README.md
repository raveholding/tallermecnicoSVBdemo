# Taller Mecánico · Sistema VB (demo)

Demo del sistema de gestión para talleres mecánicos y services del automotor, desarrollado por **VINCULAR BUSINESS**.

**Probar la demo:** https://raveholding.github.io/tallermecnicoSVBdemo/

Archivo único: `index.html`. Abre en cualquier navegador y funciona sin internet. Los datos se guardan en el navegador del equipo o celular donde se usa.

## Cómo se usa la demo
- **Abre con datos de ejemplo** (taller ficticio “Tu Taller Mecánico”). Se elige un perfil sin clave (dueño, jefe de taller, recepción o mecánico) para ver qué puede hacer cada rol. Los cambios quedan sólo en ese navegador; en *Configuración* se pueden restablecer los datos de ejemplo.
- **Sistema vacío:** con el enlace *Probar el sistema vacío* (o abriendo `index.html#real`) arranca de cero, con clave del dueño, como lo usaría un taller real.

## Módulos
Órdenes de trabajo · Ventas de mostrador · Turnos · Clientes y vehículos · Repuestos e inventario · Proveedores y compras · Caja · Equipamiento · Seguridad y ambiente · Personal · Reportes · Configuración.

## Lo principal
- **Flujo de la orden de trabajo:** Recibido → Diagnóstico (mecánico) → Presupuesto (jefe / dueño) → En reparación → Listo → Entregado y cobrado.
- **El mecánico no ve precios** en ninguna pantalla ni impresión. Ve sus órdenes y las que están sin asignar. Carga el diagnóstico con hasta 6 fotos y recomienda repuestos o trabajos.
- **Presupuesto** armado por el dueño o el jefe y aprobado por el cliente sin cobro. Se cobra al entregar el vehículo, con adicionales, descuento por renglón o sobre el total e IVA opcional. Envío por WhatsApp e impresión.
- **Condición frente a ARCA:** al elegir el cliente en la OT o en la venta (y el proveedor en las compras) se indica su condición: Consumidor Final, Responsable Inscripto, Monotributo, Exento, etc. El CUIT se valida y la condición queda guardada en la ficha y en el comprobante interno.
- **Alta completa del cliente** desde la ficha, una nueva OT, un turno o una venta: nombre o razón social, teléfono, correo, domicilio, localidad, provincia, cuenta corriente y límite, condición frente a ARCA y CUIT/DNI.
- **Inventario:** varios códigos por artículo, dimensiones y equivalencias (rosca, junta, OEM), importación y exportación CSV, alarmas de stock, trazabilidad de cada movimiento y sugerencia de equivalentes cuando falta stock.
- **Proveedores y compras:** órdenes de compra, ingreso de mercadería con actualización de costos, cuenta corriente y pagos desde una o varias cajas.
- **Caja** con turnos, varias cajas, rubros financieros y arqueo. **Cuenta corriente** de clientes con límite.
- **Turnos** por puesto de trabajo, **equipamiento**, **seguridad e higiene** (EPP, matafuegos, residuos, habilitaciones) y **reportes** con exportación.
- **Roles y claves por persona** (cifradas) y auditoría de las acciones. Respaldo y restauración en JSON.

## Límites (no afirmar más que esto)
- Los datos viven sólo en el navegador y el equipo donde se usan. No hay sincronización entre dispositivos ni copia en la nube; para eso hace falta un servidor.
- La clave es un control de uso del sistema, no seguridad de servidor.
- Sin facturación electrónica ni pagos reales: la condición frente a ARCA es un dato de registro, el sistema no emite facturas ni consulta el padrón.
- Los datos del taller, las personas, los clientes y los vehículos de la demo son ficticios.

Desarrollado por **VINCULAR BUSINESS** · (387) 4484132 · vincularbusiness@gmail.com · “Tu idea, en buenas manos.”
