
# Fz3r0 Wi-Fi Custom Model

## OSI is the map. Wi-Fi L1/L2 is the battlefield.

El Fz3r0 Wi-Fi Custom Model es un modelo conceptual diseñado para estudiar Wi-Fi desde una perspectiva más cercana a 802.11 y CWAP.

No reemplaza al modelo OSI.

No reemplaza al modelo IEEE 802.

No pretende inventar un estándar nuevo.

Su propósito es explicar mejor la parte baja del stack inalámbrico, donde un diagrama OSI tradicional se queda demasiado genérico.

En el modelo OSI clásico, Wi-Fi queda resumido así:

| OSI Layer | Nombre |
|---|---|
| Layer 2 | Data Link |
| Layer 1 | Physical |

Eso es correcto, pero para estudiar Wi-Fi no es suficiente.

En Wi-Fi, la mayor parte del análisis real ocurre dentro de esos dos bloques:

| Zona | Por qué importa en Wi-Fi |
|---|---|
| LLC/SNAP | Identifica protocolos superiores como IPv4, IPv6 o ARP dentro de tramas 802.11 data |
| 802.11 MAC | Crea MPDUs, maneja management/control/data frames, ACKs, retransmisiones, QoS, FCS y acceso al medio |
| PHY / PLCP / PMD | Convierte la unidad MAC en una PPDU lista para transmitirse como RF |
| RF / Aire | Donde entran RSSI, SNR, interferencia, airtime, MCS, retries y condiciones físicas |

Por eso el modelo Fz3r0 expande la parte baja de OSI.

La idea es simple:

> OSI te dice dónde estás.  
> Fz3r0 Wi-Fi Custom Model te muestra qué está pasando realmente en Wi-Fi.

---

## 1. Comparación rápida con OSI

El modelo OSI clásico es un mapa general.

El modelo Fz3r0 es un zoom sobre la parte baja del mapa, específicamente para Wi-Fi.

| OSI 7-Layer Model | Fz3r0 Wi-Fi Custom Model | Enfoque |
|---|---|---|
| L7 Application | L7 Application | Presente, pero no es el foco principal del análisis Wi-Fi |
| L6 Presentation | L6 Presentation / Transform | Presente como transformación, encoding, encryption, serialization |
| L5 Session | L5 Session / Context | Presente como estado o contexto |
| L4 Transport | L4 Transport | TCP/UDP siguen existiendo, pero para Wi-Fi son payload superior |
| L3 Network | L3 Network | IP/ARP importan, sobre todo por LLC/SNAP y troubleshooting |
| L2 Data Link | L2 Upper / LLC-SNAP | Identificación de protocolos superiores |
| L2 Data Link | L2 Lower / 802.11 MAC | El corazón del comportamiento Wi-Fi |
| L1 Physical | L1 PHY / PLCP-PMD-RF | Preparación PHY y transmisión RF |

La gran diferencia está en Layer 2 y Layer 1.

OSI dice:

> Data Link + Physical

Fz3r0 dice:

> LLC/SNAP + 802.11 MAC + PHY/PLCP/PMD/RF

Ese detalle es lo que hace que el modelo sea útil para Wi-Fi.

---

## 2. Por qué las capas superiores se ven menos importantes

En el Fz3r0 Wi-Fi Custom Model, las capas L7, L6, L5 y L4 pueden aparecer visualmente más apagadas o grises.

Esto no significa que no importen.

Significa que no son el objetivo principal de este modelo.

Un usuario puede estar navegando HTTP, usando HTTPS, haciendo DNS, jugando online o mandando SSH. Todo eso existe. Pero desde la perspectiva de Wi-Fi, muchas veces todo eso llega como payload dentro de una trama 802.11 data.

Cuando analizamos Wi-Fi, las preguntas principales suelen estar abajo:

| Pregunta | Capa más relevante |
|---|---|
| ¿La estación está asociada? | 802.11 MAC |
| ¿Hay beacons, probes, auth, assoc? | 802.11 Management |
| ¿Hay ACKs o retransmisiones? | 802.11 MAC |
| ¿Hay QoS? | 802.11 MAC |
| ¿Qué MCS se usó? | PHY |
| ¿Qué tan malo está el SNR? | RF / PHY |
| ¿Hay interferencia? | RF |
| ¿El frame lleva IP o es management/control? | 802.11 MAC |
| ¿Se identifica IPv4/ARP por LLC/SNAP? | LLC/SNAP |

Por eso este modelo empuja la atención hacia L2 y L1.

---

## 3. El concepto clave: SDU vs PDU

Una de las metas principales del modelo Fz3r0 es explicar claramente la diferencia entre SDU y PDU.

Estos términos suelen confundirse muchísimo.

La forma simple de verlo es:

| Término | Analogía | Significado |
|---|---|---|
| SDU | Cargo | Lo que una capa recibe desde arriba |
| PDU | Contenedor | Lo que esa capa construye agregando su propia información |

Una capa recibe una SDU.

Luego le agrega su propia información de control.

El resultado es su PDU.

Ese PDU baja hacia la siguiente capa.

Y desde la perspectiva de la capa inferior, esa misma información puede recibir otro nombre.

Ese es el punto central:

> El nombre cambia porque cambia la perspectiva de la capa.

No necesariamente cambian los bytes.  
Cambia quién los está mirando.

---

## 4. La cadena central del modelo Wi-Fi

El camino base no agregado que el modelo Fz3r0 quiere enseñar es:

```text
MSDU -> MPDU -> PSDU -> PPDU
````

Esta cadena resume el paso de la información desde MAC hacia PHY en Wi-Fi.

| Unidad | Dónde vive        | Qué representa                                   |
| ------ | ----------------- | ------------------------------------------------ |
| MSDU   | MAC service input | Lo que MAC recibe desde arriba                   |
| MPDU   | 802.11 MAC        | La unidad que MAC construye                      |
| PSDU   | PHY service input | Cómo PHY/PLCP ve los octetos recibidos desde MAC |
| PPDU   | PHY / PLCP        | La unidad PHY preparada para transmitirse por RF |

La frase más importante del modelo es esta:

> The exact same MPDU octets cross the PHY service interface and are renamed the PSDU from the physical layer’s perspective.

En español:

> Los mismos octetos del MPDU cruzan la interfaz de servicio hacia PHY y, desde la perspectiva de la capa física, se llaman PSDU.

Eso es clave.

No es que MAC cree una cosa y PHY cree otra copia completamente separada.

MAC termina su MPDU.

PHY recibe esos mismos octetos como PSDU.

Después PLCP construye el PPDU.

---

## 5. L2 Upper: LLC/SNAP

La parte superior de Layer 2 en el modelo Fz3r0 representa LLC/SNAP.

Su función es servir como puente lógico entre protocolos superiores, como IP o ARP, y el mundo 802.11.

En muchos casos de IP sobre Wi-Fi, LLC/SNAP identifica qué protocolo superior está siendo transportado.

| Campo conceptual   | L2 Upper / LLC-SNAP                                            |
| ------------------ | -------------------------------------------------------------- |
| Receives           | Network-layer PDU, por ejemplo IPv4 o IPv6 packet              |
| Builds             | LLC/SNAP framing                                               |
| Contains           | El paquete de Layer 3 identificado dentro del framing LLC/SNAP |
| Passes downward as | MSDU hacia 802.11 MAC                                          |

Esta capa no necesita el tratamiento visual pesado de PDU/SDU, porque el punto pedagógico fuerte está más abajo, en MAC y PHY.

Pero sí es importante que exista.

Sin LLC/SNAP, el estudiante puede creer que 802.11 simplemente mete IP igual que Ethernet, y no es tan simple.

---

## 6. L2 Lower: 802.11 MAC

Aquí empieza el verdadero campo de batalla Wi-Fi.

La subcapa 802.11 MAC es donde la información se vuelve una trama Wi-Fi real.

Para un data frame normal, MAC recibe un MSDU desde arriba.

Luego construye un MPDU.

El MPDU puede incluir:

| Parte          | Función                                                               |
| -------------- | --------------------------------------------------------------------- |
| MAC Header     | Control de trama, direcciones, duración, secuencia, QoS según aplique |
| Payload / Body | Donde viaja el MSDU o contenido protegido                             |
| FCS            | Verificación de integridad a nivel de frame                           |

Relación principal:

| Concepto           | 802.11 MAC                                            |
| ------------------ | ----------------------------------------------------- |
| Receives           | MSDU                                                  |
| Builds             | MPDU                                                  |
| Contains           | MSDU dentro del cuerpo del MPDU, más MAC header y FCS |
| Passes downward as | MPDU, cuyos octetos serán vistos por PHY como PSDU    |

Visualmente, esta capa debe sentirse diferente.

No debe ser solo una tarjeta amarilla más.

Debe mostrar el concepto:

```text
MPDU
└── contains MSDU
```

El MPDU es el contenedor MAC.

El MSDU es la carga útil de servicio que MAC recibió desde arriba.

---

## 7. L1: PHY / PLCP / PMD / RF

Layer 1 en Wi-Fi no es solo “el aire”.

El modelo Fz3r0 lo representa como:

```text
PHY / PLCP-PMD-RF
```

Esto permite explicar mejor qué hace la capa física.

PHY recibe desde MAC una unidad que, desde la perspectiva de PHY, se llama PSDU.

Luego PLCP construye el PPDU.

El PPDU es la unidad que se prepara para transmitirse como señal RF.

| Concepto  | PHY / PLCP-PMD-RF                      |
| --------- | -------------------------------------- |
| Receives  | PSDU                                   |
| Builds    | PPDU                                   |
| Contains  | PSDU más PLCP preamble/header behavior |
| Transmits | PPDU como RF a través de PMD           |

Visualmente, esta capa debe mostrar:

```text
PPDU
└── contains PSDU
```

El PSDU es el contenido que PHY recibe desde MAC.

El PPDU es la unidad física lista para transmisión.

La estructura exacta del PPDU depende del PHY usado. No es igual en DSSS, OFDM, HT, VHT, HE o EHT. Pero el concepto base se mantiene:

```text
PHY receives PSDU
PLCP builds PPDU
PMD transmits RF
```

---

## 8. MPDU y PSDU: mismos octetos, perspectiva diferente

Este es probablemente el punto más importante del modelo.

En el camino básico no agregado:

```text
MAC builds MPDU
PHY receives PSDU
```

Pero eso no significa que se duplicó la información o que mágicamente apareció otra estructura completamente diferente.

La forma correcta de verlo es:

| Perspectiva    | Nombre |
| -------------- | ------ |
| Desde MAC      | MPDU   |
| Desde PHY/PLCP | PSDU   |

Son los mismos octetos al cruzar la interfaz de servicio.

Ese cambio de nombre enseña algo fundamental:

> Las unidades de datos se nombran según la capa que las está usando.

Por eso el modelo Fz3r0 insiste tanto en la perspectiva.

No basta con decir “el frame baja a physical”.

Hay que entender cómo cambia el nombre y por qué.

---

## 9. La metáfora “MAC hugs PHY”

El modelo Fz3r0 puede representar visualmente que MAC “abraza” a PHY.

Esta metáfora tiene que entenderse bien.

No significa:

| No significa                     |
| -------------------------------- |
| Que MAC se convierte en PHY      |
| Que PHY vive dentro de MAC       |
| Que MAC encapsula la capa física |
| Que L1 es un payload normal      |

Significa:

| Sí significa                                                                           |
| -------------------------------------------------------------------------------------- |
| Que el handoff MAC -> PHY es crítico                                                   |
| Que el MPDU de MAC se vuelve PSDU para PHY                                             |
| Que PLCP toma ese PSDU y crea el PPDU                                                  |
| Que en Wi-Fi la frontera MAC/PHY es mucho más importante que en un dibujo OSI genérico |

La metáfora del “abrazo” sirve porque Wi-Fi no se entiende bien si MAC y PHY se ven como bloques totalmente desconectados.

En la práctica, MAC y PHY trabajan muy cerca dentro de la NIC, firmware y hardware inalámbrico.

La capa MAC prepara la unidad.

La capa PHY la transforma en transmisión.

---

## 10. Excepción importante: Management y Control frames

La cadena:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

es una excelente base para entender data frames.

Pero no todos los frames 802.11 empiezan como datos de capas superiores.

Algunos frames nacen directamente en MAC.

Ejemplos:

| Tipo                          | Ejemplos                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| Management                    | Beacon, Probe Request, Probe Response, Authentication, Association, Deauthentication |
| Control                       | ACK, RTS, CTS, Block ACK                                                             |
| Special data/control behavior | Null function frames                                                                 |

Estos frames siguen siendo MPDUs.

Pero pueden no llevar un MSDU de capas superiores.

Eso es esencial para Wi-Fi.

Un beacon no es un paquete IP encapsulado.

Un ACK no es un TCP ACK.

Un RTS/CTS no lleva HTTP, IP o UDP.

Son mecanismos propios de 802.11 MAC.

Entonces el modelo debe enseñar:

> Data frames often carry MSDUs.
> Management and Control frames may start directly at MAC.

---

## 11. Excepción importante: WPA2/WPA3 overhead

En redes protegidas, el contenido no siempre baja intacto como “MSDU limpio”.

WPA2/WPA3 puede agregar overhead criptográfico.

Dependiendo del método, pueden existir elementos como:

| Seguridad         | Ejemplos de overhead                          |
| ----------------- | --------------------------------------------- |
| CCMP              | Header, packet number, MIC/integrity behavior |
| GCMP              | Header, integrity behavior                    |
| Protected payload | Payload cifrado y autenticado                 |

La idea importante no es memorizar bytes aquí.

La idea importante es:

> MSDU size does not always equal final protected MPDU payload size.

La seguridad puede agregar información alrededor del payload protegido.

En Models, esto debe ser una nota.

No debe convertirse en un laboratorio completo de CCMP/GCMP.

---

## 12. Fragmentation y Aggregation

Fragmentation y aggregation son reales y muy importantes.

Pero no deben dominar este modelo base.

Primero hay que entender el camino simple:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

Después se puede estudiar cómo se rompe o se optimiza ese camino.

| Tema          | Qué cambia                                                    |
| ------------- | ------------------------------------------------------------- |
| Fragmentation | Un MSDU grande puede dividirse en varios MPDUs                |
| A-MSDU        | Varios MSDUs pueden agregarse dentro de un MPDU               |
| A-MPDU        | Varios MPDUs pueden agregarse dentro de una transmisión mayor |
| Block ACK     | Se confirma un bloque de MPDUs en lugar de uno por uno        |

Estos temas son avanzados y merecen su propia explicación.

El modelo Fz3r0 debe mencionarlos como nota, pero no debe intentar visualizarlos en el flujo principal.

A futuro, esto podría convertirse en un módulo separado:

```text
Doctor Fz3r0 Aggregation Lab
```

Ahí sí tendría sentido estudiar:

* A-MSDU
* A-MPDU
* MPDU delimiters
* Block ACK
* padding
* airtime efficiency
* QoS/TID
* modern Wi-Fi efficiency

Pero el modelo base debe mantenerse limpio.

---

## 13. Cómo se debe leer el modelo completo

El modelo Fz3r0 se puede leer así:

```text
Upper layers create meaning.
L3 provides packet addressing.
LLC/SNAP identifies upper protocols for 802.11 data frames.
802.11 MAC builds the MPDU.
PHY receives those MPDU octets as PSDU.
PLCP builds the PPDU.
PMD transmits it as RF.
```

O en forma compacta:

```text
IP packet
-> LLC/SNAP
-> MSDU
-> MPDU
-> PSDU
-> PPDU
-> RF
```

Y en forma conceptual:

```text
Service data becomes protocol unit.
Protocol unit becomes service data for the next layer.
Perspective changes.
The bytes continue.
```

---

## 14. Resumen de capas del modelo Fz3r0

| Fz3r0 Layer                 | Rol                                 | Recibe                 | Construye        | Punto clave                                        |
| --------------------------- | ----------------------------------- | ---------------------- | ---------------- | -------------------------------------------------- |
| L7 Application              | Significado de aplicación           | User intent / app data | App message      | No es el foco del modelo Wi-Fi                     |
| L6 Presentation / Transform | Encoding, encryption, serialization | App data               | Transformed data | Puede existir como función, no siempre como header |
| L5 Session / Context        | Estado y contexto                   | Conversation state     | Session logic    | Normalmente no es header visible                   |
| L4 Transport                | TCP/UDP                             | App bytes              | Segment/datagram | Payload superior para Wi-Fi                        |
| L3 Network                  | IP/ARP context                      | Transport PDU          | IP packet        | Importa por LLC/SNAP e identificación              |
| L2 Upper / LLC-SNAP         | Identificación lógica               | Network PDU            | LLC/SNAP framing | Pasa MSDU hacia MAC                                |
| L2 Lower / 802.11 MAC       | Wi-Fi frame behavior                | MSDU                   | MPDU             | MPDU contiene MSDU                                 |
| L1 PHY / PLCP-PMD-RF        | Transmisión física                  | PSDU                   | PPDU             | PPDU contiene PSDU y viaja por RF                  |

---

## 15. En una frase

El Fz3r0 Wi-Fi Custom Model es un zoom Wi-Fi sobre OSI Layer 1 y Layer 2, diseñado para enseñar cómo LLC/SNAP, 802.11 MAC, PHY, PLCP, PMD, MSDU, MPDU, PSDU y PPDU se relacionan realmente en 802.11.

O todavía más corto:

> OSI te da el mapa.
> Fz3r0 te muestra el campo de batalla Wi-Fi.

---

## 16. Conclusión

El modelo OSI sigue siendo útil porque organiza responsabilidades.

Pero Wi-Fi necesita más detalle.

Para entender Wi-Fi, no basta con decir “Data Link” y “Physical”.

Hay que ver qué pasa dentro.

Hay que entender que LLC/SNAP identifica protocolos superiores.

Hay que entender que MAC construye MPDUs.

Hay que entender que el MPDU contiene el MSDU.

Hay que entender que PHY ve esos mismos octetos como PSDU.

Hay que entender que PLCP crea el PPDU.

Hay que entender que el PPDU viaja por RF.

Y también hay que saber que no todos los frames siguen el mismo camino, porque Management y Control frames pueden nacer directamente en MAC, la seguridad puede agregar overhead, y aggregation puede cambiar la relación simple.

El Fz3r0 Wi-Fi Custom Model existe para enseñar exactamente eso.

No reemplaza OSI.

Lo enfoca.

Lo acerca al mundo real de 802.11.

Lo convierte en una herramienta de estudio para quien quiere entender Wi-Fi de verdad.

