








# Medium Access Methods & QoS

### ⌛💹🔢 Duration Values

The Duration Field determine the **time in microseconds (μs)** needed to complete the Frame Exchange. This is measured **AFTER the current frame**, this means: what is left after the current frame.

**There are 3 different main Duration Values types:**

1. **Data Exchange** _(AKA RTS Data Exchange)_ = `SIFS` + `Ack`
2. **RTS/CTS Data Exchange** = `x3 SIFS` + `CTS` + `Data` + `ACK`
3. **CTS-to-Self Data Exchange** = `x2 SIFS` + `Data` + `ACK`
